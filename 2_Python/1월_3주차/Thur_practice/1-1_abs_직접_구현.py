##절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.
##파이썬 내장 함수 abs()를 직접 구현한 my_abs()를 작성하시오.

def my_abs(x):
    ab = 0
    if type(x) == complex:
        a = x.real
        b = x.imag
        ab = (a**2 + b**2)**0.5
    else:
        if x > 0:
            ab = x
        elif x == 0:
            ab = x**2
        else:
            ab = -x
    return ab

print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))