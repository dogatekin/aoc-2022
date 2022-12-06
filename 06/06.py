import fileinput

data = next(fileinput.input())

for i in range(3, len(data)):
    if len(set(data[i-3:i+1])) == 4:
        print(i+1)
        break

for i in range(13, len(data)):
    if len(set(data[i-13:i+1])) == 14:
        print(i+1)
        break