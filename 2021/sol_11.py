#!/usr/bin/env python3
# 2021-12-11

import copy
import io
import sys
from pprint import pprint


def sim_step(grid):
    W = len(grid)
    assert W == len(grid[0])  # square
    flashed = [[False] * W for _ in range(W)]

    # 1. Increment every octopus
    for i in range(W):
        for j in range(W):
            grid[i][j] += 1

    # 2. Any with E > 9 flashes
    q = []
    # Starting
    for i in range(W):
        for j in range(W):
            if grid[i][j] > 9:
                q.append((i, j))

    def visit(i, j):
        if flashed[i][j] is True:
            return
        flashed[i][j] = True
        # Setting 0 in 3)

        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                if i + x < 0 or j + y < 0:
                    continue
                if i + x >= W or j + y >= W:
                    continue
                # All adjacent by 1
                grid[i + x][j + y] += 1
                if grid[i + x][j + y] > 9:
                    q.append((i + x, j + y))
    while len(q) > 0:
        c = q.pop(0)
        visit(*c)

    # 3. Zero each flashed cell
    num_flashes = 0
    for i in range(W):
        for j in range(W):
            if flashed[i][j]:
                grid[i][j] = 0
                num_flashes += 1
    return grid, num_flashes


def main1(grid) -> int:
    r = 0
    for _ in range(100):
        grid, num_fl = sim_step(grid)
        # print(num_fl, 'flashes')
        # pprint(grid)
        r += num_fl
    return r


def main2(grid, maxsteps=100) -> int:
    for i in range(1, maxsteps + 1):
        grid, num_fl = sim_step(grid)
        if num_fl == 100:
            return i
    return 10 * maxsteps


EXAMPLE_1 = """11111
19991
19191
19991
11111
"""

EXAMPLE_2 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

EXAMPLE_IN = io.StringIO(EXAMPLE_2)

if __name__ == '__main__':
    USE_EXAMPLE_IN = 'ex' in sys.argv  # False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('11-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [[int(y) for y in x] for x in inp_values]
    print(f'{len(inp_values)} by {len(inp_values[0])} grid')

    answ = main1(copy.deepcopy(inp_values))
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 1785

    answ2 = main2(inp_values, 20000)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input: 354
