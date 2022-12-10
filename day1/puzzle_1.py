

with open("./day1/inventory.txt") as inventory_file:
    items = [item.strip('\n') for item in inventory_file.readlines()]

sum = 0
max = 0
for i in items:
    if i == '':
        if (max < sum):
            max = sum
        sum = 0
        continue
    sum = sum + int(i)
print(max)
