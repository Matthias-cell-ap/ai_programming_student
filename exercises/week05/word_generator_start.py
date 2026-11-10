"""
Oefening 1: Word Generator (Genetisch Algoritme)
==================================================
Evolueer een populatie van willekeurige zinnen naar een doelzin.
"""
import random
import string


class WordPuzzle:
    def __init__(self, target_phrase, population_size=100, mutation_rate=0.01, num_generations=1000):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.num_generations = num_generations

    def generate_phrase(self, length):
        return ''.join(random.choice(string.printable) for _ in range(length))

    def calculate_fitness(self, phrase):
        score = sum(1 for a, b in zip(phrase, self.target_phrase) if a == b)
        return score / len(self.target_phrase)

    def generate_population(self, size, phrase_length):
        arr = []
        for _ in range(self.population_size):
            arr.append(self.generate_phrase(phrase_length))
        return arr

    def crossover(self, phrase1, phrase2):
        point = random.randint(1, len(phrase1) - 1)
        return phrase1[:point] + phrase2[point:]

    def mutate(self, phrase, rate):
        chars = list(phrase)
        for i in range(len(chars)):
            if random.random() < rate:
                chars[i] = random.choice(string.printable)
        return ''.join(chars)

    def select_best(self, population):
        return max(population, key=self.calculate_fitness)

    def genetic_algorithm(self):
        pop = self.generate_population('_', len(self.target_phrase))
        for gen in range(self.num_generations):
            pop.sort(key=self.calculate_fitness, reverse=True)
            if gen % 10 == 0:
                print(gen, self.select_best(pop))
            elite = pop[:int(0.1 * self.population_size)]
            new = elite.copy()
            while len(new) < self.population_size:
                p1 = random.choice(pop[:50])
                p2 = random.choice(pop[:50])
                child = self.crossover(p1, p2)
                new.append(self.mutate(child, self.mutation_rate))
            pop = new
        return pop[0]


def main():
    target_phrase = "De basiswetten van de robotica werden ontwikkeld door Asimov"
    puzzle = WordPuzzle(target_phrase)
    best_phrase = puzzle.genetic_algorithm()
    print(f"Beste zin: {best_phrase}")


if __name__ == "__main__":
    main()