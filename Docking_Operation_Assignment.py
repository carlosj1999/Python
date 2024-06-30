import gym
from gym import spaces
import numpy as np
import random

class SpaceEnv(gym.Env):
    def __init__(self):
        # Actions we can take: go left, do nothing, go right
        self.action_space = spaces.Discrete(3)
        # Alignment range: -2m to 2m
        self.observation_space = spaces.Box(low=np.array([-2]), high=np.array([2]))

        # Set initial alignment with some random noise
        self.state = random.uniform(-0.5, 0.5)
        # Set docking operation time (in seconds)
        self.docking_time = 300

    def step(self, action):
        # Apply action. 0: go left, 1: do nothing, 2: go right
        self.state += (action - 1) * 0.1  # Move 10cm left or right

        # Reduce docking time by 1 second
        self.docking_time -= 1

        # Calculate reward
        reward = 1 if abs(self.state) <= 0.15 else -1
        # Check if docking operation is done
        done = self.docking_time <= 0

        # Apply some random noise to simulate space environment
        self.state += random.uniform(-0.05, 0.05)

        # Clip state to be within the valid range
        self.state = np.clip(self.state, -2, 2)

        # Set placeholder for info
        info = {}

        return np.array([self.state]), reward, done, info

    def reset(self):
        # Reset alignment
        self.state = random.uniform(-0.5, 0.5)
        # Reset docking time
        self.docking_time = 300
        return np.array([self.state])

# Discretize the alignment range
discreteAlignmentSpace = np.linspace(-200, 200, 100)

def getState(observation):
    return int(np.digitize(observation[0] * 100, discreteAlignmentSpace))

# SARSA algorithm implementation
def sarsa(env, num_episodes, alpha, gamma, epsilon):
    Q = np.zeros((len(discreteAlignmentSpace) + 1, env.action_space.n))
    
    def choose_action(state, epsilon):
        return env.action_space.sample() if random.uniform(0, 1) < epsilon else np.argmax(Q[state])
    
    total_rewards = []
    avg_rewards = []

    for episode in range(num_episodes):
        state = getState(env.reset())
        action = choose_action(state, epsilon)
        done = False
        total_reward = 0
        
        while not done:
            next_state, reward, done, _ = env.step(action)
            next_state = getState(next_state)
            next_action = choose_action(next_state, epsilon)
            
            Q[state, action] += alpha * (reward + gamma * Q[next_state, next_action] - Q[state, action])
            
            state = next_state
            action = next_action
            total_reward += reward
        
        total_rewards.append(total_reward)
        avg_rewards.append(np.mean(total_rewards[-100:]))
        
        epsilon = max(epsilon * 0.99, 0.01)  # Decay epsilon
        
        if episode % 100 == 0:
            print(f"Episode {episode}, Average Reward: {avg_rewards[-1]:.2f}")
    
    return Q, total_rewards, avg_rewards

# Run the algorithm
env = SpaceEnv()
num_episodes = 5000
alpha = 0.1
gamma = 0.99
epsilon = 1.0

Q, total_rewards, avg_rewards = sarsa(env, num_episodes, alpha, gamma, epsilon)

# Plotting code (you'll need to add matplotlib import at the top)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(avg_rewards)
plt.title('Average Reward over Episodes')
plt.xlabel('Episode')
plt.ylabel('Average Reward')
plt.savefig('sarsa_results.png')
plt.show()

# Run with different learning rates
for alpha in [0.2, 0.5]:
    print(f"\nRunning SARSA with alpha = {alpha}")
    Q, total_rewards, avg_rewards = sarsa(env, num_episodes, alpha, gamma, epsilon)
    
    plt.figure(figsize=(10, 5))
    plt.plot(avg_rewards)
    plt.title(f'Average Reward over Episodes (alpha = {alpha})')
    plt.xlabel('Episode')
    plt.ylabel('Average Reward')
    plt.savefig(f'sarsa_results_alpha_{alpha}.png')
    plt.show()