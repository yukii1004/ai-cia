import heapq

class BBCH:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])

    def manhattan_distance(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def is_valid(self, pos):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols and self.maze[pos[0]][pos[1]] != 1

    def get_neighbors(self, pos):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [(pos[0] + d[0], pos[1] + d[1]) for d in directions if self.is_valid((pos[0] + d[0], pos[1] + d[1]))]

    def get_cost(self, pos):
        # Cost is higher for cells with higher values (except walls)
        return self.maze[pos[0]][pos[1]] if self.maze[pos[0]][pos[1]] != 1 else float('inf')

    def solve(self):
        start_cost = self.get_cost(self.start)
        start_heuristic = self.manhattan_distance(self.start)
        priority_queue = [(start_cost + start_heuristic, start_cost, start_heuristic, [self.start])]
        visited = set()
        g_scores = {self.start: start_cost}

        while priority_queue:
            _, current_cost, _, path = heapq.heappop(priority_queue)
            current = path[-1]

            if current == self.end:
                yield path, visited, True
                return

            if current in visited:
                continue

            visited.add(current)
            yield path, visited, False

            for neighbor in self.get_neighbors(current):
                neighbor_cost = current_cost + self.get_cost(neighbor)
                
                if neighbor not in g_scores or neighbor_cost < g_scores[neighbor]:
                    g_scores[neighbor] = neighbor_cost
                    heuristic = self.manhattan_distance(neighbor)
                    new_path = path + [neighbor]
                    priority = neighbor_cost + heuristic
                    heapq.heappush(priority_queue, (priority, neighbor_cost, heuristic, new_path))

        yield [], visited, False