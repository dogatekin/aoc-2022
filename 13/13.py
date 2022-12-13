import fileinput
from functools import cmp_to_key


lines = [line.strip() for line in fileinput.input()]

pairs = [(eval(lines[i]), eval(lines[i+1])) for i in range(0, len(lines), 3)]


def cmp(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        li = ri = 0
        while li < len(left) and ri < len(right):
            val = cmp(left[li], right[ri])
            if val == -1:
                return -1
            elif val == 1:
                return 1
            li += 1
            ri += 1
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return cmp([left], right)
    else:
        return cmp(left, [right])


part1 = sum(
    i+1 for i, (left, right) in enumerate(pairs) if cmp(left, right) == -1
)
print(part1)

packets = [packet for pair in pairs for packet in pair] + [[[2]], [[6]]]
sorted_packets = sorted(packets, key=cmp_to_key(cmp))

part2 = (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
print(part2)