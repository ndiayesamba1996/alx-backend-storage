#!/usr/bin/env python3
'''
exercise file
'''
import redis
import uuid
from typing import Union, Callable, Optional
import functools


def replay(method: Callable) -> None:
    '''
    function to display the history of calls of a particular function.
    '''
    cache = method.__self__
    inputs = cache._redis.lrange("{}:inputs"
                                 .format(method.__qualname__), 0, -1)
    outputs = cache._redis.lrange("{}:outputs"
                                  .format(method.__qualname__), 0, -1)
    result = zip(inputs, outputs)
    print('Cache.store was called {} times:'.format(len(inputs)))
    for el in result:
        print("Cache.store(*{}) -> {}".format(el[0].decode("utf-8"),
                                              el[1].decode("utf-8")))


def count_calls(method: Callable) -> Callable:
    ''' count_calls function '''
    mykey = method.__qualname__
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(mykey)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' call_history function '''
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        store = method(self, *args, **kwargs)
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        self._redis.rpush("{}:outputs".format(method.__qualname__), store)
        return store
    return wrapper


class Cache:
    '''
    class Cache that handless memory cache
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, int, float, bytes]) -> str:
        '''
        method that takes a data argument and returns a string
        '''
        uid: str = str(uuid.uuid4())
        try:
            self._redis.set(uid, data)
            return uid
        except redis.RedisError as e:
            return(f"Error: {e}")

    def get(
            self, key: str, fn: Optional[Callable[[str],
                                         Union[int, str]]] = None
                ) -> Union[str, int, float, bytes]:
        '''
        get method that take a key string argument
        and an optional Callable argument named fn
        '''
        result = self._redis.get(key)
        if (result):
            if fn:
                return fn(result)
            return result

    def get_str(self, value: str) -> str:
        ''' get_str function '''
        return value.decode('utf-8')

    def get_int(self, value: str) -> int:
        ''' get_int function '''
        return int(value.decode("utf-8"))
