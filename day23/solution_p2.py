import sys
from functools import reduce


conns = {}
with open(sys.argv[1]) as f:
    for line in f:
        fr, to = line.strip().split('-')
        if fr in conns:
            conns[fr].add(to)
        else:
            conns[fr] = {to}
        if to in conns:
            conns[to].add(fr)
        else:
            conns[to] = {fr}


def solve(conns):
    res = set()
    t = len(conns)
    i = 0
    frs = list(conns.keys())
    while len(conns) > 0 and i < t:
        conns_cp = conns.copy()
        res |= find_triplets(frs[i], [frs[i]], 0, conns_cp)
        i += 1
    return max(res)


def find_triplets(start, curr, depth, conns):
    if depth > 0:
        if curr[-2] in conns:
            del conns[curr[-2]]
    c = conns[curr[-1]]
    if len(c) < len(curr)-1 or any(x not in c for x in curr[:-1]):
        return {(depth, ",".join(sorted(curr[:-1])))}

    return reduce(lambda agg, x: agg | find_triplets(start, curr+[x], depth+1, conns),
                  filter(lambda x: x not in curr and x in conns, c), set())


print(solve(conns))
