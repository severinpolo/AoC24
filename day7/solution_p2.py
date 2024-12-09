import sys
import math


def concat(a, b):
    # return int(a * 10 ** math.ceil(math.log10(b)) + b)
    return int(str(a) + str(b))


def reduce(sol, cur, terms):
    if cur > sol:
        return False
    match len(terms):
        case 0: return sol == cur
        case _: return (reduce(sol, cur + terms[0], terms[1:])
                        or reduce(sol, cur * terms[0], terms[1:])
                        or reduce(sol, concat(cur, terms[0]), terms[1:]))


count = 0
with open(sys.argv[1]) as f:
    print("start")
    for line in f:
        sol, nums = line.split(":")
        sol, nums = int(sol), [int(n) for n in nums.split()]
        n_c = len(nums) - 1
        if reduce(sol, 0, nums):
            count += sol

print(count)
