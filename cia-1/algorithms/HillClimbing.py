import random

class HC:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])

    def manhattan_distance(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def is_valid(self, pos):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols and self.maze[pos[0]][pos[1]] == 0

    def get_neighbors(self, pos):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [(pos[0] + d[0], pos[1] + d[1]) for d in directions if self.is_valid((pos[0] + d[0], pos[1] + d[1]))]

    def solve(self):
        current = self.start
        path = [current]
        visited = set([current])

        while current != self.end:
            neighbors = self.get_neighbors(current)
            if not neighbors:
                # If stuck, restart from the beginning
                current = self.start
                path = [current]
                visited = set([current])
                yield path, visited, False
                continue

            # Find the neighbor closest to the goal
            best_neighbor = min(neighbors, key=self.manhattan_distance)
            
            if self.manhattan_distance(best_neighbor) >= self.manhattan_distance(current):
                # If no better neighbor, choose a random unvisited neighbor
                unvisited_neighbors = [n for n in neighbors if n not in visited]
                if unvisited_neighbors:
                    best_neighbor = random.choice(unvisited_neighbors)
                else:
                    # If all neighbors visited, restart from the beginning
                    current = self.start
                    path = [current]
                    visited = set([current])
                    yield path, visited, False
                    continue

            current = best_neighbor
            path.append(current)
            visited.add(current)
            yield path, visited, False

        yield path, visited, True