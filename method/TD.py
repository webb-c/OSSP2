import random
import numpy as np
from environment import GridWorld
from agent import Agent
from tqdm import tqdm

def get_number(n):
    number = 0
    if n == 1 :
        idx = 2
    else :
        idx = 3
    with open('number.txt', 'r') as file:
        lines = file.readlines()
    number = int(lines[idx].strip())
    lines[idx] = str(number+1) + '\n'
    with open('number.txt', 'w') as file:
        file.writelines(lines) 
    return number


def train_td(method, n, eps, gamma, alpha):
    env = GridWorld()
    number = 0
    reward = -1
    gamma = gamma
    alpha = alpha

    for i in tqdm(range(100)) :
        if n == 1 or n == 3 :
            number = get_number(n)
        agent = Agent("{}-step TD".format(n), number)
        for k in tqdm(range(eps), desc="training... "):
            done = False
            history = []
            env.reset()
            x, y = env.get_state()
            while not done:
                """ TD
                # x, y = env.get_state()
                # action = agent.select_action()
                # 
                # x_prime, y_prime = env.get_state()
                # # table update
                # temp_table = agent.get_table()
                # temp_table[x][y] = temp_table[x][y] + alpha * \
                #     (reward+gamma*temp_table[x_prime][y_prime]-temp_table[x][y])
                # agent.set_table(temp_table) """
                action = agent.select_action()
                (x_prime, y_prime), reward, done = env.step(action)
                history.append((x, y, reward))
                if len(history) >= n :
                    # n-step target 계산
                    target = sum([gamma ** i * history[i][2] for i in range(n)])
                    temp_table = agent.get_table()
                    for transition in history:
                        x, y, reward = transition
                        temp_table[x][y] = temp_table[x][y] + alpha*(target-temp_table[x][y])
                    agent.set_table(temp_table)
                    history = []
                x, y = x_prime, y_prime
            agent.save_table()
        agent.print_table()