import pytest
from my_py_algorithms.search.search import linear_search

def test_linear_search():
    assert linear_search([3, 17, 75, 80, 202], 22) is None
    assert linear_search([3, 17, 75, 80, 202], 75) == 2
