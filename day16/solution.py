import re

ticket_fields = open("tickets.txt").read().splitlines()

# ticket_fields = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9""".splitlines()


fields = {}
ranges = []
my_ticket = []
tickets = []

s1 = 0

my_flag = False
nearby_flag = False
for line in ticket_fields:
    line = line.strip()
    if len(line) == 0:
        continue
    elif my_flag:
        my_ticket = [int(x) for x in line.split(",")]
        my_flag = False
    elif nearby_flag:
        ticket = [int(x) for x in line.split(",")]
        valid2 = True
        for x in ticket:
            valid1 = False
            for r1, r2 in ranges:
                if r1 <= x <= r2:
                    valid1 = True
                    break
            if not valid1:
                valid2 = False
                s1 += x
        if valid2:
            tickets.append(ticket)
    elif line == "your ticket:":
        my_flag = True
    elif line == "nearby tickets:":
        nearby_flag = True
    else:
        match = re.search("(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
        values = []
        for field_index in range(2, 6):
            values.append(int(match.group(field_index)))
        fields[match.group(1)] = values
        ranges.append((values[0], values[1]))
        ranges.append((values[2], values[3]))

print("Solution 1:", s1)

num_fields = len(tickets[0])
field_order = [None] * num_fields
field_index = 0
while field_order.count(None) > 0:
    field_index += 1
    field_index %= num_fields
    if field_order[field_index] is not None:
        continue
    possibles = list(fields.keys())
    for ticket in tickets:
        x = ticket[field_index]
        j = 0
        while j < len(possibles):
            p = possibles[j]
            (r1, r2, r3, r4) = fields[p]
            if r1 <= x <= r2 or r3 <= x <= r4:
                j += 1
            else:
                possibles.remove(p)
        if len(possibles) == 1:
            field_order[field_index] = possibles[0]
            dd = fields.pop(possibles[0])
            break

p2 = 1
for k, field in enumerate(field_order):
    if "departure" in field:
        p2 *= my_ticket[k]

print("Solution 2:", p2)
