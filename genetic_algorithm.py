from n_queens_base import count_conflicts, random, time

def genetic_algorithm(n, pop_size=100, mutation_rate=0.1, generations=2000):
    start_time = time.time()

    population = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(pop_size)]
    
    for gen in range(generations):
        # Calculate fitness (lower conflicts = higher fitness)
        # Using 1 / (1 + conflicts) as fitness score
        population = sorted(population, key=lambda x: count_conflicts(x))
        
        if count_conflicts(population[0]) == 0:
            return population[0], 0, gen, time.time() - start_time
            
        new_population = population[:2] # Elitism: keep best 2 for next gen
        
        while len(new_population) < pop_size:
            # Selection 
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            
            # Crossover (Single point: cp)
            cp = random.randint(1, n - 1)
            child = parent1[:cp] + parent2[cp:]
            
            # Mutation
            if random.random() < mutation_rate:
                child[random.randint(0, n - 1)] = random.randint(0, n - 1)
                
            new_population.append(child)
        population = new_population
        
    return population[0], count_conflicts(population[0]), generations, time.time() - start_time
