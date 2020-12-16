ops = open("operations.txt").read().splitlines()
# ops = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6""".splitlines()


def run_commands(operations):
    ops_total = 0
    index = 0
    while index < len(operations) and operations[index] is not None:
        (cmd, val) = operations[index].split(" ")
        operations[index] = None
        if cmd == "nop":
            index += 1
        elif cmd == "acc":
            ops_total += int(val)
            index += 1
        elif cmd == "jmp":
            index += int(val)
    return index, ops_total


print(run_commands(list(ops))[1])

for index1 in range(len(ops)):
    op = ops[index1]
    (command, value) = op.split(" ")
    if command == "nop":
        ops[index1] = f"jmp {value}"
    elif command == "acc":
        pass
    elif command == "jmp":
        ops[index1] = f"nop {value}"
    (index2, total) = run_commands(list(ops))
    if index2 == len(ops):
        print(total)
        break
    ops[index1] = op
