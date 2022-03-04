ins = [int(i) for i in input().split()]

rows = ins[0]
cols = ins[1]
grid = []

for i in range(rows):
    row = [int(i) for i in input()]
    grid.append(row)

visited = []
queue = []
def getNeighbors(node, rows, cols, num):
    neighbors = []
    if node[0] - num >= 0:
        neighbors.append((node[0] - num, node[1]))
    if node[1] - num >= 0:
        neighbors.append((node[0], node[1] - num))
    if node[0] + num < rows:
        neighbors.append((node[0] + num, node[1]))
    if node[1] + num < cols:
        neighbors.append((node[0], node[1] + num))
    return neighbors

def bfs(visited, grid, start, goal):
    
    visited.append(start)
    queue.append(start)
    
    parent = {}
    parent[start] = None

    path_found = False
    step_list = []
    while len(queue) != 0: 
        current = queue.pop()
        if current == goal:
            path_found = True
            next = goal
            steps = 0
            while parent[next] is not None:
                next = parent[next]
                steps += grid[next[0]][next[1]]
            step_list.append(steps)

        neighbors = getNeighbors(current, rows, cols, grid[current[0]][current[1]])
        for n in neighbors:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                parent[n] = current #parent of the neighbor is the current node
    
    if path_found:
        step_list = step_list.sort()
        print(step_list)
        return step_list[0]
    else:
        return "IMPOSSIBLE" 
    
steps = bfs(visited, grid, (0,0), (rows - 1, cols - 1))
print(steps)

