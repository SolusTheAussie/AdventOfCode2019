from collections import defaultdict
wireGrid = defaultdict(lambda: -1)

def stepDirection(coord, direction):
    if direction == "U":
        coord[1] += 1
    elif direction == "D":
        coord[1] += -1
    elif direction == "R":
        coord[0] += 1
    elif direction == "L":
        coord[0] += -1

min_distance = float("inf")
with open("Day3/input.txt", "r") as f:
    i = -1
    while True:
        i += 1
        line = f.readline()
        if line == "":
            break
        current_coord = [0, 0]
        instructions = line.split(",")
        for instruction in instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            for _ in range(distance):
                stepDirection(current_coord, direction)
                if wireGrid[tuple(current_coord)] != i and wireGrid[tuple(current_coord)] >= 0:
                    min_distance = min(abs(current_coord[0]) + abs(current_coord[1]), min_distance)
                wireGrid[tuple(current_coord)] = i

print(min_distance)
