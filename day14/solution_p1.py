import sys

xdim = 101
ydim = 103


def count_quadrants(robots):
    x2 = xdim // 2
    y2 = ydim // 2
    print(robots)

    ur, ul, lr, ll = 0, 0, 0, 0
    for x, y in robots:
        if x < x2:
            if y < y2:
                ul += 1
            elif (ydim - y2) <= y < ydim:
                ll += 1
        elif (xdim - x2) <= x < xdim:
            if y < y2:
                ur += 1
            elif (ydim - y2) <= y < ydim:
                lr += 1
    print(ul, ur, ll, lr)
    return ul * ur * lr * ll

    # sum_quad(robots, 0, x2, 0, y2) * sum_quad(robots, 0, x2, ydim - y2, ydim) * \
    # sum_quad(robots, xdim-x2, xdim, 0, y2) * \
    # sum_quad(robots, xdim-x2, xdim, ydim-y2, ydim)


def add_tup(x, y): return (x[0]+y[0], x[1] + y[1])


def calc_pos(pos, vel):
    xpos, ypos = ((vel[0]*100 + pos[0]) % xdim, (vel[1]*100 + pos[1]) % ydim)
    if xpos < 0:
        xpos = xdim - xpos
    if ypos < 0:
        ypos = ydim - ypos
    return (xpos, ypos)


robots = []
with open(sys.argv[1]) as f:
    for line in f:
        pos, vel = line.split()
        pos = tuple(map(int, pos[2:].split(',')))
        vel = tuple(map(int, vel[2:].split(',')))
        robots.append((pos, vel))

final_pos = []
for pos, vel in robots:
    final_pos.append(calc_pos(pos, vel))

print(count_quadrants(final_pos))
