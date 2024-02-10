def my_sum(numbers, index=0):
    if index == len(numbers) - 1:
        return numbers[index]
    else:
        return numbers[index] + my_sum(numbers, index + 1)


print(my_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
