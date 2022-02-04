# WEB

## HTML & CSS

##### Browser

* 인터넷 익스플로러는 브라우저가 아니다. 주로 크롬을 사용
* Can I use?

#### HTML?

> 문서의 구조를 나타내는 태그

Hyper Text Markup Language

웹페이지를 작성(구조화)하기 위한 언어

.html

##### hyper text ? 

ex)위키백과 ( 링크에 있는 것을 하나 하나 누르면 다른 문서로 접근, 그 문서에서 다른 문서로 접근 가능)

##### markup language

* markdown과 유사.



#### html 기본구조

html(최상위 요소) - head(메타데이터) - body(본문)

```html
<!DOCTYPE html> # 규격
<html lang="ko">
<head> # 사람의 머리 (메타데이터)
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
</body>
</html>
```

##### head : 문서 메타데이터 요소

* 메타데이터 ? 
  * ex ) 사진 : 날짜, 조리개 값, gps 정보 등 사진을 설명하기 위한 데이터.

* title / meta / link / script / style
  * ex ) open graph protocol (섬네일에 설명 있는 것)

##### DOM(Document Object Model) 트리

* html문서(텍스트 파일)를 브라우저로 만들기(렌더링) 위한 구조
  * body : parent  - h1 or ul : children
  * sibling 관계

##### 요소

* ```<h1>: 여는 태그  </h1>:닫는 태그```

* 내용 없는 태그
  * br(엔터)(break line)
  * hr(수평선 그릴 때)(horizontal rule)
  * img(링크)(image)
  * input(사용자에게 내용을 받아야하므로 내용 없음), link, meta

##### 속성

* href : 속성명 "https://google.com" : 속성값

* 가능한 속성 : 
  * id(고유 식별자) / class(공통적으로 묶을 수 있음) / style 
    * title / data(java)  등

##### 시맨틱 태그

* tag에 header라고 적혀 있음. => 위에 내용을 의미할 것
* header를 바꾼다고 해도 돌아가는데는 문제가 없지만, 의미적으로 유용하지 못함.
* 문서를 분석할 때, 이해를 하기 쉬움.
  * google : 스포츠 - 주제 - 뉴스사 따라 vs naver: IT - 주제(같은 레벨이라서 헷갈림.)

* 이미지가 보여지지 않더라도 이미지 alt 속성을 지정하면 설명을 들을 수 있음.

### HTML 문서 구조화

#### 텍스트 요소

a : href 속성 활용, 다른 url로 연결하는 하이퍼링크 생성

b vs strong : 굵은 글씨

: b- bold / strong - 시맨틱 태그 (강조를 하고 싶은 의미)

i vs em : 기울임 글씨

: i-italic / em-시맨틱 태그 (강조를 하고 싶은 의미)

=> 의미적으로 다름.

br : 텍스트 내에 줄 바꿈

img : src 속성 활용, 이미지 표현

span : 의미 없는 인라인 컨테이너

[mdn](developer.mozilla.org)

#### 그룹 컨텐츠

p: 전체 문단을 묶을 때

hr : 수평선 그을 때

ol : 순서있는 리스트

ul : 순서없는 리스트

pre : ```

blockquote :꺽새로 표현하던 것(인용문)

div : 블럭 요소(의미 없는 것 묶을 때)

##### table

```python
<!DOCTYPE html>
<html>
  <head>
    <title>테이블 실습</title>
  </head>
  <body>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Major</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>홍길동</td>
          <td>Computer Science</td>
        </tr>
        <tr>
          <td>2</td>
          <td>김철수</td>
          <td>Business</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td>총계</td>
          <td colspan="2">2명</td>
        </tr>
      </tfoot>
      <caption>서울 2반</caption>
    </table>
  </body>
</html>
```

##### form

* 정보를 서버에 제출하기 위한 영역
  * action : form 처리할 서버의 url
  * methon : form 제출시 사용할 http 메서드
  * enctype : method가 post인 경우 데이터의 유형

##### input

* 다양한 타입 가지는 입력 데이터 유형과 위젯 제공
  * name : form control에 적용되는 이름
  * value : form control에 적용되는 값
  * required, readonly, autofocus, autocomplete, disabled

```html
<!--url : https://www.google.com/search?q=HTML-->
<form action="/search" method="GET">
    <input type="text" name="q">
</form>
```



##### input label

* label 클릭하여 input 활성화
* <input>의 id 속성을 <label> for 속성을 연관 시킴

##### input 유형

* text
* password : 입력시 *로 표현
* email : 이메일 형식 아닌 경우 제출 불가
* number : min, max, step 속성을 활용, 숫자 범위 설정 가능
* file : accept 속성 활용, 파일 타입 지정 가능
* 항목 중 선택
  * checkbox : 다중선택
  * radio : 단일 선택
  * value를 개발자가 지정해야 함.
* 기타
  * color / date / hidden

[input참고](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

