import numpy as np
import matplotlib.pyplot as plt

def load_maze_from_txt(filename='maze.txt'):
    return np.loadtxt(filename, dtype=int)

maze = load_maze_from_txt('./cia-1/maze.txt')

def display_maze(maze):
    fig = plt.figure(figsize=(10, 10))
    fig.canvas.manager.set_window_title('Maze Solver')
    plt.imshow(maze, cmap='binary')
    plt.axis('off')
    plt.show()

display_maze(maze)