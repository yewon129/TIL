# Spring Web MVC

* Servlet API를 기반으로 구축된 웹프레임워크
* 정식 명칭은 Spring Web MVC이지만, Spring MVC로 주로 알려짐
* Spring Framework가 제공하는 DI, AOP, WEB 개발 위한 기능 제공
* DispatcherServlet(FrontController)를 중심으로 디자인 됨
* View Resolver, Handler Mapping, Controller와 같은 객체와 함께 요청을 처리하도록 구성
* 다른 프레임워크와 같이 front controller pattern으로 구성
* 중심이 되는 DispatcherServlet(front controller)은 요청처리를 위한 기능 제공



### 컨테이너 구성

![image-20220623221945255](Spring%20Web%20MVC/image-20220623221945255.png)



### Spring MVC 구성요소

* DispatcherServlet
  * 클라이언트 요청처리
  * 요청 및 처리 결과 전달
* HandlerMapping
  * 요청을 어떤 Controller가 처리할 지 결정
* Controller
  * 요청에 따라 수행할 메서드를 선언하고, 요청처리를 위한 로직 수행
* ModelAndView
  * 요청처리를 하기 위해서 필요한 혹은 그 결과를 저장하기 위한 객체
* ViewResolver
  * Controller에 선언된 view이름을 기반으로 결과를 반환할 View를 결정
* View
  * 응답화면 생성



### Spring MVC 요청 처리 흐름

1. 클라이언트 요청 들어오면 DispatcherServlet이 받는다
2. HandlerMapping이 어떤 Controller가 요청을 처리할지 결정한다.
3. DispatcherServlet은 Controller에 요청을 전달
4. Controller는 요청을 처리한다.
5. 결과(요청처리 위한 데이터, 결과 보여줄 뷰 이름)를 ModelAndView에 담아 반환
6. ViewResolver에 의해서 실제 결과를 처리할 VIew를 결정하고 반환
7. 결과를 처리할 View에 ModelAndView를 전달
8. DispatcherServlet은 View가 만들어낸 결과를 응답