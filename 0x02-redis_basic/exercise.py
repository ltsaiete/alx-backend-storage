#!/usr/bin/env python3
"""
This is a simple module and it only has
one class called Cache
"""

import redis
from uuid import uuid4
from functools import wraps
from typing import Callable, Optional, Union


def replay(method: Callable):
    count_key = method.__qualname__
    input_key = f'{method.__qualname__}:inputs'
    output_key = f'{method.__qualname__}:outputs'
    r = redis.Redis()

    count = r.get(count_key)
    inputs = r.get(input_key)
    outputs = r.get(output_key)

    print(f'{method.__qualname__} was called {int(count)} times')

    print(inputs)


def count_calls(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        key = method.__qualname__
        r = args[0]._redis
        r.incr(key)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        r = args[0]._redis
        input_key = f'{method.__qualname__}:inputs'
        output_key = f'{method.__qualname__}:outputs'
        r.rpush(input_key, str(args))
        output = method(*args, **kwargs)
        r.rpush(output_key, output)
        return output
    return wrapper


class Cache:
    """The redis cache class
    """

    def __init__(self):
        """Constructor of cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and store the input data in
            Redis using the random key

        Args:
            data (Union[str , bytes , int , float]): _description_

        Returns:
            str: the random key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None):
        """_summary_

        Args:
            key (str): _description_
            fn (Optional[Callable], optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        data = self._redis.get(key)
        if data and fn:
            return fn(data)

        return data

    @count_calls
    def get_str(self, key: str, fn: Optional[Callable] = None):
        """_summary_

        Args:
            key (str): _description_
            fn (Optional[Callable], optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return str(self.get(key, fn))

    @count_calls
    def get_int(self, key: str, fn: Optional[Callable] = None):
        """_summary_

        Args:
            key (str): _description_
            fn (Optional[Callable], optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return int(self.get(key, fn))
