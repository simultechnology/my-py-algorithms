from my_py_algorithms.ch3.merge_sort import merge_sort


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single_element():
    assert merge_sort([1]) == [1]


def test_merge_sort_sorted_list():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_sort_reverse_list():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_merge_sort_unsorted_list():
    assert merge_sort([4, 1, 3, 9, 2]) == [1, 2, 3, 4, 9]


def test_merge_sort_with_duplicates():
    assert merge_sort([4, 2, 3, 2, 1]) == [1, 2, 2, 3, 4]


def test_merge_sort_negative_numbers():
    assert merge_sort([-3, -1, -2, -4, -5]) == [-5, -4, -3, -2, -1]
