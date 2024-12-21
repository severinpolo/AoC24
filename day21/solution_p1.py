import sys
from functools import cache


def sub_tup(x, y): return (x[0]-y[0], x[1]-y[1])


directional_buttons = {'A': (2, 0), '^': (
    1, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}
numerical_buttons = {'A': (2, 3),
                     '0': (1, 3),
                     '1': (0, 2),
                     '2': (1, 2),
                     '3': (2, 2),
                     '4': (0, 1),
                     '5': (1, 1),
                     '6': (2, 1),
                     '7': (0, 0),
                     '8': (1, 0),
                     '9': (2, 0),
                     }


@cache
def keypad(pos1, pos2, stack_pos, num_pad = False):
    pos = sub_tup(pos2, pos1)
    x, y = pos
    if stack_pos == 0:
        return abs(x) + abs(y) + 1

    steps_h = '>'*x if x > 0 else '<'*-x
    steps_v = 'v'*y if y > 0 else '^'*-y

    path1 = f"A{steps_v}{steps_h}A"
    path2 = f"A{steps_h}{steps_v}A"

    len1 = sum(map(lambda i: keypad(
        directional_buttons[path1[i]], directional_buttons[path1[i+1]], stack_pos - 1),
                   range(len(path1)-1)))
    len2 = sum(map(lambda i: keypad(
        directional_buttons[path2[i]], directional_buttons[path2[i+1]], stack_pos - 1),
                   range(len(path2)-1)))

    if num_pad:
        if pos1[1] == 3 and pos2[0] == 0:
            return len1
        if pos2[1] == 3 and pos1[0] == 0:
            return len2
    if not num_pad:
        if pos2 == (0, 1):
            return len1
        if pos1 == (0, 1):
            return len2

    return min(len1, len2)


with open(sys.argv[1]) as f:
    res_p1 = 0
    res_p2 = 0
    for line in f:
        input = "A"+line.strip()
        path_p1 = 0
        path_p2 = 0
        for pos1, pos2 in ((numerical_buttons[input[i]], numerical_buttons[input[i+1]])
                            for i in range(len(input)-1)):
            path_p1 += keypad(pos1, pos2, 2, num_pad=True)
            path_p2 += keypad(pos1, pos2, 25, num_pad=True)
        res_p1 += int(input[1:-1])*path_p1
        res_p2 += int(input[1:-1])*path_p2
        
    print("p1", res_p1)
    print("p2", res_p2)
