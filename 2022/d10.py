def parse_instr(line: str) -> tuple[int, int]:
    match line.split(' ', 1):
        case ['noop']:
            return 1, 0
        case ['addx', x]:
            return 2, int(x)
    raise ValueError(line)


def run_cpu(code: list[tuple[int, int]]):
    LIST_X = (20, 60, 100, 140, 180, 220,)
    xvals = {0: 1}
    r = 0

    clk = 0
    x = 1
    for delay, change in code:
        for j in range(1, delay+1):
            clk += 1
            xvals[clk] = x
            if clk in LIST_X:
                print(f'{clk=:4d}  {x=:4d}')
                r += clk * x
        x += change
    print('program cycles:', clk)
    print('part1:', r)
    return xvals


def run_crt(xvals: dict[int, int]):
    screen = [
        [' ' for _ in range(40)]
        for _ in range(6)
    ]
    for clk in range(1, 241):
        posr, posc = divmod(clk-1, 40)
        x = xvals[clk]
        if x-1 <= posc <= x+1:
            screen[posr][posc] = '#'
    print('')
    for r in screen:
        for c in r:
            print(c, end='')
        print('')
    print('')


if __name__ == '__main__':
    lines: str = open('input/in10.txt').read()
    # lines = TEST
    code = list(map(parse_instr,
                    lines.splitlines()))
    xvals = run_cpu(code)
    run_crt(xvals)
