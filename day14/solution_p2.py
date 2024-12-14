import sys

xdim = 101
ydim = 103


def calc_pos(pos, vel, time):
    xpos, ypos = ((vel[0]*time + pos[0]) % xdim, (vel[1]*time + pos[1]) % ydim)
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

for time in range(1000000):
    positions = set()
    for pos, vel in robots:
        post = calc_pos(pos, vel, time)
        if post in positions:
            break
        positions.add(post)
    if len(robots) == len(positions):
        pic = [[" " for _ in range(xdim)] for _ in range(ydim)]
        for x, y in positions:
            pic[y][x] = "*"
        print(f"TIME: {time:+^10}")
        print("\n".join(map(lambda x: "".join(x), pic)))
        print(100*"=")
        break
