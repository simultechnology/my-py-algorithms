def find_smallest(arr):
    min_index = 0
    min_value = arr[min_index]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_index = i
            min_value = arr[i]
    return min_index


def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr)
    while len(copied_arr) > 0:
        smallest_index = find_smallest(copied_arr)
        popped_element = copied_arr.pop(smallest_index)
        new_arr.append(popped_element)

    return new_arr


data = [34, 123, 35, 44, 5, 66, 7]
print(selection_sort(data))
