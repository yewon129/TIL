# Computer Science

#### 필요성

1. 컴퓨터(시스템)에 대한 이해
2. 자료구조, 알고리즘 활용 (일의 효율을 높이기)
3. Coder에서 Developer로 성장
4. 기업목적에 따른 기본적 CS지식 필요



### 소프트웨어 공학

##### 소프트웨어 공학_기출문제

* 소프트웨어 위기에 대해서 설명하시오
  * 싸이월드 재오픈 => 서비스에 대한 수요를 예측하지 못함
* 소프트웨어 공학이 필요한 이유는 무엇인지 설명하시오.
  * 개발, 운용, 유지보수에 필요하다
* 소프트웨어 개발경험과 소프트웨어 개발시 적용한 개발 방법론이 있다면 성명하시오
  * 경험을 설명할 때 방법론을 설명해야한다. 
* 소프트웨어 프로젝트 진행 경험에 대하여 설명하시오
  * 아키텍쳐와 방법론을 이용하여 설명하면 중요한 무기가 될 수 있다.



#### 소프트웨어 개발 생명 주시

> 계획 단계에서 유지보수 단계에 이르기까지 일어나는 일련의 절차

* 정의단계
* 개발단계
* 유지보수단계



#### 소프트웨어 개발 프로세스 정의

* 좁은 의미 : 사용자의 요구사항을 SW로 구현하기 위한 절차, 과정
* 넓은 의미 : 사용자의 목적을 이루기 위한 기회, ㅍ로젝트 관리 등을 포함한 절차, 과정, 방법
* 소프트웨어개발 7단계 : 계획 => 요구분석 => 설계 => 구현 => 테스트 => 반영 => 유지보수



#### 소프트웨어 프로세스 모델

* 폭포수 모델
  * 시간이 많이 걸림
* 프로토타입 모델
  * 먼저 만들어보고 테스트 해보자
* 나선형 모델
  * 경험을 녹여 반복해보자
* 통합프로세스 모델
  * 거의 동시적으로 시행
* 애자일 프로세스 모델
  * 애자일(agile) : 날렵한, 민첩한
  * 고객의 요구에 민첩하게 대응, 협력



#### 소프트웨어 아키텍처 정의

* 어떻게 만들지를 정의해 놓은 것
  * 구성요소, 관계, 속성 등

##### 아키텍처 모델

* 데이터 중심형 모델
  * 중앙에 데이터 중심으로 진행
* Client - Server 모델
  * 네트워크를 이용하는 분산 시스템 형태
* Layering 모델
  * 기능을 몇개의 계층으로 나누어 배치
* MVC 모델



### 프로그래밍

##### 기출문제

* 자바와 c의 차이

  * 자바 : 객체, 하드웨어 독립적
  * C : 절차, 하드웨어 최적화, IoT 수업에 사용

  ![image-20220621163102080](C:/Users/sky25/AppData/Roaming/Typora/typora-user-images/image-20220621163102080.png)

* JVM 가비지컬렉션 동작 과정

  * 메모리를 사용하지 않을 때 메모리를 갖고 있다가 Virtual Machine이 필요로 할때 사용된다.

* JAVA에 적용된 OOP

  * 사례를 통해 설계한 객체와 클래스를 비교

  ![image-20220621163136629](C:/Users/sky25/AppData/Roaming/Typora/typora-user-images/image-20220621163136629.png)

* 형성관리 활용 경험(C+Z/Y)

  * ![image-20220621163432833](Computer%20Science%20%EC%9D%B4%ED%95%B4/image-20220621163432833.png)



#### 객체지향

* 소프트웨어 객체는
  * 현실 세계의 객체를 필드와 메서드로 모델링한 것
  * 상태를 필드로 정의하고 동작을 메서드로 정의
* 필드는 객체 내부에 선언된 변수를 의미, 메서드는 객체 내부에 정의된 동작 의미

* 절차 지향 vs 객체지향
  * 절차지향 : 동작과 순서에 맞춘다.
  * 객체지향 : 객체를 중심으로 한다.
* 주요 개념
  * 캡슐화
    * 필드와 메서드를 포장해 세부 내용을 외부에서 알 수 없도록 감추는 것
  * 상속
    * Car => Sedan, SUV는 Car를 상속받는다
  * 다형성
    * 대입되는 객체에 따라 메스드를 다르게 동작하도록 구현하는 것



#### 객체지향프로그래밍 언어 - JAVA

* Write Once Run Anywhere
  * Java Virtual Machine
    * 자바 입장에서는 가상 os
