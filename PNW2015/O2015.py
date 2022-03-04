rows = 5
cols = 4
grid = []

for i in range(rows):
    grid.append([int(i) for i in input()])

def getNeighbors(num, node):
    neighbors = []
    nums = [-(num), num]
    for i in nums:
        if node[0] + i >= 0 and node[0] + i < rows:
            neighbors.append((node[0] + i, node[1]))
        if node[1] + i >= 0 and node[1] + i < cols:
            neighbors.append((node[0], node[1] + i))
    return neighbors
def bfs(start, goal):
    visited = [start]
    queue = [start]
    path_found = False
    step = {}
    step[start] = 0

    while len(queue) != 0:
        curr = queue.pop(0) 
        if curr == goal:
            path_found = True
            break
        neighbors = getNeighbors(grid[curr[0]][curr[1]], curr)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                step[neighbor] = step[curr] + 1
    
    if path_found is True:
        return step[goal]
    else:
        return "IMPOSSIBLE"
            
print(bfs((0,0), (rows - 1, cols - 1)))

