# UCSD Campus TSP Route Planner 🧭

This project applies a Genetic Algorithm (GA) to solve a Traveling Salesman Problem (TSP) over real-world geographic coordinates of landmarks on the UCSD campus.

## 🔍 Project Overview

- Uses real-world coordinates from `ucsd_locations.csv`
- Applies **Genetic Algorithm + 2-opt local search** to find optimized routes
- Visualizes the best path on a static map, an interactive campus map, and a GIF showing generation-wise evolution
- Designed for research lab applications and optimization coursework

## 📊 Features

- **Distance Matrix Optimization** using NumPy broadcasting
- **Crossover & Mutation** operators in GA
- **2-opt Local Search** for child refinement
- **Visual Outputs**:
  - `best_path.png` — static route visualization
  - `convergence.png` — GA performance over generations
  - `ucsd_map_path.html` — interactive map with route
  - `tsp_evolution.gif` — animated GIF showing path evolution

## 📁 Files

| File | Description |
|------|-------------|
| `tsp_ga_final.py` | Main script to run the algorithm |
| `map_visualization.py` | Draw TSP path on a real UCSD campus map using folium |
| `gif_animation.py` | Generate GIF of the route evolving over generations |
| `ucsd_locations.csv` | List of UCSD campus landmarks with latitude & longitude |
| `best_path.png` | Generated best route plot |
| `convergence.png` | GA convergence curve |
| `ucsd_map_path.html` | Interactive map (open in browser) |
| `tsp_evolution.gif` | Animated route evolution |
| `requirements.txt` | Required packages |

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ucsd-campus-tsp.git
   cd ucsd-campus-tsp
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python tsp_ga_final.py
   ```

4. Open generated visuals:
   - Static: `best_path.png`, `convergence.png`
   - Map: Open `ucsd_map_path.html` in a browser
   - Animation: View `tsp_evolution.gif`

## 🧠 Author's Background

This project was developed as part of an undergraduate portfolio in **Applied Math** and **Cognitive Science (ML & Neural Computation)** at UC San Diego, with the goal of joining a research lab and expanding real-world experience in optimization & algorithm design.

## 📬 Contact

If you're a lab looking for an enthusiastic research assistant with strong math and Python skills, feel free to reach out!

---
*Made with 💡 and Python*
