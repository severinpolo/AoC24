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


def solve(R: set, P: set, X: set):
    if len(P) == 0 and len(X) == 0:
        return (len(R), ",".join(sorted(R)))
    P_cp = P.copy()
    max = (0, set())
    for v in P_cp:
        res = solve(R | {v}, P & conns[v], X & conns[v])
        P.remove(v)
        X.add(v)
        if max[0] < res[0]:
            max = res
    return max


print(solve(set(), set(conns.keys()), set()))
