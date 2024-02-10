import pytest
from my_py_algorithms.ch2.selection_sort import find_smallest, selection_sort


def test_find_smallest():
    assert find_smallest([5, 3, 6, 2, 10]) == 3
    assert find_smallest([1, 2, 3, 4, 5]) == 0
    assert find_smallest([10, 9, 8, 7, 6]) == 4


def test_selection_sort():
    assert selection_sort([5, 3, 6, 2, 10]) == [2, 3, 5, 6, 10]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
