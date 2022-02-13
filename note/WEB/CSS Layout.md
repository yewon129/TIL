# CSS layout

#### CSS 원칙 1 (Normal Flow)

* block : 기본적으로 오른쪽에 margin 부여
  * div
* inline: 왼쪽에서 오른쪽으로 쌓임. (상하 margin 주지 않고, 너비 높이 부여 어려움)
  * span
  * input, img

* Positioning
  * absolute : static이 아닌 부모
  * fixed : 브라우저(Viewport)



#### Float

박스를 이동시켜 텍스트 포함 인라인요소들이 주변을 wrapping 하도록 함

* none : 기본값
* left : 요소를 왼쪽으로 띄움
* right : 요소를 오른쪽으로 띄움



1. 부모요소 높이가 0

   * 자식 float

   * clearing float (부모 요소)

   * ```html
     .clearfix::after {
     	contents:"";
     	display: block;
     	clear: both;
     }
     ```

2.  box2가 공간을 채움.



#### Flexbox

* 1차원 레이아웃 모델

* 축과 컨테이너의 개념

  * 축

    * main axis
    * cross axis
      * column 이면 main axis가 세로

  * 구성요소

    * 부모 요소(flex container) : flex item들이 놓여있는 영역

    * ```html
      .flex-container{
      	display: flex;
      }
      ```

    * 자식요소(flex item) : 컨테이너에 속해 있는 컨텐츠

* Flex box 사용 이유
  * (수동 값 부여 없이) 수직 정렬
  * 아이템의 너비와 높이 혹은 간격을 동일하게 배치 (알아서!)

##### Flex 속성

* 배치설정
  * flex-direction
  * flex-wrap
* 공간 나누기
  * justify-content (main axis)
  * align-content (cross axis)
* 정렬
  * align-items (모든 아이템을 cross axis 기준으로)
  * align-self

1. flex-direction

   * main axis 기준 방향 설정

     * row : 1 2 3

     * row-reverse : 3 2 1

     * column : 1

       ​				 2

     * colum-reverse : 2

       ​							 1

2. flex-wrap
   * wrap : container가 120 px, 개별 아이템 30 px로 구성되어, 너비 설정에 맞추어 안에 예쁘게 쌓여있음
     * 넘치면 그 다음 줄로 배치
   * nowrap : 아이템의 크기가 줄어 한줄로 배치됨.
   
3. flex-flow

   * flex-direction 과 flex-wrap의 shorthand
   * ex) flex-flow: row nowrap;

1. justify-content
   * flex-start
   * flex-end
   * center
   * space-between
   * space-around : item의 양옆의 공간이 균일
   * space-evenly : 전체 공간에서 균일
2. align-content : cross 축 기준.
3. align-items : 아이템을 cross aixs 기준으로 정렬
4. align-self : 개별 아이템을 cross axis 기준으로 정렬. (개별 아이템에 적용!)

[flex order] [flexbox]

[flexbox froggy]