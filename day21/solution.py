ingredients = open("day21.input.txt").read().splitlines()
# ingredients = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

atoi = {}
icount = {}

for food in ingredients:
    x = food.split()
    contains = x.index("(contains")
    x1 = x[:contains]
    x2 = [y[:-1] for y in x[contains+1:]]
    for a in x2:
        iset = atoi.get(a, set(x1))
        iset = iset.intersection(set(x1))
        atoi[a] = iset
    for i in x1:
        icount[i] = icount.get(i, 0) + 1

for a, items in atoi.items():
    for i in items:
        if i in icount:
            del icount[i]

s1 = 0
for i, value in icount.items():
    s1 += value
print(f"Solution 1: {s1}")

flag = True
while flag:
    flag = False
    removable = set()
    for a, iset in atoi.items():
        if len(atoi[a]) == 1:
            removable = removable.union(iset)
    new_atoi = {}
    for b, iset in atoi.items():
        if len(iset) > 1:
            newset = iset.difference(removable)
            new_atoi[b] = newset
            flag = True
        else:
            new_atoi[b] = iset
    atoi = dict(new_atoi)


allergens = list(atoi.keys())
allergens.sort()
dangerous = [atoi[a].pop() for a in allergens]
print("Solution 2:",",".join(dangerous))
