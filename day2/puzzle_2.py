import pandas

df = pandas.read_csv("input", sep=" ")

score = 0
# A = ROCK
# B = PAPER
# C = SCISSORS
# X = LOSE
# Y = DRAW
# Z = WIN

# 0 lost
# 3 draw
# 6 won


results = {"X": 0, "Y": 3, "Z": 6}
rule_win = {"A": "C", "B": "A", "C": "B"}
rule_lose = dict((v, k) for k, v in rule_win.items())
points = {"A": 1, "B": 2, "C": 3}
for index, row in df.iterrows():
    theirs = row["theirs"]
    mine = row["mine"]
    if mine == "Y":
        score += points[theirs]
    elif mine == "Z":
        score += points[rule_lose[theirs]]
    else:
        score += points[rule_win[theirs]]

    score += results[mine]

print(score)
