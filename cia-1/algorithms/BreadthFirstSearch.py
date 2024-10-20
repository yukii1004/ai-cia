from collections import deque

class BFS:
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
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])

        while queue:
            current, path = queue.popleft()

            if current == self.end:
                yield path, visited, True
                return

            yield path, visited, False

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
        yield [], visited, False

    def debug_solve(self):
        steps = 0
        for path, visited, found in self.solve():
            steps += 1
            print(f"Step {steps}: Current position: {path[-1]}, Path length: {len(path)}, Visited cells: {len(visited)}")
            if found:
                print("Solution found!")
                return
        print("No solution found.")