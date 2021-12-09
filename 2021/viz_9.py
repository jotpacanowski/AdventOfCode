#!/usr/bin/env python3
# 2021-12-09

import io
import random
from pprint import pprint

from PIL import Image, ImageColor

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


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


# 2D height map
def viz_height(values, ls, basin_id, basin_sz):
    "Vizualize simple heightmap"
    def c(x, y):
        # TODO: HSV colors / as in heatmap
        c = values[y][x] / 9  # [0..9] -> [0..1]
        c = 20 + int((1 - c) * 235)

        if values[y][x] == 9:
            return (0, 0, 0)
        elif (y, x) in ls:
            return (255, 255, 255)
        else:
            return (c, c, c // 2)
    return c


def viz_basins(values, ls, basin_id, basin_sz):
    "Color each basin"
    colors = [5 * random.randint(0, 360 // 5) for _ in range(len(basin_sz))]

    def c(x, y):
        c = basin_id[y][x]

        if values[y][x] == 9:
            return 'black'
        elif (y, x) in ls:
            # return 'white'
            return f'hsv({colors[c]}, 40%, 100%)'  # lighter color
        else:
            return f'hsv({colors[c]}, 80%, 100%)'
    return c


VIZ_FUNCS_2D = [viz_height, viz_basins]


def viz_main(values, ls, fn):
    H = len(values)
    W = len(values[0])
    visited = [[-1] * W for _ in range(H)]
    basin_sz = []
    basin_id = 0

    def dfs(row, col):
        nonlocal basin_id
        nonlocal basin_sz
        if visited[row][col] != -1:
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
        basin_sz.append(0)
        dfs(r, c)
        basin_id += 1

    for func in VIZ_FUNCS_2D:
        print(f'Vizualizing func {func.__name__}')
        hm = Image.new('RGB', (W, H))
        getcol = func(values, ls, visited, basin_sz)
        for x in range(W):
            for y in range(H):
                col_ = getcol(x, y)
                if type(col_) is tuple:
                    hm.putpixel((x, y), col_)
                elif type(col_) is str:
                    hm.putpixel((x, y), ImageColor.getrgb(col_))
                else:
                    raise 'wtf'

        FN = f'vizualize-9-{fn} {func.__name__}.png'
        print('Saving', FN)
        hm = hm.resize((4 * W, 4 * H), Image.NEAREST)
        hm.save(FN)

    print('\n3D matplotlib')

    # [[x**2 + y**2 for x in range(20)] for y in range(20)])
    z = np.array([[values[y][x] for x in range(W)] for y in range(H)], dtype='float32')
    z /= 9.0
    # z = np.log10(1 + z) * 2

    # x, y = np.meshgrid(range(z.shape[0]), range(z.shape[1]))
    x = np.arange(0, W, 1)
    y = np.arange(0, H, 1)
    x, y = np.meshgrid(x, y)

# https://stackoverflow.com/questions/30706919/how-to-create-a-3d-height-map-in-python
    # show hight map in 3d
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z,
                    cmap=cm.coolwarm, linewidth=0, antialiased=False,
                    cstride=1, rstride=1)
    ax.set_zlim(0.0, 1.5)
    plt.title('3d map of the ocean floor')
    plt.show()

    # show hight map in 2d
    # plt.figure()
    # plt.title('z as 2d heat map')
    # p = plt.imshow(z)
    # plt.colorbar(p)
    # plt.show()


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
    print('There are\x1b[32m', len(ls), '\x1b[0mlowest points / basins')

    sys.setrecursionlimit(100)

    viz_main(inp_values, ls, 'ex' if USE_EXAMPLE_IN else 'jp')
