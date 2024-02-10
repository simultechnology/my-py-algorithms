def my_sum(numbers):
    count = len(numbers)
    if count == 1:
        return numbers[0]
    else:
        return numbers[0] + my_sum(numbers[1:])


print(my_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
