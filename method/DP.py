import random
import numpy as np
from environment import GridWorld
from agent import Agent
from tqdm import tqdm

def get_number():
    number = 0
    with open('number.txt', 'r') as file:
        lines = file.readlines()
    number = int(lines[0].strip())
    lines[0] = str(number+1) + '\n'
    with open('number.txt', 'w') as file:
        file.writelines(lines) 
    return number


def train_dp(method, eps, gamma, alpha):
    env = GridWorld()
    agent = Agent(method, num)
    reward = -1
    gamma = gamma
    alpha = alpha

    for k in tqdm(range(eps), desc="training... "):
        print()
        # DP implementation        

    agent.save_table()
    agent.print_table()


if __name__ == '__main__':
    main()
