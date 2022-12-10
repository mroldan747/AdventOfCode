
with open("rucksacks.txt") as rs:
    rucksacks = rs.readlines()

total = 0
for item in rucksacks:
    item = item.strip("\n")
    size = len(item)
    mid = int((size/2))
    cmp1 = item[0:mid]
    cmp2 = item[mid:size]
    items = []
    for i in cmp1:
        if i in cmp2 and i not in items:
            total += ord(i) - 96 if i.islower() else ord(i) - 38
            items.append(i)

print(total)