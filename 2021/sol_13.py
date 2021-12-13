#!/usr/bin/env python3
# 2021-12-13

import io
import sys
from pprint import pprint


def main1(dots, fold1) -> int:
    "How many dots are visible after completing"
    "just the first fold instruction on your transparent paper?"
    MAXX = 100
    MAXY=100
    before = [[0]*MAXX for _ in range(MAXY)]
    for x,y in dots:
        before[y][x] = 1

    if fold1[0] == 'x':
        after = [[]]
    elif fold1[0]=='y':
        after = []
    else:
        raise ValueError(fold1)
    return sum(sum(x) for x in after)


def main2(values) -> int:
    return


EXAMPLE_IN = io.StringIO("""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""")

if __name__ == '__main__':
    USE_EXAMPLE_IN = 'ex' in sys.argv
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('-input', 'r') as f:
        inp_dots, inp_folds = f.read().replace('\r\n','\n').split('\n\n')
        inp_dots = [x.split(',') for x in inp_dots.splitlines()]
        inp_folds = [x[11:] for x in inp_folds.split()]
    # print(f'{len(inp_values)} lines')
    print(len(inp_dots), len(inp_folds))

    answ = main1(inp_dots, inp_folds[0])
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
