#!/usr/bin/env python3
# 2021-12-07

import io
from pprint import pprint


def main1(values) -> int:
    values.sort()
    a = values[0]   # min(values)
    b = values[-1]  # max(values)

    def f(pos):
        return sum(abs(pos - x) for x in values)

    ls = [(f(i), i) for i in range(a-1, b+2)]
    print(f'total {len(ls)} possibilities')  # < 2e3
    ls.sort()
    pprint(ls[:10])
    return ls[0][0]
    # return min((f(i), i) for i in range(a, b+1))[1]


def main2(values) -> int:
    values.sort()
    a = values[0]   # min
    b = values[-1]  # max

    def f(pos):
        def g(x):
            return x * (x+1) // 2
        return sum(g(abs(pos - x)) for x in values)

    ls = [(f(i), i) for i in range(a-1, b+2)]
    print(f'total {len(ls)} possibilities')  # < 2e3
    ls.sort()
    pprint(ls[:5])
    return ls[0][0]


EXAMPLE_IN = io.StringIO("16,1,2,0,4,2,7,1,2,14\n")

if __name__ == '__main__':
    USE_EXAMPLE_IN = False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('7-input', 'r') as f:
        inp_values = f.read().strip().split(',')
        inp_values = [int(x) for x in inp_values]
    print(f'{len(inp_values)} values')

    answ = main1(inp_values[:])
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:  344735 fuel
    # 336 - position

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
