import fileinput
from collections import deque


cubes = {tuple(map(int, line.strip().split(','))) for line in fileinput.input()}

total = 6 * len(cubes)
for cube in cubes:
    x, y, z = cube
    for d in (-1, +1):
        if (x+d, y, z) in cubes:
            total -= 1
        if (x, y+d, z) in cubes:
            total -= 1
        if (x, y, z+d) in cubes:
            total -= 1
print(total)

min_x, max_x = min(x for x, y, z in cubes) - 1, max(x for x, y, z in cubes) + 1
min_y, max_y = min(y for x, y, z in cubes) - 1, max(y for x, y, z in cubes) + 1
min_z, max_z = min(z for x, y, z in cubes) - 1, max(z for x, y, z in cubes) + 1

start = (min_x, min_y, min_z)
queue = deque([start])
seen = {start}
area = 0
while queue:
    x, y, z = queue.popleft()
    for d in (-1, +1):
        if (x+d, y, z) in cubes:
            area += 1
        if (x, y+d, z) in cubes:
            area += 1
        if (x, y, z+d) in cubes:
            area += 1
    for dx, dy, dz in [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if not (min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z):
            continue
        if (nx, ny, nz) in cubes or (nx, ny, nz) in seen:
            continue
        queue.append((nx, ny, nz))
        seen.add((nx, ny, nz))
print(area)

# def inside(x, y, z):
#     if (x, y, z) in cubes: return False
#     lx = any((cx, y, z) in cubes for cx in range(min_x, x))
#     ux = any((cx, y, z) in cubes for cx in range(x + 1, max_x + 1))
#     ly = any((x, cy, z) in cubes for cy in range(min_y, y))
#     uy = any((x, cy, z) in cubes for cy in range(y + 1, max_y + 1))
#     lz = any((x, y, cz) in cubes for cz in range(min_z, z))
#     uz = any((x, y, cz) in cubes for cz in range(z + 1, max_z + 1))
#     return all((lx, ux, ly, uy, lz, uz))

# air_pockets = {(x, y, z) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1) for z in range(min_z, max_z + 1) if inside(x, y, z)}

# print(air_pockets)
