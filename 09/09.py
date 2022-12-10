import fileinput


cmds = [line.strip() for line in fileinput.input()]

D = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

sign = lambda x: x and (1, -1)[x<0]

def update(head, tail):
    if head[0] - tail[0] > 1:
        tail[0] += 1
        tail[1] += sign(head[1] - tail[1])
    elif head[0] - tail[0] < -1:
        tail[0] -= 1
        tail[1] += sign(head[1] - tail[1])
    elif head[1] - tail[1] > 1:
        tail[1] += 1
        tail[0] += sign(head[0] - tail[0])
    elif head[1] - tail[1] < -1:
        tail[1] -= 1
        tail[0] += sign(head[0] - tail[0])


def display(knots):
    n = 7
    grid = [['.']*n for _ in range(n)]
    for i, (x, y) in enumerate(knots):
        grid[n-1-y][x] = str(i)
    for row in grid:
        print(''.join(row))
    print()


head = [0, 0]
tail = [0, 0]

visited = {(0, 0)}

for cmd in cmds:
    d, l = cmd.split()

    dx, dy = D[d]

    for _ in range(int(l)):
        head[0] += dx
        head[1] += dy

        update(head, tail)

        visited.add(tuple(tail))

print(len(visited))


knots = [[0, 0] for _ in range(10)]
visited = {(0, 0)}

for cmd in cmds:
    d, l = cmd.split()

    dx, dy = D[d]

    for _ in range(int(l)):
        knots[0][0] += dx
        knots[0][1] += dy

        for head, tail in zip(knots[:-1], knots[1:]):
            update(head, tail)

        visited.add(tuple(knots[-1]))

        # display(knots)

print(len(visited))