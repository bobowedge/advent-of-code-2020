import itertools

def active1(x, y, z, cubes):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if (i, j, k) == (x, y, z):
                    continue
                if cubes.get((i,j,k), 0) == 1:
                    count += 1
    return count == 3 or (cubes.get((x,y,z), 0) == 1 and count == 2)


def active2(x, y, z, w, cubes):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for h in range(w - 1, w + 2):
                    if (i, j, k, h) == (x, y, z, w):
                        continue
                    if cubes.get((i, j, k, h), 0) == 1:
                        count += 1
    return count == 3 or (cubes.get((x, y, z, w), 0) == 1 and count == 2)


def print_cubes1(cubes):
    (minx, maxx, miny, maxy, minz, maxz) = [0]*6
    for (x, y, z) in cubes:
        minx = min(x, minx)
        miny = min(y, miny)
        minz = min(z, minz)
        maxx = max(x + 1, maxx)
        maxy = max(y + 1, maxy)
        maxz = max(z + 1, maxz)

    for k in range(minz, maxz):
        print(f"z={k}")
        for i in range(minx, maxx):
            print(i, end= " ")
            for j in range(miny, maxy):
                if cubes.get((i,j,k), 0) == 1:
                    print("#",end="")
                else:
                    print(".",end="")
            print("")


cubesStr = """#...#.#.
..#.#.##
..#..#..
.....###
...#.#.#
#.#.##..
#####...
.#.#.##.""".splitlines()

# cubesStr = """.#.
# ..#
# ###""".splitlines()

x1 = range(-1, len(cubesStr) + 1)
y1 = range(-1, len(cubesStr[0]) + 1)
z1 = range(-1, 2)

x2 = range(-1, len(cubesStr) + 1)
y2 = range(-1, len(cubesStr[0]) + 1)
z2 = range(-1, 2)
w2 = range(-1, 2)

cubes1 = {}
cubes2 = {}
for xidx, line in enumerate(cubesStr):
    for yidx, c in enumerate(line):
        if c == "#":
            cubes1[(xidx, yidx, 0)] = 1
            cubes2[(xidx, yidx, 0, 0)] = 1

for cycle in range(6):
    new_cubes1 = {}
    for (x, y, z) in itertools.product(x1, y1, z1):
        if active1(x, y, z, cubes1):
            new_cubes1[(x, y, z)] = 1
    new_cubes2 = {}
    for (x, y, z, w) in itertools.product(x2, y2, z2, w2):
        if active2(x, y, z, w, cubes2):
            new_cubes2[(x, y, z, w)] = 1

    cubes1 = dict(new_cubes1)
    (minx, maxx, miny, maxy, minz, maxz) = [0]*6
    for (x, y, z) in cubes1:
        minx = min(minx, x - 1)
        miny = min(miny, y - 1)
        minz = min(minz, z - 1)
        maxx = max(maxx, x + 2)
        maxy = max(maxy, y + 2)
        maxz = max(maxz, z + 2)
    x1 = range(minx, maxx)
    y1 = range(miny, maxy)
    z1 = range(minz, maxz)

    cubes2 = dict(new_cubes2)
    (minx, maxx, miny, maxy, minz, maxz, minw, maxw) = [0]*8
    for (x, y, z, w) in cubes2:
        minx = min(minx, x - 1)
        miny = min(miny, y - 1)
        minz = min(minz, z - 1)
        minw = min(minw, w - 1)
        maxx = max(maxx, x + 2)
        maxy = max(maxy, y + 2)
        maxz = max(maxz, z + 2)
        maxw = max(maxw, w + 2)
    x2 = range(minx, maxx)
    y2 = range(miny, maxy)
    z2 = range(minz, maxz)
    w2 = range(minw, maxw)

print("Solution 1:", len(cubes1))
print("Solution 2:", len(cubes2))
