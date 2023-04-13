#!/usr/bin/env python3
''' web.py file '''
import requests
import redis
import uuid


def get_page(url: str) -> str:
    ''' get_page function '''
    client = redis.Redis()
    if client.get(url):
        return client.get(url)
    else:
        client.incr(f"count:{url}")
        response = requests.get(url).content
        client.setex(url, 10, response)
        return response
