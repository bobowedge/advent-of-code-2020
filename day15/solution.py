def get_number1(numbers, end):
    while len(numbers) < end:
        last = numbers[-1]
        if last not in numbers[:-1]:
            numbers.append(0)
            continue
        x = numbers[-2::-1].index(last)
        numbers.append(x+1)
    return numbers[-1]


def get_number2(numbers, end):
    table = {}
    for i, n in enumerate(numbers[:-1]):
        table[n] = i + 1

    last = numbers[-1]
    index = len(numbers)
    while index < end:
        if last not in table:
            table[last] = index
            last = 0
        else:
            diff = index - table[last]
            table[last] = index
            last = diff
        index += 1
    return last


numbers = [6,3,15,13,1,0]

print("Solution 1:",get_number1(numbers, 2020))
print("Solution 2:",get_number2(numbers, 30000000))
