import random

class BMS:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])

    def is_valid(self, pos):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols and self.maze[pos[0]][pos[1]] == 0

    def get_neighbors(self, pos):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [(pos[0] + d[0], pos[1] + d[1]) for d in directions if self.is_valid((pos[0] + d[0], pos[1] + d[1]))]

    def solve(self):
        stack = [(self.start, [self.start])]
        visited = set()

        while stack:
            current, path = stack.pop(random.randint(0, len(stack) - 1))

            if current == self.end:
                yield path, visited, True
                return

            if current in visited:
                continue

            visited.add(current)
            yield path, visited, False

            neighbors = self.get_neighbors(current)
            random.shuffle(neighbors)  # Randomize exploration order
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))

        yield [], visited, False