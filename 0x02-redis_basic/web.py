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
    conn.incr("count:{}".format(url), 1)
    text = ''
    try:
        text = requests.get(url).text
    except Exception:
        text = ''
    return text
