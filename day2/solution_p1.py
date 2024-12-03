import sys


def is_safe(numbers: list[int]) -> bool:

    if len(numbers) < 2:
        return True

    if numbers[0] == numbers[1]:
        return False

    ascending = numbers[0] < numbers[1]

    for j in range(1, len(numbers)):
        i = j-1
        dist = numbers[i] - numbers[j]
        if dist == 0:
            return False

        if (dist < 0) != ascending:
            return False
        dist = abs(dist)

        if dist > 3:
            return False
    return True


with open(sys.argv[1]) as f:
    # print(sum(map(lambda x: is_safe([int(i) for i in x.split()]), f)))
    count = 0
    for line in f:
        numbers = [int(i) for i in line.split()]
        safe = is_safe(numbers)
        print(numbers, safe)
        count += int(safe)
    print(count)
