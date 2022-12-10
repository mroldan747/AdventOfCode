def main():
    # y, x
    H = [(0, 0)]

    S = {1: [(0, 0)], 2: [(0, 0)], 3: [(0, 0)], 4: [(0, 0)], 5: [(0, 0)], 6: [(0, 0)], 7: [(0, 0)], 8: [(0, 0)], 9: [(0, 0)]}

    with open("input", "r") as datastream:
        data = datastream.readlines()

    data = [item.strip("\n") for item in data]

    directions = {
        "U": lambda x, y: (x[0] + y, x[1]),
        "D": lambda x, y: (x[0] - y, x[1]),
        "R": lambda x, y: (x[0], x[1] + y),
        "L": lambda x, y: (x[0], x[1] - y)
    }
    for instruction in data:
        direction, num = instruction.split(" ")

        for i in range(int(num)):
            new_place_H = directions[direction](H[-1], 1)
            H.append(new_place_H)
            for j in range(1, len(S) + 1):
                new_place_T = S[j][-1]
                new_place_H = dep(new_place_H, new_place_T)
                S[j].append(new_place_H)

    v = sorted(set(S[9]))
    print(len(v))
    #print(S[9])
    # print(v)


def dep(new_place_H, new_place_T):
    # 2 places on the left
    if new_place_H[1] - 2 == new_place_T[1] and new_place_H[0] == new_place_T[0]:
        new_place_T = (new_place_H[0], new_place_T[1] + 1)
    # 2 places on the right
    elif new_place_H[1] + 2 == new_place_T[1] and new_place_H[0] == new_place_T[0]:
        new_place_T = (new_place_H[0], new_place_T[1] - 1)
    # 2 places on top
    elif new_place_H[0] + 2 == new_place_T[0] and new_place_H[1] == new_place_T[1]:
        new_place_T = (new_place_T[0] - 1, new_place_T[1])
    # 2 places down
    elif new_place_H[0] - 2 == new_place_T[0] and new_place_H[1] == new_place_T[1]:
        new_place_T = (new_place_T[0] + 1, new_place_T[1])
    elif new_place_H[0] - 2 == new_place_T[0] and new_place_H[1] - 2 == new_place_T[1]:
        new_place_T = (new_place_T[0] + 1, new_place_T[1] + 1)
    elif new_place_H[0] + 2 == new_place_T[0] and new_place_H[1] + 2 == new_place_T[1]:
        new_place_T = (new_place_T[0] - 1, new_place_T[1] - 1)
    elif new_place_H[0] - 2 == new_place_T[0] and new_place_H[1] + 2 == new_place_T[1]:
        new_place_T = (new_place_T[0] + 1, new_place_T[1] - 1)
    elif new_place_H[0] + 2 == new_place_T[0] and new_place_H[1] - 2 == new_place_T[1]:
        new_place_T = (new_place_T[0] - 1, new_place_T[1] + 1)
    # diagonal down
    elif new_place_H[0] - 2 == new_place_T[0] and (
            new_place_H[1] - 1 == new_place_T[1] or new_place_H[1] + 1 == new_place_T[1]):
        new_place_T = (new_place_H[0] - 1, new_place_H[1])
    # diagonal top
    elif new_place_H[0] + 2 == new_place_T[0] and (
            new_place_H[1] - 1 == new_place_T[1] or new_place_H[1] + 1 == new_place_T[1]):
        new_place_T = (new_place_H[0] + 1, new_place_H[1])
    # diagonal right
    elif new_place_H[1] + 2 == new_place_T[1] and (
            new_place_H[0] - 1 == new_place_T[0] or new_place_H[0] + 1 == new_place_T[0]):
        new_place_T = (new_place_H[0], new_place_H[1] + 1)
    # diagonal left
    elif new_place_H[1] - 2 == new_place_T[1] and (
            new_place_H[0] - 1 == new_place_T[0] or new_place_H[0] + 1 == new_place_T[0]):
        new_place_T = (new_place_H[0], new_place_H[1] - 1)

    return new_place_T


if __name__ == '__main__':
    main()
