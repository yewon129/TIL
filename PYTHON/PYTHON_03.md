# PYTHON 03

## 함수

* 특정한 기능을 하는 코드의 조각

* 사용자 함수

  * ```python
    def function_name(parameter):
        #code block
        return returning_value
    ```

* 함수를 사용해야하는 이유?

  * 표준편차 계산 :

  * ```python
    import statistics
    list
    statistics.pstdev(list)
    ```

  * 내장함수 활용: sum

* 함수 기본 구조
  * 선언과 호출(difine & call)
  * 입력 (input)
  * 문서화(doc-string)
  * 범위(scope)
  * 결과값(output)

[실습] 입력 받은 수를 세제곱하여 반환하는 함수

```python
def cube(number):
    result = number ** 3
    return result
```



### 함수의 결과값

* Void function (print)
  * 명시적인 return 값이 없는 경우, None 반환 후 종료
* Value returning function ()
  * 함수 실행 후, return문을 통해 값 반환
  * return 하게 되면, 값 반환 후 함수 바로 종료

```python
#void function 예시
def void_product(x,y):
    print(f'{x} x {y} = {x*y}')

void_product(4,5)
ans = void_product(4,5)
ans
print(ans)
```

```bash
4 x 5 = 20
4 x 5 = 20

None
```

```python
# value returning fuction 예시
def value_returning_product(x,y):
    return x * y
value_returning_product(4,5)
ans = value_returning_product(4,5)
ans
print(ans)
```

```bash
(out) 20

(out) 20
20
```

##### 두 개 이상의 값 반환

* 함수는 항상 단일한 값만 반환

* 반환 값으로 튜플 사용하여 return문 한번 사용하고 두개 이상의 값 반환

  * ```python
    def minus_and_product(x,y):
        return x-y, x*y
    y = minus_and_product(4,5)
    print(y)
    ```

    ```bash
    (-1,20)
    ```

##### return vs print

* return : 키워드 (함수 안에서만 사용됨)

* print : 함수 (출력을 위하여 사용)

[실습] 너비와 높이 입력받아 사각형 넓이와 둘레를 튜플로 반환

```python
def rectangle(width, height):
    length = 2*width + 2*height
    area = width * hieight
    return area, length
```



### 함수의 입력

* parameter : 함수를 실행할 때 함수 내부에서 사용되는 식별자
* argument : 함수를 호출할 때, 넣어주는 값

```python
def say(anything): # parameter = anything
    print(f'hello {anything}'')

say('python') # argument = 'python'
```

* Argument
  * 함수 호출 시 함수의 parameter를 통해 전달되는 값
  * 소괄호 안에 할당 : func_name(argument)
    * 필수 argument : 반드시 전달되어야 함
    * 선택 argument : 값을 전달하지 않아도 되는 경우는 기본 값 전달.

#### positional argument

* 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달

  * ```python
    def add(x,y):
        return x+y
    
    add(2,3)
    => def add(x,y):
        x=2 ; y=3
        return x+y
    ```



#### Keyword argument

* 직접 변수의 이름으로 특정 argument 전달 가능
* keyword argument 다음에 positonal argument 활용 불가능

```python
def add(x,y):
    return x+y

add(x=2, y=5)
add(2, y=5)
```

#### Default argument values

* 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
  * 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음.

```python
def add(x,y=0):
    return x+y

add(2)
=> def add(x,y=0):
    x=2
    return x+y
```

#### Packing /Unpacking

* positional : 연산자 (*)
  * 여러개의 positional argument를 하나의 필수 parameter로 받아서 사용
* 몇개의 positional argument 를 받을지 모르는 함수를 정의시 사용.

```python
def add(*args):
    for arg in args:
        print(arg)
```

* keyword : 연산자(**)
  * 함수가 임의의 개수 argument를 keyword argument로 호출될 수 있도록.
  * argumet들은 딕셔너리로 묶여 처리, parameter에 ** 붙여 표현

```python
def family(**kwargs):
    for key, value in kwargs:
        print(key,":",value)
        
family(father = 'John', mother='Jane', me='John Jr.')
```

##### 주의 사항

