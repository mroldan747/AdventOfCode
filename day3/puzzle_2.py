
with open("rucksacks.txt") as rs:
    rucksacks = rs.readlines()

total = 0
size_max = 3
size_min = 0
while size_max <= len(rucksacks):
    items = rucksacks[size_min:size_max]
    elf1 = items[0].strip("\n")
    elf2 = items[1].strip("\n")
    elf3 = items[2].strip("\n")
    badges = []
    for i in elf1:
        if i in elf2 and i in elf3:
            value = ord(i) - 96 if i.islower() else ord(i) - 38
            badges.append(value)
    total += max(badges)
    size_min = size_max
    size_max += 3

print(total)