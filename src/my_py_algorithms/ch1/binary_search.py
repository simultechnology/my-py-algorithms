def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        quess = arr[mid]
        if item == quess:
            return mid
        elif item < quess:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 8, 23, 34, 55, 76, 92]

print(binary_search(my_list, 55))
print(binary_search(my_list, 30))
print(binary_search(my_list, 3))
