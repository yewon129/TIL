## all()은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
## 파이썬 내장 함수 all()을 직접 구현한 my_all()을 작성하시오.

def my_all(elements):
    if bool(elements) == 0:
        return True
    for element in elements:
        if element == 1:
            return True
        else:
            return False

def your_all(elements):
    for element in elements:
        if bool(element) == False:
            return False
    else :
        return True


print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

print(your_all([]))
print(your_all([1, 2, 5, '6']))
print(your_all([[], 2, 5, '6']))
