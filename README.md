# 음원 차트를 이용한 트렌드 분석

> 📅 2021.09.02 - 2021.09.14 (9일)
>
> 👨‍👦‍👦 5인

<br>

## 📑 Index

1. [프로젝트 개요](#-프로젝트-개요)
2. [기술 스택 및 라이브러리](#-기술-스택-및-라이브러리)
3. [프로젝트 수행 내용](#-프로젝트-수행-내용)
4. [담당한 기능](#-담당한-기능)
5. [배운 점](#-배운-점)

<br>

## 📖 프로젝트 개요

음원 차트 분석을 통해 계절별 선호 장르와 문장형 제목의 유행, 시기에 관계 없이 인기있는 가수 등에 대해 알아본다.

<br/>

## 🛠 기술 스택 및 라이브러리

- Python3

- 데이터 수집
  - BeautifulSoup
  - Selenium
- 데이터 분석
  - Pandas
- 데이터 시각화
  - Matplotlib
  - Plotly
- 웹 페이지 구현
  - Django

<br>

## 📝 프로젝트 수행 내용

1. 지니 뮤직(Genie), 멜론(Melon) 등 음원 사이트 차트 크롤링
2. 데이터 전처리 - 장르 정리, 계절별 데이터 추출
3. 주제별 데이터 분석 및 시각화
4. 웹 페이지 구현

<br>

## 😎 담당한 기능

데이터 수집, 전처리, 분석 및 시각화(가을), 웹 페이지 구현(메인, 계절별 장르 페이지)

- 데이터 수집
  - 지니 뮤직(Genie)의 월간 차트와 연간 차트 Top100 동적 크롤링

    > [지니 웹 크롤링 코드](./01.Web_Crawling/Genie_Web_Crawler.ipynb)

    - 연도, 월, 순위, 타이틀, 가수, 장르 추출

    <img src="https://user-images.githubusercontent.com/87269113/138381951-81412b1d-770b-4cbe-8923-5f1549d3d001.png" width="60%">

  - 멜론(Melon) 연간 차트 Top100 동적 크롤링

    > [멜론 웹 크롤링 코드](./01.Web_Crawling/Melon_Web_Crawler.ipynb)

    - 연도, 월, 순위, 타이틀, 가수, 장르 추출

    <img src='https://user-images.githubusercontent.com/87269113/138382258-860c47d2-6aa8-40da-ad1d-f41414c9ba16.png' width='60%'>

    <br>

- 데이터 전처리 - 가을 담당

  > [데이터 전처리 코드](./02.Data_Analysis_Visualization/01.Data_Preprocessing.ipynb)
  - 장르 수정

    - '가요/...', 'POP/...' 등 뒤에 써진 세부 장르로 변경
    - '가요/전체'로 표시된 장르는 멜론에서 찾은 후 변경
    - OST/드라마', 'OST/해외영화' -> OST로 통일

    <img src='https://user-images.githubusercontent.com/87269113/138382384-12743a34-677e-40bc-b55c-bda4f645675d.png' width='50%'>

  - 계절별 데이터 추출

<br>

- 데이터 분석 및 시각화

  :point_down:주제별 주피터 노트북 코드:point_down: 

  > [계절별 장르 분포 - 가을](./02.Data_Analysis_Visualization/02.Data_Analysis_Visualization_Genre_Fall.ipynb)
  >
  > [가수 분포](./02.Data_Analysis_Visualization/03.Data_Analysis_Visualization_Singer.ipynb)
  >
  > [제목 길이 분석](./02.Data_Analysis_Visualization/04.Data_Analysis_Visualization_title.ipynb)
  >
  > [제목에 들어가는 단어 빈도](./02.Data_Analysis_Visualization/05.Data_Analysis_Visualization_titleword.ipynb)

<br>

- 웹 페이지 구현 - 메인, 계절별 장르 페이지 담당

  > [웹 페이지 코드](./03.Web_Page/MusicChartAnalysis) 

  - 결과 그래프와 분석 내용을 담은 웹페이지 구현 

    - 메인

    ![웹_메인](https://user-images.githubusercontent.com/87269113/138386018-471e6858-2543-449e-8a17-deb9b1310051.gif)

    <br>

    - 계절별 장르 분석

    ![웹_계절](https://user-images.githubusercontent.com/87269113/138386016-106336de-a78f-4f1c-9946-ee778285173d.gif)

    <br>

    - 제목 분석

    ![웹_제목길이](https://user-images.githubusercontent.com/87269113/138386023-83e82ae2-2ac0-432a-83fa-d201b24bba0f.gif)

    <br>

    - 가수 분석

    ![웹_가수](https://user-images.githubusercontent.com/87269113/138386007-af8f4f8e-d653-4a2c-b243-fef1cdd1b155.gif)

<br>

## 👍 배운 점

- 크롤링을 통해 직접 데이터를 수집해볼 수 있었다.
- 데이터 분석을 하면서 Pandas를 더 능숙하게 다룰 수 있게 됐다. 
- 데이터 수집-분석-시각화 일련의 과정을 거치면서 데이터 분석에 대해 더 깊이 이해하게 됐다.
