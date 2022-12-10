
with open("input", "r") as datastream:
    data = datastream.read()


for i in range(len(data) - 14):
    subset = set(data[i: i + 14])
    if len(subset) == 14:
        print(i+14)
        break
