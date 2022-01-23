# 1. random 모듈 불러오기
import random

# 2. 숫자 통(1~45)
numbers = range(1,46) # range(n,m) : n이상 m미만

# 3. 숫자 통에서 6개를 sample 결과 출력
# random.sample(통, 개수)
lotto_number = random.sample(numbers,6)

#print(sorted(lotto_number))

for i in range(5):
    lotto_number = random.sample(numbers,6)
    print(sorted(lotto_number))

# 기타
#print(random.sample(range(1,46),6))

# def lotto_number_maker(n):
#     # n번 반복 
#     for i in range(n):
#         # 로또 번호를 추출
#         print(random.sample(range(1, 46), 6))
# lotto_number_maker(5)