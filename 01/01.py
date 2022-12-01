import fileinput
from heapq import nlargest


elves = [[]]
for x in fileinput.input():
    if x == '\n':
        elves.append([])
    else:
        elves[-1].append(int(x))

totals = list(map(sum, elves))
part1 = max(totals)
print(part1)

part2 = sum(nlargest(3, totals))
print(part2)