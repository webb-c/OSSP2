import random
import numpy as np
from environment import GridWorld
from agent import Agent


def train_mc(method, eps, gamma, alpha):
    env = GridWorld()
    agent = Agent(method, num)
    reward = -1
    gamma = gamma
    alpha = alpha

    for k in range(50000):
        done = False
        history = []

        while not done:
            action = agent.select_action()
            (x, y), reward, done = env.step(action)
            history.append((x, y, reward))
        env.reset()

        cum_reward = 0
        for transition in history[::-1]:
            x, y, reward = transition
            data[x][y] = data[x][y] + alpha*(cum_reward-data[x][y])
            cum_reward = reward + gamma*cum_reward



if __name__ == '__main__':
    main()
