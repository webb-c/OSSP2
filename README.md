# OSSP2
2023년 2학기 오픈소스SW프로젝트2 과제 구현 코드입니다. 


<br>

# 요구사항

### [DP] Dynamic Planning for 4x4 Gid World
- Design
    - Write a scratch code
    - Policy Type: 1. Random Policy
- Implement
    - ~~Policy type is a command line argument~~
    - Write a complete code


### [N-step TD] N-step TD Learning for 4x4 Gid World
- Design
    - Write a scratch code
    - Policy Type: 1. Random Policy
    - ~~Ns: N-step~~, Ne: Number of Episodes
- Implement
    - ~~Ns, Policy type, Ne are command line arguments~~
    - Write a complete code ~~which follows OpenAI gym interface~~
    - ~~Ref: [Create custom gym environments from scratch](https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e)~~


### Experiments
- Design Experiments
    - Learning Methods: DP, MC, 1-Step TD, 3-step TD  
    - With Ne ~ (100,1000, 10000)
- Perform Experiments saving results
- Analyze the results of Experiments in graphs(table)
    - Compare V(s) of all learning methods
    - Compare variance or bias of V(s) of MC, 1-step TD, 3-step TD for Ne = 100, 1000, 10000

### 제출물
- 아래 요구사항을 코딩하여 .py 또는 .ipynb 형태로 제출
- 코드는 바로 실행되도록 제출(에러 발생 시 감점 요인)

<br>


# 구현 사항
### 코드 구조 설명
- train.py : 인자로 learning method, Ne를 전달하면 그 방법대로 학습하는 코드
- agent.py : random policy를 기반으로 action을 랜덤하게 결정하는 에이전트. value table을 가짐.
- environment.py : 4x4 Gid World, action을 따라 실제로 step을 진행하는 환경.
- method/
    - DP.py : policy evalution을 통해 value function을 계산 (=정답)
    - MC.py : MC learning을 통해 value function을 계산
    - TD.py : n-step TD learning을 통해 value function을 계산
- analysis.ipynb : 학습 결과 데이터를 바탕으로 데이터를 분석하는 것 (그래프, 테이블)

### 코드 설치
```bash
git clone https://github.com/webb-c/OSSP2.git
```

### 요구 라이브러리 설치
```bash
pip install -r requirement.txt
```


### 코드 실행방법
```bash
# DP
python train.py -m DP -ne 100 

# MC
python train.py -m MC -ne 10000

# n-step TD 
python train.py -m TD -n 1 -ne 10000 -a 0.01
python train.py -m TD -n 3 -ne 10000 -a 0.01
```