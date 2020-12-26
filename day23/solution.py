def crab_cups1(cups_str, moves):
    cups = [int(x) for x in cups_str]
    length_cups = len(cups)
    for index in range(moves):
        c0 = cups.pop(0)
        pickup = [cups.pop(0) for _ in range(3)]
        destination = (c0 - 1)
        if destination == 0:
            destination = length_cups
        while destination in pickup:
            destination -= 1
            if destination == 0:
                destination = length_cups
        destination_index = cups.index(destination)
        if destination_index == (length_cups - 4):
            cups.extend(pickup)
        else:
            cups.insert(destination_index + 1, pickup[2])
            cups.insert(destination_index + 1, pickup[1])
            cups.insert(destination_index + 1, pickup[0])
        cups.append(c0)
    return list(cups)


def crab_cups2(cups_str, size, moves):
    cups = {}
    for i, x in enumerate(cups_str[:-1]):
        cups[int(x)] = int(cups_str[i+1])
    if size == len(cups_str):
        cups[int(cups_str[-1])] = int(cups_str[0])
    else:
        cups[int(cups_str[-1])] = len(cups_str) + 1
        for i in range(len(cups_str) + 1, size):
            cups[i] = i + 1
        cups[size] = int(cups_str[0])

    c0 = int(cups_str[0])
    length_cups = len(cups)
    for i in range(moves):
        x1 = cups[c0]
        x2 = cups[x1]
        x3 = cups[x2]
        x4 = cups[x3]
        pickup = [x1, x2, x3]
        destination = (c0 - 1)
        if destination == 0:
            destination = length_cups
        while destination in pickup:
            destination -= 1
            if destination == 0:
                destination = length_cups
        old = cups[destination]
        cups[destination] = x1
        cups[x1] = x2
        cups[x2] = x3
        cups[x3] = old
        cups[c0] = x4
        c0 = x4
    return cups


cups_string = "362981754"

cups1 = crab_cups1(cups_string, 100)
idx1 = cups1.index(1)
sol1 = cups1[idx1 + 1:] + cups1[:idx1]
sol1 = "".join([str(x) for x in sol1])
print(f"Solution 1: {sol1}")

cups2 = crab_cups2(cups_string, 1000000, 10000000)
val1 = cups2[1]
val2 = cups2[val1]
sol2 = val1 * val2
print(f"Solution 2: {sol2}")
