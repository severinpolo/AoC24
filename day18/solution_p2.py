import sys
from queue import PriorityQueue


directions = {(1, 0), (0, -1), (0, 1), (-1, 0)}
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])


xdim, ydim = 71, 71


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


def dijkstra(obs) -> int:

    S = (0, 0)
    E = (xdim-1, ydim-1)
    unexplored = PriorityQueue()
    unexplored.put((0, S))
    explored = {}
    while unexplored.qsize() != 0:
        current_cost, current = unexplored.get()
        if current == E:
            return current_cost
        if current in explored:
            continue
        explored[current] = current_cost
        # print(current)
        # print(current_cost, current)
        for xdir, ydir in directions:
            x2, y2 = add_tup(current, (xdir, ydir))
            if (x2, y2) in obs:
                continue
            if not check_bounds(x2, y2):
                continue
            if (x2, y2) in explored:
                continue
            unexplored.put((current_cost+1, (x2, y2)))
    return -1


obs = set()
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        ob = tuple(map(int, line.split(',')))
        obs.add(ob)
        if i >= 1024:
            steps = dijkstra(obs)
            if steps == -1:
                print(ob)
                exit()
