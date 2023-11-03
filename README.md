### 제출물
- 아래 요구사항을 코딩하여 .py 또는 .ipynb 형태로 제출
- 코드는 바로 실행되도록 제출(에러 발생 시 감점 요인)

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
    - ~~Ref: Create custom gym environments from scratch (https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e)~~


### Experiments
- Design Experiments
    - Learning Methods: DP, MC, 1-Step TD, 3-step TD  
    - With Ne ~ (100,1000, 10000)
- Perform Experiments saving results
- Analyze the results of Experiments in graphs(table)
    - Compare V(s) of all learning methods
    - Compare variance or bias of V(s) of MC, 1-step TD, 3-step TD for Ne = 100, 1000, 10000


# 현재 구현 사항
- train.py : 인자로 learning method, Ne를 전달하면 그 방법대로 학습하는 코드
- analysis.ipynb : 학습 결과 데이터를 바탕으로 데이터를 분석하는 것 (그래프, 테이블)
