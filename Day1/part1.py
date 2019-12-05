sum = 0
with open("part1_input.txt") as f:
    line = f.readline()
    while line != "":
        sum += (int(line) // 3) - 2
        line = f.readline()

print(sum)

