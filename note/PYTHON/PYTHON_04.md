# PYTHON 04

## module

### 모듈

* 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

### 패키지

* 특정 기능과 관련된 여러 모듈의 집합
* 패키지 안에는 또 다른 서브 패키지를 포함



```python
import pprint(a) # pprint : module
pprint.pprint(a)
```

vs

```python
from pprint import pprint # module / function
pprint(a)
```

or

```python
from pprint import *
```



```python
from package import module
from package.module import function, var, Class
```



### 파이썬 표준 라이브러리(Python Standard Library, PSL)

[파이썬 표준 라이브러리](https://docs.python.org/ko/3.10/library/index.html)

[자습서](https://docs.python.org/ko/3.10/index.html)



### 파이썬 패키지 관리자(pip)

```python
$pip install SomePackage # 최신 버전
$pip install SomePackage==1.0.5 # 특정 버전
$pip install 'SomePackage>=1.0.4' # 최소 버전

$pip uninstall SomePackage # 패키지 삭제

$pip list # 패키지 목록
$pip show SomePackage # 특정 패키지 정보

$pip freeze # pip istall에 활용되는 형식으로 설치된 패키지의 목록. 
$pip freeze > requirements.txt
$pip install -r requirements.txt
# 목록을 txt에 저장하여 그대로 설치 가능
```



### 가상환경

* 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음.
  * 라이브러리 A : 3 ver
  * 라이브러리 B : 2 ver
* 가상환경을 만들어 프로젝트별로 독립적인 패키지 관리 가능



### 총정리

##### 모듈 : 여러 함수를 파일(.py)로 모으고 싶다.

##### 패키지 : 여러 모듈을 모으고 싶다.

* 설치, 삭제, 목록 : pip

##### 라이브러리: 여러 패키지를 모으고 싶다.