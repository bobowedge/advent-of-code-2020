data = open("expense_report").read()
data = data.splitlines()
data = [int(d) for d in data]

for index, d1 in enumerate(data):
    for d2 in data[index:]:
        total = d1 + d2
        if (total == 2020):
            print(d1*d2)
            break
