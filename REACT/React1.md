# React

> A JavaScript library for building user interface

* 사용자 인터페이스(User Interface, UI)
  * react는 UI 라이브러리



프레임워크 vs 라이브러리

프레임워크 : 흐름의 제어권이 자신에게 있다.

라이브러리 : 흐름이 개발자에게 있다.



### 리액트 장점

* 빠른 업데이트 & 렌더링 속도
* Virtual DOM
  * 웹페이지를 담고 있는 **가상**의 큰 그릇
  * Virtual DOM에서 업데이트 된 것 중 Browser DOM에서 필요한 것만 가져가서 변화 시킨다.
* Component-Based
* 재사용성
  * 의존성 문제와 호환성 문제 등으로 재사용이 어려울 수 있다.
  * 개발 기간이 단축 됨
  * 유지 보수가 용이함
  * 리액트는 컴포넌트 기반으로 재사용성이 높다.
* 활발한 지식공유 & 커뮤니티
* 리액트 네이티브
  * 모바일 웹



### 리액트 단점

* 방대한 학습량
  * 기존과 다른 UI 라이브러리
* 높은 상태관리 복잡도





# 리액트 시작

```
npx create-react-app my-app
npm start
```

##### 파일 구조

![image-20221102162736726](React1.assets/image-20221102162736726.png)





### Redux
* Redux Toolkit
* middleware


### React vs Vue

* react는 UI 라이브러리 / Vue는 프레임워크
* react 
    * JSX(JavaScript XML) 형태로 코드를 작성하여 JavaScript 문법을 응용하기 때문에 JavaScript만으로 UI 로직과 DOM을 구현한다. 
* vue 
    * HTML, JS, CSS 코드 영역을 분리해서 작성한다. 
    * ".vue " 파일을 만들 때에도 패턴이 존재한다. 
    * ". vue"에서 <template>에 HTML 작성 영역, <script> 안에는 JS, <style> 안에 CSS를 작성한다.

* 리액트는 뷰에 비해 자유롭게 자바스크립트를 통해 코드를 구현할 수 있다. 
* 뷰는  정해진 방법만 사용하기 때문에 자유도가 낮지만 그만큼 코드 작성에 있어서 용이하다..


* react 
    * 컴포넌트의 생성 및 재사용이 용이하다. 
    * 파일별로 컴포넌트를 분리할 수 있으며, 새로운 함수형 컴포넌트를 생산하고, props 형태로 전달하거나 또는 다른 곳에서 재사용하는 것이 매우 용이하다.

* vue
    * 새로운 컴포넌트를 만들어 분리하기 위해서 새로운 파일을 하나 더 만들고, 그에 따라 하나의 파일에 해당하는 template, script, style 모두 작성해주어야 한다. 
    * props를 전달하는 과정에서도 해당 컴포넌트를 사용하는 모든 파일을 오가며 작성해주어야 한다.
