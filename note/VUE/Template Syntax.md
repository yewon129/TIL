## Template Syntax

* 렌더링 된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문 사용

1. Interpolation
2. Directive

#### Interpolation(보간법)

* Text 
  * `<span> 메시지: {{ msg }} </span>`
* Raw HTML
  * `<span v-html="rawHtml"></span>`
* Attributes
  * `<div v-bind:id="dynamicId"></div>`
* JS 표현식
  * {{ number + 1 }}
  * {{ message.split('').reverse().join('')}}



#### Directive

* v-접두사가 있는 특수 속성
* 속성 값은 단일 JS 표현식이 됨(v-for 예외)
* 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할 함
* 전달인자(Arguments)
  * `:`  : (콜론)을 통해 전달인자를 받을 수도 있음
* 수식어
  * `.`: (점)으로 표시되는 특수 접미사
  * directive를 특별한 방법으로 바인딩해야 함을 나타냄



##### v-text

* 엘리먼트의 textContent를 업데이트
* 내부적으로 interpolation문법이 v-text로 컴파일 됨

```vue
<div>
    <p v-text="message"></p>
    <!--같음-->
    <p>{{message}}</p> 
</div>

<script>
const app = new Vue({
    el:'#app',
    data: {
        message: 'hello'
    }
})
</script>
```



##### v-html

* 엘리먼트의 innerHTML을 업데이트
  * XSS 공격에 취약할 수 있음
* 임의로 사용자로부터 입력 받은 내용은 v-html에 **절대 사용 금지**



##### v-show

* 조건부 렌더링 중 하나
* 요소는 항상 렌더링 되고 DOM에 남이있음
* 단순히 엘리먼트에 display CSS 속성을 토글하는 것

```vue
<body>
    <div id="app">
        <p v-show="isTrue">
            true
        </p>
        <p v-show="isFalse">
            false
        </p>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
            isTrue: true,
            isFalse: false,
        }
    })
    </script>
</body>
```



##### v-if, v-else-if, v-else

* 조건부 렌더링 중 하나
* 조건에 따라 요소를 렌더링
* directive의 표현식이 true일 때만 렌더링
* 엘리먼트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨



##### v-show 와 v-if

* v-show
  * CSS display 속성을 hidden으로 만들어 토글
  * 실제로 렌더링은 되지만 눈에서 보이지 않는 것이기 때문에 딱 한번만 렌더링이 되는 경우라면 v-if에 비해 상대적으로 렌더링 비용이 높음
  * 하지만, 자주 변경되는 요소라면 한 번 렌더링 된 이후부터는 보여주는지에 대한 여부만 판단하면 되기 때문에 토글 비용이 적음
* v-if
  * 전달인자가 false인 경우 렌더링 되지 않음
  * 화면에서 보이지 않을 뿐만 아니라 렌더링 자체가 되지 않기 때문에 렌더링 비용이 낮음
  * 하지만, 자주 변경되는 요소의 경우 다시 렌더링 해야 하므로 비용이 증가할 수 있음



##### v-for

* 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러 번 렌더링
* item in items 구문 사용
* item 위치의 변수를 각 요소에서 사용할 수 있음
  * 객체의 경우는 key
* v-for 사용 시 반드시 key 속성을 각 요소에 작성
* v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음
  * 단, 가능하면 v-if와 v-for를 동시에 사용하지 말 것

```vue
<body>
    <div id="app">
        <div v-for="fruit in fruits">
            {{ fruit }}
        </div>
        <div v-for="(fruit, index) in fruits" :key="`fruits-${index}">
            {{ fruit }}
        </div>
        <div v-for="todo in todos" :key="todo.id">
            {{ todo.title }} : {{ todo.complete }}
        </div>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
            fruits: ['apple', 'banana', 'coconut'],
            todos: [
                {id:1, title;'todo1', completed: true},
                {id:2, title:'todo2', completed: false},
            ]
        }
    })
    </script>
</body>
```



##### v-on

* 엘리먼트에 이벤트 리스너를 연결
* 이벤트 유형은 전달인자로 표시
* 특정 이벤트가 발생했을 때, 주어진 코드가 실행 됨
* 약어
  * @
  * `v-on: click => @click`

```vue
<body>
    <div id="app">
        <button v-on:click="doAlert">
            BUTTON
        </button>
        <form action="/articles/" @submit.prevent>
            <button>SUBMIT</button>
        </form>
        <input @keyup.enter="onEnter">
        {{message}}
        <button @click="changeMessage">
            button
        </button>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
            message: 'Hello',
        },
        methods: {
            doAlter: function(){
                alert('hello')
            },
            onEnter: function(event){
                console.log(event)
                console.log(event.target.value)
            },
            onInputEnter: function(onInputValue) {
                console.log(onInputValue)
            },
            changeMessage: function(){
                this.message = 'bye'
            }
        }
    })
    </script>
