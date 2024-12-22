import sys
from functools import cache


def get_num(num):
    num = (num ^ (num * 64)) % 16777216
    num = (num ^ (num // 32)) % 16777216
    num = (num ^ (num * 2048)) % 16777216
    return num


def loop(num, times):
    nums = []
    changes = {}
    for t in range(times):
        num = get_num(num)
        p = num % 10
        nums.append(p)
        if len(nums) == 5:
            series = tuple(nums[i+1] - nums[i] for i in range(4))
            if series not in changes:
                changes[series] = p
            nums = nums[1:]

    return changes


with open(sys.argv[1]) as f:
    brokers = []
    for line in f:
        num = int(line)
        brokers.append(loop(num, 2000))
    max_bananas = 0
    max_series = None
    seen = set()
    for broker in brokers:
        for series in broker:
            if series in seen:
                continue
            test_series = 0
            for broker2 in brokers:
                if series in broker2:
                    test_series += broker2[series]
            if max_bananas < test_series:
                max_bananas = test_series
                max_series = series
            seen.add(series)
    print(max_bananas, max_series)
