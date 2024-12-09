import sys
from itertools import permutations


def reduce(sol, cur, terms):
    if cur > sol:
        return False
    match len(terms):
        case 0: return sol == cur
        case _: return reduce(sol, cur + terms[0], terms[1:]) or reduce(sol, cur * terms[0], terms[1:])


count = 0
with open(sys.argv[1]) as f:
    print("start")
    for line in f:
        sol, nums = line.split(":")
        sol, nums = int(sol), [int(n) for n in nums.split()]
        n_c = len(nums) - 1
        print(sol, n_c, 2**n_c, flush=True)
        if reduce(sol, nums[0], nums[1:]):
            count += sol

print(count)
