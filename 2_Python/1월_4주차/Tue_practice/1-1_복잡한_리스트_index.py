def sum_list_index(numbers):
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            total += numbers[i][j]
    return total

print(sum_list_index([[1, 4], [10, 5], [20, 30]]))