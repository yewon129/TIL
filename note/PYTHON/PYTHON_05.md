# PYTHON 05

## 데이터 구조

####  [introduction]

##### method

객체를 주어로 놓고, 어떤 행위를 한다(method)

* ex ) string.split() , list.append() ( s.v 로 생각하고 진행)



### 목차

#### 순서가 있는 데이터 구조

##### 문자열 

##### 리스트

##### 튜플

#### 순서가 없는 데이터 구조

##### 셋

##### 딕셔너리



### 문자열(string)

: 모든 문자는 str 타입.

* immutable

#### 문자열 조회/탐색 메소드

s.find(x) : 없으면 -1 반횐

s.index(x) : 없으면 error 발생

#### 문자열 검증 메소드

* is : boolean 반환(T/F)

s.isupper() : 대문자 여부

s.islower() : 소문자 여부

s.istitle() : 타이틀 형식 여부



##### .find(x)

* x의 첫번째 위치 반환, 없으면 -1 반환

##### .index(x)

* x의 첫번째 위치 반환, 없으면 error



#### 문자열 관련 검증 메소드

.isalpha()

.isupper()

.islower()

.istitle()

* 이런게 있다!
  * isdecimal(), isdigit(), isnumeric()

#### 문자열 변경 메소드 (?immutable : 변경된 문자열의 값을 반환한다!)

s.replace(old`(대상)`,new`(새로운값)`[,count`갯수만큼만 시행`)]) : 바꿈

s.strip([chars]) : 제거

* strip(양쪽 제거), lstrip(왼쪽 제거), rstrip(오른쪽 제거), 지정하지 않으면 공백 제거

s.split(sep = None, maxsplit = -1) : 분리

* ex) map(int,input(),split())
* 문자열을 특정한 단위로 나눠 리스트로 반환
* 공백은 빈 문자열에 포함하지 않음.

'separator'.join([iterable]) : 합침

* ['1', '2', '3'] 이것을 한 줄로 print
* iterable에 문자열 아닌 값 있으면 error

```python
# 1
numbers = ['1', '2', '3']
# 출력 : 1 2 3
for number in numbers :
    print(number, end = ' ')
```

```python
# 2. join (string 메서드)
# error : numbers.join(' ')
print(' '.join(numbers))
```

```python
## 요소가 문자열이 아닌 경우
number = [1, 2, 3]
# print(' '.join(numbers)) #typeError
print(' '.join(map(str,numbers)))
```

#### 문자열 변경 예시

capitailze() , title(), upper, lower ,swapcase()

* title -> 공백 & ' 앞을 대문자



### 리스트(List)

#### 리스트 메소드 : 리스트의 요소를 변경시키는 것 존재 (=> mutable)

##### .append(x) : 추가

* 리스트에 값 추가

##### .extend(iterable) :  두개의 리스트를 합치는 것

* 'coffee'를 붙히면 각 알파벳이 붙음. 
* ['coffee']라고 하면 list가 두개 붙음.

##### .insert(i,x) : 정해진 위치(index)에 추가.

* 리스트보다 긴 곳에 넣으면 제일 뒤에 추가 시킴

##### .remove(x) : x 를 제거

* 없는 경우 value error
* 값 제거

##### .pop() : 마지막 항을 반환 후 제거

* pop(i) : 인덱스에 있는 항목 반환 후 제거
* index 제거

##### .clear() : 모든 항목 삭제

##### .index(x) : x값 찾아 해당 index 값 반환

* 없으면 value error

##### .count(x) : 원하는 값의 개수 반환

```python
cnt = 0
for 1 in numbers:
    cnt += 1
vs
numbers.count(1)
```

##### .sort() : 원본 리스트 정렬

* .sort vs sorted

```python
a = [100, 10, 1, 5]
b = [100, 10, 1, 5]
# 1. 메소드(.sort)
print(a)
print(a.sort())
# None 출력
# 원본 리스트를 정렬시키고, None을 return
print(a)
# [1, 5, 10, 100]
```

