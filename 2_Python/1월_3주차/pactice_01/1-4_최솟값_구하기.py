##주어진 리스트의 요소 중에서 최솟값을 출력하시오.

numbers = [7, 10, 22, 4, 3, 17]

min_num = numbers[0]
for number in numbers:
    if number < min_num:
        min_num = number

print(min_num)