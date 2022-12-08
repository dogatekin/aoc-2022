import fileinput
from itertools import accumulate


transpose = lambda grid: list(map(list, zip(*grid)))

grid = [list(map(int, line.strip())) for line in fileinput.input()]

m, n = len(grid), len(grid[0])

grid_t = transpose(grid)
tallest_top = transpose(list(accumulate(col, func=max)) for col in grid_t)
tallest_bottom = transpose(list(reversed(list(accumulate(reversed(col), func=max)))) for col in grid_t)
tallest_left = [list(accumulate(row, func=max)) for row in grid]
tallest_right = [list(reversed(list(accumulate(reversed(row), func=max)))) for row in grid]

visible = 2*m + 2*n - 4
for i in range(1, m-1):
    for j in range(1, n-1):
        height = grid[i][j]
        if height > tallest_top[i-1][j] or height > tallest_bottom[i+1][j] or height > tallest_left[i][j-1] or height > tallest_right[i][j+1]:
            visible += 1

print(visible)


def scenic_score(i, j):
    height = grid[i][j]
    top = bottom = left = right = 1

    pi = i
    while pi > 0 and grid[pi-1][j] < height:
        pi -= 1
        top += 1 if pi != 0 else 0

    pi = i
    while pi < m-1 and grid[pi+1][j] < height:
        pi += 1
        bottom += 1 if pi != m-1 else 0

    pj = j
    while pj > 0 and grid[i][pj-1] < height:
        pj -= 1
        left += 1 if pj != 0 else 0

    pj = j
    while pj < n-1 and grid[i][pj+1] < height:
        pj += 1
        right += 1 if pj != n-1 else 0

    return top * bottom * left * right


print(max(scenic_score(i, j) for i in range(1, m-1) for j in range(1, n-1)))