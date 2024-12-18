import sys
from queue import PriorityQueue


obs = set()
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i >= 1024:
            break
        obs.add(tuple(map(int, line.split(','))))

directions = {(1, 0), (0, -1), (0, 1), (-1, 0)}
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])


xdim, ydim = 71, 71
S = (0, 0)
E = (xdim-1, ydim-1)
unexplored = PriorityQueue()
unexplored.put((0, S))
explored = {}
unexplored2 = set()


def check_bounds(x, y): return (0 <= x < xdim) and (0 <= y < ydim)


def print_maze(obs, explored):
    maze = ""
    for x in range(xdim):
        for y in range(ydim):
            if (x, y) in obs:
                maze += '#'
            elif (x, y) in explored:
                maze += 'O'
            else:
                maze += '.'
        maze += '\n'
    print(maze)


while unexplored.qsize() != 0:
    current_cost, current = unexplored.get()
    explored[current] = current_cost
    if current == E:
        break
    # print(current)
    # print(current_cost, current)
    for xdir, ydir in directions:
        x2, y2 = add_tup(current, (xdir, ydir))
        # print(x2, y2)
        if (x2, y2) in explored or (x2, y2) in unexplored2:
            continue
        if (x2, y2) in obs:
            continue
        if not check_bounds(x2, y2):
            continue
        # print("\t", x2, y2)
        cost = 1
        # 180 turn is unnecessary
        unexplored.put((current_cost+cost, (x2, y2)))
        unexplored2.add((x2, y2))

print(current_cost, current)
