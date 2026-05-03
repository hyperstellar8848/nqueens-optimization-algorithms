# N-Queens Algorithms Comparison

## Problem Definition
The **$N$-Queens Problem** is a constraint satisfaction challenge where $N$ queens must be placed on an $N \times N$ chessboard so that no two queens threaten each other. A solution requires that no two queens share the same:
*   **Row**
*   **Column**
*   **Diagonal**


## Algorithms Descriptions

### Hill Climbing (HC)
*   **Concept:** A local search algorithm that moves from the current state to the best neighboring state (the one with the minimum number of conflicts).
*   **Local Optima:** HC often gets stuck on "plateaus" or local peaks. To solve this, **Random Restarts** are used to begin the search from a new random configuration.

### Simulated Annealing (SA)
*   **Concept:** A probabilistic technique that mimics the cooling of metals.
*   **Probability:** It allows "bad moves" (moves that increase conflicts) based on the Boltzmann distribution formula:
  $$P = e^{-\frac{\Delta E}{T}}$$
  Where $\Delta E$ is the change in conflicts and $T$ is the current temperature. As $T$ decreases, the probability of accepting bad moves drops.

### Genetic Algorithm (GA)
*   **Concept:** A population-based heuristic inspired by natural selection. 
*   **Operators:**
    *   **Selection:** Choosing the fittest individuals.
    *   **Crossover:** Combining two "parents" to create a "child."
    *   **Mutation:** Randomly changing a queen's position to maintain genetic diversity.


## Conclusion 
1.  **Efficiency:** **Hill Climbing** is the fastest for small $N$, but it becomes inefficient as $N$ grows due to the high number of required restarts.
2.  **Robustness:** **Simulated Annealing** is usually the most reliable. It escapes local optima effectively and scales better than GA.
3.  **Computational Cost:** **Genetic Algorithm** is the most resource-heavy. It requires maintaining a population in memory and calculating fitness for every individual in every generation.

> **Final Verdict:** For a standard $N$-Queens implementation, **Simulated Annealing** provides the best balance of success rate and execution time.
