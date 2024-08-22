
def linear_search(array, search_value):
    for index, value in enumerate(array):
        if value == search_value:
            return index
        elif value > search_value:
            break
    return None