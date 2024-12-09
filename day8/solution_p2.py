import sys
from itertools import combinations

xdim = 0
ydim = 0
antennas = {}
antinodes = set()
with open(sys.argv[1]) as f:
    for line in f:
        xl = line.strip()
        xdim = len(xl)
        for ix, c in enumerate(xl):
            if c != ".":
                pos = (ix, ydim)
                antinodes.add(pos)
                if c not in antennas:
                    antennas[c] = [pos]
                else:
                    antennas[c].append(pos)
        ydim += 1

print(antennas)

for ant_type in antennas.values():
    for ant1, ant2 in combinations(ant_type, 2):
        xdiff = ant1[0] - ant2[0]
        ydiff = ant1[1] - ant2[1]

        i = 1
        while True:
            antinode_neg = (ant1[0] + i*xdiff, ant1[1] + i*ydiff)
            if 0 <= antinode_neg[0] < xdim and 0 <= antinode_neg[1] < ydim:
                antinodes.add(antinode_neg)
            else:
                break
            i += 1

        i = 1
        while True:
            antinode_pos = (ant2[0] - i*xdiff, ant2[1] - i*ydiff)
            if 0 <= antinode_pos[0] < xdim and 0 <= antinode_pos[1] < ydim:
                antinodes.add(antinode_pos)
            else:
                break
            i += 1

print(len(antinodes))
