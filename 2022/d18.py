from itertools import product


def cube_set_area(cubes: list[tuple[int, int, int]]) -> int:
    cubset = set(cubes)
    assert len(cubset) == len(cubes)
    r = 0
    for c in cubes:
        x, y, z = c
        incr = 6
        if (x+1, y, z) in cubset:
            incr -= 1
        if (x-1, y, z) in cubset:
            incr -= 1
        if (x, y+1, z) in cubset:
            incr -= 1
        if (x, y-1, z) in cubset:
            incr -= 1
        if (x, y, z+1) in cubset:
            incr -= 1
        if (x, y, z-1) in cubset:
            incr -= 1
        r += incr
    assert r % 2 == 0  # convex
    return r


def solve1(cubes: list[tuple[int, int, int]]) -> int:
    r = cube_set_area(cubes)
    print('part1:', r)
    return r


def solve2(cubes: list[tuple[int, int, int]]):
    visited = set()
    q = [(0, 0, 0)]
    while q:
        cur = q.pop(0)
        visited.add(cur)

        def try_visit(n):
            if n in cubes or n in visited or n in q:
                return
            for xyz in n:
                if xyz < -1 or xyz > 24:
                    return
            q.append(n)

        x, y, z = cur
        try_visit((x+1, y, z))
        try_visit((x-1, y, z))
        try_visit((x, y+1, z))
        try_visit((x, y-1, z))
        try_visit((x, y, z+1))
        try_visit((x, y, z-1))
    print('exterior: ', len(visited))
    interior = set()
    for test in product(range(22), repeat=3):
        if test not in cubes and test not in visited:
            interior.add(test)
    print('interior: ', len(interior))
    print('interior area: ', cube_set_area(interior))
    r = cube_set_area(cubes) - cube_set_area(interior)
    print('part2:', r)


if __name__ == '__main__':
    inp = open('input/in18.txt').read()
    # inp = EXAMPLE
    # inp = "1,1,1\n1,1,2"
    inp = [tuple(map(int, x.split(','))) for x in inp.splitlines()]
    a, b = min(x for x, y, z in inp), max(x for x, y, z in inp)
    print(f'x range: {a:3} .. {b:3}')
    a, b = min(y for x, y, z in inp), max(y for x, y, z in inp)
    print(f'y range: {a:3} .. {b:3}')
    a, b = min(z for x, y, z in inp), max(z for x, y, z in inp)
    print(f'z range: {a:3} .. {b:3}')

    solve1(inp)
    solve2(inp)

    # import numpy as np
    # import matplotlib.pyplot as plt
    # blank = np.zeros((22, 22), np.uint8)
    # for i in range(0, 22):
    #     frame = np.zeros_like(blank)
    #     for x, y, z in inp:
    #         if z != i:
    #             continue
    #         frame[x, y] = 1
    #     plt.imshow(frame)
    #     plt.savefig(f'viz-18-{i}.png')
