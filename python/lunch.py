# 1. module 불러오기
import random

# 2. 점심 메뉴 리스트 만들기
lunch = ['짜장면','볶음밥','카레','순두부찌개']

# 3. 하나를 랜덤(random)으로 선택하여(choice) 저장한다.
today_menu = random.choice(lunch)

# 4. 출력한다.
print(today_menu)

# or print(random.choice(lunch))

# 출력
# print(lunch)
# print(lunch[0])

