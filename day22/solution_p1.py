import sys
from functools import cache


def get_num(num):
    num = (num ^ (num << 6)) % 16777216
    num = (num ^ (num >> 5)) % 16777216
    num = (num ^ (num << 11)) % 16777216
    return num


def loop(num, times):
    for _ in range(times):
        num = get_num(num)
    return num


with open(sys.argv[1]) as f:
    count = 0
    for line in f:
        num = int(line)
        count += loop(num, 2000)
    print(count)
