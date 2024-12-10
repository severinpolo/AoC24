import sys
from collections import deque


files = []
frees = []
with open(sys.argv[1]) as f:
    nums = [int(n) for n in f.readline().strip()]
    # files = nums[::2]
    # frees = nums[1::2]

pos = 0
for i, n in enumerate(nums):
    if i % 2 == 0:
        files.append((i//2, pos, n))
        pos += n
    else:
        frees.append((pos, n))
        pos += n

# print(files)
# print(frees)

rev_files = list(reversed(files))
final_files = []
for i, pos, n in rev_files:
    shifted = False
    for i_free in range(len(frees)):
        if pos <= frees[i_free][0]:
            break
        if frees[i_free][1] >= n:
            final_files.append((i, frees[i_free][0], n))
            # print((i, pos, n), "->", (i, frees[i_free][0], n))
            frees[i_free] = (frees[i_free][0] + n, frees[i_free][1] - n)
            shifted = True
            break
    if not shifted:
        final_files.append((i, pos, n))

# test = sorted(final_files, key=lambda x: x[1])
# # print(test)
# final_string = ["."]*sum(nums)
# for i, pos, n in test:
    # for j in range(n):
        # final_string[pos+j] = str(i)

# print("".join(final_string))

checksum = 0
for i, pos, n in final_files:
    for j in range(n):
        checksum += (pos+j)*i

print(checksum)
