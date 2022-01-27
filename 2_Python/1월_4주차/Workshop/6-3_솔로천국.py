def lonely(numbers):
    result = []
    result.append(numbers[0])
    for i in range(1, len(numbers)):
        if numbers[i] != result[-1]:
            result.append(numbers[i])
    return result

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))