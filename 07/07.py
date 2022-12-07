import fileinput
from collections import Counter, defaultdict, deque


lines = [line.strip() for line in fileinput.input()]

path = []
contents = {}
sizes = {}
dependencies = Counter()
parent_of = {}

for line in lines:
    if line.startswith('$ cd'):
        new_directory = line[5:]
        if new_directory == '/':
            path = ['']
        elif new_directory == '..':
            path.pop()
        else:
            path.append(new_directory)
    elif line == '$ ls':
        current_path = '/'.join(path)
        contents[current_path] = []
    elif line.startswith('dir'):
        subfolder = current_path + '/' + line[4:]
        contents[current_path].append(subfolder)
        dependencies[current_path] += 1
        parent_of[subfolder] = current_path
    else:
        contents[current_path].append(int(line.split()[0]))

folders = contents.keys()
queue = deque()

for folder in folders:
    if dependencies[folder] == 0:
        queue.append(folder)

while queue:
    folder = queue.popleft()

    size = sum(filesize if isinstance(filesize, int) else sizes[filesize] for filesize in contents[folder])
    sizes[folder] = size

    if folder in parent_of:
        parent = parent_of[folder]
        dependencies[parent] -= 1
        if dependencies[parent] == 0:
            queue.append(parent)

print(sum(size for size in sizes.values() if size <= 100000))

unused_space = 70000000 - sizes['']
needed = 30000000 - unused_space

print(min(size for size in sizes.values() if size >= needed))