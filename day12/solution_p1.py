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
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])
def check_bounds(x): return 0 <= x[0] < xdim and 0 <= x[1] < ydim


def solve_region(matrix, letter, pos) -> int:
    tiles = {pos}
    seen = set()
    n_t = 0
    n_f = 0
    while len(tiles) != 0:
        tile = tiles.pop()
        if tile in seen:
            continue
        n_t += 1
        fence_needed = 4
        for step in steps:
            new_tile = add_tup(tile, step)
            if check_bounds(new_tile):
                new_letter = matrix[new_tile[1]][new_tile[0]]
                if new_letter == letter:
                    fence_needed -= 1
                    tiles.add(new_tile)
        seen.add(tile)
        n_f += fence_needed
    for tile in seen:
        matrix[tile[1]][tile[0]] = "."
    # print(n_t, n_f)
    return n_t * n_f


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
