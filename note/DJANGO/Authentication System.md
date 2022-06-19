# Authentication System

* django.contrib.auth에 Django contrib module로 제공
  * django.contrib.auth
  * django.contrib.contenttypes
* Authentication (인증)
  * 신원확인
  * 사용자가 자신이 누구인지 확인
* Authorization ( 권한, 허가 )
  * 권한 부여
  * 인증된 사용자가 수행할 수 있는 작업 결정



### HTTP

* 비연결 지향
  * 서버는 요청에 대한 응답을 보낸 후 연결 끊음

* 무상태
  * 연결 끊으면 상태 정보가 유지되지 않음
  * 클라이언트와 서버가 주고 받는 메시지들은 서로 독립적임

* 클라이언트와 서버가 지속적 관계 유지 위해 쿠키와 세션이 존재



#### 쿠키와 세션

##### 쿠키

* 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
* 사용자가 웹사이트 방문 시 해당 웹사이트 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  * 클라이언트가 서버에 로그인 요청시, 응답과 함께 쿠키를 준다. 이후 클라이언트가 요청을 보낼 때 매번 쿠키와 함께 요청을 보낸다.(로그인이 유지되는 것과 같이 보이기 위하여 쿠키를 붙혀서 보낸다)
* HTTP 쿠키는 상태가 있는 세션을 만들어 줌
* 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
  * 이를 이용해 사용자 로그인 상태 유지

##### 요청과 응답

1. 브라우저가 웹페이지에 요청
2. 서버가 페이지와 쿠키를 보냄
3. 브라우저가 같은서버의 다른 페이지 요청시 쿠키와 함께

##### 쿠키 사용 목적

1. 세션관리 ( Session management )
   * 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화 (Personalization)
   * 사용자 선호, 테마 등의 설정
3. 트래킹 (Tracking)
   * 사용자 행동을 기록 및 분석

##### 세션

* 사이트와 특정 브라우저 사이의 상태 유지시키는 것
* 클라이언트가 서버에 접속하면 서버가 특정 session id 발급,클라이언틑는 발급 받은 session id 쿠키에 저장
* 로그아웃 : 세션 삭제



##### 쿠키 lifetime

1. session cookies
   * 현재 세션이 종료되면 삭제
   * 브라우저가 현제세션이 종료되는 시기를 정의
2. persistent cookies
   * Expires속성에 지정된 날짜 혹은 Max-age기간 지나면 삭제



##### Session in Django

* Django의 세션은 미들웨어 통해 구현
* Django는 database-backed sessions 저장 방식을 기본 값으로 사용



### 로그인

> 사용자의 요청정보를 바탕으로 로그인
>
> 비밀번호가 맞는지 확인하는 프로세스

* `AuthenticationForm` : `forms.Form`

  ```python
  AuthenticationForm(request, request.POST)
  ```

* 로그인

  * 요쳥정보, 사용자정보

    ```python
    from django.contrib.auth import login as auth_login
    auth_login(request, form.get_user())
    ```

* 로그인 완료된 이후

  * `@login_required`: 요청 url로그인 완료한 다음으로 넘어갈 원래 주소

  ```python
  redirect(request.GET.get('next') or 'article:index')
  ```

* 로그인은 로그인하지 않은 사람만

```python
if request.user.is_authenticated:
    return redirect('articles:index')
```



### 로그아웃

* 로그아웃 기능

```python
from django.contrib.auth import logout as auth_logout
auth_logout(request)
```

* 로그아웃은 로그인 한사람만

```python
if request.user.is_authenticated:
```



### 회원관리

#### 회원가입(User Create)

* `UserCreationForm`: `forms.ModelForm`

##### 선택적인 부분

* 로그인 되어 있으면 => 회원가입 왜해?

```python
if request.user.is_authenticated:
    return redirec('articles:index')
```

* 회원가입한 다음에 로그인 자동으로 해줄까?

```python
auth_login(request, user)
return redirect('articles:index')
```

* 만약 회원가입하고 로그인 직접 하려면?

```python
if form.is_valid():
    user = form.save()
    return redirect('accounts:login')
```



#### 회원 삭제(User Delete)

* 회원 삭제하면 로그아웃 시켜야함

* 회원정보는 어디서 가져와?

  ```python
  request.user
  # 삭제
  request.user.delete()
  ```



#### 회원 수정(User Update)

* `CustomUserChangeForm`

  * 직접 필드를 커스텀한다.

  ```python
  class CustomUserChangeForm(UserChangeForm):
      class Meta:
          model = get_user_model()
          fields = ('email', 'first_name', 'last_name',)
  ```

* 회원 정보 가져오는 곳? => `request.user`



#### 비밀번호 수정 (password)

* `PasswordChangeForm`: `forms.Form`
  * 옛날 비밀번호가 맞는지 확인
  * 비밀번호 두개가 맞는지 확인