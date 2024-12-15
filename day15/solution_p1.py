import sys


class Room(list):

    def __call__(self, pos, tile=None):
        if tile is not None:
            self[pos[1]][pos[0]] = tile
        return self[pos[1]][pos[0]]

    def print(self):
        string = "\n".join(map(lambda x: "".join(x), self))
        print(string)

    def solve(self) -> int:
        res = 0
        for y, row in enumerate(self):
            for x, c in enumerate(row):
                if c == "O":
                    res += y*100 + x
        return res

    def __copy__(self):
        new_room = Room()
        for row in self:
            new_room.append([c for c in row])
        return new_room

    def copy(self):
        return self.__copy__()


directions = {">": (1, 0), "^": (0, -1), "v": (0, 1), "<": (-1, 0)}
def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])
def check_bounds(x): return 0 <= x[0] < xdim and 0 <= x[1] < ydim


def move(room: Room, pos, step) -> bool:
    next_pos = add_tup(pos, step)
    steps = 0
    while room(next_pos) == "O":
        steps += 1
        next_pos = add_tup(next_pos, step)

    if room(next_pos) == "#":
        return False
    elif steps > 0:
        room(next_pos, "O")
        room(pos, ".")
        return True
    else:
        room(pos, ".")
        return True


room = Room()
steps = []
start = None
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        if line.isspace():
            break
        row = []
        for x, c in enumerate(line.strip()):
            if c == "@":
                start = (x, y)
                c = "."
            row.append(c)
        room.append(row)
    for line in f:
        steps.extend((directions[c] for c in line.strip()))

xdim, ydim = len(room[0]), len(room)

pos = start
for step in steps:
    print(step)
    if move(room, pos, step):
        print(pos, room(pos))
        pos = add_tup(pos, step)
        print(pos, room(pos))
    room2 = room.copy()
    room2(pos, "@")
    room2.print()

room(pos, "@")
print(room.solve())
