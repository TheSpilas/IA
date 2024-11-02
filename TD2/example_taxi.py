import random
import gym
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    env = gym.make("Taxi-v3", render_mode="human")

    env.reset()
    print(env.render())

    for i in range(4):
        env.reset()
        time.sleep(2)
        print(env.render())

    env.close()

if __name__ == "__main__":
    main()