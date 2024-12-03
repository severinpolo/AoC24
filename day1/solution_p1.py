import sys
from functools import reduce

inp = sys.argv[1]
with open(inp) as f:
    l_list = []
    r_list = []
    for line in f:
        l, r = line.split()
        l_list.append(int(l))
        r_list.append(int(r))

l_list = sorted(l_list)
r_list = sorted(r_list)

res = reduce(lambda agg, x: agg + abs(x[0] - x[1]), zip(l_list, r_list), 0)
print(res)
