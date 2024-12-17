import sys


def solve_bits(pos, a_guess, prog):
    if pos < 0:
        print(a_guess)
        return True
    b = 0
    c = 0
    for test in range(8):
        a = a_guess << 3 | test
        ip = 0
        while ip < len(prog):
            ins = prog[ip]
            op = prog[ip+1]
            cop = op
            match op:
                case 4: cop = a
                case 5: cop = b
                case 6: cop = c
                case 7: raise ValueError("7 is invalid")
            match ins:
                case 0: a = a//(2**cop)
                case 1: b = b ^ op
                case 2: b = cop % 8
                case 3: ip = op - 2 if a != 0 else ip
                case 4: b = b ^ c
                case 5:
                    out = cop % 8
                    break
                case 6: b = a//(2**cop)
                case 7: c = a//(2**cop)
            ip += 2
        if out == prog[pos] and solve_bits(pos-1, a_guess << 3 | test, prog):
            return True
    return False


regs = {}

with open(sys.argv[1]) as f:
    f.readline()

    f.readline()
    f.readline()

    f.readline()
    raw = [int(x) for x in f.readline().split()[1].split(",")]
    print(raw)
    solve_bits(len(raw)-1, 0, raw)
