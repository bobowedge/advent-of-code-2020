data = open("expense_report.txt").read()
data = data.splitlines()
data = [int(d) for d in data]

solution1 = 0
solution2 = 0

for index1, d1 in enumerate(data):
    for index2, d2 in enumerate(data[index1:]):
        total2 = d1 + d2
        if total2 == 2020:
            solution1 = d1 * d2
        elif total2 < 2020:
            for d3 in data[index2:]:
                total3 = total2 + d3
                if total3 == 2020:
                    solution2 = d1 * d2 * d3

print(solution1, solution2)
