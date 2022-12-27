import fileinput
from collections import defaultdict, deque
from operator import add, mul, sub, truediv, floordiv


lines = [line.strip() for line in fileinput.input()]

dep_of = defaultdict(list)
deps = defaultdict(int)
values = {}
ops = {'+': add, '*': mul, '-': sub, '/': floordiv}
monkey_ops = {}
operands = {}

queue = deque()
for line in lines:
    monkey1, rest = line.split(': ')
    if rest.isnumeric():
        if monkey1 != 'humn':
            values[monkey1] = int(rest)
            queue.append(monkey1)
    else:
        monkey2, op, monkey3 = rest[:4], rest[5], rest[7:]
        monkey_ops[monkey1] = op
        operands[monkey1] = (monkey2, monkey3)
        dep_of[monkey2].append(monkey1)
        dep_of[monkey3].append(monkey1)
        deps[monkey1] += 2

while queue:
    monkey = queue.popleft()
    if monkey not in values:
        monkey2, monkey3 = operands[monkey]
        values[monkey] = ops[monkey_ops[monkey]](values[monkey2], values[monkey3])

    for monkey2 in dep_of[monkey]:
        deps[monkey2] -= 1
        if deps[monkey2] == 0:
            queue.append(monkey2)

# print(operands['root'])
# print(values['sjmn'])
# print(operands['pppw'])
# print(values['lfqf'])

cur = 'root'
while True:
    # assert cur not in values
    op = monkey_ops[cur]
    monkey1, monkey2 = operands[cur]

    assert monkey1 in values or monkey2 in values
    unknown = monkey2 if monkey1 in values else monkey1
    known = monkey1 if monkey1 in values else monkey2

    print(cur, 'depends on', monkey1, 'and', monkey2, 'but', unknown, 'is unknown.')

    print(cur, '=', monkey1, op, monkey2)

    if cur == 'root':
        values[unknown] = values[known]
    elif op == '+':
        values[unknown] = values[cur] - values[known]
    elif op == '-' and unknown == monkey1:
        values[unknown] = values[cur] + values[known]
    elif op == '-' and unknown == monkey2:
        values[unknown] = values[known] - values[cur]
    elif op == '*':
        values[unknown] = values[cur] // values[known]
    elif op == '/' and unknown == monkey1:
        values[unknown] = values[cur] * values[known]
    elif op == '/' and unknown == monkey2:
        values[unknown] = values[known] // values[cur]


    if unknown == 'humn':
        break

    cur = unknown

print(values['humn'])