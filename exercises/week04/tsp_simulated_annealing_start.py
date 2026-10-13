"""
Oefening: TSP met Simulated Annealing
======================================
"""
import math
import random

import numpy as np


class TSPSolver:
    def __init__(self, distance_matrix, initial_temperature=100,
                 cooling_rate=0.95, num_iterations=1000):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations

    def total_distance(self, tour: list[int]) -> float:
        """Bereken de totale afstand van een tour, inclusief terugkeer
        naar de startstad.

        Args:
            tour: permutatie van steden (lijst van indices).

        Returns:
            De totale afstand van de tour.
        """
        distance = 0
        for i in range(len(tour)-1):
            distance += distance_matrix[tour[i], tour[i+1]]
        distance += distance_matrix[tour[-1]][tour[0]]
        return distance

    @staticmethod
    def _canonical(tour: list[int]) -> list[int]:
        """Draai de tour zodat stad 0 vooraan staat (richting blijft gelijk).
        Hulpfunctie, hoeft niet aangepast te worden.
        """
        start = tour.index(0)
        return tour[start:] + tour[:start]

    def simulated_annealing(self) -> tuple[list[int], float]:
        """Simulated annealing voor TSP.

        Returns:
            Een tuple (best_tour, best_distance).
        """
        # TODO Stap 3:
        # - start met een willekeurige tour (beste tot nu toe = deze)
        # - herhaal num_iterations keer:
        #     - kies 2 willekeurige steden en verwissel hun positie
        #     - bereken de nieuwe afstand
        #     - korter: aanvaard
        #     - langer: aanvaard met kans exp(-Δ / T)
        #     - update temperatuur: T *= cooling_rate
        #     - hou de beste tour bij
        # - return best_tour, best_distance
        best_tour = list(range(self.num_cities))
        best_distance = self.total_distance(best_tour)
        temp = self.initial_temperature

        for i in range(self.num_iterations):
            num1, num2 = random.sample(range(self.num_cities), 2)
            tour = best_tour.copy()
            tour[num1], tour[num2] = tour[num2], tour[num1]
            distance = self.total_distance(tour)

            mindelta = best_distance - distance

            if mindelta > 0 or random.random() < math.exp(mindelta / temp):
                best_tour = tour
                best_distance = distance
            temp *= self.cooling_rate

        return self._canonical(best_tour), best_distance


if __name__ == "__main__":
    distance_matrix = np.array([
        [0, 29, 20, 21],
        [29, 0, 15, 18],
        [20, 15, 0, 25],
        [21, 18, 25, 0]
    ])

    avg_dist=0

    for i in range(50):
        tsp_solver = TSPSolver(distance_matrix)
        best_tour, best_distance = tsp_solver.simulated_annealing()
        avg_dist += best_distance/50

    print("Avg Best Tour:", avg_dist)
    print("Best Distance:", best_distance)