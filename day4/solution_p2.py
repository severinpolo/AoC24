import sys

matrix = []
with open(sys.argv[1]) as f:
    for line in f:
        matrix.append(line[:-1])

count = 0
dy = len(matrix[0])
dx = len(matrix)
for ix in range(dx-2):
    for iy in range(dy-2):
        # tl = matrix[ix][iy]
        # tr = matrix[ix][iy+2]
        # ce = matrix[ix+1][iy+1]
        # bl = matrix[ix+2][iy]
        # br = matrix[ix+2][iy+2]
        # print(f"{tl}.{tr}\n.{ce}.\n{bl}.{br}\n")
        test = matrix[ix][iy] + matrix[ix][iy+2] + \
            matrix[ix+1][iy+1] + matrix[ix+2][iy] + matrix[ix+2][iy+2]
        if test == 'MSAMS' or test == 'SSAMM' or test == 'MMASS' or test == 'SMASM':
            # print("check")
            count += 1


print(count)
