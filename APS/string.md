## APS(algorithm problem solving)

### 문자열

  문자열

* fixed length
* variable length
  * length controlled 
    * java 언어에서의 문자열
  * delimited
    * c 언어에서의 문자열



##### 두 코드 차이 이해하기

```python
s1 = list(input())
s2 = input()
print(s1)
print(s2)
s1[0] ='d'
print(s1[0])
# s1[0] = 'd' 를 하면 에러가 난다.(수정 불가)
print(s2[0])
```

```bash
 123
 123
 ['1', '2', '3']
 '123'
 d
 1
```



##### strlen() 함수

* 참고

```python
print('a', end='')
print('\n', end='')  # == print()
print('b')
```

```bash
a
b
```



```python
def mystrlen(s):
    i = 0
    while s[i] !='\0':
        i += 1
    return 1

a = ['a', 'b', 'c', '\0']
print(mystrlen(a))
```

```bash
3
```



##### python에서의 문자열 처리

* char 타입 없음
* 텍트스 데이터의 취급방법이 통일
* 문자열 기호
  * '' , "", ''', """"""
  * +연결
    * 문자열 + 문자열 : 이어 붙여주는 역할
  * *반복
    * 문자열 * 수 : 수만큼 문자열 반복
* 시퀀스 자료형. 인덱싱, 슬라이싱 연산 사용 가능
* replace(), split(), isalpha(), find()
* immutable



##### 문자열 뒤집기

1. 자기 문자열에서 뒤집는 방법
2. 새로운 빈 문자열을 만들어 소스의 뒈어서부터 읽어서 타겟에 쓰는 방법



##### 문자열 비교

* c strcmp() 함수를 제공
* java에서는 equals() 메소드 제공

파이썬에서는 == 연산자와 is 연산자를 제공한다.

```python
s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1==s2)
print(s1 is s2)
print(s5)
print(s1 == s5)
print(s1 is s5)
```

```
True
True
abc
True  ## 내용만 같으면 true
False ## 슬라이싱하면 새롭게 만들어지는 것, 참조가 다름.
```



```python
a = 'ab'
b = 'abc'
c = 'de'
d = 'Abc'

print(a<b)
print(a>b)
print(a<c)
print(a>c)
print(a<d)
print(a==d)
```

```
True
False
True
False
False
False
```

C 파일

```c
int my_strmp(const char *str1, const char *str2)
{
    int i = 0;
    while(str1[i] != '\0') break;
    {
        if(str1[i] != str2[i]) break;
        i++;
    }
    return(str1[i] - str2[i]);
}
```

python 파일

```python
def my_strcmp(s1, s2):
    if s1<s2:
        return -1
    elif s1>s2:
        return 1
    else:
        return 0
```



##### 문자열 숫자를 정수로 변환하기

int("123"), float("3.14")

```python
a = list(input())
print(a)
```

```
123
['1', '2', '3']
```

```python
a = list(map(int, input().split))
print(a)
```

```
123
[1, 2, 3]
```



int()와 같은 atoi() 함수

```python
def atoi(s):
    i = 0
    for x in s:
    	i = i*10 + ord(x) - ord('0')
	reutrn i
    
a = '123'
print(atoi(a))
```

```
123
```

#### 패턴 매칭

* 고지식한 알고리즘

* 카프-라빈 알고리즘
* KMP 알고리즘
* 보이어-무어 알고리즘



##### 고지식한 알고리즘

* 본문 문자열을 처음부터 끝까지 차례대로 순회하며 패턴 내의 문자들을 일일이 비교하는 방식으로 동작

```python
t = 'TTTTAACTT'
p = 'TTA'       # 패턴이 더 짧은 경우에 한정
N = len(t)
M = len(p)
ans = -1
for i in range(N-M+1):  # 비교 시작 인덱스
    for j in range(M):
        if t[i+j] != p[j]:
            break
    else:
        ans = i
        break
print(ans)

for i in range(N-M+1):  # 비교 시작 인덱스
    j = 0
    while j < M:
        if t[i+j] != p[j]:
            break
        j += 1
    if j==M: # 패턴을 찾음
        ans = i
        break
print(ans)
```



##### KMP 알고리즘

* 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행

* 패턴을 전처리하여 배열 next[M]을 구하여 잘못된 시작을 최소화함
  * next[M] : 불일치가 발생했을 때, 이동할 다음 위치

```python
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    
    j = 0
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    
```

