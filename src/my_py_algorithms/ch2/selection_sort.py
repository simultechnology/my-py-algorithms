def find_smallest(arr):
    min_index = None
    min_value = None
    for i in range(len(arr)):
        if min_value is None or arr[i] < min_value:
            min_index = i
            min_value = arr[i]

    return min_index


def selection_sort(arr):
    new_arr = []
    while len(arr) > 0:
        smallest_index = find_smallest(arr)
        popped_element = arr.pop(smallest_index)
        new_arr.append(popped_element)

    return new_arr


data = [34, 123, 35, 44, 5, 66, 7]
print(selection_sort(data))
