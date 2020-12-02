solution1 = 0
solution2 = 0

with open("passwords.txt") as file:
    for line in file:
        (policy, value, pwd) = line.split()
        policy = policy.split('-')
        policy0 = int(policy[0])
        policy1 = int(policy[1])
        value = value[0]
        count = pwd.count(value)
        if policy0 <= count <= policy1:
            solution1 += 1
        valid0 = (pwd[policy0-1] == value)
        valid1 = (pwd[policy1-1] == value)
        if valid0 ^ valid1:
            solution2 += 1

print(solution1, solution2)
