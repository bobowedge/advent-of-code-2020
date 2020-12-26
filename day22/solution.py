def play_combat(p1: list, p2: list):
    lp1 = len(p1)
    lp2 = len(p2)
    while lp1 > 0 and lp2 > 0:
        x1 = p1.pop(0)
        x2 = p2.pop(0)
        if x1 > x2:
            p1.append(x1)
            p1.append(x2)
            lp1 += 1
            lp2 -= 1
        else:
            p2.append(x2)
            p2.append(x1)
            lp2 += 1
            lp1 -= 1
    return p1, p2


def play_recursive_combat(p1: list, p2: list):
    seen = set()
    while len(p1) > 0 and len(p2) > 0:
        s = (tuple(p1), tuple(p2))
        if s in seen:
            return True, []
        seen.add(s)
        x1 = p1.pop(0)
        x2 = p2.pop(0)
        if x1 <= len(p1) and x2 <= len(p2):
            result, _ = play_recursive_combat(list(p1[:x1]), list(p2[:x2]))
        else:
            result = (x1 > x2)
        if result:
            p1.append(x1)
            p1.append(x2)
        else:
            p2.append(x2)
            p2.append(x1)
    if len(p1) == 0:
        return False, p2
    else:
        return True, p1


def score_p(p: list):
    s = 0
    for i, c in enumerate(p[::-1]):
        s += (i + 1) * c
    return s


player1 = [44, 31, 29, 48, 40, 50, 33, 14, 10, 30, 5, 15, 41, 45, 12, 4, 3, 17, 36, 1, 23, 34, 38, 16, 18]
player2 = [24, 20, 11, 32, 43, 9, 6, 27, 35, 2, 46, 21, 7, 49, 26, 39, 8, 19, 42, 22, 47, 28, 25, 13, 37]

play_combat(player1, player2)
score1 = max(score_p(player1), score_p(player2))
print(f"Solution 1: {score1}")

player3 = [44, 31, 29, 48, 40, 50, 33, 14, 10, 30, 5, 15, 41, 45, 12, 4, 3, 17, 36, 1, 23, 34, 38, 16, 18]
player4 = [24, 20, 11, 32, 43, 9, 6, 27, 35, 2, 46, 21, 7, 49, 26, 39, 8, 19, 42, 22, 47, 28, 25, 13, 37]

outcome, winner = play_recursive_combat(player3, player4)
print(outcome, winner)
score2 = score_p(winner)
print(f"Solution 2: {score2}")
