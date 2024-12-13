import sys


def get_nums_button(line) -> (int, int):
    x, y = line.split()[-2:]
    x, y = int(x.split("+")[1][:-1]), int(y.split("+")[1])
    return (x, y)


def get_nums_price(line) -> (int, int):
    x, y = line.split()[-2:]
    x, y = int(x.split("=")[1][:-1]), int(y.split("=")[1])
    # return (x, y)
    return (x+10000000000000, y+10000000000000)


lses = []
with open(sys.argv[1]) as f:
    line = True
    while line:
        A = [get_nums_button(f.readline()) for _ in range(2)]
        B = get_nums_price(f.readline())
        lses.append((A, B))
        line = f.readline()  # skips empty lines

tokens = 0
for ab, (x_p, y_p) in lses:

    x_b, y_b = ab[1]
    x_a, y_a = ab[0]
    a = (x_p*y_b - y_p*x_b)/(x_a*y_b - y_a*x_b)

    if a > 0 and a.is_integer():
        b = (x_p - a*x_a)/x_b
        if b > 0 and b.is_integer():
            tokens += a*3 + b

print(int(tokens))
