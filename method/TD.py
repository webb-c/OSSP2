import random
import numpy as np
from environment import GridWorld
from agent import Agent


def get_number(n):
    number = 0
    if n == 1 :
        idx = 2
    else :
        idx = 3
    with open('number.txt', 'r') as file:
        lines = file.readlines()
    number = int(lines[idx],strip())
    lines[idx] = str(number+1) + '\n'
    with open('number.txt', 'w') as file:
        file.writelines(lines) 
    return number


def train_td(method, n, eps, gamma, alpha):
    env = GridWorld()
    number = 0
    if n == 1 or n == 3 :
        number = get_number(n)
    agent = Agent("{}-step TD".format(n), number)
    reward = -1
    gamma = gamma
    alpha = alpha

    for k in range(eps):
        done = False
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            x_prime, y_prime = env.get_state()
            # table update
            temp_table = agent.get_table()
            temp_table[x][y] = temp_table[x][y] + alpha * \
                (reward+gamma*temp_table[x_prime][y_prime]-temp_table[x][y])
            agent.set_table(temp_table)
        if k % (eps//10) == 0 :
            agent.print_table()
        agent.save_table()
        env.reset()
        agent.reset()


if __name__ == '__main__':
    main()
