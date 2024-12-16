import sys
from heapq import heapify, heappush, heappop


maze = []
with open(sys.argv[1]) as f:
    for line in f:
        maze.append([c for c in line.strip()])


def solve(maze):
    S = (1, len(maze)-2, 1, 0)
    E = (len(maze[0])-2, 1, 1, 0)
    unexplored = [(0, S)]
    dists = {S: 0}
    explored = set()
    heapify(unexplored)
    while len(unexplored) != 0:
        current_cost, current = heappop(unexplored)
        if current[0] == E[0] and current[1] == E[1]:
            end = current
            break
        if current in explored:
            continue
        explored.add(current)
        x, y, xdir, ydir = current
        for cost2, (x2, y2, xdir2, ydir2) in [(1, (x + xdir, y+ydir, xdir, ydir)),
                                              (1000, (x, y, -ydir, xdir)),
                                              (1000, (x, y, ydir, -xdir))]:
            if maze[y2][x2] == '#':
                continue
            total_dist = current_cost + cost2
            if (x2, y2, xdir2, ydir2) not in dists or total_dist < dists[(x2, y2, xdir2, ydir2)]:
                heappush(unexplored, (total_dist, (x2, y2, xdir2, ydir2)))
                dists[(x2, y2, xdir2, ydir2)] = total_dist

    q = [end]
    seen = {end}
    while q:
        current = q.pop()
        if current == S:
            continue

        x, y, xdir, ydir = current
        for cost2, (x2, y2, xdir2, ydir2) in [(1, (x - xdir, y-ydir, xdir, ydir)),
                                              (1000, (x, y, -ydir, xdir)),
                                              (1000, (x, y, ydir, -xdir))]:
            if (x2, y2, xdir2, ydir2) in dists and dists[(x2, y2, xdir2, ydir2)] == dists[current] - cost2:
                if (x2, y2, xdir2, ydir2) not in seen:
                    q.append((x2, y2, xdir2, ydir2))
                    seen.add((x2, y2, xdir2, ydir2))
    seats = set((x, y) for x, y, _, _ in seen)

    return current_cost, len(seats)


min_cost, seats = solve(maze)
print(min_cost, seats)
