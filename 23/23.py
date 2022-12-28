import fileinput
from collections import deque, defaultdict
from itertools import product, count

grid = [line.strip() for line in fileinput.input()]

elves = set()
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == '#':
            elves.add((r, c))

DELTAS = set(product((-1, 0, 1), repeat=2)) - {(0, 0)}
to_check = {
    (-1, 0): [(-1, -1), (-1, 0), (-1, 1)],
    (1, 0): [(1, -1), (1, 0), (1, 1)],
    (0, -1): [(-1, -1), (0, -1), (1, -1)],
    (0, 1): [(-1, 1), (0, 1), (1, 1)],
}

directions = deque([(-1, 0), (1, 0), (0, -1), (0, 1)])

for round in count(1):
    proposals = defaultdict(list)

    for r, c in elves:
        if not any((r+dr, c+dc) in elves for dr, dc in DELTAS):
            continue
        for d in directions:
            if not any((r+dr, c+dc) in elves for dr, dc in to_check[d]):
                proposal = (r + d[0], c + d[1])
                proposals[proposal].append((r, c))
                break

    done = True
    for proposal, proposers in proposals.items():
        if len(proposers) > 1:
            continue
        elves.add(proposal)
        elves.remove(proposers[0])
        done = False

    directions.append(directions.popleft())

    if round == 10:
        minr, maxr = min(elf[0] for elf in elves), max(elf[0] for elf in elves)
        minc, maxc = min(elf[1] for elf in elves), max(elf[1] for elf in elves)

        print((maxr - minr + 1) * (maxc - minc + 1) - len(elves))

    if done:
        print(round)
        break