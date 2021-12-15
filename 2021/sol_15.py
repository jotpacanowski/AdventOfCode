#!/usr/bin/env python3
# 2021-12-15

import io
import heapq
import sys
from pprint import pprint


def main1(values) -> int:
    W = len(values[0])  # Note: square
    H = len(values)
    row = [0] * W

    # First row:
    for i in range(W):
        pass  # if values[0][i]

    # visited = {k: 0 for k in G.keys()}
    known_min = [[0xffffffff] * W for _ in range(H)]
    known_min[0][0] = 0

    q = [(0, 0, 0)]  # dist, y, x
    # print(len(q))
    while len(q) > 0:  # Dijkstra
        plen, r, c = heapq.heappop(0)
        # print(f'Visiting {r,c} with {plen}')
        if known_min[r][c] < plen:
            continue

        # print(len(q))
        known_min[r][c] = plen

        for ny, nx in {(0, -1), (0, 1), (-1, 0), (1, 0)}:
            breakpoint
            if not (0 <= r + ny < H and 0 <= c + nx < W):
                continue

            q.append((plen + values[r][c], r + ny, c + nx))

    return known_min[-1][-1]

    # def dfs_visit(node, plen):
    #     r, c = node
    #     if node == (H - 1, W - 1):
    #         # stack.append('end')
    #         # if display:
    #         #     print('New path: ', '-'.join(stack))
    #         # stack.pop()
    #         known_min[node[0]][node[1]] = min(
    #             known_min[node[0]][node[1]], plen)
    #     stack.append(node)

    #         dfs_visit((r + ny, c + nx), plen + )

    #         if neigh.islower() and neigh not in stack:
    #             dfs_visit(neigh)
    #         elif neigh.isupper():
    #             dfs_visit(neigh)
    #         else:
    #             pass  # raise ValueError(f'node name {node!r}')
    #     stack.pop()

    # dfs_visit('start')
    # return total_paths


def main2(values) -> int:
    return


EXAMPLE_IN = io.StringIO("""1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""")

if __name__ == '__main__':
    USE_EXAMPLE_IN = 'ex' in sys.argv
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('15-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [[int(y) for y in x] for x in inp_values]
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
