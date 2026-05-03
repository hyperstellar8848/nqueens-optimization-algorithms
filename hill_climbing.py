from n_queens_base import count_conflicts, random
import time

def hill_climbing(n, max_restarts=100):
    start_time = time.time()
    iterations = 0
    
    for r in range(max_restarts):
        # Initial random state
        current_state = [random.randint(0, n - 1) for _ in range(n)]
        current_conflicts = count_conflicts(current_state)
        
        while True:
            iterations += 1
            neighbor_found = False
            best_neighbor = list(current_state)
            min_conflicts = current_conflicts
            
            # Check all possible neighbors
            for i in range(n):
                for j in range(n):
                    if current_state[i] == j:
                        continue
                    
                    temp_state = list(current_state)
                    temp_state[i] = j
                    conflicts = count_conflicts(temp_state)
                    
                    if conflicts < min_conflicts:
                        min_conflicts = conflicts
                        best_neighbor = temp_state
                        neighbor_found = True
            
            if not neighbor_found:
                break # Stuck in local optimum
            
            current_state = best_neighbor
            current_conflicts = min_conflicts
            
            if current_conflicts == 0:
                return current_state, current_conflicts, iterations, time.time() - start_time
                
    return current_state, current_conflicts, iterations, time.time() - start_time
