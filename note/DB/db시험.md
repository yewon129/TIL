Model

> 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

* 단일한 데이터에 대한 정보를 가짐
  * 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
* 저장된 데이터베이스의 구조(Layout)
* Django는 model을 통해 데이터에 접속하고 관리
* 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨



데이터베이스

* 체계화된 데이터의 모임

쿼리

* 데이터를 조회하기 위한 명령어
* 조건에 맞는 데이터를 추출하거나 조작하는 명령어
* query를 날린다 : DB 조작한다.

스키마

* 데이터베이스에서 자료의 구조, 표현방법, 관계등 정의한 구조

테이블

* 열 : 필드 or 속성
* 행 : 레코드 or 튜플



데이터베이스 기본구조

* 스키마 : 데이터베이스의 구조와 제약 조건(자료의 구조, 표현방법 관계)에 관련한 전반적인 명세를 기술
* 테이블 : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합, SQL 데이터베이스에서는 테이블을 관계라고도 한다.

열 (Column) : 각 열에는 고유한 데이터 형식이 지정된다. INTER TEXT NULL 등

행 (Row) : 테이블의 데이터는 행에 저장된다. user 테이블에 4명의 고객정보가 저장되어 있으며, 행은 4개 존재.

PK(기본키) : 각 행의 고유값 (Primary Key)  반드시 설정하여야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용

![image-20220418003329599](db%EC%8B%9C%ED%97%98/image-20220418003329599.png)



### ORM

* Object - Relational - Mapping
* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간에(Django - SQL)데이터를 변환하는 프로그래밍 기술
* OOP 프로그래밍에서 RDBMS을 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
* Django는 내장 Django ORM 사용

![image-20220418003801223](db%EC%8B%9C%ED%97%98/image-20220418003801223.png)

* 장점
  * SQL을 잘 알지 못해도 db 조작 가능
  * SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
* 단점
  * ORM만으로 완전한 서비스를 구현하기 어려운 경우가 있음
* 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것(생산성)



ORM 사용 이유 => 우리는 DB를 객체로 조작하기 위하여 ORM 사용



```python
# models.py

from django.db import models

class Article(models.Model):
    title = moels.CharField(max_length=10)
    content = models.TextField()
```

* models 모듈을 통해 어떠한 타입의 DB컬럼을 정의할 것인지 정의
  * title과 content는 모델의 필드를 나타냄
  * 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑

#### 사용 모델 필드

* `CharField(max_length=100)`
  * 길이에 제한 있는 문자열 넣을 때 사용
  * CharField의 max_length는 필수 인자
  * 필드의 최대 길이, 데이터베이스 레벨과 Django의 유효성 검사에서 활용
* `TextField()`
  * 글자의 수가 많을 때 사용
  * max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에는 적용되지 않음
  * max_length 사용은 CharField에서 사용해야 함



### Migrations

* 'Django가 model에 생긴 변화를 반영하는 방법'

* migration : 모델에 생긴 변화(필드를 추가했다던가 모델을 삭제했다던가 등등)를 반영하는 Django의 방식

* Migration 실행 및 DB 스키마를 다루기 위한 몇가지 명령어

  * makemigrations
    * model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용
  * migrate
    * 마이그레이션을 DB에 반영하기위해 사용
    * 설계도를 실제 DB에 반영하는 과정
    * 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

  * sqlmigrate
    * 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    * 마이그레이션이 SQL 문으로 어떻게 해석되어서 동작할지 미리 확인할 수 있음.
  * showmigrations
    * 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
    * 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인할 수 있음

```bash
$ python manage.py makemigrations  # migrations/0001_initial.py 생성
$ python manage.py migrate  # 0001_initial.py 설계도를 실제 DB에 반영
```

##### sqlmigrate

```bash
$ python manage.py sqlmigrate articles 0001
```

```sql
BEGIN;
CREATE TABLE 'articles_article'
('id' integer NOT NULL PRIMART KEY AUTOINTCREMENT,
'title' varchar(10) NOT NULL, 'content' text NOT NULL);
COMMIT;
```

