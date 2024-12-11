import sys

stones = {}
with open(sys.argv[1]) as f:
    for x in map(int, f.readline().split()):
        if x in stones:
            stones[x] += 1
        else:
            stones[x] = 1


def update_stones(stone, n_stones, stones):
    if stone in stones:
        stones[stone] += n_stones
    else:
        stones[stone] = n_stones


for i in range(75):
    stones_new = {}
    for stone, n_stone in stones.items():
        if stone == 0:
            update_stones(1, n_stone, stones_new)
            continue

        str_stone = str(stone)
        len_stone = len(str_stone)
        if len_stone % 2 == 0:
            update_stones(int(str_stone[:len_stone//2]), n_stone, stones_new)
            update_stones(int(str_stone[len_stone//2:]), n_stone, stones_new)
            continue

        update_stones(stone * 2024, n_stone, stones_new)
    # stones = {k: v for k, v in stones_new.items()}
    stones = stones_new
    # print(len(stones))

# print(sorted(((k, v) for k, v in stones.items()), key=lambda x: x[1]))
print(sum(stones.values()))
