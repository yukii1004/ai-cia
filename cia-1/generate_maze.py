import numpy as np
import matplotlib.pyplot as plt
import random

def generate_maze_dfs(width, height):
    width = width if width % 2 == 1 else width + 1
    height = height if height % 2 == 1 else height + 1

    # 1's represent the walls and 0's represent the paths.
    maze = np.ones((height, width), dtype=int)

    def carve_passages(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions) # to keep the path random
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy // 2][x + dx // 2] = 0
                carve_passages(nx, ny)

    # start from top-left
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0 
    carve_passages(start_x, start_y)

    return maze

maze = generate_maze_dfs(99, 99)

def save_maze_as_txt(maze, filename='maze.txt'):
    np.savetxt(filename, maze, fmt='%d')
    print(f'Maze saved to {filename}')

save_maze_as_txt(maze)