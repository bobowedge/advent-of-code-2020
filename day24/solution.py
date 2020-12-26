directions = open("day24.input.txt").read().splitlines()
# directions = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew""".splitlines()


def adjacent_tiles(pos):
    tiles = set()
    for d in [(0, 1), (0, -1), (0.5, 0.5), (0.5, -0.5), (-0.5, 0.5), (-0.5, -0.5)]:
        tiles.add((pos[0] + d[0], pos[1] + d[1]))
    return tiles


blacks = set()
for direction in directions:
    p = (0, 0)
    idx = 0
    while idx < len(direction):
        v = []
        if direction[idx] == 'e':
            v = [0, 1]
            idx += 1
        elif direction[idx] == 'w':
            v = [0, -1]
            idx += 1
        else:
            if direction[idx:idx+2] == 'ne':
                v = [0.5, 0.5]
            elif direction[idx:idx+2] == 'nw':
                v = [0.5, -0.5]
            elif direction[idx:idx+2] == 'se':
                v = [-0.5, 0.5]
            elif direction[idx:idx+2] == 'sw':
                v = [-0.5, -0.5]
            else:
                raise RuntimeError("FAIL")
            idx += 2
        p = (p[0] + v[0], p[1] + v[1])
    if p in blacks:
        blacks.remove(p)
    else:
        blacks.add(p)

print(f"Solution 1: {len(blacks)}")

for day in range(1, 101):
    counts = {}
    for b in blacks:
        for t in adjacent_tiles(b):
            counts[t] = counts.get(t, 0) + 1

    new_blacks = set()
    for t in counts:
        count = counts.get(t, 0)
        if (t in blacks and count == 1 or count == 2) or (t not in blacks and count == 2):
            new_blacks.add(t)
    blacks = new_blacks

print(f"Solution 2: {len(blacks)}")