* models.DateField
* auto_now_add
  * 최초 생성 일자
  * Django ORM이 최초 INSERT시에만 현재 날짜와 시간으로 갱신(테이블에 어떤 값을 최초로 넣을 때)
* auto_now
  * 최종 수정 일자
  * Django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신



### DB API

> DB를 조작하기 위한 도구

* django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
* Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동으로 만듦
* dataabase-abstract API 혹은 database-access API 라고도 함

##### 구문

Making query

Classname.Manager.QuerySet API

Article.objects.all()

* Manager
  * Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
  * 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가
* QuerySet
  * 데이터베이스로부터 전달받은 객체 목록
  * queryset 안의 객체는 0개, 1개 혹은 여러개일 수 있음
  * 데이터베이스로부터 조회, 필터, 정렬등을 수행할 수 있음

Django shell

* 일반 Python shell을 통해서는 장고 프로젝트 환경에 접근할 수 없음
* 그래서 장고 프로젝트 설정이 load된 Python shell을 활용해 DB API 구문 테스트 진행
* 기본 Django shell보다 더 많은 기능을 제공하는 shell_plus를 사용해서 진행

```bash
$ pip instal ipython
$ pip install django-extensions
```

```python
# settings.py
INSTALLED_APPS = [
    'django_extensions'
]
```

```bash
$ python manage.py shell_plus
```



#### CRUD

### CREATE

```shell
Article.objects.all()
<QuerySet []>
```

```shell
article = Article()
article # <Article: Article object (None)>
article.title = 'first'
article.content = 'django'
article # <Article: Article object(None)>
article.save()
article # <Article: Article object(1)>
```

```shell
article.title # 'first'
article.created_at # datetme.datetime(2019, 8, 21, 2, 43, 56, 49345)
```

```shell
article = Article(title='second', content='django')
article.save()
article # <Article: Article object (2)>
Article.objects.all() #<QuerySet [<Article: Article object(1)>, <Article: Article object(2)>]>
```

```shell
Article.objects.create(title='third', content='django')
#<Article: Article object (3)>
```

##### save() method

* saving objects
* 객체를 데이터베이스에 저장
* 데이터 생성 시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
  * ID 값은 Django가 아니라 DB에서 계산되기 때문
* 단순히 모델을 인스턴스화 하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save() 필요



* str method
  * 표준 파이썬 클래스의 메소드인 str()을 정의, 각각의 object가 사람이 읽을 수 있는 문자열을 반환(return)하도록 할 수 잇음
  * 작성 후 반드시 shell_plus를 재시작해야 반영

```python
# models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
```

### READ

* all()
  * 현재 QuerySet의 복사본을 반환

```shell
Article.objects.all()
# <QuerySet [<Article:Article object (1)>]>
```

* get()

  * 주어진 lookup 매개변수와 일치하는 객체 반환
  * 객체 없으면 DoesNotExist예외 발생
  * 둘이상의 객체 찾으면 MultipleObjectsReturned 예외 발생
  * primary key와 같이 교유성 보장하는 조회에서 사용

  ```shell
  article = Article.objects.get(pk=100)
  # DoesNotExist: Article matching query does not exist
  Article.objects.get(content='django')
  # MultipleObjectsReturned
  ```

* filter()

  * 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet 반환

  ```python
  Article.objects.filter(content='django')
  # <QuerySet [<Article:first>, <Article: third>]>
  
  Article.objects.filter(title='first')
  # <QuerySet [<Article: first>]>
  ```



### UPDATE

```shell
article = Article.objects.get(pk=1)
article.title = 'byebye'
article.save()
article.title # 'byebye'
```



### DELETE

* delete()

  * QuerySet의 모든 행에 대해 SQL 삭제 쿼리를 수행하고, 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리를 반환

  ```shell
  article = Article.objects.get(pk=1)
  article.delete()
  Article.objects.get(pk=1) # DoesNotExist
  ```



##### CRUD with views

