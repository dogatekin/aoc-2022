import fileinput

ops = [line.strip() for line in fileinput.input()]

X = [0, 1]

for op in ops:
    if op == 'noop':
        X.append(X[-1])
    else:
        V = int(op.split()[1])
        X.append(X[-1])
        X.append(X[-1] + V)

cycle = 20
strength = 0
while cycle < len(X):
    strength += cycle * X[cycle]
    cycle += 40
print(strength)

grid = [['.']*40 for _ in range(6)]
for cycle in range(240):
    y = cycle // 40
    x = cycle % 40
    if abs(X[cycle+1] - x) <= 1:
        grid[y][x] = '#'

for row in grid:
    print(''.join(row))
print()

