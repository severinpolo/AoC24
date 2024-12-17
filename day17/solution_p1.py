import sys


def combo(op, regs):
    match op:
        case 0 | 1 | 2 | 3: return op
        case 4: return regs["A"]
        case 5: return regs["B"]
        case 6: return regs["C"]
        case 7: raise ValueError("7 is invalid")


regs = {}

with open(sys.argv[1]) as f:
    # global A, B, C, IP, OUT
    regs["A"] = int(f.readline().split()[-1])
    # A = 2024
    regs["B"] = int(f.readline().split()[-1])
    regs["C"] = int(f.readline().split()[-1])
    A = regs["A"]
    B = regs["B"]
    C = regs["C"]
    regs["IP"] = 0
    regs["OUT"] = []

    f.readline()
    raw = [int(x) for x in f.readline().split()[1].split(",")]
    while regs["IP"] + 1 < len(raw):
        # run_ins(raw[regs["IP"]], raw[regs["IP"]+1])
        ins = raw[regs["IP"]]
        op = raw[regs["IP"]+1]
        # print(regs["IP"], raw[regs["IP"]], op,
        # "   ", regs["A"], regs["B"], regs["C"])
        match ins:
            case 0:
                print(f'    a = a // (2 ** {combo(op, regs)})  ({op})')
                regs["A"] = regs["A"]//(2**combo(op, regs))
            case 1:
                print(f'    b = b ^ {op}')
                res = regs["B"] ^ op
                regs["B"] = res
            case 2:
                print(f'    b = {combo(op, regs)} % 8  ({op})')
                regs["B"] = combo(op, regs) % 8
            case 3:
                print(f'    IF a != 0 GOTO OP{op})')
                if regs["A"] != 0:
                    regs["IP"] = op - 2
            case 4:
                print('    b = b ^ c')
                res = regs["B"] ^ regs["C"]
                regs["B"] = res
            case 5:
                print(f'    out += ,{combo(op, regs)} % 8   ({op})')
                regs["OUT"].append(str(combo(op, regs) % 8))
            case 6:
                print(f'    b = a // (2 ** {combo(op, regs)})  ({op})')
                regs["B"] = regs["A"]//(2**combo(op, regs))
            case 7:
                print(f'    c = a // (2 ** {combo(op, regs)})  ({op})')
                regs["C"] = regs["A"]//(2**combo(op, regs))
        regs["IP"] += 2
    print(",".join(regs["OUT"]))
