# Search Algorithms Implementation

## CIA-1:
> The 12 search algorithms implemented in this repository are:
1. British Museum Search
2. Depth-first Search                   
3. Breadth-first Search
4. Hill-climbing Search
5. Beam Search
6. ORACLE
7. Branch and Bound
8. Dead Horse Principle (B&B with Exteded List)
9. B&B with Cost + Heuristics
10. A* (B&B with Cost + Heuristics + Dead Horse Principle) 
11. AO*
12. Best First Search

> Details:
- All of the algorithms in this repository are implemented with python.
- They are implemented with a twist to visually distinguish the properties of each search algorithm. 
- First we generate a maze using DFS and recursive backtracking algorithm.
- Then each of the algorithms solve the maze which is visualized using matplotlib.

<hr>

## CIA-2:
>  Details:
- The Min-Max algorithm recursively evalutes all possible moves in a game tree and finds the optimal move for the player assuming the opponent also plays optimally.
- The Minimizing level finds the move with the lowest score and the Maximizing level finds the move with the highest score.
- This algorithm repeats this process for the predefined depth of the game tree, and outputs the best move and the best score.

> Initial Min-Max Tree:

![Min-Max Tree](./cia-2/min-max%20tree.png)

> Final tree after Min-Max evaluation:

![Min-Max Result](./cia-2/min-max%20result.png)

