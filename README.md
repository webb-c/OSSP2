# OSSP2
2023년 2학기 오픈소스SW프로젝트2 과제 구현 코드입니다. <sup>202111309 손본</sup>

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
- train.py : 인자로 learning method(`-m`), episode 횟수(`-ne`)를 전달하면 그 방법대로 학습하는 코드
- agent.py : random policy를 기반으로 action을 랜덤하게 결정하는 에이전트. value table을 가짐.
- environment.py : 4x4 Gid World, action을 따라 실제로 step을 진행하는 환경. ([Reference](https://github.com/seungeunrho/RLfrombasics))
- method/
    - DP.py : policy evalution을 통해 value function을 계산 (=정답)
    - MC.py : MC learning을 통해 value function을 계산
    - TD.py : n-step TD learning을 통해 value function을 계산
- analysis.ipynb : 학습 결과 데이터를 바탕으로 데이터를 분석 및 그래프 생성

### 코드 설치
```bash
git clone https://github.com/webb-c/OSSP2.git
```

### 요구 라이브러리 설치
단, requirement.txt는 @webb-c가 사용한 가상환경에 설치된 라이브러리 버전으로, 이 버전보다 더 높거나 낮아도 호환될 가능성이 높습니다.  
또한 해당 requirement.txt에서는 `analysis.ipynb`를 실행하는데 필요로하는 라이브러리의 버전을 명시되어있지 않습니다. ipynb에 출력된 각 라이브러리의 버전을 확인하고 맞는 버전을 다운로드하길 바랍니다.
```bash
pip install -r requirement.txt
```


### 코드 실행방법 - 예시코드
```bash
# DP
python train.py -m DP

# MC
python train.py -m MC -ne 10000 -a 0.001

# n-step TD 
python train.py -m TD -n 1 -ne 10000 -a 0.01
python train.py -m TD -n 3 -ne 10000 -a 0.01
```

### 주의사항
- ⚠️ 인자를 입력할 때 `-d True`를 전달하면 value table을 .csv파일로 저장하며, 상대 경로이기 때문에 지정 경로에 디렉토리가 존재하지 않는다면 오류가 발생할 수 있습니다. 결과 저장이 아니라 단순 실행을 원한다면 default 값인 False를 사용하길 바랍니다. 
- ⚠️ 분석 및 figure 생성을 위해 사용하는 analysis.ipynb 파일 역시 상대경로를 사용하기 때문에 경로를 잘 확인하고 오류가 생기지 않도록 csv파일을 위치하길 바랍니다. 
- 인자를 입력할 때 `-r True`를 전달하게 된다면 데이터 수집을 위해 동일한 조건의 실험을 100번 반복하므로 default 값인 False를 사용하길 바랍니다. 
- 인자에 존재하는 `-s` 는 단순히 policy evalution이 아닌 optimal policy에서 optiaml value를 찾는 과정을 사용하길 원할 때 사용하는 인자입니다. 본 과제에서는 random policy를 가정하기 때문에 해당 인자는 무시하셔도 좋습니다.
- 현재 구현된 코드에서는 seed를 설정하지 않았기 때문에 `random`에 의존하는 TD, MC에서는 매번 실행할 때마다 결과가 다르게 나올 수 있습니다. 고정된 결과를 원한다면 seed를 별도로 선언하는 코드를 삽입하길 바랍니다.