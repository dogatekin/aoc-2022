import fileinput

pairs = [line.strip().split(",") for line in fileinput.input()]
pairs = [[list(map(int, elf.split("-"))) for elf in pair] for pair in pairs]

part1 = 0
part2_diff = 0
for elf1, elf2 in pairs:
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0] <= elf1[0] and elf2[1] >= elf1[1]):
        part1 += 1
    elif elf2[0] <= elf1[0] <= elf2[1] or elf1[0] <= elf2[0] <= elf1[1]:
        part2_diff += 1
print(part1)
print(part1 + part2_diff)
