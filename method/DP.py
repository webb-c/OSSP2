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

def is_stable(prev_table, next_table):
    prev_table = np.asarray(prev_table)
    next_table = np.asarray(next_table)
    return np.all(np.abs(next_table - prev_table) <= 1e-4)

def value_iteration():
    global env, agent, gamma, episode
    i = 0
    while True :
        prev_table = agent.get_table()
        next_table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for x in range(4) :
            for y in range(4) :
                if x == 3 and y == 3:
                    next_table[x][y] = 0.0
                    continue 
                value_list = []
                for action in range(4):
                    env.set_state(x, y)
                    (x_prime, y_prime), reward, done = env.step(action)
                    next_value = prev_table[x_prime][y_prime]
                    value_list.append((reward + gamma * next_value))
                next_table[x][y] = max(value_list)
        agent.set_table(next_table)
        next_table = agent.get_table()
        agent.save_table()
        if is_stable(prev_table, next_table) or i >= episode :
            break
        i += 1

def policy_iteration():
    global episode
    policy = [[[0.25, 0.25, 0.25, 0.25]] * 4 for _ in range(4)]
    i = 0
    while True :
        prev_table = agent.get_table()
        policy_evaluation(policy)
        policy = policy_improvement(policy)
        next_table = agent.get_table()
        agent.save_table()
        if is_stable(prev_table, next_table) or i >= episode:
            break
        i += 1

def policy_evaluation(policy):
    global env, agent, gamma
    prev_table = agent.get_table()
    next_table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(4) :
        for y in range(4) :
            if x == 3 and y == 3:
                next_table[x][y] = 0.0
                continue 
            value = 0.0
            for action in range(4):
                env.set_state(x, y)
                (x_prime, y_prime), reward, done = env.step(action)
                next_value = prev_table[x_prime][y_prime]
                value += policy[x][y][action] * (reward + gamma * next_value)
            next_table[x][y] = value
    agent.set_table(next_table)
    return next_table
    
def policy_improvement(policy):
    global env, agent, gamma
    next_policy = policy
    table = agent.get_table()
    for x in range(4) :
        for y in range(4) :
            if x == 3 and y == 3:
                continue 
            best_value = -99999999
            max_index = []
            result = [0.0, 0.0, 0.0, 0.0]
            for action in range(4):
                env.set_state(x, y)
                (x_prime, y_prime), reward, done = env.step(action)
                next_value = table[x_prime][y_prime]
                temp = reward + gamma * next_value
                if temp == best_value:
                    max_index.append(action)
                elif temp > best_value:
                    best_value = temp
                    max_index = [action]
            prob = 1 / len(max_index)
            for index in max_index:
                result[index] = prob
            next_policy[x][y] = result
    return policy
            
            
def train_dp(method, sub, eps, g):
    print("test")
    global env, agent
    global gamma, episode
    env = GridWorld()
    agent = Agent(method, get_number())
    gamma, episode = g, eps
    
    if sub == "v" :
        value_iteration()
    elif sub == "p" :
        policy_iteration()
    else :
        print("wrong args :", sub)
        return

    agent.print_table()
    agent.save_table()