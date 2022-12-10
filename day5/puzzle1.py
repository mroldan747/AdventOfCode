import re


def getInput() -> list:
    with open('directions.txt', 'r') as file:
        lines = file.readlines()

    index_vide = lines.index('\n')
    tower = lines[:index_vide]
    towers = {int(index): [] for index in tower[-1] if index.isnumeric()}
    containers = tower[:-1]
    for item in containers:
        item = item.replace('\n', ' ')
        j = 1
        for i in range(0, len(item), 4):
            x = item[i:i + 4]
            if x.strip(' ') != '':
                towers[j].append(x.strip(' ').strip('[').strip(']'))
            j += 1
    towers = {k: list(reversed(v)) for k, v in towers.items()}
    infos = [item.strip('\n') for item in lines[index_vide + 1:]]
    print(towers)
    return [towers, infos]


def main():
    input = getInput()
    towers = input[0]
    infos = input[1]
    for info in infos:
        match = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", info)
        items_to_get_out = int(match.group(1))
        from_stock = int(match.group(2))
        to_stock = int(match.group(3))
        for i in range(items_to_get_out):
            if len(towers[from_stock]) > 0:
                towers[to_stock].append(towers[from_stock].pop())

    final = ''
    for k, v in towers.items():
        if len(v) > 0:
            final += v[-1]

    print(final)


if __name__ == '__main__':
    main()
