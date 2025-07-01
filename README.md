PathfinderBot
PathfinderBot is a Python-based simulation of a rescue robot that uses the A* search algorithm to navigate a grid and reach all designated targets while avoiding obstacles. This project demonstrates intelligent pathfinding in a discrete environment using Manhattan distance as a heuristic.

Features
Implements A* (A-Star) algorithm for shortest path search

Uses Manhattan distance heuristic for grid-based movement

Supports multiple targets (rescues) in a single grid

Dynamically selects the nearest target at each step

Marks the complete traversal path on the final grid

Modular and easy-to-understand Python implementation

How It Works
The robot:

Starts at a designated starting point (R)

Identifies all targets (T) on the grid

Chooses the closest target based on Manhattan distance

Uses A* search to compute the optimal path to that target

Repeats the process until all targets are visited

The grid includes:

R: Robot’s starting position

T: Targets to rescue

X: Obstacles the robot cannot cross

_: Empty traversable space

*: Cells marked as part of the robot’s path after traversal

Example Grid
_ _ _ X _
_ X X T _
_ X R _ _
T _ _ X _
_ _ X T _
After execution, the robot navigates the grid, reaches all targets, and outputs:

The final grid with visited cells marked

Total number of steps taken (cost)

The full path coordinates taken by the robot

Requirements
Python 3.x

No external libraries required (uses built-in heapq)
