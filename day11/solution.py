def transform(matrix_string):
    matrix_int = []
    for row in matrix_string:
        rowlist = list(row)
        output_row = []
        for r in rowlist:
            if r == "L":
                output_row.append(0)
            elif r == "#":
                output_row.append(1)
            else:
                output_row.append(-1)
        matrix_int.append(output_row)
    return matrix_int


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            if col == 0:
                print("L", end="")
            elif col == 1:
                print("#", end="")
            else:
                print(".", end="")
        print()


def flip1(matrix, i, j):
    if matrix[i][j] == -1:
        return False
    adjacent_count = 0
    mini = max(i - 1, 0)
    maxi = min(i + 2, len(matrix))
    minj = max(j - 1, 0)
    maxj = min(j + 2, len(matrix[0]))
    for i2 in range(mini, maxi):
        for j2 in range(minj, maxj):
            if i == i2 and j == j2:
                continue
            if matrix[i2][j2] == 1:
                adjacent_count += 1
    if matrix[i][j] == 0 and adjacent_count == 0:
        return True
    if matrix[i][j] == 1 and adjacent_count >= 4:
        return True
    return False


def flip2(matrix, i, j):
    if matrix[i][j] == -1:
        return False
    occupied_count = 0
    eight_directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    for direction in eight_directions:
        i2 = i
        j2 = j
        while True:
            i2 += direction[0]
            j2 += direction[1]
            if i2 < 0 or j2 < 0 or i2 >= len(matrix) or j2 >= len(matrix):
                break
            value = matrix[i2][j2]
            if value == -1:
                continue
            if value == 1:
                occupied_count += 1
            break
    if matrix[i][j] == 0 and occupied_count == 0:
        return True
    if matrix[i][j] == 1 and occupied_count >= 5:
        return True
    return False


def apply_rules(matrix, flip):
    new_matrix = []
    occupied_count = 0
    for i, row in enumerate(matrix):
        new_row = []
        for j, col in enumerate(row):
            value = matrix[i][j]
            if flip(matrix, i, j):
                value ^= 1
            new_row.append(value)
            if value == 1:
                occupied_count += 1
        new_matrix.append(new_row)
    no_change = (new_matrix == matrix)
    return new_matrix, occupied_count, no_change


seats = open("seats.txt").read().splitlines()

# seats = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL""".splitlines()

outputs1 = transform(seats)
outputs2 = transform(seats)
same1 = False
same2 = False
count1 = 0
count2 = 0
while not same1 or not same2:
    (outputs1, count1, same1) = apply_rules(outputs1, flip1)
    (outputs2, count2, same2) = apply_rules(outputs2, flip2)

print(count1, count2)
