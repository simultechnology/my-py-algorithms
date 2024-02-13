from my_py_algorithms.ch6.breadth_first_search import bread_first_search


def test_bread_first_search():
    graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "claire": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}

    search = bread_first_search("you", graph)
    assert search == True
