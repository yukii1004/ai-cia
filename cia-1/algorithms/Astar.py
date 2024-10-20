import numpy as np
from queue import PriorityQueue

class ASTAR:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows, self.cols = maze.shape
        self.visited = set()
        self.g_score = {}
        self.f_score = {}
        self.came_from = {}

    def heuristic(self, a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def get_neighbors(self, node):
        x, y = node
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx][ny] != 1:
                neighbors.append((nx, ny))
        return neighbors

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]

    def solve(self):
        start = self.start
        goal = self.end

        open_set = PriorityQueue()
        open_set.put((0, start))
        self.g_score[start] = 0
        self.f_score[start] = self.heuristic(start, goal)

        while not open_set.empty():
            current = open_set.get()[1]

            if current == goal:
                path = self.reconstruct_path(current)
                yield path, list(self.visited), True
                return

            self.visited.add(current)
            yield self.reconstruct_path(current), list(self.visited), False

            for neighbor in self.get_neighbors(current):
                tentative_g_score = self.g_score[current] + 1

                if neighbor not in self.g_score or tentative_g_score < self.g_score[neighbor]:
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    self.f_score[neighbor] = f_score
                    if neighbor not in [i[1] for i in open_set.queue]:
                        open_set.put((f_score, neighbor))

        yield [], list(self.visited), False  # No path found