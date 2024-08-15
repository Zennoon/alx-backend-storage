#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    get_page - Receives a url and returns the html content

    Decorators
    ==========
    count_url - Wraps get_page and keeps count of the number of
    times a url has been requested (given to the function), and
    caches the result for 10 seconds
"""
import redis
import requests
from functools import wraps
from typing import Callable


def count_url(func: Callable) -> Callable:
    """Tracks the urls passed to the get_page function"""
    conn = redis.Redis()

    @wraps(func)
    def incr_count(url: str):
        """
        Increments the count of the url in the redis server by 1
        and sets an expiration date of 10 seconds for the count
        """
        key = "count:{}".format(url)
        conn.incr(key, 1)
        conn.expire(key, 10)
        return (func(url))
    return incr_count


@count_url
def get_page(url: str) -> str:
    """Receives a url and retrieves the decoded (utf-8) content"""
    return requests.get(url).text
