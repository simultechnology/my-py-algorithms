from my_py_algorithms.ch6 import search
from my_py_algorithms.ch6.search import bread_first_search

# create sample graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def test_bread_first_search_found():
    assert bread_first_search("you", graph) == True


def test_bread_first_search_not_found():
    # thomを売り手ではないように変更してテスト
    original_person_in_seller = search.person_in_seller
    search.person_in_seller = lambda x: False
    assert bread_first_search("you", graph) == False
    # モックを元に戻す
    search.person_in_seller = original_person_in_seller


def test_bread_first_search_empty_graph():
    assert bread_first_search("you", {}) == False
