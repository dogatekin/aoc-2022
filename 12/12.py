import fileinput
from collections import deque


grid = [[ord(c) - ord('a') for c in line.strip()] for line in fileinput.input()]

m, n = len(grid), len(grid[0])

for i in range(m):
    for j in range(n):
        if grid[i][j] == -14:
            start = (i, j, 0)
            grid[i][j] = 0
        if grid[i][j] == -28:
            end = (i, j)
            grid[i][j] = 25

def shortest_path(start):
    queue = deque([start])
    visited = {(start[0], start[1])}
    while queue:
        i, j, l = queue.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and grid[ni][nj] <= (grid[i][j] + 1):
                if (ni, nj) == end:
                    return l + 1
                queue.append((ni, nj, l+1))
                visited.add((ni, nj))
    return float('inf')

print(shortest_path(start))
print(min(shortest_path((i, j, 0)) for i in range(m) for j in range(n) if grid[i][j] == 0))