import fileinput
from collections import defaultdict, deque

lines = [line.strip() for line in fileinput.input()]

m, n = len(lines), len(lines[0])

walls = {(-1, 1), (m, n-2)}
blizzards = defaultdict(list)
directions = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}

for r, row in enumerate(lines):
    for c, col in enumerate(row):
        if col == '#':
            walls.add((r, c))
        elif col in '^><v':
            blizzards[r, c].append(directions[col])

empty_spots = [{(r, c) for r in range(1, m-1) for c in range(1, n-1) if (r, c) not in blizzards}]

def get_next(r, c, dr, dc):
    r += dr
    c += dc
    if r == m - 1:
        r = 1
    if r == 0:
        r = m - 2
    if c == n - 1:
        c = 1
    if c == 0:
        c = n - 2
    return r, c

start = (0, 1)
end = (m-1, n-2)

seen = {frozenset(empty_spots[0]): 0}
for t in range(1, 1000):
    new_blizzards = defaultdict(list)
    for (r, c), bs in blizzards.items():
        for d in bs:
            nex = get_next(r, c, *d)
            new_blizzards[nex].append(d)
    blizzards = new_blizzards
    empty_spots.append({(r, c) for r in range(1, m-1) for c in range(1, n-1) if (r, c) not in blizzards})
    fro = frozenset(empty_spots[-1])
    if fro in seen:
        cycle_len = t - seen[fro]
        break

queue = deque([(start, 0)])
seen = {(start, 0)}
while queue:
    cur, t = queue.popleft()

    if cur == end:
        break

    r, c = cur
    for dr, dc in [[0, 0], [0, -1], [0, 1], [1, 0], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if (nr, nc) not in walls and (
            (nr, nc) in empty_spots[(t+1) % cycle_len] or (nr, nc) in (start, end)
        ) and ((nr, nc), (t + 1) % cycle_len) not in seen:
            queue.append(((nr, nc), t + 1))
            seen.add(((nr, nc), t + 1))

print(t)

queue = deque([(end, t)])
seen = {(end, t)}

while queue:
    cur, t = queue.popleft()

    if cur == start:
        break

    r, c = cur
    for dr, dc in [[0, 0], [0, -1], [0, 1], [1, 0], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if (nr, nc) not in walls and (
            (nr, nc) in empty_spots[(t+1) % cycle_len] or (nr, nc) in (start, end)
        ) and ((nr, nc), (t + 1) % cycle_len) not in seen:
            queue.append(((nr, nc), t + 1))
            seen.add(((nr, nc), t + 1))

queue = deque([(start, t)])
seen = {(start, t)}

while queue:
    cur, t = queue.popleft()

    if cur == end:
        break

    r, c = cur
    for dr, dc in [[0, 0], [0, -1], [0, 1], [1, 0], [-1, 0]]:
        nr, nc = r + dr, c + dc
        if (nr, nc) not in walls and (
            (nr, nc) in empty_spots[(t+1) % cycle_len] or (nr, nc) in (start, end)
        ) and ((nr, nc), (t + 1) % cycle_len) not in seen:
            queue.append(((nr, nc), t + 1))
            seen.add(((nr, nc), (t + 1) % cycle_len))

print(t)