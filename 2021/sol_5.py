#!/usr/bin/env python3
# 2021-12-05
# AoC 2021 Day 5: Hydrothermal Venture

import io
from pprint import pprint


def coord_range(s, t):
    if s <= t:
        return range(s, t+1)
    else:
        return range(t, s+1)


def diagram(list_lines):
    max_x = 1 + max(max(x[0] for x in ln) for ln in list_lines)
    max_y = 1 + max(max(x[1] for x in ln) for ln in list_lines)
    area = [[0] * max_x for _ in range(max_y)]
    for a, b in list_lines:
        if a[0] == b[0]:    # equal X
            # print('H line x=', a[0], 'y', coord_range(a[1], b[1]+1))
            for y in coord_range(a[1], b[1]):
                area[a[0]][y] += 1
        elif a[1] == b[1]:  # equal Y
            # print('V line y=', a[1], 'x', coord_range(a[0], b[0]+1))
            for x in coord_range(a[0], b[0]):
                area[x][a[1]] += 1
        else:
            pass  # not horizontal / vertical
    return list(zip(*area))  # transpose


def pprint_diagram(list_lines):
    area = diagram(list_lines)
    for ln in area:
        print(*(str(min(9, x)) if x>0 else '.' for x in ln), sep='')


def main1(values) -> int:
    """determine the number of points where at least two lines overlap"""
    pass


def main2(values) -> int:
    return


EXAMPLE_IN = io.StringIO("""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""")

if __name__ == '__main__':
    USE_EXAMPLE_IN = True
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('5-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [
            [tuple(map(int, y.split(','))) for y in x.partition(' -> ')[::2]]
            for x in inp_values]
    print(f'{len(inp_values)} lines')
    # pprint(inp_values)
    if len(inp_values) < 30:  # TODO: Use min/max
        pprint_diagram(inp_values)

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
