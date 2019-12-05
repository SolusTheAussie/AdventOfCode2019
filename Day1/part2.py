sum = 0

def calcFuelWeight(mass):
    fuelMass = (mass // 3) - 2
    if fuelMass <= 0:
        return 0
    return fuelMass + calcFuelWeight(fuelMass)

with open("part1_input.txt") as f:
    while True:
        line = f.readline()
        if (line == ""):
            break
        mass = int(line)
        sum += calcFuelWeight(mass)

print(sum)