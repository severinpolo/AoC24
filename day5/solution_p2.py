import sys


def check_rule(update: list[int], rule: [int, int]) -> (bool, int, int):
    try:
        i1 = update.index(rule[0])
    except ValueError:
        return True, -1, -1
    try:
        i2 = update.index(rule[1])
    except ValueError:
        return True, -1, -1
    if i1 > i2:
        return False, i1, i2
    return True, -1, -1


count = 0
rules = []
updates = []
with open(sys.argv[1]) as f:
    for line in f:
        if '|' in line:
            rules.append([int(x) for x in line.split("|")])
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])

for u in updates:
    if not all(check_rule(u, r)[0] for r in rules):
        invalid = True
        while invalid:
            invalid = False
            for r in rules:
                check, i1, i2 = check_rule(u, r)
                if not check:
                    invalid = True
                    u[i1] = r[1]
                    u[i2] = r[0]
        count += u[(len(u) - 1)//2]


print(count)
