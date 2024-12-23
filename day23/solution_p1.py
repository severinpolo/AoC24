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
    res = reduce(lambda agg, fr: agg | find_triplets(
        fr, [fr], 0, conns), filter(lambda fr: fr[0] == 't', conns), set())
    print(res)
    return len(res)


def find_triplets(start, curr, depth, conns):
    if depth == 3:
        if start == curr[-1]:
            return {",".join(sorted(curr[:-1]))}
        else:
            return set()
    return reduce(lambda agg, x: agg | find_triplets(start, curr+[x], depth+1, conns), conns[curr[-1]], set())


print(solve(conns))
