import sys
import functools


@functools.cache
def match(pattern):
    res = int(pattern in subs)
    for i in range(1, len(pattern)):
        if pattern[:i] in subs and (add := match(pattern[i:])):
            res += add
    return res


patterns = []
with open(sys.argv[1]) as f:
    subs = {s for s in f.readline().strip().split(', ')}
    f.readline()
    for line in f:
        patterns.append(line.strip())

print(sum(map(match, patterns)))
