from queue import PriorityQueue

class BS:
    def __init__(self, maze, start, end, beam_width=3):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.beam_width = beam_width

    def manhattan_distance(self, pos):
        return abs(pos[0] - self.end[0]) + abs(pos[1] - self.end[1])

    def is_valid(self, pos):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols and self.maze[pos[0]][pos[1]] == 0

    def get_neighbors(self, pos):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return [(pos[0] + d[0], pos[1] + d[1]) for d in directions if self.is_valid((pos[0] + d[0], pos[1] + d[1]))]

    def solve(self):
        beam = PriorityQueue()
        beam.put((self.manhattan_distance(self.start), [self.start]))
        visited = set()

        while not beam.empty():
            current_beam = []
            
            for _ in range(min(self.beam_width, beam.qsize())):
                _, path = beam.get()
                current = path[-1]

                if current == self.end:
                    yield path, visited, True
                    return

                if current in visited:
                    continue

                visited.add(current)
                yield path, visited, False

                for neighbor in self.get_neighbors(current):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        priority = self.manhattan_distance(neighbor)
                        current_beam.append((priority, new_path))

            # Sort and select the best candidates for the next beam
            current_beam.sort(key=lambda x: x[0])
            for candidate in current_beam[:self.beam_width]:
                beam.put(candidate)

        yield [], visited, False