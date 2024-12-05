import sys

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
    valid = True
    for r in rules:
        try:
            i1 = u.index(r[0])
        except ValueError:
            continue
        try:
            i2 = u.index(r[1])
        except ValueError:
            continue
        if i1 > i2:
            valid = False
            break
    if valid:
        print(u, (len(u)-1)//2)
        count += u[(len(u)-1)//2]


print(count)
