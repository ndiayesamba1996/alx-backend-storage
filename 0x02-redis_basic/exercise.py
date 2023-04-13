#!/usr/bin/env python3
''' The method should generate a random key'''

import uuid import uuid4
import redis
from typing import union, callable, optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    ''' Follow up numbers of calls in the cache class'''

    @wraps(method)
     def invoker(self, *args, **kwargs) -> union:
         ''' Gather the givren metthod after incrementing'''

         if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    ''' Follow up the call details in the cache class'''

    @wraps(method)
    def invoker(self, *args, **kwargs) -> union:
        ''' After storing the inputs and output, return the method output'''

        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker
