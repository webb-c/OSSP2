import random
import numpy as np
from environment import GridWorld
from agent import Agent


def get_number():
    with open('number.txt', 'r') as file:
        for i, line in enumerate(file):
            if i == 1:  
                number = int(line.strip())
                break
    with open('number.txt', 'w') as file:
        file.write(str(number+1)) 
    return number

def train_mc(method, eps, gamma, alpha):
    env = GridWorld()
    agent = Agent(method, get_number())
    reward = -1
    gamma = gamma
    alpha = alpha

    for k in range(eps):
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
        if k % (eps//10) == 0 :
            agent.print_table()
        agent.save_table()
        agent.reset()


if __name__ == '__main__':
    main()
