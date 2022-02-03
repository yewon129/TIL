# WEB

## HTML & CSS

인터넷 익스플로러는 브라우저가 아니다. 주로 크롬을 사용

#### HTML?

> 문서의 구조를 나타내는 태그

Hyper Text Markup Language

웹페이지를 작성(구조화)하기 위한 언어

.html

##### hyper text ? 

ex)위키백과 ( 링크에 있는 것을 하나 하나 누르면 다른 문서로 접근, 그 문서에서 다른 문서로 접근 가능)

##### markup language



#### html 기본구조

html(최상위 요소) - head(메타데이터) - body(본문)

메타데이터 ? 

ex ) 사진 : 날짜, 조리개 값, gps 정보 등 사진을 설명하기 위한 데이터.

##### head

title / meta / link / script / style

ex ) open graph protocol

##### DOM(Document Object Model) 트리

html문서를 브라우저로 만들기 위한 구조

body : parent

h1 or ul : children

##### 요소

* ```<h1>: 여는 태그  </h1>:닫는 태그```

* 내용 없는 태그
  * br(엔터), hr(수평선 그릴 때), img, input(사용자에게 내용을 받아야하므로 내용 없음), link, meta

##### 속성

* href : 속성명 "https://google.com" : 속성값

* 가능한 속성 : i
  * id / class / style 
    * title / data  등



##### 시맨틱 태그

### HTML 문서 구조화

#### 텍스트 요소

a : href 속성 활용, 다른 url로 연결하는 하이퍼링크 생성

b vs strong : 굵은 글씨

: b- bold / strong - 시맨틱 태그

i vs em : 기울임 글씨

: i-italic / em-시맨틱

=> 의미적으로 다름.

br : 텍스트 내에 줄 바꿈

img : src 속성 활용, 이미지 표현

span : 의미 없는 인라인 컨테이너

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
* 기타
  * color / date / hidden

[input참고](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)



## CSS

> 스타일을 지정하기 위하여 필요한 것?
>
> 선택자
>
> 같은 속성이 다르게 지정되어 있으면 어떻게 선택?
>
> 선택자 우선순위
>
> 태그가 복잡하게 되어있는데 자식에게 상속되는 CSS가 있다.
>
> (아니라면 모두 다 지정 해줘야 함)

CSS : Cascading Style Sheets

스타일을 지정하기 위한 언어

#### 선택자

* `*` : 전체 선택
* `태그명` : 요소 선택자
* `class` : class 선택자
* `# id` : id 선택자
* `div > .children` : 자식 선탲가
  * div 태그 바로 밑에 있는 children 클래스를 가진 것
* `div . baby` : 자손 선택자
  * div 태그 하위 모든 baby 클래스를 가진 것

#### 기본 선택자 우선순위

* `! important` 
*  인라인 `style`

* `*` < `태그명` < `.class` <`#id`
  * 같은 점수일 경우 CSS가 나중에 선언된 것.

#### CSS 상속

* 상속 되는 속성 -> style
* 상속 되지 않는 속성 => box, position



### CSS 기본 스타일

* em
  * 바로위, 부모 요소에 대한 상속의 영향 받음
  * 배수단위, 요소에 지정된 사이즈에 상대적인 크기.
* rem



### CSS Boxmodel

> 모든 요소가 네모

* box model 구성요소
  * contents
  * padding
  * border
  * margin
* box model 너비지정(`box-sizing`)

> 너비 지정할건데 기준을 무엇으로 할것인지?

* content - box(기본값)
* border-box => 일반적 선호



### CSS Display

* block 
  * 줄 바꿈
  * 화면 크기 전체의 가로 폭을 차지
  * 블록 레벨 요소 안에 인라인 레벨 요소가 들어 있음.
    * `div / ul, ol , li /p / hr / form`
* inline 
  * 줄 바꿈 일어나지 않는 행의 일부 요소
  * content 너비만큼 가로 폭 차지
  * width, height, margin-top, margin-bottom
  * 상하 여백 : line-height로 지정
    * `span / a / img / input, label / b, em, i, strong`

* inline-block
  * block과 inline 레벨 요소의 특징
  * inline처럼 한줄에 표시 가능
  * block처럼 width, height, margin 속성 지정 가능
* none
  * 화면에표시하지 않고, 공간 부여 X



### CSS Position

* static
* 좌표 프로퍼디(`top, bottom, left, right`) 사용하여 이동 가능
  * relative : 상대위치
    * 자신의 static 위치를 기준
    * 레이아웃에서 요소가 차지하는 공간은 static과 같음
  * absolute : 절대위치
    * 일반적인 흐름에서 제거 후 레이아웃에 공간 차지 않음
    * static 아닌 가장 가까이 있는 부모 요소를 기준
  * fixed : 고정위치
    * 스크롤 시에도 항상 같은 위치



