def my_avg(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(my_avg(77,83,95,80,70))