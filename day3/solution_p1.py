import sys
import re

with open(sys.argv[1]) as f:
    # print(sum(map(lambda x: is_safe([int(i) for i in x.split()]), f)))
    total = 0
    for line in f:
        matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
        print(matches)
        total += sum((int(x[0]) * int(x[1]) for x in matches))
    print(total)