</body>
```



##### v-bind

* HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당
* Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당
* 약어
  * : (콜론)
  * `v-bind:href => :href`

```vue
<body>
    <div id="app">
        <!-- 속성 바인딩 -->
        <img v-bind:src="imageSrc">
        <img :src="imageSrc">
        
        <!-- 클래스 바인딩 -->
        <div :class="{active: isRed}">
            클래스 바인딩
        </div>
        <h2 :class="[activeRed, myBackground]">
            Hello Vue.js
        </h2>
        <!-- 스타일 바인딩 -->
        <ul>
          	<il v-for="todo in todos" :class="{active: todo.isActive}" :style="{fontSize:fontSize + 'px'}">
            {{ todo }}
            </il>
        </ul>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
            imageSrc: 'https://pcsum.photos/200/300/',
            isRed: true,
            activeRed: 'active',
            myBackground: 'my-background-color',
            todos: [
                {id:1, title:'todo 1', isActive: true},
                {id:2, title:'todo 2', isActive: false},
            ],
            fontSize:30,
        },
        methods: {
            doAlter: function(){
                alert('hello')
            },
            onEnter: function(event){
                console.log(event)
                console.log(event.target.value)
            },
            onInputEnter: function(onInputValue) {
                console.log(onInputValue)
            },
            changeMessage: function(){
                this.message = 'bye'
            }
        }
    })
    </script>
</body>
```



##### v-model

* HTML form 요소의 값과 data를 양방향 바인딩
* 수식어
  * .lazy
    * input 대신 change 이벤트 이후에 동기화
  * .number
    * 문자열을 숫자로 변경
  * .trim
    * 입력에 대한 trim을 진행

```vue
<body>
    <div id="app">
        <h2>1. input => data</h2>
        <h3>{{ myMessage }}</h3>
        <input @input="onInputChage" type="text">
        <h2>2. input <=> data</h2>
        <h3>{{ myMessage2 }}</h3>
        <input v-model="myMessage2" type="text">
        <h2>3. Checkbox</h2>
        <input type="checkbox" id="checkbox" v-model="checked">
        <label for="checkbox">{{checked}}</label>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
            myMessage:'',
            myMessage2: '',
            checked: true,
        },
        methods: {
            onInputChange: function(event) {
                this.myMessage = event.target.value
            },
        }
    })
    </script>
</body>
```



##### Options/Data - 'computed'

* 데이터를 기반으로 하는 계산된 속성
* 함수의 형태로 정의하지만 함수가 아닌 함수의 반환 값이 바인딩 됨
* 종속된 데이터에 따라 저장(캐싱)됨
* 종속된 데이터가 변경될 때만 함수를 실행
* 즉, 어떤 데이터에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않음
* 반드시 반환 값이 있어야 함

```vue
<body>
    <div id="app">
        <p> {{ num }}</p>
        <p> {{ doubleNum }}</p>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
        	num:2
        },
        computed: {
            doubleNum: function(){
                return this.num * 2
            }
        }
    })
    </script>
</body>
```



##### computed & methods

* computed 속성 대신 methods에 함수를 정의할 수도 있음
  * 최종 결과에 대해 두 가지 접근 방식은 서로 동일
* 차이점은 computed 속성은 종속 대상을 따라 저장(캐싱) 됨
* 즉, computed는 종속된 대상이 변경되지 않는 한 computed에 작성된 함수를 여러 번 호출해도 계산을 다시 하지 않고 계산되어 있던 결과를 반환
* 이에 비해 methods를 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행



##### options/Data - 'watch'

* 데이터를 감시
* 데이터에 변화가 일어났을 때 실행되는 함수

```vue
<body>
    <div id="app">
        <p> {{ num }}</p>
        <button @click="num +- 1">
            add 1
        </button>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
        	num:2,
        },
        watch: {
            num: function(){
                console.log(`${this.num}이 변경되었습니다.`)
            }
        }
    })
    </script>
</body>
```



##### computed & watch

* computed
  * 특정 데이터를 직접적으로 사용/사공하여 다른 값으로 만들 때 사용
  * 속성은 계산해야 하는 목표 데이터를 정의하는 방식으로 소프트웨어 공학에서 이야기하는 '선언형 프로그래밍' 방식
    * 선언형 프로그래밍 : 계산해야 하는 목표 데이터를 정의
  * `특정 값이 변동하면 해당 값을 다시 계산해서 보여준다.`
* watch
  * 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용
  * 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수를 실행하는 방식
  * 소프트웨어 공학에서 이야기하는 '명령형 프로그래밍' 방식
    * 명령형 프로그래밍 : 데이터가 바뀌면 특정 함수를 실행
  * `특정 값이 변동하면 다른 작업을 한다.`
  * 특정 대상이 변경되었을 때 콜백 함수를 실행시키기 위한 트리거
* computed와 watch는 어떤 것이 더 우수한 것이 아닌 사용하는 목적과 상황이 다름



##### Options/Assets - 'filter'

* 텍스트 형식화를 적용할 수 있는 필터
* interpolation 혹은 v-bind를 이용할 때 사용 가능
* 필터는 자바스크립트 표현식 마지막에 | (파이프)와 함께 추가되어야 함
* 이어서 사용 가능

```vue
<body>
    <div id="app">
        <p> {{ numbers | getOddNums | getUnderTenNums }}</p>
    </div>
    
    <script src="https://cdn.jsdeliver.net/npm/vue/dist/vue.js"></script>
	<script>
    const app = new Vue({
        el: '#app',
        data: {
        	numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15],
        },
        filters: {
            getOddNums: function(nums){
                const oddNums = nums.filter(function(num){
                    return num % 2
                })
                return oddNums
            },
            getUnderTenNums: function(nums){
                const UnderTen = nums.filter(function(num) {
                    return num<10
                })
                return underTen
            }
        }
    })
    </script>
</body>
```

