import sys

matrix = []
with open(sys.argv[1]) as f:
    for line in f:
        matrix.append(line[:-1])

count = 0
dy = len(matrix[0])
dx = len(matrix)
for ix in range(dx):
    for iy in range(dy):
        cell = matrix[ix][iy]
        # if cell != 'S' and cell != 'X':
        # continue

        if iy < dy - 3:
            row = cell + matrix[ix][iy+1:iy+4]
            if row == 'XMAS' or row == 'SAMX':
                count += 1
        if ix < dx - 3:
            col = cell + matrix[ix+1][iy] + matrix[ix+2][iy] + matrix[ix+3][iy]
            if col == 'XMAS' or col == 'SAMX':
                count += 1
        if (ix < dx - 3) and (iy < dy - 3):
            diag = cell + matrix[ix+1][iy+1] + \
                matrix[ix+2][iy+2] + matrix[ix+3][iy+3]
            if diag == 'XMAS' or diag == 'SAMX':
                count += 1
        if (iy > 2) and (ix < dx - 3):
            bdiag = cell + matrix[ix+1][iy-1] + \
                matrix[ix+2][iy-2] + matrix[ix+3][iy-3]
            if bdiag == 'XMAS' or bdiag == 'SAMX':
                count += 1


print(count)
