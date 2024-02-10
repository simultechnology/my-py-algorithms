import pytest
from my_py_algorithms.ch1.binary_search import binary_search


def test_binary_search_found():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 10) == 9


def test_binary_search_not_found():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert binary_search(arr, -1) is None
    assert binary_search(arr, 11) is None
    assert binary_search(arr, 0) is None


def test_binary_search_empty_array():
    arr = []
    item = 5

    with pytest.raises(ValueError):
        binary_search(arr, item)
