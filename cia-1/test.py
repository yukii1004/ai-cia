import numpy as np
import matplotlib.pyplot as plt
import time

# Function to load the maze from a file
def load_maze(filename='maze.txt'):
    return np.loadtxt(filename, dtype=int)

# Function to display the maze
def display_maze(maze, path=None, backtrack=None, final=False):
    plt.imshow(maze, cmap='binary')
    plt.title('DFS Maze Solver')
    plt.axis('off')
    
    if path is not None:
        if final:
            # Color the cells of the final path red
            path_array = np.array(path)
            maze_rgb = plt.cm.binary(maze)
            maze_rgb[path_array[:, 0], path_array[:, 1], :3] = [1, 0, 0]  # Red color
            plt.imshow(maze_rgb)
        else:
            # Mark the path on the maze in red
            for (x, y) in path:
                plt.text(y, x, 'o', color='red', ha='center', va='center', fontsize=8)

    if backtrack is not None and not final:
        # Mark the backtracked points in blue
        for (x, y) in backtrack:
            plt.text(y, x, 'o', color='blue', ha='center', va='center', fontsize=8)

    plt.draw()
    plt.pause(0.05)  # Pause for a short time to visualize the updates
    
    if not final:
        plt.clf()  # Clear the figure for the next iteration, but not for the final display

# Depth-First Search algorithm with visualization
def dfs(maze, start, end):
    stack = [start]
    visited = set()
    path = []  # This will store the current path being explored
    backtrack = []  # This will store nodes that were visited but not part of the final path

    try:
        while stack:
            current = stack.pop()

            # If already visited, skip processing this node
            if current in visited:
                continue

            visited.add(current)
            path.append(current)  # Add current position to the path being explored

            # Check if we reached the end
            if current == end:
                display_maze(maze, path, final=True)  # Display the final path in red
                return path  # Return the path if we reached the end

            # Get possible moves: up, down, left, right
            x, y = current
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            
            # Track if we find any valid unvisited neighbor
            found_neighbor = False
            for neighbor in neighbors:
                nx, ny = neighbor
                if (0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and
                    maze[nx, ny] == 0 and neighbor not in visited):
                    stack.append(neighbor)
                    found_neighbor = True

            # If no valid neighbors were found, mark this point as backtrack
            if not found_neighbor:
                backtrack.append(current)
                display_maze(maze, path, backtrack)

    except KeyboardInterrupt:
        print("Maze solving interrupted. Exiting...")
        return None

    return None  # Return None if no path is found

# Main function to execute the maze solver
def main():
    maze = load_maze('./cia-1/maze.txt')
    if maze is None:
        return
    
    start = (1, 1)  # Starting point (you can change this)
    end = (maze.shape[0] - 2, maze.shape[1] - 2)  # End point (you can change this)

    # Start the DFS
    path = dfs(maze, start, end)

    if path:
        print("Path found!")
    else:
        print("No path found or interrupted.")

    plt.show(block=True)  # Keep the window open until manually closed

# Run the maze solver
if __name__ == "__main__":
    plt.ion()  # Turn on interactive mode
    main()
    input("Press Enter to close the plot...")  # Wait for user input before closing