import heapq

class DHP:
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
        priority_queue = [(self.manhattan_distance(self.start), 0, [self.start])]
        extended_list = {self.start: 0}  # Store the lowest cost to reach each position
        visited = set()

        while priority_queue:
            _, cost, path = heapq.heappop(priority_queue)
            current = path[-1]

            if current == self.end:
                yield path, visited, True
                return

            if current in visited:
                continue

            visited.add(current)
            yield path, visited, False

            for neighbor in self.get_neighbors(current):
                new_cost = cost + 1
                if neighbor not in extended_list or new_cost < extended_list[neighbor]:
                    extended_list[neighbor] = new_cost
                    new_path = path + [neighbor]
                    priority = new_cost + self.manhattan_distance(neighbor)
                    heapq.heappush(priority_queue, (priority, new_cost, new_path))

        yield [], visited, False