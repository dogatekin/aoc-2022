import fileinput
import re
from tqdm import trange

lines = [line.strip() for line in fileinput.input()]

pattern = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
vals = [list(map(int, re.match(pattern, line).groups())) for line in lines]

dist = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

def merge(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0] - 1:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def blocked(ty):
    blocked_ranges = []
    for sx, sy, bx, by in vals:
        r = dist(sx, sy, bx, by)
        dy = abs(sy - ty)
        if dy < r:
            blocked_ranges.append([sx - (r - dy), sx + (r - dy)])
    return merge(blocked_ranges)

l, r = blocked(2000000)[0]
beacons_there = len({(bx, by) for sx, sy, bx, by in vals if by == 2000000 and l <= bx <= r})
print(r - l + 1 - beacons_there)

for y in trange(0, 4000000):
    intervals = blocked(y)
    if len(intervals) > 1:
        x = intervals[1][0] - 1
        print(x * 4000000 + y)

