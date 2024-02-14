from collections import deque


def bread_first_search(name, graph):
    if name not in graph:
        return False
    search_queue = deque()  # A
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_in_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


def person_in_seller(name):
    return name[-1] == 'm'
