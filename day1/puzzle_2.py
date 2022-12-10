
with open("./day1/inventory.txt") as inventory_file:
    items = [item.strip('\n') for item in inventory_file.readlines()]

total_calories = 0
elves_total_calories = []
for i in items:
    if i == '':
        elves_total_calories.append(total_calories)
        total_calories = 0
        continue
    total_calories = total_calories + int(i)
elves_total_calories.sort(reverse=True)
print(sum(elves_total_calories[0:3]))