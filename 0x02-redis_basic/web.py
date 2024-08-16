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
    text = conn.get(url)
    if not text:
        text = requests.get(url).content
        conn.setex(url, 10, text)
    text = text.decode("utf-8")
    return text
