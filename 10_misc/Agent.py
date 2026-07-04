import gymnasium as gym
import numpy as np
import random

# Hyperparameters
LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 10000
SHOW_EVERY = 1000

# Q-Table parameters
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

# Exploration settings
epsilon = 1  # Exploration rate
START_EPSILON_DECAYING = 1
END_EPSILON_DECAYING = EPISODES // 2
epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)

# Create environment
env = gym.make("CartPole-v1")

# Initialize Q-table
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

def get_discrete_state(state):
    """Convert continuous state into discrete bucket."""
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

# Training the agent
for episode in range(EPISODES):
    discrete_state = get_discrete_state(env.reset()[0])
    done = False

    if episode % SHOW_EVERY == 0:
        render = True
        print(f"Episode: {episode}")
    else:
        render = False

    while not done:
        if random.uniform(0, 1) > epsilon:
            # Exploit: Choose action from Q-table
            action = np.argmax(q_table[discrete_state])
        else:
            # Explore: Random action
            action = np.random.randint(0, env.action_space.n)

        new_state, reward, done, _, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)

        if render:
            env.render()

        if not done:
            # Update Q-value using Q-learning formula
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action,)]

            # Q-learning equation
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action,)] = new_q
        elif new_state[0] >= env.goal_position:
            # Update Q-value for reaching the goal
            q_table[discrete_state + (action,)] = 0

        discrete_state = new_discrete_state

    # Decay epsilon
    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

env.close()
