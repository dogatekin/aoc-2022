import fileinput

lines = [line.rstrip() for line in fileinput.input()]

path = lines[-1]
lines = lines[:-2]

m, n = len(lines), max(len(line) for line in lines)
print(m, n)

grid = {}
start = None
for i, row in enumerate(lines, 1):
    for j, tile in enumerate(row, 1):
        if start is None and i == 1 and tile == '.':
            start = (i, j)
        if tile != ' ':
            grid[i, j] = tile

D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

steps = []
cur = ""
for c in path:
    if c.isnumeric():
        cur += c
    else:
        steps.append(int(cur))
        cur = ""
        steps.append(c)
steps.append(int(cur))

def get_next(cur, dr, dc):
    r, c = cur
    r += dr
    c += dc
    if r == m + 1:
        r = 1
    if c == n + 1:
        c = 1
    if r == -1:
        r = m
    if c == -1:
        c = n
    return r, c

def move(cur, n, d):
    for _ in range(n):
        dr, dc = D[d]

        nex = get_next(cur, dr, dc)
        if nex not in grid:
            while nex not in grid:
                nex = get_next(nex, dr, dc)
            pass

        if grid[nex] == '.':
            cur = nex
        elif grid[nex] == '#':
            break

    return cur

cur = start
for step in steps:
    if isinstance(step, int):
        cur = move(cur, step, d)
    elif step == 'R':
        d = (d + 1) % 4
    elif step == 'L':
        d = (d - 1) % 4

print(cur[0] * 1000 + cur[1] * 4 + d)