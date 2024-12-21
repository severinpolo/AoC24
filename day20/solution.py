import sys
from itertools import chain


track = set()
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c != "#":
                track.add((x, y))
            if c == "S":
                start = (x, y)
            if c == "E":
                end = (x, y)


directions = {(1, 0), (0, -1), (0, 1), (-1, 0)}


def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])
def dist_tup(x, y): return abs(x[0] - y[0]) + abs(x[1] - y[1])


def find_cheats(race) -> int:
    cheats = 0
    for i, pi in enumerate(race[:-102]):
        for j, pj in enumerate(race[i+102:]):
            dist = dist_tup(pi, pj)
            if dist < 21 and j+3 > dist:
                cheats += 1

    return cheats


def run_track(track, start, end) -> dict:
    pos = start
    race = [start]
    while pos != end:
        for pos_new in map(lambda x: add_tup(pos, x), directions):
            if pos_new in track:
                track.remove(pos_new)
                break
        pos = pos_new
        race.append(pos)

    return race


cheats = find_cheats(run_track(track, start, end))
print(cheats)