```python
# 2. 함수(sorted)
print(b)
print(sorted(b))
#[1, 5, 10, 100]
# 원본 리스트는 변경 x, 정렬된 리스트를 return
print(b)
# [100, 10, 1, 5]
```

```python
a = [100, 2]
a.sort()
#바로 사용 가능
b = [100, 2]
b = sorted(b)
# 값을 저장해야함
```

##### .reverse() : 순서를 반대로 뒤집음(정렬 x)

* 원본 자체의 순서를 뒤집는다!

```python
a = [100, 2, 6]
a.sort()
a.reverse()
print(a)
# [100, 6, 2]
```

### 튜플(Tuple)

####  immutable - 값에 영향을 미치지 않는 메소드만 지원.

* 리스트 메소드 중 항목을 변경하는 메소드 제외하고 대부분 동일



### 셋(Set)

* 순서없음.

.copy(), .clear(), .isdisjoint(t), .issubset(t), .issuperset(t)

##### .add(x) : 셋에 값 추가

* 순서가 유지되지 않는다!

##### .update(*others) : 여러 값 추가

* 중복되는 것은 알아서 삭제

##### .remove(elem) : 셋에서 삭제

* 없으면 key error

##### .discard(elem): 셋에서 삭제

* 없어도 에러가 발생하지 않음

##### .pop() : 임의의 원소를 제거,반환

* 셋;임의의 원소 제거(순서 x) vs list ;인덱스에 따라, 기본적으로 마지막 제거(순서 o)



### 딕셔너리(Dictionary)

* 키와 값의 조작
* 키로 접근. 인덱스 접근 x

.clear(), .copy(), .keys(), .values(), .items(),  .pop(k), .update([other])

##### .get(key[,default]) : key통하여 value 가져옴

* key error 발생 x (기본 : None)

##### .pop(key[,default]) : key가 딕셔너리에 있으면 제거

* default값 없으면 keyerror
  * 리스트 : 마지막 or index
  * 셋 : 랜덤
  * 딕셔너리 : key

##### .update() : 값을 제공하는 key, value로 덮어쓴다.

[파이썬 자습서](docs.python.org)



### 얕은 복사와 깊은 복사

* 할당
  * 대입 연산자(=)
    * 리스트 복사 확인

```python
orginal_list = [1, 2, 3]
copy_list = original_list

copy_list[0] = 'h'
print(copy_list, original_list)
# 같은 객체를 참조 = 같은 리스트(곳)을 바라보고 있다.
['h', 2, 3], ['h', 2, 3]
```

```python
original_list = [1, 2, 3]
copy_list = original_list[:]
#slicing : 처리를 했기 때문에 다른 결과
copy_list[0] = 'h'
print(copy_list, original_list)
['h', 2, 3], [1, 2, 3]
```

```python
original_list = [1, 2, 3]
copy_list = list(original_list)
#형변환 했기 때문에 다른 것
copy_list[0] = 'h'
print(copy_list, original_list)
['h', 2, 3], [1, 2, 3]
```

* 변수를 처리한 후 똑같은 결과값을 부여하자!



#### 얕은 복사 주의사항

* 복사하는 리스트의 원소가 주소를 참조하는 경우

```python
original_list = [1, 2, [0, 1]]
copy_list = original_list[:]

copy_list[2][0] = 'h'
print(copy_list, original_list)
[1, 2, ['h', 1]], [1, 2, ['h', 1]]
# 2차원 list등은주소가 저장되어 있기 때문에 안의 내용은 풀어내지 못함.
```

#### 깊은 복사

```python
import copy
original_list = [1, 2, [0, 1]]
copy_list = copy.deepcopy(original_list)

copy_list[2][0] = 'h'
print(copy_list, original_list)
[1, 2, ['h', 1]], [1, 2, [0, 1]]
```

