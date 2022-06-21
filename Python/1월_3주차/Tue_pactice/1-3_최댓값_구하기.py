## 주어진 리스트의 요소 중에서 최댓값을 출력하시오.

numbers = [7, 10, 22, 4, 3, 17]

max_num = numbers[0]
for number in numbers :
    if number > max_num :
        max_num = number
    else :
        pass

print(max_num)