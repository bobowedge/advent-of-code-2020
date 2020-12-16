data = open("data.txt").read().splitlines()

def seat_id(s):
    min = 0
    max = 127
    for i in range(7):
        if s[i] == "F":
            max -= (max+1-min)/2
        elif s[i] == "B":
            min += (max+1-min)/2
    row = int(min)
    min = 0
    max = 7
    for i in range(7, 10):
        if s[i] == "L":
            max -= (max+1-min)/2
        elif s[i] == "R":
            min += (max+1-min)/2
    column = int(min)
    return (row, column, row * 8 + column)

print(seat_id("BFFFBBFRRR"))
print(seat_id("FFFBBBFRRR"))
print(seat_id("BBFFBBFRLL"))

maxSeat = 0
allSeats = []
for seat in data:
    row, col, id = seat_id(seat)
    maxSeat = max(id, maxSeat)
    allSeats.append(id)

allSeats = list(set(allSeats))
allSeats.sort()
print(allSeats[:10])
for i in range(1, len(allSeats)-1):
    if allSeats[i-1] + 2 == allSeats[i]:
        print(allSeats[i] - 1)
print(maxSeat)