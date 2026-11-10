"""
Oefening 2: Knapsack Probleem met pygad
=========================================
Los het knapsack probleem op met een genetisch algoritme.
"""
import pygad
import numpy as np

# Data
capaciteit = 10
gewichten = np.array([5, 4, 6, 3])
waarden = np.array([10, 40, 30, 50])
n_voorwerpen = len(gewichten)


def fitness_func(ga_instance, solution, solution_idx):
    fitness = 0
    cost = 0
    for i in range(n_voorwerpen):
        if solution[i] == 1:
            fitness += waarden[i]
            cost += gewichten[i]
    if cost > capaciteit:
        return fitness - 1000
    return fitness


# TODO: configureer pygad.GA (zie OneMax.py uit de cursus)
ga_instance = pygad.GA(
    num_generations=50,
    num_parents_mating=4,
    fitness_func=fitness_func,
    sol_per_pop=10,
    num_genes=n_voorwerpen,
    gene_space=[0, 1],
    gene_type=int,
    mutation_percent_genes=10,
)
ga_instance.run()

solution, solution_fitness, _ = ga_instance.best_solution()
print("Gekozen voorwerpen:", solution)
print("Totale waarde:", solution_fitness)