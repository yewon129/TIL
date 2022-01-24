## 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

def sum_of_digit(number):
    num_sum = 0
    while number // 10 > 0:
        num_sum += number % 10
        number = number // 10
        if number // 10 == 0:
            num_sum += number % 10
            break
    return num_sum

print(sum_of_digit(1234))
