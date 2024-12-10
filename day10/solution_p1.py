import sys

matrix = []
trailheads = []
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        vec = []
        for x, i in enumerate(map(int, line.strip())):
            if i == 0:
                trailheads.append((x, y))
            vec.append(i)
        matrix.append(vec)

xdim, ydim = len(matrix[0]), len(matrix)
steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])
def check_bounds(x): return 0 <= x[0] < xdim and 0 <= x[1] < ydim


def solve(matrix, head, height):
    if height == 9:
        return {head}
    score = set()
    for step in steps:
        new_head = add_tup(head, step)
        if check_bounds(new_head):
            new_height = matrix[new_head[1]][new_head[0]]
            if new_height == height + 1:
                score.update(solve(matrix, new_head, new_height))
    return score


print(sum(len(solve(matrix, trailhead, 0)) for trailhead in trailheads))
