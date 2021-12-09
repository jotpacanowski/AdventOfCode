#!/usr/bin/env python3
# 2021-12-09

import io
import random
from pprint import pprint

from PIL import Image


def lowest_points(values: list[list[int]]) -> list[tuple[int, int]]:
    # nines = 0
    for row in range(len(values)):
        for col in range(len(values[0])):
            if values[row][col] == 9:
                # nines += 1
                continue

            if row - 1 >= 0:
                if values[row][col] > values[row - 1][col]:
                    continue
            if col - 1 >= 0:
                if values[row][col] > values[row][col - 1]:
                    continue
            if col + 1 < len(values[0]):
                if values[row][col] > values[row][col + 1]:
                    continue
            if row + 1 < len(values):
                if values[row][col] > values[row + 1][col]:
                    continue

            yield row, col
    # print(f'{nines=}')


EXAMPLE_IN = io.StringIO("""2199943210
3987894921
9856789892
8767896789
9899965678
""")


def viz_main(values, ls, fn):
    H = len(values)
    W = len(values[0])
    visited = [[-1] * W for _ in range(H)]
    basin_sz = []
    basin_id = 0

    def dfs(row, col):
        nonlocal basin_id
        nonlocal basin_sz
        if visited[row][col] == -1:
            return
        visited[row][col] = basin_id
        basin_sz[basin_id] += 1
        if row > 0 and values[row - 1][col] != 9:
            dfs(row - 1, col)
        if col > 0 and values[row][col - 1] != 9:
            dfs(row, col - 1)
        if row + 1 < H and values[row + 1][col] != 9:
            dfs(row + 1, col)
        if col + 1 < W and values[row][col + 1] != 9:
            dfs(row, col + 1)

    for r, c in ls:
        # basin_id = len(basin_sz)
        basin_sz.append(0)
        dfs(r, c)
        basin_id += 1
    # basin_sz.sort(reverse=True)

    def random_color():
        return random.randint(40, 250), random.randint(40, 250), random.randint(40, 250)
    colors = [random_color() for _ in range(len(basin_sz))]

    print(set(colors))

    # HEIGHT_COLS = [
    #     ()
    # ]

    # 2D height map
    hm = Image.new('RGB', (W, H))
    for x in range(W):
        for y in range(H):
            c = values[y][x] / 9  # [0..9] -> [0..1]
            c = 20 + int((1 - c) * 235)

            if values[y][x] == 9:
                hm.putpixel((x, y), (0, 0, 0))
            elif (y,x) in ls:
                hm.putpixel((x, y), (255, 255, 255))
            else:
                hm.putpixel((x, y), (c, c, c//2))
            # if values[y][x] == 9:
            #     hm.putpixel((x, y), (255, 255, 255))
            # else:
            #     hm.putpixel((x, y), colors[visited[y][x]])
    print('Saving', f'vizualize-9-{fn}.png')
    # hm = hm.resize((4 * W, 4 * H), Image.NEAREST)
    hm.save(f'vizualize-9-{fn}.png')


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

    sys.setrecursionlimit(100)

    viz_main(inp_values, ls, 'ex' if USE_EXAMPLE_IN else 'jp')
