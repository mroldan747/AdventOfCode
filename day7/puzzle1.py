import re

with open("input", "r") as datastream:
    data = datastream.readlines()

data = [item.strip('\n') for item in data]

directories = {}
commands = []
directory = ""
for info in data:

    if info[0] == "$":
        command = info.strip("$ ").split(" ")
        if command[0] != "ls" and command[1] == "..":
            commands.pop()
            directory = "".join(commands)
        elif command[0] != "ls":
            commands.append(command[1])
            directory = "!".join(commands)
            if directory not in directories.keys():
                directories[directory] = 0
        continue

    matches = re.search(r"^([0-9]+) [a-z]*", info)
    if matches:
        directories[directory] = directories[directory] + int(matches.group(1))


total = 0
for k, v in directories.items():
    for c, j in directories.items():
        if k == c:
            continue
        if k in c:
            directories[k] += j

for k, v in directories.items():
    if v <= 100000:
        total += v

# 1845346
print(total)
# print(directories)
