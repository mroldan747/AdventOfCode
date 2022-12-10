import pandas

df = pandas.read_csv("sections.txt")

total = 0
for index, row in df.iterrows():
    limits1 = row['first'].split('-')
    limits2 = row['second'].split('-')
    range1 = set(range(int(limits1[0]), int(limits1[1]) + 1))
    range2 = set(range(int(limits2[0]), int(limits2[1]) + 1))
    if range1.issubset(range2) or range2.issubset(range1):
        total += 1
print(total)

