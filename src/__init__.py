import copy
import functools
import json
import warnings
from typing import Sequence, Any

__all__ = [
    'traverse',
    'jsonl_gen',
    'deepcache',
]


def traverse(data, keys: Sequence[int | str | type[dict, list]], raise_exception: bool = False, default: Any = None):
    """
    For traversing JSON-like structures.
    Equivalent to data[a][b][c][d], etc. where each a, b, c, d in `keys`. if not `raise_exception`, a missing key
    (or index) will return `default`.
    """
    keys_iter = iter(keys)

    for k in keys_iter:
        if isinstance(k, type) and issubclass(k, (dict, list)) and not ((k is dict) or (k is list)):
            warnings.warn(f"{k} is a subclass of dict or list, but only the dict and list classes exactly are supported.")

        if k is list:
            keys_tuple = tuple(keys_iter)
            return [
                traverse(elem, keys_tuple, raise_exception, default)
                for elem in data
            ]
        elif k is dict:
            keys_tuple = tuple(keys_iter)
            return {
                k: traverse(v, keys_tuple, raise_exception, default)
                for k, v in data.items()
            }

        try:
            data = data[k]
        except (IndexError, KeyError) as e:
            if raise_exception:
                raise e
            return default

    return data

def jsonl_gen(jsonl_path):
    with open(jsonl_path) as f:
        yield from map(json.loads, f)


def deepcache(func):
    cached_func = functools.cache(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = cached_func(*args, **kwargs)
        return copy.deepcopy(value)

    wrapper.cache_clear = cached_func.cache_clear
    wrapper.cache_info = cached_func.cache_info

    return wrapper
