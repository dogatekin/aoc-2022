import fileinput

lines = [line.strip() for line in fileinput.input()]

rocks = set()

for line in lines:
    points = line.split(' -> ')
    points = [list(map(int, point.split(','))) for point in points]

    x, y = points[0]
    rocks.add((x, y))

    for nx, ny in points[1:]:
        for dx in range(min(x, nx), max(x, nx)+1):
            for dy in range(min(y, ny), max(y, ny)+1):
                rocks.add((dx, dy))
        x, y = nx, ny

lowest = max(rock[1] for rock in rocks)

# rest = 0
# while True:
#     sx, sy = (500, 0)
#     abyss = False
#     while True:
#         if sy > lowest:
#             abyss = True
#             break
#         if (sx, sy + 1) not in rocks:
#             sy += 1
#         elif (sx - 1, sy + 1) not in rocks:
#             sx -= 1
#             sy += 1
#         elif (sx + 1, sy + 1) not in rocks:
#             sx += 1
#             sy += 1
#         else:
#             rocks.add((sx, sy))
#             rest += 1
#             break
#     if abyss:
#         break
# print(rest)

def in_rocks(tuple):
    x, y = tuple
    return (x, y) in rocks or y == lowest + 2

rest = 0
while True:
    sx, sy = (500, 0)

    if (sx, sy) in rocks:
        break

    while True:
        if not in_rocks((sx, sy + 1)):
            sy += 1
        elif not in_rocks((sx - 1, sy + 1)):
            sx -= 1
            sy += 1
        elif not in_rocks((sx + 1, sy + 1)):
            sx += 1
            sy += 1
        else:
            rocks.add((sx, sy))
            rest += 1
            break
print(rest)