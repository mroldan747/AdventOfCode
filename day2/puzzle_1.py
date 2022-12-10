import pandas

df = pandas.read_csv("input", sep=" ")

score = 0

points = {"X": 1, "Y": 2, "Z": 3}
rule_win = {"X": "C", "Y": "A", "Z": "B"}
rule_draw = {"X": "A", "Y": "B", "Z": "C"}
for index, row in df.iterrows():
    theirs = row["theirs"]
    mine = row["mine"]
    if rule_win[mine] == theirs:
        score += 6
    elif rule_draw[mine] == theirs:
        score += 3
    score += points[mine]

print(score)