```python
def index(request):
    articles = Article.objects.all()[::-1]
    or
    articles = Article.objects.order_by('-pk')
```



##### HTTP method

* .GET
  * 특정 리소스를 가져오도록 요청할 때 사용
  * 반드시 데이터를 가져올 때만 사용해야 함
  * DB에 변화를 주지 않음
  * CRUD에서 R 역할 담당
* .POST
  * 서버로 데이터를 전송할 때 사용
  * 리소스를 생성 / 변경하기 위해 데이터를 HTTP body에 담아 전송
  * 서버에 변경사항 만듦
  * CRUD에서 CUD 담당
* 사이트 간 요청 위조(Cross-site request forgery)
  * csrf
  * 웹 애플리케이션 취약점 중 하나로 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
  * django는 middleware와 template tag를 제공
  * {% csrf_token%}  => 없으면 403 forbidden



### Database

* 데이터베이스는 체계화된 데이터의 모임
* 여러사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
* 논리적으로 연관된 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
* 즉, 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

##### 데이터베이스로 얻은 장점

* 데이터 중복 최소화
* 데이터 무결성
* 데이터 일관성
* 데이터 독립성
* 데이터 표준화
* 데이터 보안 유지



#### 관계형 데이터베이스(RDB)

* Relational DataBase
* 키와 값들의 간단한 관계를 표 형태로 정리한 데이터베이스
* 관계형 모델에 기반

#### 관계형 데이터베이스 관리 시스템 (RDBMS)

* 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템

* SQLite
  * 비교적 가벼운 데이터베이스
  * 데이터 타입
    * NULL / INTEGER / REAL / TEXT / BLOB(별다른 타입 없이 그대로 저장)
  * Type Affinity
    * 특정 컬럼에 저장하도록 권장하는 데이터 타입
    * INTEGER / TEXT / BLOB / REAL / NUMERIC



### SQL (Structured Query Languge)

* 관계형 데이터베이스 관리시스템의 데이터관리를 위해 설계된 특수 목적 프로그래밍 언어
* 데이터베이스 스키마 생성 및 수정
* 자료의 검색 및 관리
* 데이터베이스 객체 접근 조정 관리

