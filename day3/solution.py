import sys
import re

with open(sys.argv[1]) as f:
    # print(sum(map(lambda x: is_safe([int(i) for i in x.split()]), f)))
    total = 0
    active = True
    for line in f:
        matches = re.findall(
            r"(mul\((\d{1,3}),(\d{1,3})\))|(do(?:n't)?\(\))", line)
        print(matches)
        for match in matches:
            if match[3] == "do()":
                active = True
                continue
            if match[3] == "don't()":
                active = False
                continue
            if active:
                total += int(match[1]) * int(match[2])

    print(total)
