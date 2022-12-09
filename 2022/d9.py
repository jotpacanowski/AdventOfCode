import math
try:
    from rich.pretty import pprint
except ImportError:
    from pprint import pprint  # type: ignore [assignment]


def are_touching(head, tail) -> bool:
    """Chebyshev distance <= 1"""
    hx, hy = head
    tx, ty = tail
    return max(
        abs(hx-tx),
        abs(hy-ty)
    ) <= 1


def move_head(head, dir):
    hx, hy = head
    match dir:
        case 'U':
            return (hx, hy+1)
        case 'D':
            return (hx, hy-1)
        case 'L':
            return (hx-1, hy)
        case 'R':
            return (hx+1, hy)
    return None, None


def move_tail(head, tail) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail
    if hx == tx and hy == ty:  # overlap
        return head
    elif are_touching(head, tail):
        return tail
    # else, tail is at least 2 tiles away

    # vector towards H
    dx = hx - tx
    dy = hy - ty

    if hx == tx:
        return tx, ty + int(math.copysign(1, dy))
    elif hy == ty:
        return tx + int(math.copysign(1, dx)), ty
    else:
        # diagonal
        return (
            tx + int(math.copysign(1, dx)),
            ty + int(math.copysign(1, dy))
        )


def solve1(moves: list[tuple[str, int]]):
    pos_once = set()
    pos_twice = set()
    head = (0, 0)
    tail = (0, 0)
    for mdir, mcount in moves:
        for _ in range(mcount):
            head = move_head(head, mdir)
            tail = move_tail(head, tail)
            # print('')
            # for j in range(0, 6):
            #     for i in range(0, 6):
            #         if head == (i, 5-j):
            #             print('H', end='')
            #         elif tail == (i, 5-j):
            #             print('T', end='')
            #         else:
            #             print('.', end='')
            #     print('')
            # print('')

            if tail not in pos_once:
                pos_once.add(tail)
            else:
                pos_twice.add(tail)

    # pprint(pos_twice)
    # print('')
    # for j in range(0, 6):
    #     for i in range(0, 6):
    #         # if (i, 5-j) in pos_twice:
    #         if (i, 5-j) in pos_once:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print('')
    # print('')
    print('part1:', len(pos_once))


def solve2(moves: list[tuple[str, int]]):
    pos_once = set()
    rope = [
        (0, 0)
        for _ in range(10)
    ]
    for mdir, mcount in moves:
        for _ in range(mcount):
            rope[0] = move_head(rope[0], mdir)
            for i in range(1, 10):
                rope[i] = move_tail(rope[i-1], rope[i])

            if rope[-1] not in pos_once:
                pos_once.add(rope[-1])

        # print('')
        # for j in range(0, 6):
        #     for i in range(0, 6):
        #         if head == (i, 5-j):
        #             print('H', end='')
        #         elif tail == (i, 5-j):
        #             print('T', end='')
        #         else:
        #             print('.', end='')
        #     print('')
        # print('')

    print('part2:', len(pos_once))


TEST = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

TEST2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

if __name__ == '__main__':
    lines: str = open('input/in9.txt').read()
    # lines = TEST2
    moves = list(map(lambda ln:
                     (ln.split(' ', 1)[0],
                      int(ln.split(' ', 1)[1])),
                     lines.splitlines()))
    pprint(moves[:18])

    solve1(moves)
    solve2(moves)
