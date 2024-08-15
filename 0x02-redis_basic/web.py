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


def count_requests(method: Callable) -> Callable:
    """ Decortator for counting """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper for decorator """
        conn.incr("count:{}".format(url))
        cached_html = conn.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        conn.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    req = requests.get(url)
    return req.text
