import numpy as np
import random
import matplotlib.pyplot as plt
import csv

def create_distance_matrix(locations):
    coords = np.array(locations)
    diff = coords[:, None, :] - coords[None, :, :]
    return np.sqrt((diff ** 2).sum(axis=-1))

def total_distance(path, dist_matrix):
    return sum(dist_matrix[path[i], path[(i+1) % len(path)]] for i in range(len(path)))

def two_opt(path, dist_matrix):
    best = path[:]
    best_dist = total_distance(best, dist_matrix)
    n = len(path)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue
                new_route = best[:i] + best[i:j][::-1] + best[j:]
                new_dist = total_distance(new_route, dist_matrix)
                if new_dist < best_dist:
                    best, best_dist = new_route, new_dist
                    improved = True
        path = best
    return best

def tournament_selection(population, fitnesses, k=5):
    competitors = random.sample(range(len(population)), k)
    winner = min(competitors, key=lambda idx: fitnesses[idx])
    return population[winner]

def order_crossover(p1, p2):
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    child = [-1] * n
    child[a:b] = p1[a:b]
    pos = b
    for city in p2[b:] + p2[:b]:
        if city not in child:
            if pos >= n:
                pos = 0
            child[pos] = city
            pos += 1
    return child

def genetic_algorithm(locations,
                      population_size=100,
                      generations=200,
                      elite_size=10,
                      mutation_rate=0.1,
                      tourney_k=5):
    dist_matrix = create_distance_matrix(locations)
    n = len(locations)
    population = [random.sample(list(range(n)), n) for _ in range(population_size)]

    best_distances = []
    avg_distances = []

    for gen in range(generations):
        fitnesses = [total_distance(p, dist_matrix) for p in population]
        sorted_idx = sorted(range(population_size), key=lambda i: fitnesses[i])
        elites = [population[i] for i in sorted_idx[:elite_size]]

        new_pop = elites.copy()
        while len(new_pop) < population_size:
            parent1 = tournament_selection(population, fitnesses, k=tourney_k)
            parent2 = tournament_selection(population, fitnesses, k=tourney_k)
            child = order_crossover(parent1, parent2)
            if random.random() < mutation_rate:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]
            child = two_opt(child, dist_matrix)
            new_pop.append(child)
        population = new_pop

        best_dist = total_distance(elites[0], dist_matrix)
        avg_dist = sum(fitnesses) / len(fitnesses)
        best_distances.append(best_dist)
        avg_distances.append(avg_dist)

    final_fitnesses = [total_distance(p, dist_matrix) for p in population]
    best_idx = min(range(population_size), key=lambda i: final_fitnesses[i])
    return population[best_idx], best_distances, avg_distances

def plot_path(locations, path, save_path="best_path.png"):
    ordered = [locations[i] for i in path] + [locations[path[0]]]
    xs, ys = zip(*ordered)
    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, marker='o', linestyle='-', color='b')
    for idx, (x, y) in enumerate(ordered[:-1]):
        plt.text(x, y, str(path[idx]), fontsize=9, ha='right')
    plt.title("Best TSP Route")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()

def plot_convergence(best_distances, avg_distances, save_path="convergence.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(best_distances, label='Best Distance')
    plt.plot(avg_distances, label='Average Distance', linestyle='--')
    plt.xlabel("Generation")
    plt.ylabel("Distance")
    plt.title("GA Convergence over Generations")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()

if __name__ == '__main__':
    with open('ucsd_locations.csv') as f:
        reader = csv.DictReader(f)
        locs = [(float(row['lon']), float(row['lat'])) for row in reader]
    best_path, best_hist, avg_hist = genetic_algorithm(locs)
    print("Best tour length:", total_distance(best_path, create_distance_matrix(locs)))
    plot_path(locs, best_path)
    plot_convergence(best_hist, avg_hist)
