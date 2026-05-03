from n_queens_base import count_conflicts, random, math, time

def simulated_annealing(n, initial_temp=100, cooling_rate=0.95, max_iter=5000):
    start_time = time.time()
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = count_conflicts(current_state)
    temp = initial_temp
    
    for i in range(max_iter):
        if current_conflicts == 0 or temp <= 0.01:
            break
            
        # Select a random neighbor
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        neighbor_state = list(current_state)
        neighbor_state[row] = col
        
        neighbor_conflicts = count_conflicts(neighbor_state)
        delta_e = neighbor_conflicts - current_conflicts
        
        # Acceptance probability
        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / temp):
            current_state = neighbor_state
            current_conflicts = neighbor_conflicts
            
        temp *= cooling_rate # Cooling schedule
        
    return current_state, current_conflicts, i, time.time() - start_time
