












#### DOM 조작

* 조작 순서
  1. 선택 ( Select )
  2. 변경 ( Manipulation )
* 상속 구조
  * EventTarget
    * Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
  * Node
    * 여러가지 DOM 타입들이 상속하는 인터페이스
  * Element
    * Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
    * 부모인 Node와 그 부모인 EventTarget의 속성을 상속
  * Document
    * 브라우저가 불러온 웹페이지를 나타냄
    * DOM 트리의 진입점 역할 수행
  * HTMLElement
    * 모든 종류의 HTML 요소
    * 부모 elemnet의 속성 상속

##### DOM 선택 메서드

* document.querySelector(selector)
  * 
* document.querySelectorAll(selector)