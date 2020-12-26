import numpy as np
import math
import itertools


def to_int(c):
    if c == ".":
        return 0
    if c == "#":
        return 1
    return -1


def bool2int(x):
    y = 0
    for index, value in enumerate(x):
        y += value << index
    return y


def get_grid_ids(id00, bmap, bcounts):
    gids = []
    chosen_ids = set()
    for row in range(width):
        row_ids = []
        for col in range(width):
            if row == 0 and col == 0:
                row_ids.append(id00)
                chosen_ids.add(id00)
            elif row == 0:
                border_ints = bmap[row_ids[col - 1]]
                for oid, other_ints in bmap.items():
                    if oid in chosen_ids or bcounts[oid] == 4:
                        continue
                    iset = border_ints.intersection(other_ints)
                    if len(iset) > 0:
                        row_ids.append(oid)
                        chosen_ids.add(oid)
                        break
            elif col == 0:
                border_ints = bmap[gids[row - 1][0]]
                for oid, other_ints in bmap.items():
                    if oid in chosen_ids or bcounts[oid] == 4:
                        continue
                    iset = border_ints.intersection(other_ints)
                    if len(iset) > 0:
                        row_ids.append(oid)
                        chosen_ids.add(oid)
                        break
            else:
                row_up = bmap[gids[row - 1][col]]
                col_left = bmap[row_ids[col - 1]]
                for oid, other_ints in bmap.items():
                    if oid in chosen_ids:
                        continue
                    inter_up = row_up.intersection(other_ints)
                    inter_left = col_left.intersection(other_ints)
                    if len(inter_up) > 0 and len(inter_left) > 0:
                        row_ids.append(oid)
                        chosen_ids.add(oid)
                        break
        gids.append(row_ids)
    return gids


def transformations(g):
    return [g, np.rot90(g), np.rot90(g, 2), np.rot90(g, 3),
            np.flipud(g), np.fliplr(g), np.rot90(np.flipud(g)),
            np.rot90(np.fliplr(g))]


def arrange_grid(gids, tmap, w):
    grid_matrix = []
    for row in range(w):
        row = []
        for col in range(w):
            row.append(tmap[gids[row][col]])
        grid_matrix.append(row)

    grid00 = grid_matrix[0][0]
    grid01 = grid_matrix[0][1]
    grid10 = grid_matrix[1][0]
    for g1, g2, g3 in itertools.product(transformations(grid00), transformations(grid01), transformations(grid10)):
        if np.array_equal(g1[:, 9], g2[:, 0]) and np.array_equal(g1[9], g3[0]):
            grid_matrix[0][0] = g1
            grid_matrix[0][1] = g2
            grid_matrix[1][0] = g3
            break

    for row in range(w):
        for col in range(w):
            if (row == 0 and (col == 0 or col == 1)) or (row == 1 and col == 0):
                continue
            if col == 0:
                up = grid_matrix[row-1][0]
                for gij in transformations(grid_matrix[row][col]):
                    if np.array_equal(gij[0], up[9]):
                        grid_matrix[row][col] = gij
                        break
            else:
                left = grid_matrix[row][col - 1]
                for gij in transformations(grid_matrix[row][col]):
                    if np.array_equal(gij[:, 0], left[:, 9]):
                        grid_matrix[row][col] = gij
                        break

    np_grid = np.zeros([8 * w, 8 * w], int)
    for row in range(w):
        for col in range(w):
            tile = grid_matrix[row][col]
            np_grid[row * 8:(row + 1) * 8, col * 8:(col + 1) * 8] = tile[1:9, 1:9]
    return np_grid


tiles = open("day20.input.txt").read().splitlines()
# tiles = open("day20.test.txt").read().splitlines()

border_counts = {}
border_map = {}
tile_map = {}
idx = 0
tile_id = -1
right_col = []
left_col = []
for line in tiles:
    line = line.strip()
    if "Tile" in line:
        tile_id = int(line[5:9])
        idx = 0
        right_col = []
        left_col = []
        tile_map[tile_id] = np.zeros([10, 10], int)
        continue
    if len(line) == 0:
        continue
    int_line = np.array([to_int(c) for c in line])
    tile_map[tile_id][idx] = int_line
    if idx == 0 or idx == 9:
        int1 = bool2int(int_line)
        int2 = bool2int(int_line[::-1])
        int_set = border_map.get(tile_id, set())
        int_set.add(int1)
        int_set.add(int2)
        border_map[tile_id] = int_set
    left_col.append(to_int(line[0]))
    right_col.append(to_int(line[-1]))
    if idx == 9:
        int1 = bool2int(left_col)
        int2 = bool2int(left_col[::-1])
        int3 = bool2int(right_col)
        int4 = bool2int(right_col[::-1])
        int_set = border_map.get(tile_id, set())
        int_set.add(int1)
        int_set.add(int2)
        int_set.add(int3)
        int_set.add(int4)
        border_map[tile_id] = int_set
        for other_id, other_set in border_map.items():
            if other_id == tile_id:
                continue
            inter_set = int_set.intersection(other_set)
            if len(inter_set) > 0:
                border_counts[tile_id] = border_counts.get(tile_id, 0) + 1
                border_counts[other_id] = border_counts.get(other_id, 0) + 1
    idx += 1

prod1 = 1
top_left_id = None
for tile_id, counter in border_counts.items():
    if counter == 2:
        prod1 *= tile_id
        top_left_id = tile_id
print(f"Solution 1: {prod1}")

width = int(math.sqrt(len(border_counts)))

grid_ids = get_grid_ids(top_left_id, border_map, border_counts)

grid = arrange_grid(grid_ids, tile_map, width)

nessie_string = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.replace(" ", ".").splitlines()

nessie = np.zeros([3, 20], int)
for i, line in enumerate(nessie_string):
    nessie[i] = np.array([to_int(c) for c in line])

for trans_grid in transformations(grid):
    flag = False
    indexes = []
    height, width = grid.shape
    for i in range(height-3):
        for j in range(width-20):
            mask = trans_grid[i:i + 3, j:j + 20]
            if np.array_equal(mask & nessie, nessie):
                indexes.append((i, j))
                flag = True
    if flag:
        for (i, j) in indexes:
            trans_grid[i:i + 3, j:j + 20] -= nessie
        nonzero = np.count_nonzero(trans_grid)
        print(f"Solution 2: {nonzero}")
        break
