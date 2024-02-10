from time import sleep


def merge_sort(arr):
    # If the list is of length 1 or less, return the list (base case for recursion)
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves of the list
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    left_index, right_index = 0, 0

    # Compare elements from left and right lists and add the smaller one to sorted_arr
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    # Add any remaining elements from either list to sorted_arr
    while left_index < len(left):
        sorted_arr.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_arr.append(right[right_index])
        right_index += 1

    return sorted_arr


def print_items(my_list):
    for item in my_list:
        # sleep(1)
        print(item)


data = [45, 43, 1, 94, 7, 321, 6, 33, 59, 9584, 54, 39]
print(print_items(data))

print(merge_sort(data))
