from my_py_algorithms.ch3.quick_sort import quick_sort


def test_quick_sort():
    arr = [45, 43, 1, 94, 7, 321, 6, 33, 59, 9584, 54, 39]
    assert quick_sort(arr) == [1, 6, 7, 33, 39, 43, 45, 54, 59, 94, 321, 9584]


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single_element():
    assert quick_sort([1]) == [1]


def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_quick_sort_reverse_sorted():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_quick_sort_unsorted():
    assert quick_sort([3, 6, 2, 5, 4, 1]) == [1, 2, 3, 4, 5, 6]


def test_quick_sort_duplicates():
    assert quick_sort([3, 6, 2, 5, 4, 1, 2]) == [1, 2, 2, 3, 4, 5, 6]


def test_quick_sort_negative_numbers():
    assert quick_sort([-3, -6, 2, 5, -4, 1]) == [-6, -4, -3, 1, 2, 5]
