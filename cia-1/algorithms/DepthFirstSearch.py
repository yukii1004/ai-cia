import numpy as np

class DFS:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.rows, self.cols = maze.shape
        self.start = start
        self.end = end
        self.visited = set()
        self.path = []

    def is_valid_move(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x, y] != 1

    def solve(self):
        stack = [(*self.start, [self.start])]
        
        while stack:
            x, y, current_path = stack.pop()
            
            if (x, y) == self.end:
                self.path = current_path
                yield self.path, list(self.visited), True  # Path found
                return
            
            if (x, y) not in self.visited and self.is_valid_move(x, y):
                self.visited.add((x, y))
                yield current_path, list(self.visited), False  # Intermediate step
                
                # Check all four directions: up, right, down, left
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    next_x, next_y = x + dx, y + dy
                    if self.is_valid_move(next_x, next_y):
                        new_path = current_path + [(next_x, next_y)]
                        stack.append((next_x, next_y, new_path))
        yield [], list(self.visited), False