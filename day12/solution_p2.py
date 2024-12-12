import sys

matrix = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        vec = []
        for x, i in enumerate(line.strip()):
            vec.append(i)
        matrix.append(vec)

xdim, ydim = len(matrix[0]), len(matrix)
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
diag_steps = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])
def check_bounds(x): return 0 <= x[0] < xdim and 0 <= x[1] < ydim


def solve_region(matrix, letter, pos) -> int:
    tiles = {pos}
    seen = set()
    while len(tiles) != 0:
        tile = tiles.pop()
        if tile in seen:
            continue
        seen.add(tile)
        for step in steps:
            new_tile = add_tup(tile, step)
            if check_bounds(new_tile):
                new_letter = matrix[new_tile[1]][new_tile[0]]
                if new_letter == letter:
                    tiles.add(new_tile)
    n_t = len(seen)
    corners = 0
    for tile in seen:
        for step in diag_steps:
            diag_tile = add_tup(tile, step)
            tile1 = add_tup(tile, (step[0], 0))
            tile2 = add_tup(tile, (0, step[1]))
            if diag_tile not in seen:
                if tile1 not in seen and tile2 not in seen:
                    corners += 1
                elif tile1 in seen and tile2 in seen:
                    corners += 1
            elif tile1 not in seen and tile2 not in seen:
                corners += 1

        matrix[tile[1]][tile[0]] = "."
    return n_t * corners


cost = 0
for y in range(ydim):
    for x in range(xdim):
        tile = matrix[y][x]
        if tile != ".":
            cost_reg = solve_region(matrix, tile, (x, y))
            # print(tile, cost_reg)
            # print("\n".join(map(lambda x: "".join(x), matrix)))
            cost += cost_reg

print(cost)
