import itertools

sat_messages = open("day19.input.txt").read().splitlines()

# sat_messages = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb""".splitlines()

def legal_from_rule(rules, index):
    legal = set()
    ri = rules[index]
    if type(ri) is not list:
        legal.add(ri)
        return legal
    rule_index = []
    for r in ri:
        rule_index.append(("", r))
    while len(rule_index) > 0:
        new_ri = []
        for s, t in rule_index:
            x = rules[t[0]]
            if type(x) == list:
                snew = s
                for y in x:
                    tnew = y + t[1:]
                    new_ri.append((snew, tnew))
            else:
                snew = s + x
                tnew = t[1:]
                if len(tnew) == 0:
                    legal.add(snew)
                else:
                    new_ri.append((snew, tnew))
        rule_index = list(new_ri)
    return legal


flag = True
count1 = 0
count2 = 0
rules = dict()
for line in sat_messages:
    line = line.strip()
    if len(line) == 0:
        continue
    if ":" in line:
        idx = line.index(":")
        ruleNo = int(line[:idx])
        ruleList = line[idx+1:].split("|")
        if len(ruleList) == 1 and '"' in ruleList[0]:
            char = ruleList[0].split('"')[1]
            rules[ruleNo] = char
        else:
            rList = []
            for r in ruleList:
                y = [int(x) for x in r.strip().split()]
                rList.append(y)
            rules[ruleNo] = rList
    else:
        if flag:
            legal42 = legal_from_rule(rules, 42)
            legal31 = legal_from_rule(rules, 31)
            flag = False
        if len(line) < 24:
            continue
        if line[:8] not in legal42:
            continue
        if line[8:16] not in legal42:
            continue
        if line[-8:] not in legal31:
            continue
        remainder = line[16:-8]
        if len(remainder) == 0:
            count1 += 1
            count2 += 1
            continue
        counter31 = 0
        counter42 = 0
        while (remainder[-8:]) in legal31:
            remainder = remainder[:-8]
            counter31 += 1
        while (remainder[:8]) in legal42:
            remainder = remainder[8:]
            counter42 += 1
        if len(remainder) == 0 and counter31 <= counter42:
            count2 += 1

print(f"Solution 1: {count1}")
print(f"Solution 2: {count2}")




