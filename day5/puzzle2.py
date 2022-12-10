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
    infos = [item.strip('\n') for item in lines[index_vide + 1:]]

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
        items_out = towers[from_stock][:items_to_get_out]
        del towers[from_stock][:items_to_get_out]
        towers[to_stock] = items_out + towers[to_stock]

    final = ''
    for k, v in towers.items():
        if len(v) > 0:
            final += v[0]

    print(final)

if __name__ == '__main__':
    main()
