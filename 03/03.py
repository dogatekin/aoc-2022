import fileinput

sacks = [line.strip() for line in fileinput.input()]

def calc_priority(c):
    if c.isupper():
        priority = 27 + ord(c) - ord('A')
    else:
        priority = 1 + ord(c) - ord('a')
    return priority

part1 = 0
for sack in sacks:
    n = len(sack)
    l, r = sack[:n//2], sack[n//2:]
    common = (set(l) & set(r)).pop()
    part1 += calc_priority(common)

part2 = 0
for i in range(0, len(sacks), 3):
    badge = set.intersection(*map(set, sacks[i:i+3])).pop()
    part2 += calc_priority(badge)

print(part1)
print(part2)