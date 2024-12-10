import sys
from collections import deque


files = None
frees = None
with open(sys.argv[1]) as f:
    nums = [int(n) for n in f.readline().strip()]
    files = nums[::2]
    frees = nums[1::2]


dq = deque()

for fi, size in enumerate(files):
    for _ in range(size):
        dq.append(fi)

checksum = 0
pos = 0
for i_free, free_space in enumerate(frees):
    file = dq[0]
    while file == dq[0]:
        file = dq.popleft()
        checksum += pos * file
        pos += 1
        if len(dq) == 0:
            break
    for _ in range(free_space):
        if len(dq) == 0:
            break
        file = dq.pop()
        checksum += pos * file
        pos += 1
    if len(dq) == 0:
        break
    print(checksum)

print(checksum)
