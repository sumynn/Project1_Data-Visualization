# 음원 차트를 이용한 트렌드 분석

> 📅 2021.09.02 - 2021.09.14 (9일)
>
> 👨‍👦‍👦 5인 (데이터 수집, 데이터 전처리, 분석 및 시각화 담당)

<br>

## 📑 Index

1. [프로젝트 개요](#-프로젝트-개요)
2. [기술 스택 및 라이브러리](#-기술-스택-및-라이브러리)
3. [프로젝트 수행 내용](#-프로젝트-수행-내용)
4. [담당한 기능](#-담당한-기능)
5. [배운 점](#-배운-점)

<br>

## 📖 프로젝트 개요

음원 차트 분석을 통해 계절별 선호 장르, 문장형 제목의 유행, 시기에 관계 없이 인기있는 가수 등 음악 트렌드에 대해 알아본다.

<br/>

## 🛠 기술 스택 및 라이브러리

- Python3
- BeautifulSoup
- Selenium
- Pandas
- Matplotlib
- Plotly

<br>

## 📝 프로젝트 수행 내용

1. 지니 뮤직(Genie), 멜론(Melon) 등 음원 사이트 차트 크롤링
2. 데이터 전처리 - 장르 정리, 계절별 데이터 추출
3. 주제별 데이터 분석 및 시각화

<br>

## 😎 담당한 기능

> 데이터 수집, 데이터 전처리, 분석 및 시각화(가을) 담당

- 데이터 수집 - 지니 뮤직(Genie), 멜론(Melon)의 음원 차트에서 연도, 월, 순위, 타이틀, 가수, 장르 추출
  
  - 지니 뮤직 2017년 ~ 2021년 월간 차트와 연간 차트 Top100 동적 크롤링
  
    (총 **49200개** 로우 데이터 수집)
  
    > [지니 웹 크롤링 코드](./01.Web_Crawling/Genie_Web_Crawler.ipynb)
  
    - `BeautifulSoup`을 이용해 데이터 추출
  
    <img src="https://user-images.githubusercontent.com/87269113/138381951-81412b1d-770b-4cbe-8923-5f1549d3d001.png" width="60%">
  
  - **멜론(Melon)** 연간 차트 Top100 동적 크롤링
  
    > [멜론 웹 크롤링 코드](./01.Web_Crawling/Melon_Web_Crawler.ipynb)
  
    - `Selenium`을 이용해 차트 파인더 조건 선택
    - `BeautifulSoup`을 이용해 데이터 추출
    
    <img src='https://user-images.githubusercontent.com/87269113/138382258-860c47d2-6aa8-40da-ad1d-f41414c9ba16.png' width='60%'>

<br>

- 데이터 전처리

  > [데이터 전처리 코드](./02.Data_Analysis_Visualization/01.Data_Preprocessing.ipynb)
  - 장르 수정

    <img src='https://user-images.githubusercontent.com/87269113/138382384-12743a34-677e-40bc-b55c-bda4f645675d.png' width='30%'>
  
    - '가요/...', 'POP/...' 등 뒤에 써진 세부 장르로 변경
    - '가요/전체'로 표시된 장르는 멜론에서 찾은 후 변경
    - OST/드라마', 'OST/해외영화' -> OST로 통일

    
  
  - 계절별 데이터 추출

<br>

- `Pandas` , `Matplotlib` , `Plotly` 등의 파이썬 라이브러리를 이용해 데이터 분석 및 시각화 진행

  - 계절별 장르 분포

    > [계절별 장르 분포(가을 부분) 분석 코드](./02.Data_Analysis_Visualization/02.Data_Analysis_Visualization_Genre_Fall.ipynb)
  
    ![장르 그래프](https://user-images.githubusercontent.com/87269113/155985394-ce11c49f-a772-42a1-8ec9-471e2aabc77a.jpg)
  
  - 가수 분포
  
    > [가수 분포 분석 코드](./02.Data_Analysis_Visualization/03.Data_Analysis_Visualization_Singer.ipynb)
  
    <img src="https://user-images.githubusercontent.com/87269113/155986191-e9fe179b-6c58-4588-9a50-703fc4abb9db.png" alt="image" style="zoom: 50%;" />
  
  - 제목 길이 분석
  
    > [제목 길이 분석 코드](./02.Data_Analysis_Visualization/04.Data_Analysis_Visualization_title.ipynb)
  
    <img src="https://user-images.githubusercontent.com/87269113/155986497-aaee214e-a4ff-406a-9627-7b4bfd3c88a3.png" alt="image" style="zoom: 40%;" />

<br>

## 👍 배운 점

- 웹 크롤링을 통해 직접 음원 사이트의 음원 차트 데이터를 수집해볼 수 있었다.
- 데이터 전처리 과정과 분석 과정에서 `Pandas` 라이브러리를 주로 사용함으로써 Pandas에 더 익숙해질 수 있었다.
- 데이터 수집-분석-시각화 등 데이터 분석을 위한 일련의 과정을 직접 수행하며 데이터 분석에 대해 더 깊이 이해할 수 있는 경험이 됐다.
