import fileinput

lines = [line.rstrip("\n") for line in fileinput.input()]

n = (len(lines[0]) + 1) // 4

stacks = [[] for _ in range(n + 1)]
for line in lines[: lines.index("") - 1]:
    for i in range(n):
        if line[4 * i : 4 * i + 3] != "   ":
            stacks[i + 1].append(line[4 * i + 1])

for stack in stacks:
    stack.reverse()

stacks1 = [stack.copy() for stack in stacks]

for line in lines[lines.index("") + 1 :]:
    _, cnt, _, fro, _, to = line.split()
    for _ in range(int(cnt)):
        stacks1[int(to)].append(stacks1[int(fro)].pop())
    stacks[int(to)].extend(stacks[int(fro)][-int(cnt) :])
    stacks[int(fro)] = stacks[int(fro)][: -int(cnt)]

print("".join(stack[-1] for stack in stacks1[1:]))
print("".join(stack[-1] for stack in stacks[1:]))
