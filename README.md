# 2020-2-simulation

## 엘리베이터 사용 최적화 시뮬레이션 : 00 건물에 하나의 엘리베이터를 추가한다고 가정할 때 어떤 방법이 가장 효과적인것 일까?

엘리베이터 action
1. 모든층 가능
2. 짝수층 가능
3. 홀수층 가능
4. 위층 
5. 아래층

policy  | 엘리베이터 1 | 엘리베이터 2
|---|---|---|
1 | 모든층 가능 | 모든층 가능
2 | 짝수층 가능 | 홀수층 가능   
3 | 위층 가능 | 아래층 가능

-- 건물에서 얻은 데이터를 easy fit 이란 모듈을 활용해 분포 fit하고 이를 활용해 random number & random variable 만들어서 시뮬레이션 구함
