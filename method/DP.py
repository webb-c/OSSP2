import random
import numpy as np
from environment import GridWorld
from agent import Agent


def get_number():
    with open('number.txt', 'r') as file:
        line = file.readline().strip()
    number = int(line)
    with open('number.txt', 'w') as file:
        file.write(str(number+1)) 
    return number


def train_dp(method, eps, gamma, alpha):
    env = GridWorld()
    agent = Agent(method, num)
    reward = -1
    gamma = gamma
    alpha = alpha

    for k in range(eps):
        print()
        # DP implementation        

    agent.save_table()


if __name__ == '__main__':
    main()
