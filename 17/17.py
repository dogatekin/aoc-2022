import fileinput
from itertools import cycle
from tqdm import trange


jets = [line.strip() for line in fileinput.input()][0]

rocks = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [0, 1], [1, 1]]
]

grid = set()

def blocked(x, y, grid):
    return y == 0 or x == 0 or x == 8 or (x, y) in grid

def tower_height(rocks, jets, num_rocks, grid):
    jet_cycler = cycle(jets)

    max_y = 0
    for i, rock in enumerate(cycle(rocks)):
        if i == num_rocks:
            break

        x = 3
        y = max_y + 4

        while True:
            jet = next(jet_cycler)
            dx = 1 if jet == '>' else -1

            if not any(blocked(x + px + dx, y + py, grid) for px, py in rock):
                x += dx

            dy = -1
            if not any(blocked(x + px, y + py + dy, grid) for px, py in rock):
                y += dy
            else:
                grid.update({(x + px, y + py) for px, py in rock})
                max_y = max(max_y, max(y + py for _, py in rock))
                break

    # top = [max_y - max(py for px, py in grid if px == gx) for gx in range(1, 8)]
    # return max_y, top

    return max_y

print(tower_height(rocks, jets, 2022, set()))

# base = 45
base = 3700

# for cycle_length in trange(1, multiple):
#     m1, t1 = tower_height(rocks, jets, base, set())
#     m2, t2 = tower_height(rocks, jets, base + cycle_length, set())
#     if t1 == t2:
#         print(cycle_length)  # gave 35 for sample, 1700 for input
#         break

# cycle_length = 35
cycle_length = 1700

total = 1_000_000_000_000

h = tower_height(rocks, jets, base, set())
total -= base

reps, rem = total // cycle_length, total % cycle_length

diff = tower_height(rocks, jets, base + cycle_length, set()) - h
mini_diff = tower_height(rocks, jets, base + rem, set()) - h

h += reps * diff + mini_diff
print(h)