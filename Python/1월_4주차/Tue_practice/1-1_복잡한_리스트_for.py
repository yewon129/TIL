def sum_list(numbers):
    total = 0
    for element in numbers:
        for number in element:
            total += number
    return total

print(sum_list([[1, 4], [10, 5], [20, 30]]))