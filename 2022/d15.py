import re
# from tqdm import tqdm


def solve1(inp: list[tuple[int]], y=2_000_000):
    print(f'{y=}')
    disallowed = set()
    r = 0
    for a, b, c, d in inp:
        # No other beacon in distance `dist`
        dist = abs(a-c) + abs(b-d)
        # vertical distance to the row
        dist -= abs(b-y)
        # Solve |x - a| <= dist
        for i in range(a - dist, a + dist + 1):
            disallowed.add(i)
    for a, b, c, d in inp:
        if b == y and a in disallowed:
            disallowed.remove(a)
        if d == y and c in disallowed:
            disallowed.remove(c)
    r = len(disallowed)
    print('part1:', r)


def solve2_brute(inp: list[tuple[int]], limit=4_000_000) -> tuple[int, int]:
    assert limit <= 20
    for x in range(0, 21):
        for y in range(0, 21):
            ok = True
            for a, b, c, d in inp:
                if (x, y) == (a, b) or (x, y) == (c, d):
                    ok = False
                    continue
                dist = abs(a-c) + abs(b-d)
                dist -= abs(b-y)
                # |x - a| <= dist
                if a - dist <= x <= a + dist:
                    ok = False
                    continue
            if ok:
                print('coords', x, y)
                return x, y


def solve2(inp: list[tuple[int]], limit=4_000_000) -> tuple[int, int]:
    min_dist = min((abs(a-c) + abs(b-d)) for a, b, c, d in inp)
    max_dist = max((abs(a-c) + abs(b-d)) for a, b, c, d in inp)
    print('dbg, smallest dist is', min_dist)  # > 1e5
    print('dbg,  largest dist is', max_dist)  # < 2e6
    sdist = sum(
        4*(abs(a-c) + abs(b-d) + 1)
        for a, b, c, d in inp
    )
    print('dbg, length of all borders is', f'{sdist:_}')  # 74_597_904
    # Let's check borders only

    def chk(X: int, Y: int) -> bool:
        if X < 0 or Y < 0:
            return False
        elif X > 4e6 or Y > 4e6:  # >= limit
            return False
        for a, b, c, d in inp:
            if (X, Y) == (a, b):
                return False
            if (X, Y) == (c, d):
                return False
            dist = abs(a-c) + abs(b-d)
            # (X,Y) in reach?
            dist -= abs(b-Y)
            if a - dist <= X <= a + dist:
                return False

        print(f'POINT {X} {Y}')
        return True

    # for a, b, c, d in tqdm(inp):
    for a, b, c, d in inp[2:3]:
        # "Manhattan circle"
        radius = (abs(a-c) + abs(b-d) + 1)
        for dx in range(0, radius+1):
            dy = radius - dx
            assert dx + dy == radius  # def. of a circle
            if chk(a+dx, b+dy):
                return a+dx, b+dy
            if chk(a-dx, b+dy):
                return a-dx, b+dy
            if chk(a+dx, b-dy):
                return a+dx, b-dy
            if chk(a-dx, b-dy):
                return a-dx, b-dy


REGEX = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): '
                   r'closest beacon is at x=(-?\d+), y=(-?\d+)')


def parse_input_line(line: str) -> tuple[int]:
    m = REGEX.match(line)
    return tuple(int(x) for x in m.groups())


if __name__ == '__main__':
    # fmt: off
    inp = open('input/in15.txt').read()
    y = 2_000_000
    # inp = EXAMPLE; y = 10
    # fmt: on
    inp = [parse_input_line(x) for x in inp.splitlines()]
    print(f'{len(inp)} sensors')  # and less beacons
    solve1(inp, y=y)

    x, y = solve2(inp, 20 if y == 10 else 4_000_000)
    print('part2:', x * 4_000_000 + y)
    try:
        x, y = solve2_brute(inp, 20 if y == 10 else 4_000_000)
        print('part2:', x * 4_000_000 + y)
    except AssertionError:
        ...

    # import matplotlib.pyplot as plt
    # plt.style.use('ggplot')
    # fig, ax = plt.subplots()
    # ax.scatter([a for a, b, c, d in inp],
    #            [b for a, b, c, d in inp], marker='o')
    # ax.scatter([c for a, b, c, d in inp],
    #            [d for a, b, c, d in inp], marker='^')
    # # lines S-to-nearest-B
    # for a, b, c, d in inp:
    #     ax.plot([a, c], [b, d], color='black', linestyle='dashed')
    # plt.show()
