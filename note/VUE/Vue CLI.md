# Vue CLI



### SFC (Single File Component)

##### Component

> 재사용 가능한 부품

* 기본 html 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움을 줌

* 단일 파일에서의 개발
  * 코드 양 많아지면 유지보수 어려움
  * 한 화면을 구성하는 여러 컴포넌트를 만듦

##### SFC

> .vue 확장자를 가진 파일
>
> html, css, javascript 코드가 다 있다!



##### Vue Component 구조 예시

* 트리 : 사이클이 일어나지 않는 그래프
  * 1번 노드(컴포넌트) : 가장 바깥 프레임
  * 2, 3, 4 번 노드 : 그 안에 박스
  * 그 안의 박스들
  * 조립되는 각 컴포넌트.
* 반드시 파일 단위로 구분되어야 하는 것은 아니지만, 우리는 이렇게 사용함.



### Vue CLI

##### Node.js

* 브라우저가 아닌 환경에서 구동할 수 있도록 하는 자바스크립트 런타임 환경
* 플랫폼

##### NPM (Node Package Manager)

python 에서 pip 같은 존재.

설치 도와준다



#### Babel

* JavaScript compiler
* 자바스크립트 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해 주는 도구
* 신버전을 구버전으로 번역해줘야 다른 브라우저에서도 작동 가능



#### Static Module Bundler

* 모듈은 단지 파일 하나를 의미
* 라이브러리를 만들어 모듈 불러오거나 코드를 파일단위로 작성하는 노력 생김.
* 여러 모듈 시스템(import 구문)
  * ESM (ECMA Script Module)
  * AMD
  * CommonJS
  * UMD
* 모듈 의존성 문제
  * 모듈의 수가 많아지고 라이브러리 혹은 모듈 간 의존성이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
  * Webpack이 등장하게 됨.

* Bundling : 의존성 해결하는 작업
  * **Webpack**은 Bundler 중 하나



### Pass Props & Emit Events

* components











