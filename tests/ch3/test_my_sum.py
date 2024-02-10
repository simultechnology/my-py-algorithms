import pytest

from my_py_algorithms.ch3.my_sum import my_sum


def test_my_sum():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert my_sum(arr) == 55


def test_my_sum_empty_array():
    with pytest.raises(IndexError):
        my_sum([])
