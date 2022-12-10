def main():
    cycle = 0
    sprite = list(range(1, 4))

    with open("input", "r") as datastream:
        data = datastream.readlines()

    data = [item.strip("\n") for item in data]

    for signal in data:
        if signal == "noop":
            cycle = write_pixel(cycle, sprite)
        else:
            for i in range(2):
                instruction, v = signal.split(" ")
                cycle = write_pixel(cycle, sprite)
                if i == 1:
                    sprite = list(range(sprite[0] + int(v), sprite[-1] + int(v) + 1))


def write_pixel(cycle, sprite):
    cycle += 1
    cycle_signal = 40
    print("#", end="") if cycle in sprite else print(".", end="")
    if cycle == cycle_signal:
        print("\n", end="")
        cycle = 0
    return cycle


if __name__ == '__main__':
    main()

# EJCFPGLH
