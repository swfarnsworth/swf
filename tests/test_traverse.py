import pytest

from swf import traverse


@pytest.fixture
def example():
    return {
        'a': [3, 4],
        'b': {'c': [1, 2, 3]},
        'c': {
            'd': {'f': 1},
            'e': {'f': 5},
        },
    }


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (('a', 1), 4),
        (('b', 'c', -1), 3),
        (('c', dict, 'f'), {'d': 1, 'e': 5}),
        # TODO add test case for `list`
    ],
)
def test_traverse(test_input, expected, example):
    assert traverse(example, test_input) == expected

