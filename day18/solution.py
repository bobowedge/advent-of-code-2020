import math


def no_paren_eval1(s: str):
    x = s.split()
    value = int(x.pop(0))
    while len(x) > 0:
        operation = x.pop(0)
        if operation == "+":
            value += int(x.pop(0))
        elif operation == "*":
            value *= int(x.pop(0))
        else:
            raise RuntimeError("blah")
    return value


def no_paren_eval2(s: str):
    x = s.split()
    value = int(x.pop(0))
    y = []
    while len(x) > 0:
        operation = x.pop(0)
        if operation == "+":
            value += int(x.pop(0))
        elif operation == "*":
            y.append(value)
            value = int(x.pop(0))
        else:
            raise RuntimeError("blah")
    y.append(value)
    return math.prod(y)


def paren_eval(s: str, npe):
    if '(' not in s:
        return npe(s)
    lidx = s.index('(')
    ridx = lidx
    count = 1
    while count > 0:
        ridx += 1
        left_paren = s.find('(', ridx)
        right_paren = s.find(')', ridx)
        if left_paren == -1 or left_paren > right_paren:
            ridx = right_paren
            count -= 1
        else:
            ridx = left_paren
            count += 1
    s = s[:lidx] + str(paren_eval(s[lidx + 1:ridx], npe)) + s[ridx + 1:]
    return paren_eval(s, npe)


def paren_eval1(s: str):
    return paren_eval(s, no_paren_eval1)


def paren_eval2(s: str):
    return paren_eval(s, no_paren_eval2)


homework = open("day18.input.txt").read().splitlines()

print(paren_eval1("1 + 2 * 3 + 4 * 5 + 6"))
print(paren_eval1("1 + (2 * 3) + (4 * (5 + 6))"))
print(paren_eval1("2 * 3 + (4 * 5)"))
print(paren_eval1("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(paren_eval1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(paren_eval1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

print(paren_eval2("1 + 2 * 3 + 4 * 5 + 6"))
print(paren_eval2("1 + (2 * 3) + (4 * (5 + 6))"))
print(paren_eval2("2 * 3 + (4 * 5)"))
print(paren_eval2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print(paren_eval2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print(paren_eval2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

s1 = 0
s2 = 0
for line in homework:
    s1 += paren_eval1(line)
    s2 += paren_eval2(line)
print(f"Solution 1: {s1}")
print(f"Solution 2: {s2}")