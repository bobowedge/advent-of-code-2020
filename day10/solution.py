joltages = open("joltages.txt").read().splitlines()

# joltages = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4""".splitlines()

# joltages = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3""".splitlines()

joltages = [int(j) for j in joltages]
joltages = [0] + joltages[:]
joltages.sort()
joltages.append(joltages[-1] + 3)

total1 = 0
total3 = 0
stacks = dict()
stacks[0] = 1
for i, jolt in enumerate(joltages):
    if jolt == joltages[-1]:
        break
    if (jolt + 1) == joltages[i + 1]:
        total1 += 1
    elif (jolt + 3) == joltages[i + 1]:
        total3 += 1
    for jolt2 in joltages[i+1:i+4]:
        if jolt2 < jolt + 4:
            stacks[jolt2] = stacks.get(jolt2, 0) + stacks[jolt]

print(total1, total3, total1 * total3)
print(stacks[joltages[-1]])