* 프로그램 개발을 쉽게 하였다.
  * Garbage Collection
    * 메모리 관리가 어려움을 쉽게 해준다.
* Process
  * Thread
    * 병행성 문제
      * 동기화를 통해 해결



* 멀티태스킹
* 멀티프로세싱
* CPU 멀티 Thread
* 멀티 Thread



#### 형상관리

> SW개발 및 유지보수 과정에서 발생하는 변경 사항들을 관리하기 위해 개발된 일련의 활동

* 목적 : 소프트웨어 개발의 비용 줄이고, 개발 과정을 최적화 한다.
* 빌드 도구
  * 소스코드를 컴파일, 테스트, 정적 분석 등
  * ANT
  * MAVEN
  * Gradle



### 웹 & 모바일

##### 웹 

> HTTP, HTML, URL

##### 웹서비스

* 플랫폼에 독립적
* 디바이스 및 위치에 독립적
* 동적인 기능
* 비용 효율적
* 기존 시스템에 적용

##### 정적 웹 페이지 vs 동적 웹 페이지

* 정적 : 저장된 텍스트 파일을 그대로 보는 것
  * HTML
* 동적 : 저장된 다른 변수로 가공 처리하여 보는 것
  * PHP, ASP

##### 클라이언트 서버

* 요청 : 클라이언트, 받는 것: 서버

* 서버 : 아파치, IIS
* 클라이언트 : 크롬 등



##### 웹서버의 구성

* 예시
  * 윈도우 서버 + TOMCAT + JSP + Oracle
  * 리눅스 서버 + APACHE + TOMCAT + JSP + MySQL

* front & backend 하나의 맵으로 공부



##### 모바일 서비스

* 시스템 소프트웨어
* 애플리케이션
  * 다운로드 애플리케이션 등
* 모바일 운영체제 (OS)

* 모바일 앱 , 모바일 웹, 하이브리드 웹
  * 모바일 앱 : 안드로이드 - 자바 / 아이폰 - Swift
  * 하이브리드 앱 :  React Native
  * 모바일 웹 : HTML



### 자료구조

> 자료를 효율적으로 표현, 저장, 처리하도록 정리한 것

##### 분류

* 단순 구조, 선형 구조, 비선형 구조(1:N, N:M), 파일 구조(색인 파일)

##### 순차 자료구조

* 자료가 논리적 순서로 연속 저장하는 형식
* 리스트 : 나열하는 구조
* 선형 리스트 : 순서 리스트

##### 연결 자료구조

* 논리적 순서와 물리적 순서 불일치
* 단순 연결 리스트
* 원형 연결리스트
* 이중 연결 리스트
  * 양쪽 방향으로 순회



##### 스택

* 접시를 쌓듯이 자료를 차곡차곡 쌓는 것

* 후입선출
* PUSH / POP

##### 큐

* 삽입과 삭제 위치 같음

* 선입선출
* enQueue / deQueue

##### 데크

* 양방향

##### 트리

* 1:n 관계 비선형
* 이진트리
  * 노드가 2개 이하로 제한
  * 포화 이진트리
  * 완전 이진트리
  * 편향 이진트리

##### 그래프

* N:M
* 무방향 그래프
* 방향 그래프
* 완전 그래프
* 부분 그래프
* 가중 그래프

##### 알고리즘

* 검색의 정의
* 탐색 키
* 삽입/삭제



### 데이터 베이스

##### 분류

* 정형 데이터 : 구조화된 데이터
* 반정형 데이터 : HTML / XML / JSON
* 비정형 데이터 

##### 용어

* 스키마 : 구조, 제약조건을 정의한 것 - 테이블
* 인스턴스 : 스키마에 따라 데이터베이스에 실제로 저장된 값
* 데이터 독립성

##### View

* SQL에서 하나 이상의 테이블에서 원하는 모든 데이터를 서낵하여 그들을 사용자 정의하여 나타낸 것

* 데이터를 실제로 저장하지 않고 논리적으로만 존재하는 테이블이지만, 일반 테이블과 동일한 방법으로 사용함

##### 인덱스

* 테이블에 대한 동작의 속도를 높여주는 자료 구조
* 테이블 내의 1개의 컬럼, 혹은 여러 개의 컬럼을 이용하여 생성
* 고속의 검색 동작 뿐만 아니라 레코드 접근과 관련 효율적인 순서 매김 동작에 대한 기초를 제공

##### 키

