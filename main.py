import hill_climbing as hc
import simulated_annealing as sa
import genetic_algorithm as ga
from n_queens_base import print_board, plot_history

def main():
    # Input Section
    n = int(input("1. Enter number of Queens (N): "))
    print("\nChoose Algorithm:")
    print("1: Hill Climbing\n2: Simulated Annealing\n3: Genetic Algorithm")
    choice = input("Choice: ")

    if choice == '1':
        restarts = int(input("Enter Max Restarts (e.g. 50): "))
        res = hc.hill_climbing(n, restarts)
        title = "Hill Climbing"
    elif choice == '2':
        t0 = float(input("Enter Initial Temp (e.g. 100): "))
        rate = float(input("Enter Cooling Rate (e.g. 0.99): "))
        iters = int(input("Enter Max Iterations (e.g. 5000): "))
        res = sa.simulated_annealing(n, t0, rate, iters)
        title = "Simulated Annealing"
    else:
        pop = int(input("Enter Population Size (e.g. 100): "))
        mut = float(input("Enter Mutation Rate (e.g. 0.1): "))
        gens = int(input("Enter Generations (e.g. 1000): "))
        res = ga.genetic_algorithm(n, pop, mut, gens)
        title = "Genetic Algorithm"

    # Output Section
    state, final_conf, steps, duration, history = res
    print(f"\nResults for {title}:")
    print(f"Final Conflicts: {final_conf}")
    print(f"Steps/Generations: {steps}")
    print(f"Time Taken: {duration:.4f} seconds")
    print(f"Final State: {state}")
    
    if n <= 15: # Print board only for smaller N
        print_board(state)
    
    # Plotting the Path
    plot_history(history, title)

if __name__ == "__main__":
    main()
