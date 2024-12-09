import sys

matrix = []
current = None
stones = {".": 0, "#": 1}
with open(sys.argv[1]) as f:
    y = 0
    for line in f:
        lab = [s for s in line.strip()]
        if "^" in lab:
            x = lab.index("^")
            current = (x, y, 0, -1)
            lab[x] = "."
        elif ">" in lab:
            x = lab.index(">")
            current = (x, y, 1, 0)
            lab[x] = "."
        elif "v" in lab:
            x = lab.index("v")
            current = (x, y, 0, 1)
            lab[x] = "."
        elif "<" in lab:
            x = lab.index("<")
            current = (x, y, -1, 0)
            lab[x] = "."
        matrix.append([stones[s] for s in lab])
        y += 1


def check_path(matrix, start):
    current = tuple(s for s in start)  # shallow copy
    visited = set()

    xdim = len(matrix[0])
    ydim = len(matrix)

    while True:
        if current in visited:
            # print("cycle detected!!!", cycle)
            return visited, True
        visited.add(current)
        xstep = current[2]
        ystep = current[3]
        new_pos = (current[0] + xstep, current[1] + ystep, xstep, ystep)
        if new_pos[0] >= xdim or new_pos[1] >= ydim or new_pos[0] < 0 or new_pos[1] < 0:
            break
        r = 0
        while matrix[new_pos[1]][new_pos[0]] == 1:  # obstacle detected
            r += 1
            if r < 1:
                print("rotations", r)
            # print("obstacle!")
            if (xstep, ystep) == (0, -1):
                xstep, ystep = 1, 0
            elif (xstep, ystep) == (1, 0):
                xstep, ystep = 0, 1
            elif (xstep, ystep) == (0, 1):
                xstep, ystep = -1, 0
            elif (xstep, ystep) == (-1, 0):
                xstep, ystep = 0, -1
            new_pos = (current[0] + xstep, current[1] + ystep, xstep, ystep)
        if new_pos[0] >= xdim or new_pos[1] >= ydim or new_pos[0] < 0 or new_pos[1] < 0:
            break
        current = new_pos
    return visited, False


def print_path(matrix, visited):
    stones_r = {0: " ", 1: "#"}
    guard = {(0, -1): "^", (1, 0): '>', (0, 1): "v", (-1, 0): '<'}
    with open("test.txt", 'w') as f:
        matrix = [[stones_r[x] for x in y] for y in matrix]
        for pos in visited:
            matrix[pos[1]][pos[0]] = guard[(pos[2], pos[3])]
        for m in matrix:
            f.write("".join(m) + "\n")


visited, cycle = check_path(matrix, current)
count = 0
for x, y in set((x, y) for x, y, _, _ in visited):
    test_mat = [[s for s in l] for l in matrix]  # copy mat
    test_mat[y][x] = 1  # set stone
    if check_path(test_mat, current)[1]:
        count += 1

print(count)
