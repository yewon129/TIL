# Database

### 데이터베이스(DB)

* 체계화된 데이터의 모임
* 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체



### 관계형 데이터베이스 (RD : Relational Database)

* 키와 값들의 간단한 관계를 **표** 형태로 정리한 데이터베이스

##### 스키마(schema) : 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술.

| column  | datatype |
| :-----: | :------: |
|   id    |   INT    |
|  name   |   TEXT   |
| address |   TEXT   |
|   age   |   INT    |

##### 테이블(table) : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

|  id  |  name  | address | age  |
| :--: | :----: | :-----: | :--: |
|  1   | 홍길동 |  제주   |  20  |
|  2   | 김길동 |  서울   |  30  |
|  3   | 박길동 |  독도   |  40  |

* 열(column) : 각 열에는 고유한 데이터 형식이 지정됨.
* 행(row) : 실제 데이터가 저장되는 형태
* 기본키(Primary Key) : 각 행(레코드)의 고유 값
  * 반드시 설정해야 함(id)



### 관계형 데이터베이스 관리 시스템 (RDBMS)

##### Sqlite Data Type

1. NULL
2. INTEGER
3. REAL : 소수점 값
4. TEXT
5. BLOB : 입력된 그대로 저장된 데이터



### SQL (Structured Query Language)

* 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어.

| 분류 |                    개념                     |                예시                |
| :--: | :-----------------------------------------: | :--------------------------------: |
| DDL  | 구조(테이블, 스키마)를 정의하기 위한 명령어 |        CREATE/ DROP/ ALTER         |
| DML  |  데이터를 저장,조회,수정,삭제 위한 명령어   |   INSERT/ SELECT/ UPDATE/ DELETE   |
| DCL  |      사용자의 권한 제어를 위한 명령어       | GRANT / REVOKE / COMMIT / ROLLBACK |



#### 테이블 생성 및 삭제

```sqlite
$ sqlite3 tutorial.sqlite3
sqlite> .database
sqlite> .mode csv
sqlite> .import hellodb.csv examples => csv를 테이블 형태로 다룸.
```

* SELECT : 특정 테이블의 레코드 정보를 반환

```sql
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
```

```sqlite
.headers on -- 분류 추가
.mode column -- 줄맞춤
```

* 테이블 생성 statement

```sqlite
CREATE TABLE 테이블이름 (
	name TEXT,
    age INT,
    address TEXT
);
```

* 테이블 확인

```sqlite
sqlite> .schema classmates
CREATE TABLE classmates(
name TEXT,
age INT,
address TEXT
);
```

* 테이블 삭제 statement

```sqlite
DROP TABLE 테이블이름;
```



##### 참고

sqlite 파일 우 클릭 => Open Database

SQLITE EXPLORER => tutorial.sqlite3 => New Query



### CRUD

#### CREATE

* INSERT : 테이블에 단일 행 삽입

```sqlite
INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);
```

* Q . 이름이 홍길동이고 나이가 23인 데이터 넣기

```sqlite
INSERT INTO classmates(name, age) VALUES('홍길동, 23');
```

* Q . 이름이 홍길동, 나이 30, 주소 서울인 데이터 넣기
  * 모든 열에 데이터가 있는 경우 column 명시하지 않아도 됨.


```sqlite
INSERT INTO classmates VALUES('홍길동', 30, '서울');
```



* SQLite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 자동으로 rowid 컬럼을 정의

```sqlite
SELECT rowid, * FROM classmates;
```



* NOT NULL 설정

```sqlite
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);
```

* Q . 이름 홍길동, 나이 30, 주소 서울
  * 스키마에 id 직접 작성했으므로 입력한 column을 명시하지 않으면 자동 입력 안됨

![image-20220314134629098](C:/Users/sky25/AppData/Roaming/Typora/typora-user-images/image-20220314134629098.png)

```sqlite
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
```



```sqlite
CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INT NOT NULL, 
  address TEXT NOT NULL
);

INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');

SELECT * FROM classmates;
```

