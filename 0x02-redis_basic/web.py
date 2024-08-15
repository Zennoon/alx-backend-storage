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

conn = redis.Redis()


def get_page(url: str) -> str:
    """Receives a url and retrieves the decoded (utf-8) content"""
    if not url or len(url.strip()) == 0:
        return ''
    text = conn.get(url)
    count_key = "count:{}".format(url)
    conn.incr(count_key, 1)
    if not text:
        try:
            text = requests.get(url).text
        except Exception:
            return ''
        else:
            conn.set(url, text)
            conn.expire(url, timedelta(seconds=10))
    return text.decode('utf-8')
