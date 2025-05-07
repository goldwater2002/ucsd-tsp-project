import numpy as np
import random

def compute_distance(loc1, loc2):
    return np.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

def total_distance(path, locations):
    dist = 0
    for i in range(len(path)):
        loc1 = locations[path[i]]
        loc2 = locations[path[(i + 1) % len(path)]]
        dist += compute_distance(loc1, loc2)
    return dist

def genetic_algorithm(locations, population_size=100, generations=200):
    n = len(locations)
    population = [random.sample(range(n), n) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda p: total_distance(p, locations))
        next_gen = population[:10]
        for _ in range(population_size - 10):
            p1, p2 = random.sample(next_gen, 2)
            cut = random.randint(1, n - 2)
            child = p1[:cut] + [x for x in p2 if x not in p1[:cut]]
            if random.random() < 0.1:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]
            next_gen.append(child)
        population = next_gen

    best_path = min(population, key=lambda p: total_distance(p, locations))
    return best_path
