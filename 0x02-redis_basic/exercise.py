#!/usr/bin/env python3
"""
Contains:
    Classes
    =======
    Cache - Wrapper to enable caching using redis
"""
import redis
import uuid
from typing import Any, Awaitable, Callable, Type, Union
from functools import wraps


def call_history(method):
    @wraps(method)
    def record_method_io(self, *args):
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        output = method(self, *args)
        self._redis.rpush("{}:outputs".format(method.__qualname__), output)
        return output
    return record_method_io


def count_calls(method):
    @wraps(method)
    def incr_call_counter(self, *args, **kwargs):
        self._redis.incr(method.__qualname__, 1)
        return method(self, *args, **kwargs)
    return incr_call_counter


class Cache:
    """Provides caching using redis"""
    def __init__(self) -> None:
        """Initializes a newly created instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data to the client with a random key
        generated by uuid

        Args:
            data (str | bytes | int | float) : The data to store

        Returns:
            (str): The randomly generated key used to store the data
        """
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return (str(key))

    def get(self, key: str, fn: Any = None) -> Any:
        """
        Receives a key and returns the value stored after using the
        given callback function (if given) to convert the bytes that
        redis returns by default
        """
        val = self._redis.get(key)
        if val:
            if fn:
                return fn(val)
        return (val)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Gets a value from redis server and attempts to convert to
        int using the get method with the int() function passed as
        callback
        """
        return self.get(key, int)

    def get_str(self, key: str) -> Union[str, None]:
        """
        Gets a value from redis server and attempts to convert to
        str using the get method with the .decode('utf-8') function
        passed as lambda callback
        """
        return self.get(key, lambda val: val.decode("utf-8"))


def replay(method):
    """
    Replays the history of a method of the Cache class
    """
    conn = redis.Redis()
    method_name = method.__qualname__
    count = conn.get(method_name)
    if count:
        count = count.decode("utf-8")

    print("{} was called {} times:".format(method_name, count))
    inputs = conn.lrange(
        "{}:inputs".format(method_name), 0, -1
    )
    outputs = conn.lrange(
        "{}:outputs".format(method_name), 0, -1
    )
    zipped = zip(inputs, outputs)

    for inp, outp in zipped:
        print("{}(*{}) -> {}".format(
            method_name,
            inp.decode("utf-8"),
            outp.decode("utf-8")
        ))
