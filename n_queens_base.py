import random
import time
import math

# Function to calculate the number of conflicts (attacking pairs)
def count_conflicts(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Same column
            if state[i] == state[j]:
                conflicts += 1
            # Same diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# Function to print the board visually
def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[row] == col:
                line += " Q "
            else:
                line += " . "
        print(line)
    print("\n")
