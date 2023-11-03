import random
import numpy as np
from environment import GridWorld
from agent import Agent
from tqdm import tqdm

def get_number():
    number = 0
    with open('number.txt', 'r') as file:
        lines = file.readlines()
    number = int(lines[1].strip())
    lines[1] = str(number+1) + '\n'
    with open('number.txt', 'w') as file:
        file.writelines(lines) 
    return number


def train_mc(method, eps, gamma, alpha):
    env = GridWorld()
    reward = -1
    gamma = gamma
    alpha = alpha

    for i in tqdm(range(100)) :
        agent = Agent(method, get_number())
        for k in tqdm(range(eps), desc="training... "):
            done = False
            history = []

            while not done:
                action = agent.select_action()
                (x, y), reward, done = env.step(action)
                history.append((x, y, reward))
            env.reset()

            # table update
            temp_table = agent.get_table()
            cum_reward = 0
            for transition in history[::-1]:
                x, y, reward = transition
                temp_table[x][y] = temp_table[x][y] + alpha*(cum_reward-temp_table[x][y])
                cum_reward = reward + gamma*cum_reward
            agent.set_table(temp_table)
            agent.save_table()
        agent.print_table()
