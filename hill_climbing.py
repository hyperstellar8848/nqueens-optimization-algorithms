from n_queens_base import count_conflicts, random, time

def hill_climbing(n, max_restarts=100):
    start_time = time.time()
    history = []
    total_iterations = 0
    
    for r in range(max_restarts):
        current_state = [random.randint(0, n - 1) for _ in range(n)]
        current_conflicts = count_conflicts(current_state)
        
        while True:
            total_iterations += 1
            history.append(current_conflicts)
            
            if current_conflicts == 0:
                return current_state, 0, total_iterations, time.time() - start_time, history
            
            neighbors = []
            for i in range(n):
                for j in range(n):
                    if current_state[i] != j:
                        temp = list(current_state)
                        temp[i] = j
                        neighbors.append((temp, count_conflicts(temp)))
            
            # Select the best neighbor
            best_neighbor, min_conflicts = min(neighbors, key=lambda x: x[1])
            
            if min_conflicts >= current_conflicts:
                break # Local optimum reached, will restart
            
            current_state = best_neighbor
            current_conflicts = min_conflicts
            
    return current_state, current_conflicts, total_iterations, time.time() - start_time, history
