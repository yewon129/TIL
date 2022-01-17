import random

def lotto_number_maker(n):
    # n번 반복 
    for i in range(n):
        # 로또 번호를 추출
        print(sorted(random.sample(range(1, 46), 6)))
lotto_number_maker(5)