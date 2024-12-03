import sys
from functools import reduce

inp = sys.argv[1]
with open(inp) as f:
    l_counts = {}
    r_counts = {}
    for line in f:
        l, r = line.split()
        r = int(r)
        l = int(l)
        if l not in l_counts:
            l_counts[l] = 0
        l_counts[l] += 1
        if l not in r_counts:
            r_counts[l] = 0

        if r not in r_counts:
            r_counts[r] = 0
        r_counts[r] += 1

print(l_counts, r_counts)

res = reduce(lambda agg, x: agg + x *
             r_counts[x]*l_counts[x], l_counts.keys(), 0)


print(res)
