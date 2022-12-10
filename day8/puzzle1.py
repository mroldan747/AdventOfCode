with open("input", "r") as datastream:
    data = datastream.readlines()

data = [item.strip("\n") for item in data]

total = 0
for row in range(len(data)):
    item_row = data[row]
    if row == 0 or row == len(data) - 1:
        total += len(item_row)
        continue
    for j in range(len(item_row)):
        item = item_row[j]
        if j == 0 or j == len(item_row) - 1:
            total += 1
            continue
        # trees to the right
        found_right = False
        for r in item_row[j+1:]:
            if r >= item:
                found_right = True
                break

        # trees to the left
        found_left = False
        for left in item_row[0:j]:
            if left >= item:
                found_left = True
                break

        # trees down
        found_down = False
        for down in data[row+1:]:
            if down[j] >= item:
                found_down = True
                break

        # trees top
        found_top = False
        for top in data[0: row]:
            if top[j] >= item:
                found_top = True
                break
        total = total + 1 if not found_top or not found_down or not found_left or not found_right else total

# 1807
print(data)
print(total)
