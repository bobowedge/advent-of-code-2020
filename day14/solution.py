import re


def apply_mask1(mask, value):
    bin_value = bin(value)[2:]
    lvalue = len(bin_value)
    bin_value = "0"*(36-lvalue) + bin_value
    result = list(mask)
    for i in range(36):
        if result[i] == "X":
            result[i] = bin_value[i]
    result = "0b" + "".join(result)
    return int(result, 2)


def apply_mask2(mask, address):
    add_value = bin(address)[2:]
    lvalue = len(add_value)
    add_value = "0"*(36-lvalue) + add_value
    results = ["0b"]
    for i in range(36):
        if mask[i] == "0":
            for j in range(len(results)):
                results[j] += add_value[i]
        elif mask[i] == "1":
            for j in range(len(results)):
                results[j] += "1"
        else:
            new_results = []
            for r in results:
                new_results.append(r + "0")
                new_results.append(r + "1")
            results = list(new_results)
    int_results = []
    for r in results:
        int_results.append(int(r, 2))
    return int_results


program = open("memory.txt").read().splitlines()

# program = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0""".splitlines()

# program = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1""".splitlines()

mask = ""
memory1 = {}
memory2 = {}
for line in program:
    if "mask" in line:
        mask = line.split()[2]
    else:
        match = re.search("mem\[(\d+)\] = (\d+)", line)
        location = int(match.group(1))
        value = int(match.group(2))
        memory1[location] = apply_mask1(mask, value)
        addresses = apply_mask2(mask, location)
        for a in addresses:
            memory2[a] = value

s1 = 0
for m in memory1:
    s1 += memory1[m]
print("solution 1:", s1)

s2 = 0
for m in memory2:
    s2 += memory2[m]
print("solution 2:", s2)