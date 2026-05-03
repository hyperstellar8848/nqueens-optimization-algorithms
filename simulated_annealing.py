from n_queens_base import count_conflicts, random, math, time

def simulated_annealing(n, initial_temp, cooling_rate, max_iter):
    start_time = time.time()
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = count_conflicts(current_state)
    temp = initial_temp
    history = []
    
    for i in range(max_iter):
        history.append(current_conflicts)
        if current_conflicts == 0:
            break
            
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        neighbor = list(current_state)
        neighbor[row] = col
        neighbor_conf = count_conflicts(neighbor)
        
        delta = neighbor_conf - current_conflicts
        # Acceptance probability
        if delta < 0 or (temp > 0 and random.random() < math.exp(-delta / temp)):
            current_state, current_conflicts = neighbor, neighbor_conf
            
        temp *= cooling_rate
        
    return current_state, current_conflicts, i, time.time() - start_time, history
