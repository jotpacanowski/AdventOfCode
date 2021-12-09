#!/usr/bin/env python3
# 2021-12-09

import io
from pprint import pprint


def lowest_points(values):
    nines = 0
    for row in range(len(values)):
        for col in range(len(values[0])):
            is_min = True

            if row - 1 >= 0:
                if values[row][col] > values[row - 1][col]:
                    is_min = False
                    continue
            if col - 1 >= 0:
                if values[row][col] > values[row][col - 1]:
                    is_min = False
                    continue
            if col + 1 < len(values[0]):
                if values[row][col] > values[row][col + 1]:
                    is_min = False
                    continue
            if row + 1 < len(values):
                if values[row][col] > values[row + 1][col]:
                    is_min = False
                    continue

            if values[row][col] == 9:
                nines += 1
                continue
            if is_min:
                yield row, col
    print(f'{nines=}')


def main1(values) -> int:
    return sum(1 + values[r][c] for r, c in lowest_points(values))


def main2(values, ls) -> int:
    visited = [[0] * len(values[0]) for _ in range(len(values))]
    basin_sz = []

    def dfs(basin_id, row, col):
        if visited[row][col] == 1:
            return
        visited[row][col] = 1
        basin_sz[basin_id] += 1
        if row > 0 and values[row - 1][col] != 9:
            dfs(basin_id, row - 1, col)
        if col > 0 and values[row][col - 1] != 9:
            dfs(basin_id, row, col - 1)
        if row + 1 < len(values) and values[row + 1][col] != 9:
            dfs(basin_id, row + 1, col)
        if col + 1 < len(values[0]) and values[row][col + 1] != 9:
            dfs(basin_id, row, col + 1)

    for r, c in ls:
        basin_id = len(basin_sz)
        basin_sz.append(0)
        dfs(basin_id, r, c)

    basin_sz.sort(reverse=True)
    return basin_sz[0] * basin_sz[1] * basin_sz[2]


EXAMPLE_IN = io.StringIO("""2199943210
3987894921
9856789892
8767896789
9899965678
""")

if __name__ == '__main__':
    import sys
    USE_EXAMPLE_IN = 'ex' in sys.argv
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('9-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [[int(y) for y in x] for x in inp_values]
    print(f'{len(inp_values)} lines, {len(inp_values[0])} columns each')

    ls = list(lowest_points(inp_values))
    print('There are', len(ls), 'lowest points')
    # print(set(inp_values[i][j] for i, j in ls))
    # pprint(ls)
    # print(*(inp_values[i][j] for i,j in ls), sep=' ')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 545

    sys.setrecursionlimit(100)

    answ2 = main2(inp_values, ls)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input: 950600
