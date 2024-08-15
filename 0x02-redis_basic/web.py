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
    if url is None or len(url.strip()) == 0:
        return ''
    redis_store = redis.Redis()
    res_key = 'result:{}'.format(url)
    req_key = 'count:{}'.format(url)
    result = redis_store.get(res_key)
    if result is not None:
        redis_store.incr(req_key)
        return result
    result = requests.get(url).content.decode('utf-8')
    redis_store.setex(res_key, timedelta(seconds=10), result)
    return result
