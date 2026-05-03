from n_queens_base import count_conflicts, random, time

def genetic_algorithm(n, pop_size, mutation_rate, generations):
    start_time = time.time()
    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(pop_size)]
    history = []
    
    for gen in range(generations):
        population = sorted(population, key=lambda x: count_conflicts(x))
        best_conf = count_conflicts(population[0])
        history.append(best_conf)
        
        if best_conf == 0:
            return population[0], 0, gen, time.time() - start_time, history
            
        new_pop = population[:2] # Elitism
        while len(new_pop) < pop_size:
            p1, p2 = random.choice(population[:pop_size//2]), random.choice(population[:pop_size//2])
            cp = random.randint(1, n-1)
            child = p1[:cp] + p2[cp:]
            if random.random() < mutation_rate:
                child[random.randint(0, n-1)] = random.randint(0, n-1)
            new_pop.append(child)
        population = new_pop
        
    return population[0], count_conflicts(population[0]), generations, time.time() - start_time, history
