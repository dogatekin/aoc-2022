import fileinput
from collections import deque
from dataclasses import dataclass
from typing import Callable
from heapq import nlargest
from tqdm import trange


@dataclass
class Monkey:
    items: deque
    operation: Callable
    test: Callable
    true_target: int
    false_target: int


def create_adder(val):
    return lambda old: old + val

def create_multer(val):
    return lambda old: old * val

def create_squarer():
    return lambda old: old * old

def create_remainder(val):
    return lambda worry: worry % val == 0


lines = [line.strip() for line in fileinput.input()] + ['']

monkeys = []
for line in lines:
    if line == '':
        monkeys.append(Monkey(items, operation, test, true_target, false_target))
    elif line.startswith('Starting items: '):
        line = line.removeprefix('Starting items: ')
        items = deque(map(int, line.split(', ')))
    elif line.startswith('Operation: '):
        line = line.removeprefix('Operation: ')
        op, val = line.split()[-2:]
        if op == '*':
            if val == 'old':
                operation = create_squarer()
            else:
                operation = create_multer(int(val))
        else:
            operation = create_adder(int(val))
    elif line.startswith('Test: '):
        line = line.removeprefix('Test: ')
        divisor = int(line.split()[-1])
        test = create_remainder(divisor)
    elif line.startswith('If true: '):
        line = line.removeprefix('If true: ')
        true_target = int(line.split()[-1])
    elif line.startswith('If false: '):
        line = line.removeprefix('If false: ')
        false_target = int(line.split()[-1])

inspections = [0]*len(monkeys)
for round in trange(10000):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            inspections[i] += 1
            worry = monkey.items.popleft()
            # worry = monkey.operation(worry) // 3
            worry = monkey.operation(worry)
            # worry %= (23 * 19 * 13 * 17)
            worry %= (19 * 2 * 13 * 5 * 7 * 11 * 17 * 3)
            if monkey.test(worry):
                monkeys[monkey.true_target].items.append(worry)
            else:
                monkeys[monkey.false_target].items.append(worry)

# print(inspections)
print(nlargest(2, inspections)[0] * nlargest(2, inspections)[1])