# Django 03

## Django Form

### Django Form Class

Django form : 유효성 검증 해준다.

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

* Form Class
  * field, field배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 대한 에러메세지 결정
  * 과중한 작업 줄여준다.



### ModelForm

* Django Form을 사용하다 보면 Model에 정의한 필드를 유저로부터 입력 받기 위해 Form에서 Model필드를 재정의하는 행위가 중복될 수 있음
* 그래서 Django는 ModelForm 제공



* Meta class

```python
from django import forms
from .models import Article

# ModelForm은 모델의 필드로 HTML을 만들어줌
# 필요햔 정보 ? 모델 / 필드
# ArticleForm의 정보를 담는 Meta 클래스
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

* 모델폼이 쉽게 해주는 것

1. 모델 필드 속성에 맞는 html element를 만들어주고
2.  이를 통해 받는 데이터를 view 함수에서 유효성 검사를 할 수 있도록 함.



```python
# views.py

def new(request):
	form = ArticleForm()
	context = {
		'form':form
	}
	return render(request, 'articles/new.html', context)

def create(reauest):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
    	return redirect('articles:detail', article.pk)
```





#### 질문

##### ModelForm 사용 이유

* HTML Form : 사용자로부터 정보를 받아서 서버에 전송하는 양식
  * 데이터베이스에 저장(django Model)

##### Form vs ModelForm

Form => DB필드 - HTML input // Db : 사용자 입력  

ModelForm 

	1. Model
	1. 필드

```
class ArticleForm(forms.ModelForm):
	class Meta:
		model
		fields
```

##### 구현

둘 중 하나 선택은 view에서 처리 : POST vs GET

- Form 화면

- Form 제출

  * Valid O
    * DB에 저장

  * Valid X
    * 사용자에게 에러메세지와 함께 Form 화면 보여주기





----------------------------------------------------------------------------------------

* **게시판 + ModelForm 활용해서 만들어보기**
* 게시판 (과거)
---
* 코드를 디테일하게 외우고 X
  * 모델 코드 처음부터 못 짜겠다.
  * 코드를 보고 어떤 내용이었는지 확인하고 작성하기.
* 순서
  * 가상환경
  * django 설치
  * 프로젝트 만들기
  * articles 앱 만들기 -> 등록 / urls.py 분리하기
  * article 모델 만들기 -> 마이그레이션 -> 마이그레이트
  * admin 등록해서 확인하기
  * 게시판 기능 구현 (urls.py => views.py => template/redirect)
    * 목록 페이지 만들기
    * 생성
    * 상세보기
    * 삭제
    * 수정