```python
def greeting(name = 'john doe', age) ## 불가능!!!
```

* 기본 argument 값을 가지는 argument 다음에 기본값이 없는 argument로 정의할 수 없음.
* keyword argument 다음에 positional argument를 활용할 수 없음.



### 함수의 범위

local : 함수 내부에서만 사용 가능 / 함수가 호출될 때 생성, 종료될때까지 유지

global : 코드 어디에서든 참조할 수 있음 / 모듈이 호출된 시점 이후까지 유지

built-in : 파이썬이 실행된 이후 영원히 유지

##### 이름 검색 규칙

**LEGB**

Local scope(함수) - Enclosed scope(특정 함수의 상위 함수) - Global scope(함수 밖의 변수, Import 모듈) - Built-in scope(파이썬 안에 내장되어 있는 함수)

```python
a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a,b,c)
    local(300)
    print(a,b,c)
enclosed() # 10 1 300 # 10 1 3
print(a,b) # 0 1
```

```python
print(sum) # <built-in function sum>
pirnt(sum(range(2))) # 1
sum = 5 
print(sum) # 5
print(sum(range(2))) # error
```

#### 상위 scope에 있는 변수 수정

##### global 문

* 현재 코드 블록 전체에 적용, 나열된 이름이 global variable임을 나타냄
  * global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장 불가
  * global에 나열된 이름은 parameter, for루프 대상, 클래스/함수 정의 등으로 정의 되지 않음

```python
# 함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
    global a
    a = 3

print(a) # 10
func1()
print(a) # 3
```

* local scope에서 global 변수 값 변경 가능
* global 키워드 사용하지 않으면, local scope에 a 변수 생성.

##### nonlocal

* global을 제외하고 가장 가까운 scope의 변수를 연결.
* global과 달리 이미 존재하는 이름과의 연결만 가능

```python
#nonlocal 예시
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x)
    
func1() # 2
print(x) # 0
```

* enclosed scope(func1)의 변수 x의 변경

```python
# 선언된 적 없는 변수의 활용
def func1():
    global out
    out = 3
func1()
print(out) #3
```

```python
# 선언된 적 없는 변수의 활용
def func1():
    def func2():
        nonlocal y
        y = 2
    func2()
    print(y)
    
func1() # error : nonlocal은 이름공간상에 존재하는 변수만 가능
```



### 함수 응용

#### 내장함수

#### map

##### `map (function, iterable)`

 * function : 각 요소에 적용하고 싶은 함수 이름
 * map(함수이름, list) 라고 가정

   * => list : 길이가 10만 => 통이 만들어지는데, 다음 것들을 기억하고 하나씩 뽑아주기만 함 => 이 통을 다 보고싶을 때에만 list를 사용하면 됨

```python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result, type(result)) #<map object at 0x10e2ca100> <class 'map'>
list(result) # ['1', '2', '3']
```

```python
n, m = map(int, input().split()) # 3 5
print(n, m) # 3 5
print(type(n), type(m)) #<class 'int'> <class 'int'>
```



#### filter

##### `filter(function, iterable)`

* 함수 : True / False 반환

```python
def odd(n):
    return n% 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result)) #<filter object at 0x10e3dfc10> <class 'filter'>
list(result) # [1,3]
```



#### zip

##### `zip(*iterables)`

* tuple, tuple

```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(pair, type(pair)) # <zip object at ~> <class 'zip'>
list(pair) # [('jane','justin'), ('ashley', 'eric')]
```



#### lambda 함수 (선택적으로 생각.)

##### lambda [parameter] : 표현식

* 익명함수! filter에 사용

  ```python
  def odd(n):
      return n % 2
  print(filter(odd, range(5)))
  ```

  vs

  ```python
  print(list(filter(lambda n : n % 2, range(5))))
  ```

  

#### 재귀함수

##### 자기 자신을 호출하는 함수

* 1개 이상의 종료되는 상황(base case) 존재, 수렴하도록 작성

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else :
        return n * factorial(n-1)
factorial(4)
```

* stack overflow
* 1000번까지 반복, 이후 Recursion Error 발생

