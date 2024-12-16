import sys
from heapq import heapify, heappush, heappop


maze = []
with open(sys.argv[1]) as f:
    for line in f:
        maze.append([c for c in line.strip()])

tiles = []
paths = {}
directions = {(1, 0), (0, -1), (0, 1), (-1, 0)}
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])


S = (1, len(maze)-2, 1, 0)
E = (len(maze[0])-2, 1, 1, 0)
unexplored = [(float('inf'), E)]
explored = set()
heapify(unexplored)
current = S
current_cost = 0
while len(unexplored) != 0:
    if current[0] == E[0] and current[1] == E[1]:
        break
    x, y, xdir, ydir = current
    # print(current)
    for xdir2, ydir2 in directions:
        x2, y2 = add_tup((x, y), (xdir2, ydir2))
        # print(x2, y2)
        if maze[y2][x2] == '#':
            continue
        cost2 = "error"
        if xdir == xdir2 and ydir == ydir2:
            cost2 = 1
        # 180 turn is unnecessary
        if (xdir == xdir and ydir != ydir2) or (xdir != xdir2 and ydir == ydir2):
            cost2 = 2001
        if xdir != xdir2 and ydir != ydir2:
            if maze[y2][x2] == "E":
                cost2 = 1
            else:
                cost2 = 1001
        if (x2, y2, xdir2, ydir2) not in explored:
            heappush(unexplored, (current_cost+cost2, (x2, y2, xdir2, ydir2)))
    explored.add(current)
    current_cost, current = heappop(unexplored)

print(current_cost, current)
