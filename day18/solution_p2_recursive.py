import sys


xdim, ydim = 71, 71
directions = {(1, 0), (0, -1), (0, 1), (-1, 0)}


def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])


def check_ob(ob, ob_prev, obs, dirs, edge):
    res = False
    if not check_bounds(*ob):
        res = False
    elif ob not in obs:
        res = False
    elif ob[edge] == 0 or ob[(edge + 1) % 2] == xdim:
        res = True
    else:
        res = ((add_tup(ob, dirs[0]) != ob_prev and check_ob(add_tup(ob, dirs[0]), ob, obs, dirs, edge))
               or (add_tup(ob, dirs[1]) != ob_prev and check_ob(add_tup(ob, dirs[1]), ob,  obs, dirs, edge))
               or (add_tup(ob, dirs[2]) != ob_prev and check_ob(add_tup(ob, dirs[2]), ob, obs, dirs, edge))
               or (add_tup(ob, dirs[3]) != ob_prev and check_ob(add_tup(ob, dirs[3]), ob, obs, dirs, edge))
               or (add_tup(ob, dirs[4]) != ob_prev and check_ob(add_tup(ob, dirs[4]), ob, obs, dirs, edge)))
    # if res:
        # print(ob)
    return res


def check_bounds(x, y): return (0 <= x < xdim) and (0 <= y < ydim)


def print_maze(obs):
    maze = ""
    for x in range(xdim):
        for y in range(ydim):
            if (x, y) in obs:
                maze += '#'
            else:
                maze += '.'
        maze += '\n'
    print(maze)


dir_l = [(0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
dir_u = [(1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1)]
edge_r = set()
edge_d = set()
obs = set()
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        ob = tuple(map(int, line.split(',')))
        if ob[0] == xdim - 1:
            edge_r.add(ob)
        elif ob[1] == ydim - 1:
            edge_d.add(ob)

        obs.add(ob)
        print(ob)

        done = False
        if i >= 1024:
            # check r_edge:
            for ob in edge_r:
                if check_ob(ob, (-1, -1), obs, dir_l, 0):
                    print(ob)
                    done = True
                    break

            for ob in edge_d:
                if check_ob(ob, (-1, -1), obs, dir_u, 1):
                    print(ob)
                    done = True
                    break
        if done:
            break
print_maze(obs)
