# Spring



### Framework

* 웹 어플리케이션 개발을 위해서 많은 기능을 설계, 잘성해야한다. 하지만 **기본적인 공통 구조(framework)를 제공**한다면 개발자는 웹 어플리케이션 기능 자체 개발에만 집중하여 **생산성 높아진다.**

* 개발자 입장에서 완성된 구조에 자신이 맡은 코드만 개발해서 넣어주면 되기 때문에 **개발 시간 단축**이 가능하다.



### Spring Framework의 특징

> 객체 관리 컨테이너

* POJO(Plain Old Java Object)방식의 프레임워크
  * EJB가 기능 작성 위하여 인터페이스를 구현하거나 상속하는 것에 비해 일반적인 자바 객체를 이용, 그대로 사용 가능
* 의존성 주입을 통한 객체관계 구성
  * 프레임워크 내부에서 사용되는 객체간 의존성이 존재할 경우, 개발자는 의존성에 관련한 설정만 해주면 실제 의존성 생성은 프레임워크가 담당한다.
* 관점지향 프로그래밍(AOP) 지원
  * 트랜젝션, 로깅 등 여러 모듈에서 공통적으로 사용하는 기능 대해 별도로 분리하여 작성, 관리하는 기능 제공
* 제어 역전
  * 객체 및 프로세스의 제어를 프레임워크가 담당한다. 필요에 따라 개발자의 코드 호출
* 높은 확장성과 다양한 라이브러리 제공



### Spring Framework 사용 이유

* Spring is everywhere
  * 전자정부 표준프레임워크 

* Spring is flexible
* Spring is productive



### Spring Framework 아키텍쳐

![image-20220621223930333](C:/Users/sky25/AppData/Roaming/Typora/typora-user-images/image-20220621223930333.png)