## 주어진 리스트의 요소 중에서 최댓값과 등장 횟수를 출력하시오

numbers = [7, 10, 22, 7, 22, 22]

count = 0
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    else :
        pass
        if number == max_num:
            count += 1

print(max_num, count)