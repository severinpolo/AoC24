import sys


def match(pattern):
    if pattern in subs:
        return True
    for i in range(1, len(pattern)):
        if pattern[:-i] in subs and match(pattern[len(pattern)-i:]):
            subs.add(pattern[len(pattern)-i:])
            return True
    return False


subs = set()
patterns = []
with open(sys.argv[1]) as f:
    subs = {s for s in f.readline().strip().split(', ')}
    f.readline()
    for line in f:
        patterns.append(line.strip())


print(sum(map(match, patterns)))
