from time import time
from dataclasses import dataclass
import fileinput

t = time()

nums = [int(line.strip()) for line in fileinput.input()]

@dataclass
class Node:
    val: int = 0
    pre: 'Node' = None
    nex: 'Node' = None

i2n = {}

dummy = Node()
cur = dummy
for i, num in enumerate(nums):
    node = Node(num, cur)
    i2n[i] = node
    if num == 0:
        start = node
    cur.nex = node
    cur = cur.nex
cur.nex = dummy.nex
cur.nex.pre = cur
head = dummy.nex

def move(node, num):
    if num < 0:
        for _ in range(abs(num)):
            pre2 = node.pre.pre
            pre = node.pre
            nex = node.nex

            pre2.nex = node
            node.pre = pre2
            node.nex = pre
            pre.pre = node
            pre.nex = nex
            nex.pre = pre
    else:
        for _ in range(abs(num)):
            nex2 = node.nex.nex
            nex = node.nex
            pre = node.pre

            nex2.pre = node
            node.nex = nex2
            node.pre = nex
            nex.nex = node
            nex.pre = pre
            pre.nex = nex

for i, num in enumerate(nums):
    node = i2n[i]
    move(node, num)

part1 = 0
cur = start
for _ in range(3):
    for _ in range(1000):
        cur = cur.nex
    print(cur.val)
    part1 += cur.val
print(part1)

print('Took', int(time() - t), 'seconds.')