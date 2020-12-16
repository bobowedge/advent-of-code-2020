shuttles = open("shuttles.txt").read().splitlines()

timestamp = int(shuttles[0])
big_buses = shuttles[1].split(",")

# timestamp = 939
# buses1 = [7, 13, 'x', 'x', 59, 'x', 31, 19]
min_wait = None
minIdx = None
for i, b in enumerate(big_buses):
    if b != 'x':
        wait = int(b) - timestamp % int(b)
        if min_wait is None or wait < min_wait:
            min_wait = wait
            minIdx = i
min_bus = int(big_buses[minIdx])
print(min_wait, minIdx)
print("Solution 1:", min_wait * min_bus)


def euclidean(n1, n2):
    r0 = n1
    s0 = 1
    t0 = 0
    r1 = n2
    s1 = 0
    t1 = 1
    while r1 > 0:
        r2 = r0 % r1
        q1 = (r0 - r2) // r1
        s2 = s0 - q1 * s1
        t2 = t0 - q1 * t1
        (r0, s0, t0) = (r1, s1, t1)
        (r1, s1, t1) = (r2, s2, t2)
    return r0, s0, t0


def bootstrap(n1, n2, a1, a2):
    (r, m1, m2) = euclidean(n1, n2)
    t = (a1 + (a2 - a1) * m1 * n1) % (n1 * n2)
    if t < 0:
        t += n1 * n2
    return t


def solution2(buses):
    sorted_buses = []
    for b in buses:
        if b != 'x':
            sorted_buses.append(int(b))
    sorted_buses.sort(reverse=True)
    sorted_buses_indexes = []
    for b in sorted_buses:
        sorted_buses_indexes.append(buses.index(str(b)))

    a = [(sorted_buses[i] - sorted_buses_indexes[i]) % sorted_buses[i] for i in range(len(sorted_buses))]
    print(sorted_buses, a)
    t = a[0]
    n1 = sorted_buses[0]
    for i in range(1, len(a)):
        n2 = sorted_buses[i]
        t = bootstrap(n1, n2, t, a[i])
        print(t)
        n1 *= n2
    return t


print(euclidean(240, 46))

print(solution2("17,x,13,19".split(",")))
# print(solution2("7,13,x,x,59,x,31,19".split(",")))
# print(solution2("67,7,59,61".split(",")))
# print(solution2("67,x,7,59,61".split(",")))
# print(solution2("67,7,x,59,61".split(",")))
# print(solution2("1789,37,47,1889".split(",")))
print("Solution 2:", solution2(big_buses))