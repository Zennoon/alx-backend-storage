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
from datetime import timedelta
import redis
import requests


def get_page(url: str) -> str:
    """Receives a url and retrieves the decoded (utf-8) content"""
    conn = redis.Redis()
    try:
        text = requests.get(url).text
    except Exception:
        pass
    else:
        count_key = "count:{}".format(url)
        with conn.pipeline() as pipe:
            pipe.incr(count_key, 1)
            pipe.expire(count_key, timedelta(seconds=10))
            pipe.execute()
        return text
    return text
