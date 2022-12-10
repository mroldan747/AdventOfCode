with open("input", "r") as datastream:
    data = datastream.readlines()

data = [item.strip("\n") for item in data]

highest = 0
for row in range(len(data)):
    total = 0
    item_row = data[row]
    if row == 0 or row == len(data) - 1:
        continue
    for j in range(len(item_row)):
        item = item_row[j]
        if j == 0 or j == len(item_row) - 1:
            continue

        # trees to the right
        total_right = 0
        for r in range(j + 1, len(item_row)):
            total_right += 1
            if item_row[r] >= item:
                break

        # trees to the left
        total_left = 0
        for left in range(j - 1, -1, -1):
            total_left += 1
            if item_row[left] >= item:
                break

        # trees down
        total_down = 0
        for down in range(row + 1, len(data)):
            total_down += 1
            if data[down][j] >= item:
                break

        # trees top
        total_top = 0
        for top in range(row - 1, -1, -1):
            total_top += 1
            if data[top][j] >= item:
                break

        total = total_top * total_down * total_left * total_right
        if total > highest:
            highest = total

# 480000
print(data)
print(highest)
