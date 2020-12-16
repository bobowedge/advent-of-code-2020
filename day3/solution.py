import numpy as np
pattern = open("trees.txt").read().splitlines()

# pattern = """..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#""".splitlines()
repeatLength = len(pattern[0])
patternLength = len(pattern)

pattern = np.array([[1 if dot == "#" else 0 for dot in p] for p in pattern])

index = np.zeros((2, 5), int)
hitTrees = np.zeros(5, int)
slopes = np.array([[1, 1, 1, 1, 2], [1, 3, 5, 7, 1]])

while index[0][0] < patternLength:
    index[1] %= repeatLength
    hitTrees += pattern[index[0], index[1]]
    index += slopes
    if index[0][4] >= patternLength:
        index[0][4] = 0
        index[1][4] = 0
        slopes[0][4] = 0
        slopes[1][4] = 0

print(hitTrees, np.prod(hitTrees, dtype=np.int64))
