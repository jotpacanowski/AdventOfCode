# 2021-12-02
# Python 3.10 port of day 2 solution

def main1(lines):
    fwd = 0
    dep = 0
    for x, y in lines:
        if x == 'forward':
            fwd += y
        elif x == 'up':
            dep -= y
        elif x == 'down':
            dep += y
        else:
            print(f'??? {x!r}')
    print(f' * {fwd=} {dep=}')
    return fwd * dep


def main2(lines):
    fwd = 0
    dep = 0
    aim = 0
    for x, y in lines:
        if x == 'forward':
            fwd += y
            dep += aim * y
        elif x == 'up':
            # dep -= y
            aim -= y
        elif x == 'down':
            # dep += y
            aim += y
        else:
            print(f'??? {x!r}')
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
