directions = open("directions.txt").read().splitlines()

# directions = """F10
# N3
# F7
# R90
# F11""".splitlines()

grid1 = [0, 0]
heading1 = [1, 0]

position2 = [0, 0]
waypoint2 = [10, 1]

for direction in directions:
    d = direction[0]
    val = int(direction[1:])
    if d == "N":
        grid1[1] += val
        waypoint2[1] += val
    elif d == "S":
        grid1[1] -= val
        waypoint2[1] -= val
    elif d == "E":
        grid1[0] += val
        waypoint2[0] += val
    elif d == "W":
        grid1[0] -= val
        waypoint2[0] -= val
    elif d == "F":
        grid1[0] += val * heading1[0]
        grid1[1] += val * heading1[1]
        position2[0] += val * waypoint2[0]
        position2[1] += val * waypoint2[1]
    elif direction == "L90" or direction == "R270":
        heading1 = [-heading1[1], heading1[0]]
        waypoint2 = [-waypoint2[1], waypoint2[0]]
    elif direction == "R90" or direction == "L270":
        heading1 = [heading1[1], -heading1[0]]
        waypoint2 = [waypoint2[1], -waypoint2[0]]
    elif val == 180:
        heading1 = [-heading1[0], -heading1[1]]
        waypoint2 = [-waypoint2[0], -waypoint2[1]]
    else:
        raise RuntimeError(f"Unknown direction: {direction}")

print("Solution 1:", abs(grid1[0]) + abs(grid1[1]))
print("Solution 2:", abs(position2[0]) + abs(position2[1]))