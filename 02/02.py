import fileinput

rounds = [line.strip().split() for line in fileinput.input()]

points = {'X': 1, 'Y': 2, 'Z': 3}
beats = {'X': 'C', 'Y': 'A', 'Z': 'B', 'A': 'Z', 'B': 'X', 'C': 'Y'}
loses = {'A': 'Y', 'B': 'Z', 'C': 'X'}
translate = {'A': 'X', 'B': 'Y', 'C': 'Z'}

part1 = 0
part2 = 0
for them, us in rounds:
    score = points[us]
    if beats[us] == them:
        score += 6
    elif beats[them] == us:
        score += 0
    else:
        score += 3
    part1 += score

    if us == 'X':
        score = points[beats[them]]
    elif us == 'Y':
        score = 3 + points[translate[them]]
    else:
        score = 6 + points[loses[them]]
    part2 += score

print(part1)
print(part2)