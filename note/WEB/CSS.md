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

#### CSS 정의 방법

* 인라인
* 내부 참조
* 외부 참조 (주로 이것을 사용)



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
* 인라인 `style`

* `*` < `태그명` < `.class` <`#id`
  * 같은 점수일 경우 CSS가 나중에 선언된 것.

#### CSS 상속

* 상속 되는 속성 (눈에 보이는 시각적인 요소)
  * style


* 상속 되지 않는 속성
  * margin, box, position



### CSS 기본 스타일

* em
  * 바로위, 부모 요소에 대한 상속의 영향 받음
  * 배수단위, 요소에 지정된 사이즈에 상대적인 크기.
* rem

```html
<html lang="en">
<head>
  <title>Document</title>
  <style>
    .em {
      font-size: 1.5em;
    }

    .rem {
      font-size: 1.5rem;
    }
  </style>
</head>
<body>
  <!-- 부모(root => 16px) 대비 1.5배 ul => 24px-->
  <ul class="em">
    <!-- 부모(ul) 대비 1.5배 => 36px-->
    <li class="em">1.5em</li>
    <!--root 대비 1.5배 => 24px-->
    <li class="rem">1.5rem</li>
    <li>no class</li>
  </ul>
</body>
</html>
```

* viewport

#### 결합자





### CSS Boxmodel

> 모든 요소가 네모

* box model 구성요소
  * contents : 글이나 이미지 등 요소의 실제 내용
  * padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경색. 이미지는 padding까지 적용
  * border : 테두리 영역
  * margin : 테두리 바깥의 외부여백. 배경색 지정 불가
* box model 너비지정(`box-sizing`)

> 너비 지정할건데 기준을 무엇으로 할것인지?

* content의 사이즈 - box(기본값)
* border-box => 일반적 선호



### CSS Display

* block 
  * 아래로 쌓임
  * 줄 바꿈
  * 화면 크기 **전체**의 가로 폭을 차지
  * 블록 레벨 요소 안에 인라인 레벨 요소가 들어 있음.
    * `div / ul, ol , li /p / hr / form`
  * block : 너비를 가질수 없다면 자동으로 margin이 부여됨.
* inline
  * 우측으로 쌓임 
  * 줄 바꿈 일어나지 않는 행의 일부 요소
  * **content 너비**만큼 가로 폭 차지
  * **width, height, margin-top, margin-bottom 지정 불가**
    * 정의가 content 너비만큼만 차지하므로 
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



##### chrome devtools (ctrl + shift + i)

* view and chages css
