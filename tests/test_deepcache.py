import pytest

from swf import deepcache


def test_deepcache():

    @deepcache
    def my_func(letters, numbers):
        return {k.upper(): v * 2 for k, v in zip(letters, numbers)}

    letters = 'abcde'
    numbers = (1, 2, 3, 4, 5)
    a = my_func(letters, numbers)
    b = my_func(letters, numbers)

    assert a == b
    assert a is not b

    a['A'] = 'not a number'
    assert a != b