* 유일하게 구별하는 속성 또는 속성들의 집합
* Unique
* 무결성, 개체 무결성, 참조 무결성



### 컴퓨터 구조

##### 폰노이만 구조

* CPU, 메모리, 입출력장치, 저장장치가 버스로 연결되어 있는 구조
* 사람의 구조와 같은 컴퓨터
* 구성요소
  * 프로세서, 버스, 레지스터, 메모리, 주변장치



##### 운영체제 아키텍쳐

* 모놀리식 커널
* 마이크로 커널

##### 커널

* 프로세스, 메모리, 저장장치 관리와 같은 핵심적인 기능을 모아 놓은 것
* 단일형 구조 커널
* 계층형 구조 커널
* 마이크로 구조 커널

##### 가상머신

> 커널 위에서의 새로운 운영체제

##### 시스템의 주요 개념

* 캐시
  * 중간 데이터를 모아 두는 것
* 버퍼 
  * 일시적으로 데이터를 보관
* 스풀링
  * 스풀을 둬서 데이터를 중간에 주고받게 한다.
* 폴링
  * 데이터를 가져오는 것
  * 처리해줘! : 푸쉬 / 주세요! : 폴링
* 인터럽트
  * 입출력 관리자가 대신 입출력을 해주는 방식

##### 리눅스 커널

* 하드웨어 자원을 제어하여 운영체제의 기본적인 기능을 사용자에게 제공



### 네트워크

> Protocol : 통신 규약

##### TCP / IP > 목적 중요

* Transmission Control Protocol : 전송 제어 프로토콜
* Internet Protocol : 인터넷 프로토콜
* 물리 주소 : 내 컴퓨터의 주소가 무엇인가
* 인터넷 주소 : 그 위에서 가상으로 존재하는 IP 주소
* 포트 주소 : 수신지 컴퓨터까지 전송하려면 IP 주소와 물리주소가 필요

##### OSI 7 Layer vs TCP/IP

* OSI 7 Layer : 규약만 존재

* TCP/IP : 실체가 존재

##### IP Address

* 인터넷에 연결된 모든 컴퓨터에는 고유의 주소가 부여
* IP 주소를 효율적으로 배정하려고 클래스라는 개념 도입
* 클래스에는 A, B, C, D, E 다섯 종류

##### IPv4 vs IPv6

* 네트워크 규모가 IPv6에서 제공한다

##### Routing

* 패킷의 전송 경로를 지정
* 전송 경로 결정시 고려 사항
* 공평 원칙 : 다른 패킷의 우선 처리를 위해 다른 패킷이 손해를 보면 안됨
* 효율성
* static routing vs dynamic routing

##### HTTP 프로토콜

* 상태가 존재하지 않는다 ( 상태가 독립적으로 사용)

##### URL

* 숫자로 되어 있는 IP 주소보다는 기억하기 쉽기 때문에 사용
* protocol://host:port/resource path/query

##### HTTP 요청메소드

GET, POST, DELETE, PUT

* 상태 코드



* IPv4 & IPv6 비교

![image-20220621172507102](Computer%20Science%20%EC%9D%B4%ED%95%B4/image-20220621172507102.png)



### 보안

##### 서비스 거부 공격(DoS)

* 취약점 공격형 : 프로토콜의 오류 제어
* 랜드 공격 : IP
* 자원고갈 공격 : 핑 공격 : App
* SYN 플러딩 공격 : SYN => TCP
* HTTP GET 플러딩 공격
* 스머프 공격 : ICMP 
* 메일 폭탄 공격

##### 분산 서비스 거부 공격(DDoS)

* 공격자(공격 주도) , 마스터(직접 명령 받는 시스템) , 핸들러 , 에이전트(마스터가 관리) , 데몬

##### 스니핑 (도청)

* 스위치 재밍 공격 : 맥 주소 테이블 기반으로 스위칭 기능 마비 시킴
* SPAN 포트 태핑 공격
* 포트 미러링

##### 스푸핑 (속인다)

* ARP 스푸핑 공격
* IP 스푸핑
* ICMP 리다이렉트 공격

##### 세션하이재킹 (세션을 가로챈다)

* 두 사용자 사이 로그인 상태를 가로챈다

##### 보안 프로토콜

* SSL : 방대한 인터넷 상거래의 안전을 위해 사용되는 프로토콜
* 암호화 시켜서 보내자
* SSL 세션 vs 접속
* IPSec
  * IP를 바꿔버린다. ( 돈이 많이 들어 )
  * 과도하게 기술적