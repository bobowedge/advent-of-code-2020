customs = open("customs.txt").read().splitlines()

groupSum = 0
questions = set()
first = True
for line in customs:
    line = line.strip()
    if len(line) == 0:
        groupSum += len(questions)
        questions = set()
        first = True
    else:
        if first:
            questions = set(line)
            first = False
        else:
            questions = questions.intersection(set(line))

groupSum += len(questions)
print(groupSum)
