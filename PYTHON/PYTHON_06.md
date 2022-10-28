# PYTHON 06

## 에러/예외 처리



#### 디버깅

* 1st ) Syntax Error(Indentation)

  * 2nd)
  * branches(조건) : 모든 조건 커버

  * for : 반복문이 원하는 횟수? & 반복문 값 변경(진입 & 결과)

  * while : for & 종료 조건

  * function(&method) : 호출, 파리미터, 결과// type



##### 디버깅 방법

* print 함수 활용
  * 끊어서 생각
* python tutor 사용



#### 에러와 예외

##### 문법 에러 (Syntax Error)

* assign to literal :
* EOL(End of Line)
* EOF(End of File)

##### 예외

* ZeroDivisionError : 0으로 나눌 수 없어요
* NameError : 이름 없거나 이름에 오타
* TypeError : 
  * 다른 타입끼리 연산
  * 함수에서 타입이 잘못됨
  * argument 누락, 개수 초과
  * argument type 불일치
* ValueError:
  * 타입은 없으나 값이 적절치 않음
* IndexError:
  * 인덱스가 존재하지 않거나 범위
* KeyError:
  * 해당 키 존재하지 않는 경우

* ModuleNotFoundError:
  * 존재하지 않는 모듈을 import 하는 경우


* ImportError:
  * Module은 있으나 존재하지않는 클래스/함수 가져오는 경우
* KeyboardInterrupt:
  * 임의로 프로그램 종료했을 때
* IndentationError:
  * Indentation이 적절하지 않는 경우

### 예외 처리 ( try / except )

##### try

* 오류가 발생할 가능성이 있는 코드 실행
* 예외가 발생되지 않으면, except 없이 실행 종료

##### except

* 예외가 발생하면 실행
* 예외 상황을 처리하는 코드를 받아서 적절한 조치 취힘.

```python
try:
    num = input('숫자입력:')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
```

[실습]

```python
try:
	num = input('100으로 나눌 값을 입력하시오 :')
	print(100/int(num))
except ValueError :
    print('숫자를 넣어주세요')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러는 모르지만 에러가 발생하였습니다.')
```

```python
## 순차적으로 순행되므로, 가장 작은 범주부터 예외 처리해야함
try:
	num = input('100으로 나눌 값을 입력하시오 :')
	print(100/int(num))
except Exception: # Exception은 가장 큰 범주
    print('에러는 모르지만 에러가 발생하였습니다.')
except ValueError:
    print('숫자를 넣어')
# 안녕
# 에러는 모르지만 에러가 발생하였습니다.
```

##### 종합

try : 코드 실행

except : try 에서 예외 발생시 실행

else : try에서 예외가 발생하지 않으면 실행

finally : 예외 발생 여부와 관련없이 항상 실행



### 예외 발생 시키기

* raise
  * 예외 강제 발생

```python
raise ValueError('값 에러 발생')
```

* assert statement
  * 예외 강제 발생(무조건 AssertionError 발생)
  * 디버깅 용도

```python
assert len([1,2])== 1, '길이가 아닙니다.'
```

