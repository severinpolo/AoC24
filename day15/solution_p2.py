import sys


class Room(list):

    def __call__(self, pos, tile=None):
        if tile is not None:
            self[pos[1]][pos[0]] = tile
        return self[pos[1]][pos[0]]

    def print(self):
        string = "\n".join(map(lambda x: "".join(x), self))
        print(string)
        if "[[" in string or "]]" in string or ".][" in string or "][." in string:
            raise RuntimeError("Error!!!")

    def solve(self, xdim, ydim) -> int:
        res = 0
        for y, row in enumerate(self):
            for x, c in enumerate(row):
                if c == "[":
                    res += y * 100 + x

        return res

    def __copy__(self):
        new_room = Room()
        for row in self:
            new_room.append([c for c in row])
        return new_room

    def copy(self):
        return self.__copy__()


directions = {">": (1, 0), "^": (0, -1), "v": (0, 1), "<": (-1, 0)}
directions_rev = {v: k for k, v in directions.items()}


def add_tup(x, y): return (x[0] + y[0], x[1] + y[1])
def check_bounds(x): return 0 <= x[0] < xdim and 0 <= x[1] < ydim


def move_box(room: Room, box, step, stack) -> bool:
    lpos, rpos = box
    new_rpos = add_tup(rpos, step)
    new_lpos = add_tup(lpos, step)
    res = False
    match step, room(new_lpos), room(new_rpos):
        case (_, "#", _) | (_, _, "#") | (_, "#", "#"): res = False
        case ((1, 0), "]", "."):
            res = True
        case ((-1, 0), ".", "["):
            res = True
        case ((1, 0), "]", "["):
            if move_box(room, (add_tup(new_lpos, step), add_tup(new_rpos, step)), step, stack):
                res = True
        case ((-1, 0), "]", "["):
            if move_box(room, (add_tup(new_lpos, step), add_tup(new_rpos, step)), step, stack):
                res = True
        case ((0, 1 | -1), "[", "]"):
            if move_box(room, (new_lpos, new_rpos), step, stack):
                res = True
        case ((0, 1 | -1), "]", "."):
            if move_box(room, (add_tup(new_lpos, directions["<"]), new_lpos), step, stack):
                res = True
        case ((0, 1 | -1), ".", "["):
            if move_box(room, (new_rpos, add_tup(new_rpos, directions[">"])), step, stack):
                res = True
        case ((0, 1 | -1), "]", "["):
            if move_box(room, (add_tup(new_lpos, directions["<"]), new_lpos), step, stack) and move_box(room, (new_rpos, add_tup(new_rpos, directions[">"])), step, stack):
                res = True
        case ((0, 1 | -1), ".", "."):
            res = True
        case _ as x:
            raise RuntimeError(f"case not covered: {x}")

    if res:
        stack.append(box)
    return res


def move(room: Room, pos, step, stack) -> bool:
    next_pos = add_tup(pos, step)
    next_tile = room(next_pos)
    match step, next_tile:
        case (-1, 0), "]":
            return move_box(room, (add_tup(next_pos, step), next_pos), step, stack)
        case (1, 0), "[":
            return move_box(room, (next_pos, add_tup(next_pos, step)), step, stack)
        case (0, 1 | -1), "[" | "]":
            if next_tile == "[":
                return move_box(room, (next_pos, add_tup(next_pos, directions[">"])), step, stack)
            if next_tile == "]":
                return move_box(room, (add_tup(next_pos, directions["<"]), next_pos), step, stack)
        case _, "#":
            return False
        case _, ".":
            return True
        case _ as x:
            raise RuntimeError(f"move Error: {x}")

    raise RuntimeError("move Error")


room = Room()
steps = []
start = None
with open(sys.argv[1]) as f:
    for y, line in enumerate(f):
        if line.isspace():
            break
        row = []
        x = 0
        for c in line.strip():
            if c == "@":
                start = (x, y)
                row.append(".")
                row.append(".")
            elif c == "O":
                row.append("[")
                row.append("]")
            else:
                row.append(c)
                row.append(c)
            x += 2
        room.append(row)
    for line in f:
        for c in line.strip():
            steps.append(directions[c])

xdim, ydim = len(room[0]), len(room)

pos = start
for istep, step in enumerate(steps):
    stack = []
    if move(room, pos, step, stack):
        for lpos, rpos in stack:
            room(lpos, ".")
            room(rpos, ".")
        for lpos, rpos in stack:
            room(add_tup(lpos, step), "[")
            room(add_tup(rpos, step), "]")
        pos = add_tup(pos, step)

room(pos, "@")
room.print()
print(istep, room.solve(xdim, ydim))
