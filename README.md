# ML_Project

## 회의 및 아카이빙 

https://www.notion.so/9dfd78b8a1cd4f8891a9799fb9e7c313

## 주관: 중소기업벤처부 이어드림 스쿨 2기

<br>

![image](https://user-images.githubusercontent.com/86671456/172179003-29299766-6706-4328-a3cf-4ee7684a9b82.png)


## Abstract

| 분석명 |목적|결과|
|:-----:|----------|-----|
|물류 유통량 예측 경진대회 X 제주도 물류 허브 공장 구축| 제주시 내 택배 운송 데이터를 이용하여 운송량 예측 AI개발 및 아이디어 제공|Top 5%|

|  소스 데이터 |     데이터 입수 난이도    |      분석방법     |데이터 출처|
|:------------------:| -----|:---------------:|-----------|
|CSV,Json,XML|중 |EDA, Visualization, Regression   |데이콘, 국토연구원, 한살림, 제주도허브데이터|
|  분석 적용 난이도  |     분석적용 난이도 사유    |      분석주기     | 분석결과 검증 Owner|
|상| 실제 물류허브 공장의 위치를 예측하여 적절한 위치 찾기|Daily  | 실습코치님, 이재원강사님, 고려대학교 강필성 교수님의 대학원생분들 |



<br>

### Machine Learning Project 

---
**진행: 애자일 방법론**

|  프로젝트 순서 |     Point    | 세부 내용 |  
|:------------------:| -----|------|
|문제 정의|해결할 점, 찾아내야할 점 |제주도와 그 외 지역의 유통 제품 및 건수 예측하는 지도학습|
|데이터 수집|공개 데이터, 자체 수집, 제공된 데이터 |데이콘data, 한살림data(수집), 국토연구원data(수집), 제주도허브데이터(수집)|   
|데이터 전처리|문제에 따라서 처리해야할 방향 설정 |제주도와 활발히 유통하는 지역, 제주도의 물류 문제를 해결할 허브를 어떻게 구축할까?|
|Feature Engineering|모델 선정 혹은 평가 지표에 큰 영향|항구별로 오는 유통 제품 파악하여 labeling and Encoding|
|연관 데이터 추가|추가 수집 |제주도민의 유통 제품, 쿠팡의 제주도 물류 허브를 구축하기 위한 시도  |
|알고리즘 선택| 기본적, 현대적|Catboost, DNN, Blending|   
|모델 학습|모델을 통해서 얻고 싶은 것 |기존 데이터의 양이 적어서 국토연구원 데이터를 추가하여 항구별 유통 파악 및 지역별 운송장 건수 파악|
|모델 평가|확률 | 상위 10%|
|모델 성능 향상|성능 지표, 하이퍼파라미터, 데이터 리터러시 재수정 |하이퍼파라미터 조정 및 추가 Ensembling, Top5%   |

<br>

### Basic information

**공식기간: 2022.06.03 ~ 2022.06.24**


- 인원:김호민, 이근희, 이기수, 안세호, 이세현
- 직책: PL(Project Leader)
- 데이터: Dacon 유통 데이터, 국토연구원, 도로교통부
- 주 역할:Project Leading, Data 수집  및 가공 , 데이터 파이프라인 구축, ML/DL
- 보조 역할: Data Preprocessing, EDA, Feature engineering
- 추가 역할:회의록 작성, 창업 대회 참가 계획서
- 협업장소: Github, GoogleMeet
- 소통: Slack, Notion,Git project, Google OS
- 저장소: Github, Google Drive
- 개발환경: Visual studio code, Juypter Notebook, colab
- 언어 :python 3.8.x
- 라이브러리:Numpy,Pandas, Scikit-learn 1.1.x, lazypredict, Pycaret,Keras, Tensorflow, Pytorch
- 시각화 라이브러리: Seaborn, Matplotlib, Plot,Plotly, Tensorboard
- 시각화 도구: Tableau, GA
- 웹 크롤링: Slunimue

<br>

#### 파일 설명


- docs: 문서화 작업
- conf: 환경설정 관련
- build: 데이터 집산
- Definition: 프로젝트의 전반적인 문제 정의 및 내용 설정
- Data: 전처리 파일 및 모델링을 위한 파일
- models: 여러 모델들의 집합
- src :scripts
