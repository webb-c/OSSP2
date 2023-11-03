import random
import numpy as np
from environment import GridWorld


def train_td(method, n, eps, gamma, alpha):
    env = GridWorld()
    agent = Agent(method, num)
    reward = -1
    gamma = gamma
    alpha = alpha

    for k in range(50000):
        done = False
        while not done:
            x, y = env.get_state()
            action = agent.select_action()
            (x_prime, y_prime), reward, done = env.step(action)
            x_prime, y_prime = env.get_state()
            data[x][y] = data[x][y] + alpha * \
                (reward+gamma*data[x_prime][y_prime]-data[x][y])
        env.reset()


if __name__ == '__main__':
    main()
