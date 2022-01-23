# for문 while문 비교

greeting ='안녕하세요.'

## while 
i = 0
while i<10:  # 해당 조건이 False가 되면, 종료
    print(greeting)
    i = i + 1

## for 
# 통 : range(10)
print(list(range(0,10)))

for i in range(10):
    print(greeting)

# lunch
lunch = ['짜장면','볶음밥','카레','순두부찌개']

for menu in lunch :
    print(menu)

for i in range(len(lunch)):
    print(lunch[i])