import random
import numpy as np
from environment import GridWorld


def train_td(method, n, eps, gamma, alpha):
    env = GridWorld()
    agent = Agent(method, num)
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
        agent.save_table()
        env.reset()
        agent.reset()


if __name__ == '__main__':
    main()
