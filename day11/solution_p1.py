import sys
import math

stones = []
with open(sys.argv[1]) as f:
    stones = [int(x) for x in f.readline().split()]


def blink(stone, depth):
    if depth == 75:
        return 1

    if stone == 0:
        return blink(1, depth+1)

    str_stone = str(stone)
    len_stone = len(str_stone)
    if len_stone % 2 == 0:
        return blink(int(str_stone[:len_stone//2]), depth+1) + blink(int(str_stone[len_stone//2:]), depth+1)

    return blink(stone * 2024, depth+1)


print(sum(blink(stone, 0) for stone in stones))
