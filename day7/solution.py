import re

rules = open("bags.txt").read().splitlines()

bagMap = dict()
reverseMap = dict()
for rule in rules:
    firstBagMatch = re.search("(\S+ \S+) bags contain (.+)", rule)
    if firstBagMatch is not None:
        bag1 = firstBagMatch.group(1)
        bagList = bagMap.get(bag1, [])
        secondBags = re.split("bags?[,\.]{1}", firstBagMatch.group(2))
        for bag in secondBags:
            bag = bag.strip()
            if len(bag) > 0:
                if bag != "no other":
                    bagMatch = re.search("([0-9]+) (\S+ \S+)", bag)
                    if bagMatch is not None:
                        bag2 = bagMatch.group(2)
                        bagList.append((bag2, int(bagMatch.group(1))))
                        reverseList = reverseMap.get(bag2, [])
                        reverseList.append(bag1)
                        reverseMap[bag2] = reverseList
        bagMap[bag1] = bagList
    else:
        print("Rule: ", rule)


def holders(color, colorHolders):
    for color2 in reverseMap.get(color, []):
        colorHolders.add(color2)
        holders(color2, colorHolders)


shinyGoldHolders = set()
holders("shiny gold", shinyGoldHolders)
print(len(shinyGoldHolders))


def count(color):
    bagList = bagMap.get(color, [])
    if len(bagList) > 0:
        total = 0
        for (color2, number) in bagList:
            total += number + number * count(color2)
        return total
    else:
        return 0

total = count("shiny gold")
print(total)