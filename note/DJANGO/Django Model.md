# Django Model

#### Model

> 데이터 구조화 / 조작

DB를 조작하는 언어 : SQL (structured query language)

python과 SQL을 연결하는 것 : ORM - 파이썬 객체 조작으로 DB조작

Django(서버) : URL 요청이 들어오면 처리해서 응답

Model : 모델을 통해서

1. 데이터 구조화,클래스로 구조화, 이를 DB에 반영 (마이그레이션(migration:이주)).
   * migration : 파이썬으로 만든 것을 DB에 옮기는 것

2. 데이터를 조작, 객체를 조작 ,DB반영(Django ORM(쿼리문 작성))
   * 쿼리 : 질의



## Model

##### 데이터구조화(DB)

1. 클래스 만들기 ( models.py )
   * models.Model 상속
   * 속성 : 필드(타입)
2. 마이그레이션 파일 생성 ( makemigrations )
3. DB에 반영 ( migrate )

##### 데이터 조작(ORM) : 클래스(객체)조작으로 db를 조작하게삳.

* Article.objects.all() => QuerySet(리스트 형태)
* CRUD(Create Read Update Delete)

### 데이터 조작

#### create

* `save`메서드가 호출되는 순서 DB에 저장됨
  * id
  * pk (primary key)

```bash
#1. 객체 조작 + save
a1 = Article()
a1.title = '제목'
a1.content = '내용'
a1.save()

#2 . 객체조작 + save
a2 = Article(title = '제목', content = '내용')
a2.save()

#3. create메서드
a3 = Article.objects.create(title='제목', content='내용')
```

#### Read

##### all()

> 해당 클래스 데이터 조회 => QuerySet데이터

```bash
# 1. 전체 데이터 조회
Article.objects.all()
# => <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
```

##### get

> 단일 데이터 조회 => 객체

* 일반적으로 고유한 값(unique)인 경우 사용하는 메서드.
  * 결과가 없는 데이터 => 에러
  * 결과가 여러개 있는 데이터 => 에러
* `pk` : primary key는 데이터베이스에서 유일한값이므로 pk를 기준으로 조회할 때 사용

```bash
# 2. 단일 데이터 조회
Article.objects.get(pk=1)
# => <Article: Article object (1)>

# 2-1. 없는 데이터 => 에러
Article.objects.get(pk=100)
# => DoesNotExist: Article matching query does not exist.

# 2-2. 여러개 있는 경우 => 에러
Article.objects.get(title='제목')
# => MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

##### filter()

> 여러 데이터를 조회 => QuerySet (QuerySet은 리스트 형태)

```bash
Article.objects.filter(title='제목')
#=><QuerySet [<Article: Article object (1)>]>

# 없는 데이터
Article.objects.filter(title='냉무')
# => <QuerySet []>
```



#### Update

```bash
a2 = Article.objects.get(pk=2)
a2.title = '변경된 제목'
a2.save()
```

#### Delete

##### delete()

```bash
a3 = Article.objects.get(pk=3)
a3.delete()
```



## 게시판 만들기

urls - views - html

form : 사용자에게 입력을 받아서 서버에 전송

* 사용자 입력 : input
* 서버에 전송 : form(action, method), input(name)

