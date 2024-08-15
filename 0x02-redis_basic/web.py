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


def get_page(url: str) -> str:
    """Receives a url and retrieves the decoded (utf-8) content"""
    conn = redis.Redis()
    key = "count:{}".format(url)
    conn.incr(key, 1)
    conn.expire(key, 10)
    return requests.get(url).text
