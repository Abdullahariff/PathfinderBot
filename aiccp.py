import heapq

# Manhattan distance
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Heuristic: sum of Manhattan distances to remaining targets
def heuristic(pos, targets):
    return sum(manhattan(pos, t) for t in targets)

# A* search from current to next target
def a_star(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (heuristic(start, [goal]), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X':
                neighbor = (nr, nc)
                if neighbor not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(neighbor, [goal])
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

# Main function to find full path to all targets
def solve_rescue(grid):
    rows, cols = len(grid), len(grid[0])
    targets = []
    start = None

    # Find start and targets
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'R':
                start = (r, c)
            elif grid[r][c] == 'T':
                targets.append((r, c))

    full_path = []
    total_cost = 0
    current = start

    while targets:
        # Choose closest target
        next_target = min(targets, key=lambda t: manhattan(current, t))
        path, cost = a_star(current, next_target, grid)

        if not path:
            print("No path to", next_target)
            return

        full_path.extend(path[1:])  # Avoid duplicating current
        total_cost += cost
        current = next_target
        targets.remove(next_target)

    # Mark the final grid
    for r, c in full_path:
        if grid[r][c] == '_':
            grid[r][c] = '*'

    return grid, full_path, total_cost
grid = [
    ['_', '_', '_', 'X', '_'],
    ['_', 'X', 'X', 'T', '_'],
    ['_', 'X', 'R', '_', '_'],
    ['T', '_', '_', 'X', '_'],
    ['_', '_', 'X', 'T', '_']
]

final_grid, path, cost = solve_rescue(grid)

print("Final Grid:")
for row in final_grid:
    print(" ".join(row))


print("\nTotal Moves:", cost)
print("Full Path:", path)
