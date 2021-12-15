#!/usr/bin/env python3
# 2021-12-15

import io
import heapq
import sys
from pprint import pprint


def main1(values, do_path=False) -> int:
    N = len(values)

    # 'inf' is always greater than any integer
    known_min = [[float('inf')] * N for _ in range(N)]
    if do_path:
        vis_before = [[None] * N for _ in range(N)]

    q = [(0, 0, 0, (0, 0))]  # dist, y, x

    while len(q) > 0:  # Dijkstra
        plen, r, c, prev = heapq.heappop(q)
        if known_min[r][c] <= plen:  # No upgrade
            continue
        # print(f'Visiting {r,c} with {plen}')
        # cur_risk = values[r][c]

        known_min[r][c] = plen
        if do_path:
            vis_before[r][c] = prev

        if r == N - 1 and c == N - 1:
            break

        for ny, nx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if not (0 <= r + ny < N and 0 <= c + nx < N):
                continue

            next_risk = values[r + ny][c + nx]
            if plen + next_risk < known_min[r + ny][c + nx]:
                heapq.heappush(q,
                               (plen + next_risk, r + ny, c + nx, (r, c)))

    if do_path:
        path = []
        node = (N - 1, None - 1)
        while node != (0, 0):
            path.append(node)
            node = vis_before[node[0]][node[1]]
        if len(path) < 22:
            print('Best path:')
            pprint(path)
        path.append((0, 0))  # loop!
        # pprint(path[::-1])

    return known_min[N - 1][N - 1]


def main2(values):
    N = len(values)
    assert N == len(values[0])
    fullmap = [[None] * 5 * N for _ in range(5 * N)]

    for x in range(N):
        for y in range(N):
            fullmap[y][x] = values[y][x]

    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                continue
            sq_j = j - 1 if j > 0 else 0
            sq_i = i - 1 if i > 0 else 0
            if j >= 1 and i >= 1:
                sq_j = j        # to the left or to the right
            for x in range(N):
                for y in range(N):
                    v = fullmap[N * sq_j + y][N * sq_i + x]
                    v += 1
                    if v > 9:
                        v = 1
                    fullmap[N * j + y][N * i + x] = v
    print(f'full map {len(fullmap)} by {len(fullmap[0])}')
    # for row in fullmap:
    #     print(*row, sep='')
    return fullmap


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
    print(f'{len(inp_values)} by {len(inp_values[0])} rectangle')

    answ = main1(inp_values, True)
    print(f'\x1b[32;1mAnswer1: {answ} \x1b[0m')
    # Correct answer for my input: 811

    fullmap = main2(inp_values)
    answ2 = main1(fullmap)
    print(f'\x1b[32;1mAnswer2: {answ2} \x1b[0m')
    # Correct answer for my input: 3012
