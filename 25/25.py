import fileinput

lines = [line.strip() for line in fileinput.input()]

def convert(snafu):
    d = 0
    i = 1
    for c in reversed(snafu):
        if c == '-':
            v = -1
        elif c == '=':
            v = -2
        else:
            v = int(c)
        d += i * v
        i *= 5
    return d

t = 0
for snafu in lines:
    t += convert(snafu)
print(t)

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

base5 = numberToBase(t, 5)

base5.reverse()
for i in range(len(base5)):
    if base5[i] == 3:
        base5[i] = '='
        base5[i+1] += 1
    elif base5[i] == 4:
        base5[i] = '-'
        base5[i+1] += 1
    elif base5[i] == 5:
        base5[i] = 0
        base5[i+1] += 1
print(''.join(map(str, reversed(base5))))
