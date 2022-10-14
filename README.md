# Movie_pair
<br>

    - 프로젝트 소개
    깃허브 협업으로 게시판 서비스 구현하기
<hr>
<br>

## 🧰 사용기술

<br>

<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> 　<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=ffffff"/>

<br>

<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/>　<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## 📅 프로젝트 기간

<br>

### 2022-10-14

<br>

## 👩🏻‍💻 Members
<a href="https://github.com/HYUNSIK-JI/Movie_pair/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HYUNSIK-JI/Movie_pair" />
</a>

백엔드 담당 : 지현식<br>
프론트 담당 : 백솔비

<br>

## ✨ 1. 목표 서비스
<br>

### 1.1 게시판

<br>

1. 게시판 생성, 읽기, 수정, 삭제
2. 로그인한 회원에게 글 관리 권한 부여

<br>

### 1.2 회원 관리

<br>

1. 회원가입 및 로그인/로그아웃
2. 회원 정보 수정
3. 회원 탈퇴



### 1.3 검색(주제, 내용, 댓글, 평점, 작성자로 검색가능)
<br>

1. 주제
2. 내용
3. 평점
4. 외래키로 이용하여 회원의 이름 으로 검색
5. 댓글이 달린 댓글 id 값과 게시글 id 값 이용해서 검색
<br>

## ✨ 2. 실제 구현 정도
<br>

### 2.1 게시판

<br>

1. 게시판 글 생성, 글 목록, 글 수정, 글 삭제
2. 로그인 한 상태에서 자신의 글만 수정 및 삭제 가능
3. 검색
4. 좋아요
5. 댓글
6. 페이지네이션
<br>

### 2.2 회원 관리

<br>

1. 회원가입 후 로그인, 로그아웃 기능 
2. 회원 목록 페이지
3. 회원 정보 수정
4. 회원 탈퇴 기능

<br>

### 2.3 검색(주제, 내용, 댓글, 평점, 작성자로 검색가능)
<br>

1. 주제
2. 내용
3. 평점
4. 외래키로 이용하여 회원의 이름 으로 검색
5. 댓글이 달린 댓글 id 값과 게시글 id 값 이용해서 검색
<hr>

### 2.4 댓글(각 게시글에 댓글)
1. 댓글
<br>

### 2.5 게시글 좋아요

1. 좋아요, 취소
## ✏ 3. 프로젝트 진행과정

<br>

### 3.1 깃허브 협업 과정

<br>

#### 3.1.1 협업용 organization 레포지토리 생성

<br>

#### 3.1.2 협업 할 폴더 생성

<br>

```python
mkdir 2022-10-14
```

<br>

##### 3.1.2.1 가상 환경 생성

<br>

```python
python -m venv venv
```

<br>

##### 3.1.2.2 프로젝트 생성

<br>

```bash
$ pip install django==3.2.13
```

```python
django-admin startproject pjt
```

<br>

##### 3.1.2.3 게시판 앱 & 회원관리 앱 생성

<br>

```python
python manage.py startapp articles # 게시판
python manage.py startapp accounts # 회원관리
```
<br>

##### 3.1.2.4 게시판 모델 & 회원정보 모델 생성

<br>

#### 3.1.3 브랜치 생성

<br>

##### 3.1.3.1 최종 완성본 브랜치 master

<br>

```bash
$ git checkout -b master
```

<br>

##### 3.1.3.2 중간 협업용 브랜치 develop

<br>

```bash
$ git checkout -b develop
```

<br>

##### 3.1.3.3 개인 별 담당 기능 브랜치

<br>

```bash
$ git checkout -b signup # 회원가입 브랜치
```

<br>

#### 3.1.4 각 브랜치에서 담당 기능 구현

<br>

#### 3.1.5 구현 완료 후 커밋, 푸쉬, 풀리퀘스트 요청

<br>

```bash
$ git add .
$ git commit -m 'create signup'
$ git push origin signup
```

<br>

#### 3.1.6 구현 확인

<br>

##### 3.1.6.1 승인자가 확인 후 이상 없을 시 머지 

<br>

##### 3.1.6.2 이상 발생 시 충돌 해결 후 머지

<br>

## 🖥 4. 실제 구현 화면

<br>

### 4.1 게시판 페이지

<br>

    1. 회원가입 후 로그인한 회원만 글쓰기 권한을 부여받음
    2. 회원이 작성한 글 목록을 테이블 형식으로 구현
    3. 회원이 작성한 글의 제목을 클릭하면 상세 글 확인
    4. 회원 본인이 작성한 글만 수정, 삭제 가능

<br>

![메인페이지 구현 화면](url)

<br>

### 4.2 회원가입 페이지

<br>

    1. 네브바에 있는 회원가입 버튼을 누르면 회원가입 폼 화면으로 이동

<br>

### 4.3 로그인 페이지

<br>

    1. 회원가입 후 로그인 성공하면 회원 이름의 표기와 함께 로그아웃 버튼 생성된 페이지로 이동

<br>


### 4.3 회원정보 페이지

<br>

    1. 네브바에 표시된 자신의 이름을 클릭하면 회원정보 페이지로 이동
    2. 회원정보에서 이름, 이메일, 비밀번호 변경 가능

<br>

<hr>
<br>

## 5. 프로젝트를 통해 배운 점 및 느낀 점

<br>
검색 기능을 활성화 시키는데 있어서
특정 댓글이 달린 댓글을 검색창에 검색하여 게시글 전체를 보여주는 부분이 어려웠습니다.
게시글 id 와 댓글 id 를 lookup 문법을 이용하는것이 익숙하지 않다보니 어려웟고
구글 검색 및 장고 문서를 검색하여 lookup 문법를 익혀 갔고 이것으로 문제를 해결해 나갈수 있었습니다.
아직 많이 부족하다고 느꼈지만 재미있다는것을 느껴서 더 많은 시간을 할애하여 공부하게 될거같습니다.


<br>