* 분류
  * DDL (데이터 정의 언어 : CREATE / DROP / ALTER)
  * DML(데이터 조작 언어 : INSERT / SELECT / UPDATE / DELETE)
  * DCL(데이터 제어 언어 : GRANT / REVOKE / COMMIT / ROLLBACK



##### 데이터베이스 생성

```sql
$ sqlite3 tutorial.sqlite3
sqlite> .database
```

```sql
.mode csv
.import hellodb.csv examples
.tables  # examples
```

```sql
SELECT * FROM examples;
```

```sql
.headers on  # 말 그대로 header(열 이름)
.mode column  # column 잘 나눠서
```

### 테이블 생성 및 삭제

* CREATE

```sql
CREATE TABLE classmates (
    id INTEGER PRIMART KEY,
    name TEXT);

.tables  # classmates examples
```

* 스키마 조회

```sql
.schema classmates
# CREATE TABLE classmates(
#id INTEGER PRIMARY KEY.
#name TEXT
#);
```

* DROP

```sql
DROP TABLE classmates;
.tables # examples
```

![image-20220418045327833](db%EC%8B%9C%ED%97%98/image-20220418045327833.png)

```sql
CREATE TABLE classmates(
name TEXT,
age INT,
address TEXT);
```

### CRUD

#### CREATE

```sql
INSERT INTO 테이블이름 (컬럼1, 컬럼2) VALUES (값1, 값2)
```

```sql
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
```

```sql
INSERT INTO classmates VALUES('홍길동', 30, '서울');
# 모든 열에 데이터가 있는 경우 컬럼을 명시하지 않아도 됨
SELECT * FROM classmates;
```

* id : rowid로 SQLite가 관리 중.
* 조회하려면 `SELECT rowid, * FROM classmates;`

* NOT NULL 옵션

```sql
DROP TABLE classmates;
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL);
```

=> 이때는 id를 내가 지정했기 때문에 자동으로 입력되지 않음

```sql
INSERT INTO classmates (name, age, address) VALUES (30, '홍길동', '서울');
```



#### READ

* classmates에서 id, name 컬럼 값 조회

```sql
SELECT rowid, name FROM classmates;
```

* classmates 에서 id, name컬럼 값 하나만 조회

```sql
SELECT rowid, name FROM classmates LIMIT 1;
```

* classmates에서 id, name 컬럼 값을 세번째에 있는 하나만 조회

```sql
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
```

=> 0부터 시작해서 LIMIT 10 OFFSET 5 라면 "6번째 행부터 10개행을 조회"

* 주소가 서울인 경우의 데이터 조회

```sql
SELECT rowid, name FROM classmates WHERE address='서울';
```

* age값 전체를 중복없이 조회하세요

```sql
SELECT DISTINCT age FROM classmates;
```

#### DELETE

* 중복 불가능한 rowid 기준으로 삭제

```sql
DELETE FROM classmates WHERE rowid=5;
```

* SQLite는 id 재사용!

* 재사용하지 않으려면!

```sql
CREATE TABLE classmates(
id INTEGER PRIMARY KEY AUTOINCREMENT,
...);
```

#### UPDATE

* 중복 불가능한 rowid 기준으로 수정

```sql
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
```



##################################

* users 테이블에서 age가 30이상인 유저의 모든 컬럼 조회

```sql
SELECT * FROM users WHERE age >= 30;
```

* users 테이블에서 age가 30 이상인 유저의 이름만 조회

```sql
SELECT first_name FROM users WHERE age >= 30;
```

* age 30 이상 성 '김'인 사람의 나이와 성만 조회

```sql
SELECT age, last_name FROM users WHERE age >= 30 and last_name='김';
```



### Aggregate Functions

* COUNT
* AVG
* MAX
* MIN
* SUM

##############################3

* users 테이블의 레코드 총 개수를 조회하면?

```sql
SELECT COUNT(*) FROM users;
```

* 30 이상 사람들의 평균 나이

```sql
SELECT AVG(age) FROM users WHERE age>=30;
```

* 계좌 잔액이 가장 높은사람과 그 액수 조회

```sql
SELECT first_name, MAX(balance) FROM users;
```

* 나이가 30 이상의 계좌 평균 잔액 조회

```sql
SELECT AVG(balance) FROM users WHERE age>=30;
```

#### LIKE

* % : 0개 이상의 문자
* _ : 임의의 단일 문자

* users 테이블에서 나이가 20대인 사람만 조회한다면?

```sql
SELECT * FROM users WHERE age LIKE '2_';
```

* users 테이블에서 지역 번호가 02인 사람만 조회한다면?

```sql
SELECT * FROM users WHERE phone LIKE '02-%';
```

* 이름이 준으로 끝나는 사람

```sql
SELECT * FROM users WHERE first_name LIKE '%준';
```

* 중간번호가 5114인 삶

```sql
SELECT * FROM users WHERE phone LIKE '%-5114-%'
```

#### ORDER BY

* ASC - 오름차순 (default) / DESC - 내림차순

* 나이순으로 오름차순 정렬하여 상위 10개

```sql
SELECT * FROM users ORDER BY age ASC LIMIT 10;
```

* 나이, 성 순으로 오름차순 정렬하여 상위 10개

```sql
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
```

* 게좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름 10개

```sql
SELECT first_name, last_name FROM users ORDER BY balance DESC LIMIT 10;
```

#### GROUP BY

* 각 성씨가 몇명씩 있는지 조회

```sql
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```



#### ALTER TABLE

```sql
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL,
);
```

```sql
INSERT INTO articles VALUES ('1번제목', '1번내용');
```

```sql
ALTER TABLE articles RENAME TO news;
```

```sql
ALTER TABLE news ADD COLUMN create_at TEXT NOT NULL DEFAULT '소제목';
```

