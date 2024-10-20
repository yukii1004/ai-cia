import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from algorithms.AOstar import AO
from algorithms.Astar import ASTAR
from algorithms.BB_CH import BBCH
from algorithms.BeamSearch import BS
from algorithms.BestFirstSearch import BESTFS
from algorithms.Branch_Bound import BB
from algorithms.BreadthFirstSearch import BFS
from algorithms.BritishMuseumSearch import BMS
from algorithms.DeadHorsePrinciple import DHP
from algorithms.DepthFirstSearch import DFS
from algorithms.HillClimbing import HC
from algorithms.ORACLE import OR

# Define the Maze
maze = np.loadtxt('maze.txt', dtype=int)

# Algorithm dictionary
algorithms = {
    'AO*': AO,
    'A*': ASTAR,
    'Branch and Bound with Cost and Heuiristics': BBCH,
    'Beam Search': BS,
    'Best First Search': BESTFS,
    'Branch and Bound': BB,
    'Breadth First Search': BFS,
    'British Museum Search': BMS,
    'Dead Horse Principle': DHP,
    'Depth First Search': DFS,
    'Hill Climbing': HC,
    'ORACLE': OR
}

def choose_algorithm():
    print("Available algorithms:")
    for i, algo in enumerate(algorithms.keys(), 1):
        print(f"{i}. {algo}")
    
    while True:
        try:
            choice = int(input("Enter the number of the algorithm you want to use: "))
            if 1 <= choice <= len(algorithms):
                return list(algorithms.values())[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Choose the algorithm
selected_algorithm = choose_algorithm()

# Initialize the chosen algorithm
start = (1, 1)  # Starting point
end = (maze.shape[0] - 2, maze.shape[1] - 2)  # End point
algo_instance = selected_algorithm(maze, start, end)

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title(f"Maze solving using {selected_algorithm.__name__}")
ax.axis('off')

im = ax.imshow(maze, cmap='binary')
visited_plot = ax.scatter([], [], color='blue', alpha=0.3, s=50)
path_plot, = ax.plot([], [], color='red', linewidth=2, marker='o', markersize=6)

def init():
    visited_plot.set_offsets(np.empty((0, 2)))
    path_plot.set_data([], [])
    return visited_plot, path_plot

def update(frame):
    current_path, visited, path_found = frame
    
    if visited:
        visited_y, visited_x = zip(*visited)
        visited_plot.set_offsets(np.c_[visited_x, visited_y])
    
    if current_path:
        path_y, path_x = zip(*current_path)
        path_plot.set_data(path_x, path_y)
    
    if path_found:
        ax.set_title(f"Path found using {selected_algorithm.__name__}")
    
    return visited_plot, path_plot

anim = FuncAnimation(fig, update, frames=algo_instance.solve,
                     init_func=init, blit=True, interval=50,
                     repeat=False, save_count=1000)  # Limit frames to 1000

plt.show()