# 2021-12-02
# Python 3.10 port of day 2 solution

import sys
if sys.version_info < (3, 10):
    raise SystemExit('Python 3.10 is required.')


def main1(lines):
    fwd = 0
    dep = 0
    for line in lines:
        match line:
            case ['forward', int(X)]:
                fwd += X
            case ['up', int(X)]:
                dep -= X
            case ['down', int(X)]:
                dep += X
            case _:
                print(f'??? {line!r}')
    print(f' * {fwd=} {dep=}')
    return fwd * dep


def main2(lines):
    fwd = 0
    dep = 0
    aim = 0
    for x, y in lines:
        match x, y:
            case ['forward', int(X)]:
                fwd += X
                dep += aim * X
            case ['up', int(X)]:
                aim -= X
            case ['down', int(X)]:
                aim += X
            case _:
                print(f'??? {x,y!r}')
    print(f' * {fwd=} {dep=}')
    return fwd * dep


if __name__ == '__main__':
    inp_values = open('2-input', 'r').read().splitlines()
    inp_values = [(x.split()[0], int(x.split()[1])) for x in inp_values]
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'Answer: {answ} \n Pt. 2')

    answ = main2(inp_values)
    print(f'Answer: {answ}')
