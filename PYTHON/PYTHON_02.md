# PYTHON 02

## 제어문

### 조건문

* 참/거짓을 판단할 수 있는 조건식

* expression에는 참/거짓에 대한 조건식

* ```python
  if <expression == True>:
      # Run ths Code block
  else:
      # Run this Code block
  ```

[예제]

```python
a = 5
if a > 5:
    print('5 초과')
else:
    print('5 이하')
print(a)
```

[실습] 조건문을 통해 변수 num 값의 홀수/짝수 여부 출력

```python
num = int(input('숫자입력: '))
if num % 2 : # if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
```



#### 복수 조건문

* elif 사용

[예제] 미세먼지 농도

```python
dust = int(input('미세먼지 농도:'))

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
print('미세먼지 확인 완료!')
```



#### 중첩 조건문

* 조건문은 다른 조건문에 중첩 가능 (들여쓰기 주의)

```python
dust = int(input('미세먼지 농도:'))

if dust > 150:
    print('매우나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요.')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust >= 0:
    	print('좋음')
    else:
        print('값이 잘못 되었습니다.')
print('미세먼지 확인 완료!')
```



#### 조건 표현식

```python
<true인 경우 값>if<expression>else<false인 경우 값>
```

[예제]

```python
value=num if num>=0 else -num
```

: 절대값을 저장하기 위한 코드

[실습]

```python
num = 2
if num % 2:
    result = '홀수입니다.'
else:
    result = '짝수입니다.'
print(result)
```

```python
print('홀수입니다.') if num % 2 else print('짝수입니다.')
```

[실습]

```python
num = -5
value = num if num >= 0 else 0
print(value)
```

```python
num = -5
if num >= 0:
    value = num
else:
    value = 0
print(value)
```



### 반복문

* while
  * 종료조건
* for
  * 객체의 순회
* 반복제어
  * break, continue, for-else



#### while

* 참인 경우 반복적으로 코드 실행

[예제]

```python
a = 0
while a<5:
    print('a')
    a += 1
print('끝')
```

[실습] 1부터 사용자가 입력한 양의 정수까지의 총합

```python
n = 0
total = 0
user_input = int(input())
while n <= user_input:
    total += n
    n += 1
print(total)
```



#### for

* 시퀀스(string, tuple, list, range) 포함한 순회가능한 객체 요소를 모두 순회

##### 문자열 순회

[예제]

```python
for fruit in ['사과', '망고', '바나나']:
    print(fruit)
print('끝')
```

* iterable
  * 순회 가능한 자료(str, list, dict 등)
  * 순회형 함수(range, enumerate)

[예제] : 사용자가 입력한 문자 한글자씩 출력

```python
chars = input()
for char in chars:
    print(char)
```

[예제] : 사용자가 입력한 문자를 range 활용하여 한 글자씩 출력

```python
chars = input()
for i in range(len(chars)):
    print(chars[i])
```

##### 딕셔너리 순회

* key를 통하여 값을 활용

```python
grades = {'john' : 80, 'eric' : 90}
print(grades.keys())
print(grades.values())
print(grades.items())
for name, score in grades.items():
    print(name, score)
```

```bash
dict_keys(['john', 'eric'])
dict_values([80, 90])
dict_items([('john', 80), ('eric', 90)])
john 80
eric 90
```



##### enumerate 순회

* 인덱스와 객체를 쌍으로 담은 열거형(enumerate)
  * (idx, value) 형태의 tuple로 구성된 열거 객체 반환

```python
memebers = ['민수', '영희', '철수']
for i, members in enumerate(members):
    print(i, member)
```

```bash
0 민수
1 영희
2 철수
```

```python
list(enumerate(members, start = 1))
```

[(1, '민수'), (2, '영희'), (3, '철수')]



##### list comprehension

```python
[<expression>for<변수>in<iterable>]
[<expression>for<변수>in<iterable>if<조건식>]
```

[예제]

```python
cubic_list = []
for number in range(1,4):
    cubic_list.append(number ** 3)
cubic_list
```

```python
[numbers**3 for number in range(1,4)]
```

##### Dictionary Comprehension

```python
{key:value for <변수> in <iterable>}
```

```python
cubic_dict = {}
for number in range(1,4):
    cubic_dict[number] = number ** 3
cubic_dict
```

```python
{nubmer : number**3 for number in range(1,4)}
```

[실습]

```python
for number in range(1,31):
    if number % 2:
        print(number)
```



#### 반복문 제어

* break : 반복문 종료
* continue : continue 이후 코드 블록은 수행하지 않고, 다음 반복 수행
* for - else : 끝까지 반복문 실행 후 else문 실행
  * break 통해 중간에 종료되는 경우 else 실행되지 않음