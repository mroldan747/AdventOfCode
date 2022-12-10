with open("input", "r") as datastream:
    data = datastream.readlines()

data = [item.strip("\n") for item in data]

cycle = 0
x = 1
cycle_signal = 20
total_x = 0

for signal in data:
    if signal == "noop":
        cycle += 1
        if cycle == cycle_signal and cycle_signal <= 220:
            total_x += (cycle_signal * x)
            cycle_signal += 40
    else:
        for i in range(2):
            instruction, v = signal.split(" ")
            cycle += 1
            if cycle == cycle_signal and cycle_signal <= 220:
                total_x += (cycle_signal * x)
                cycle_signal += 40
            if i == 1:
                x += int(v)


# 11960
print(total_x)