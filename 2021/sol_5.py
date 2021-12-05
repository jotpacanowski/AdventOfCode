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


def diagram(list_lines, diagonal=False):
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
            if not diagonal:
                continue
            if abs(b[0] - a[0]) != abs(b[1] - a[1]):
                raise ValueError(f'Not a 45* line: {a} to {b}')

            dir_ = [(b[i] - a[i]) // abs(b[i] - a[i]) for i in range(2)]
            assert sum(abs(x) for x in dir_) == 2

            for i in range(0, abs(a[0] - b[0])+1):
                area[a[0] + i*dir_[0]][a[1] + i*dir_[1]] += 1

    return list(zip(*area))  # transpose


def pprint_diagram(list_lines, b):
    area = diagram(list_lines, b)
    for ln in area:
        print(*(str(min(9, x)) if x > 0 else '.' for x in ln), sep='')


def main1(list_lines) -> int:
    """determine the number of points where at least two lines overlap"""
    area = diagram(list_lines)
    return sum(1 for ln in area for x in ln if x > 1)


def main2(list_lines) -> int:
    area = diagram(list_lines, diagonal=True)
    return sum(1 for ln in area for x in ln if x > 1)


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
    USE_EXAMPLE_IN = False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('5-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [
            [tuple(map(int, y.split(','))) for y in x.partition(' -> ')[::2]]
            for x in inp_values]
    print(f'{len(inp_values)} lines')
    # pprint(inp_values)
    max_coord = 1 + max(max(max(*x) for x in ln) for ln in inp_values)
    if max_coord <= 30:
        print('  diagram:\n')
        pprint_diagram(inp_values, True)
        print('')
    else:
        print(f'Max coordinate: {max_coord}')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
