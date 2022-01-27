def sum_list_while(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        j = 0
        while j < len(numbers[i]):
            total += numbers[i][j]
            j += 1
        i += 1
    return total

print(sum_list_while([[1, 4], [10, 5], [20, 30]]))