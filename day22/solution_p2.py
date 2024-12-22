import sys
import line_profiler
from collections import Counter


def get_num(num):
    num = (num ^ (num << 6)) % 16777216
    num = (num ^ (num >> 5)) % 16777216
    num = (num ^ (num << 11)) % 16777216
    return num


@line_profiler.profile
def solve(brokers, times):
    bananas = Counter()
    for num in brokers:
        seen = set()
        nums = [num % 10]
        do_series = False
        for t in range(times):
            num = get_num(num)
            p = num % 10
            nums[-1] = p - nums[-1]
            if do_series or len(nums) == 4:
                do_series = True
                series = tuple(nums)
                if series not in seen:
                    bananas[series] += p
                    seen.add(series)
                nums.pop(0)
            nums.append(p)
    return max(bananas.items(), key=lambda x: x[1])


with open(sys.argv[1]) as f:
    print(solve([int(x) for x in f.read().strip().split('\n')], 2000))
