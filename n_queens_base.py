import random
import time
import math
import matplotlib.pyplot as plt

# Function to calculate the number of attacking pairs
def count_conflicts(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# to plot
def plot_history(history, title):
    plt.figure(figsize=(10, 5))
    plt.plot(history, color='blue', linewidth=1)
    plt.title(f"Path: {title}")
    plt.xlabel("Iteration / Step")
    plt.ylabel("Number of Conflicts")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            line += " Q " if state[row] == col else " . "
        print(line)
