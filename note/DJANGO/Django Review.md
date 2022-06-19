# Django Review

### Model

> 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구

* 데이터베이스의 구조를 클래스를 통해 관리
* 데이터베이스 : 체계화된 데이터의 모임
  * 스키마 : 자료 구조 등 
* 쿼리 : 데이터를 조회하기 위한 명령어

### ORM : object - relational - mapping

SQL -> ORM -(object , querryset)-> Python -(Queryset API)->ORM ->SQL



##### models.py

```python
# articles/models.py

class Artice(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```



### migrations

> Django가 model에 생긴 변화를 반영하는 방법

1. makemigrations
   * 새로운 마이그레이션 만들 때 사용
2. migrate
   * 마이그레이션을 DB에 반영하는 과정
3. sqlmigrate
4. showmigrations

##### 3단계

1. models.py
   * model 변경사항 발생시
2. $ python manage.py makemigrations
   * migrations 파일 생성
3. $ python manage.py migrate
   * DB 반영 (모델과 db의 동기화)



### CRUD

* Read

```
>>> Article.objects.all()
<QuerySet []>
```

* CREATE

```
>>> article = Article()
>>> article
<Article:Article object (None)>
>>> article.title = 'd'
>>> article.content = 'django'
>>> article.save()
>>> article
<Article:Article object (1)>
```

```
>>> article = Article(title = 'second', content = 'django')
>>> article.save()
```

```
>>> Article.objects.create(title = 'third', content = 'django')  # save없어도 됨
```



* Read
  * all() : 전체
  * get() : 쿼리셋 x, 객체 반환 ( 없으면 DoesNotExist ), 둘이상 x
  * filter() : 검색이 안되어도 에러 없음



* UPDATE

```
>>> article.title = 'bye'
>>> article.save()
```

* DELETE

```
>>> article = Article.objects.get(pk=1)
>>> article.delete()
```



* Field lookup
  * 조회시 특정 검색 조건 지정

![image-20220406123808584](Django%20Review/image-20220406123808584.png)

#### 프로젝트 만들기

1. 가상환경 : 패키지 버전 관리

2. 프로젝트 생성 

   ```python
   django-admin startproject .
   ```

3. 앱 생성

4. 모델 정의 : 데이터 조작 정의 테이블 대응



#### 요청 처리

URL -> View -> Template

