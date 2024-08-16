#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    get_page - Receives a url and returns the html content

"""
import redis
import requests
from datetime import timedelta

conn = redis.Redis()


def get_page(url: str) -> str:
    """Receives a url and retrieves the HTML content"""
    count_key = "count:{}".format(url)
    if conn.get(count_key):
        conn.incr(count_key, 1)
    else:
        conn.set(count_key, 0)
    text = ''
    try:
        text = requests.get(url).text
    except Exception:
        text = ''
    return text
