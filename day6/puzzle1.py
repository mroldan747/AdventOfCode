
with open("input", "r") as datastream:
    data = datastream.read()


for i in range(len(data) - 4):
    subset = set(data[i: i + 4])
    if len(subset) == 4:
        print(i+4)
        break
