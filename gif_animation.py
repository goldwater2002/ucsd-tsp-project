import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_path_evolution(locations, path_history, filename="tsp_evolution.gif"):
    """
    Generate an animated GIF showing how the TSP path evolves over generations.
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    def update(i):
        ax.clear()
        path = path_history[i] + [path_history[i][0]]
        xs, ys = zip(*[locations[j] for j in path])
        ax.plot(xs, ys, marker='o', linestyle='-', color='blue')
        for idx in range(len(path) - 1):
            ax.text(xs[idx], ys[idx], str(path[idx]), fontsize=8, ha='right')
        ax.set_title(f'Generation {i+1}')
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.grid(True)

    ani = FuncAnimation(fig, update, frames=len(path_history), interval=200)
    ani.save(filename, writer='pillow')
    print(f"[GIF saved] → {filename}")
