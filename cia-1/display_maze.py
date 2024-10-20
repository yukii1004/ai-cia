import numpy as np
import matplotlib.pyplot as plt

maze = np.loadtxt('./cia-1/maze.txt', dtype=int)

def display_maze(maze):
    fig = plt.figure(figsize=(10, 10))
    fig.canvas.manager.set_window_title('Maze Solver')
    plt.imshow(maze, cmap='binary')
    plt.axis('off')
    plt.show()

display_maze(maze)