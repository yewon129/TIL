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

![image-20220628232257229](Vue%20CLI/image-20220628232257229.png)

* components

  * Vue app은 자연스럽게 중첩된 컴포넌트 트리로 구성됨
  * 컴포넌트간 부모-자식 관계가 구서되며 이들 사이에 필연적으로 위사 소통이 필요함
  * 부모는 자식에게 데이터를 전달(Pass props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event)
    * 부모와 자식이 명확하게 정의된 인터페이스를 통해 격리된 상태를 유지할 수 있음

  * **props는 아래로, events는 위로**
  * 부모는 props를 통해 자식에게 데이터를 전달하고, 자식은 events를 통해 부모에게 메시지를 보냄.

* 컴포넌트 구조

  * 템플릿 (HTML)
    * HTML의 body 부분
    * 각 컴포넌트를 작성

  * 스크립트(JavaScript)
    * JavaScript가 작성되는 곳
    * 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스가 구성하는 대부분이 작성됨

  * 스타일 (CSS)
    * CSS가 작성되며 컴포넌트의 스타일을 담당

* 컴포넌트 등록 3단계

  * 불러오기 (import)
  * 등록하기 (register)
  * 보여주기 (print)

  ```vue
  <template>
  	<div id="app">
          <img alt="Vue logo" src="./assets/logo.png">
          <!-- 3. 보여주기 -->
          <about></about>
      </div>
  </template>
  
  <script>
  // 1. 불러오기
  import About from './components/About.vue'
  
  export default {
      name: 'App',
      components: {
          //2. 등록하기
          About
      }
  }
  </script>
  ```

  

#### Props

* props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
* 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
* 데이터는 props 옵션을 사용하여 자식 컴포넌트로 전달됨
* 주의
  * 모든 컴포넌트 인스턴스에는 자체 격리된 범위가 있음
  * 자식 컴포넌트의 템플릿에서 상위 데이터를 직접 참조할 수 없음.

##### Static Props 작성

* 자식 컴포넌트(About.vue)에서 보낼 prop 데이터 선언
* `prop-data-name="value"`

```vue
//App.vue 
<template>
	<div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <about my-message="This is prop data"></about>
    </div>
</template>
```

* 수신할 prop 데이터를 명시적으로 선언 후 사용

```vue
// About.vue

<template>
	<div>
        <h1>About</h1>
        <h2>{{ myMessage }}</h2>
    </div>
</template>

<script>
export default {
    name: 'About',
    props: {
        myMessage: String,
    }
}
</script>
```



##### Dynamic props 작성

* v-bind directive를 사용해 부모의 데이터의 props를 동적으로 바인딩
* 부모에게 데이터가 업데이트 될 때마다 자식 데이터로도 전달 됨

```vue
// App.vue

<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <the-about 
      my-message="This is prop data" 
      :parent-data="parentData"
    ></the-about>
  </div>
</template>


<script>
import TheAbout from './components/TheAbout.vue'

export default {
  name: 'App',
  components: {
    TheAbout,
  },
  data: function () {
    return {
      parentData: 'This is parent data by v-bind'
    }
  },
}
</script>
```

* 수신 할 데이터를 명시적으로 선언 후 사용

```vue
//TheAbout.vue

<template>
	<div>
        <h1>About</h1>
        <h2>{{ myMessage }}</h2>
        <h2>{{ parentData }}</h2>
    </div>
</template>

<script>
export default {
    name: 'About',
    props: {
        myMessage: String,
        parentData: String,
    }
}
</script>
```

##### Props 이름 컨벤션

* during declaration (선언 시)
  * camelCase
* in template(HTML)
  * kebab-case

`컴포넌트의 data는 반드시 함수여야 함.`

`JavaScript 숫자를 전달하려면 값이 JavaScript 표현식으로 평가되도록 v-bind를 사용해야함`



##### 단방향 데이터 흐름

* 모든 props는 하위 속성과 상위 속성 사이의 단방향 바인딩을 형성
* 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안됨
  * 자식 요소가 의도치 않게 부모 요소의 상태를 변경하여 앱의 데이터 흐름을 이해하기 어렵게 만드는 일을 방지
* 부모 컴포넌트가 업데이트될 때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트됨
