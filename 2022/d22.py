import numpy as np
try:
    from rich.pretty import pprint
except ImportError:
    from pprint import pprint

# https://adventofcode.com/2022/day/22 - Monkey Map
EXAMPLE = """
e       ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


def parse_moves(moves_str: str) -> list:
    num = ''
    r = []
    for char in moves_str:
        if char.isdigit():
            num += char
        else:
            assert char in 'LR'
            num = int(num)
            r.append(num)
            r.append(char)
            num = ''
    # assert num == ''
    if num:
        r.append(int(num))
    return r


def find_start(board: np.ndarray) -> tuple[int, int]:
    H, W = board.shape
    start = None
    for row in range(H):
        for col in range(W):
            if board[row, col] == 1:
                return row, col
    return ...


def next_pos_common(board, current, dir):
    cr, cc = current
    if dir == 0:  # >
        nextpos = cr, cc+1
        v = np.array([0, 1])
    elif dir == 1:  # \/
        nextpos = cr+1, cc
        v = np.array([1, 0])
    elif dir == 2:  # <
        nextpos = cr, cc-1
        v = np.array([0, -1])
    elif dir == 3:  # ^
        nextpos = cr-1, cc
        v = np.array([-1, 0])

    try:
        if board[nextpos] == 1:
            return v, (nextpos, dir)
        elif board[nextpos] == 2:
            return v, 'wall'
    except IndexError:
        ...
    return v, None


def next_pos_on_map(board, current, dir):
    v, ret = next_pos_common(board, current, dir)
    if ret is not None:
        return ret
    cr, cc = current

    pos = np.array([cr, cc])
    v = -v  # opposite direction
    valid = True
    lastok = pos
    while valid:
        pos += v
        try:
            if pos[0] < 0 or pos[0] > board.shape[0]:
                break
            if pos[1] < 0 or pos[1] > board.shape[1]:
                break
            if board[pos[0], pos[1]] in (1, 2):
                lastok = pos.copy()
                continue
        except IndexError:
            ...
        valid = False
    return (lastok[0], lastok[1]), dir


# hard-coded mapping that I computed with pen and paper
EXAMPLE_LUT = {
    (0, 2, 2): (1, lambda r, c: (4, 8 + (r - 4))),
    (1, 1, 3): (2, lambda r, c: (4 - (8 - c), 8)),

    (1, 2, 0): (1, lambda r, c: (8, 12 + (7 - r))),
    (2, 3, 3): (2, lambda r, c: (7 - (c - 11), 11)),

    (2, 2, 1): (3, lambda r, c: (7, 3 - (c - 8))),
    # ...
}
MY_INPUT_LUT = {
    (0, 1, 2): (0, lambda r, c: (100 + (49 - r), 0)),
    (2, 0, 2): (0, lambda r, c: (49 - (r - 100), 50)),

    (0, 1, 3): (0, lambda r, c: (150 + (c - 50), 0)),
    (3, 0, 2): (1, lambda r, c: (0, 50 + (r - 150))),

    (1, 1, 0): (3, lambda r, c: (49, 100 + (r - 50))),
    (0, 2, 1): (2, lambda r, c: (50 + (c - 100), 99)),

    (0, 2, 3): (3, lambda r, c: (199, c - 100)),
    (3, 0, 1): (1, lambda r, c: (0, c + 100)),

    (0, 2, 0): (2, lambda r, c: (100 + (49 - r), 99)),
    (2, 1, 0): (2, lambda r, c: (49 - (r - 100), 149)),

    (2, 0, 3): (0, lambda r, c: (99 - (49 - c), 50)),
    (1, 1, 2): (1, lambda r, c: (100, 49 - (99 - r))),

    (3, 0, 0): (3, lambda r, c: (149, 50 + (r - 150))),
    (2, 1, 1): (2, lambda r, c: (150 + (c - 50), 49)),
}
cube_lookup = None
cube_side = None


def prepare_cube_lookup(board: np.ndarray, side):
    global cube_lookup, cube_side
    bmap_h = board.shape[0] / side
    bmap_w = board.shape[1] / side
    assert bmap_h.is_integer()
    assert bmap_w.is_integer()
    bmap_h = int(bmap_h)
    bmap_w = int(bmap_w)

    # bmap = np.zeros((bmap_h, bmap_w))
    # for i in range(bmap_h):
    #     for j in range(bmap_w):
    #         if (board[side*i: side*i+side, side*j: side*j+side] != 0).any():
    #             bmap[i, j] = 1
    cube_side = side
    if side == 4:
        cube_lookup = EXAMPLE_LUT
    else:
        cube_lookup = MY_INPUT_LUT


def next_pos_cube(board, current, dir):
    v, ret = next_pos_common(board, current, dir)
    if ret:
        return ret
    cr, cc = current

    sider = (cr // cube_side) + ((cr % cube_side) // cube_side)
    sidec = (cc // cube_side) + ((cc % cube_side) // cube_side)
    # print(f'cur-row: {cr:3} side-row: {sider}')
    # print(f'cur-col: {cc:3} side-col: {sidec}')

    newd, func = cube_lookup[sider, sidec, dir]
    nr, nc = func(cr, cc)

    if board[nr, nc] == 2:
        return 'wall'
    else:
        return (nr, nc), newd


def solve(board: np.ndarray, moves: list[str | int], next_pos_func):
    start = find_start(board)
    print('start:', start)
    r, c = start
    dir = 0  # right=0 down left up
    for move in moves:
        if move == 'L':
            dir = (dir - 1) % 4
        elif move == 'R':
            dir = (dir + 1) % 4
        else:
            for j in range(move):
                nextmove = next_pos_func(board, (r, c), dir)
                if nextmove == 'wall' and j == 0:
                    break
                elif nextmove == 'wall':
                    break
                if board[nextmove[0]] == 0:
                    print('!!!', (r, c), dir)
                    print('to:', nextmove[0], nextmove[1])
                (r, c), dir = nextmove
                # assert board[r, c] != 0
    return r, c, dir


if __name__ == '__main__':
    inp = open('input/in22.txt').read()
    # inp = EXAMPLE
    board, moves = inp.replace('\r\n', '\n').split('\n\n')
    board = board.rstrip().splitlines()
    board = [ln for ln in board if ln.strip()]
    moves = parse_moves(moves.strip())

    if len(board) < 20:
        pprint(board)
        pprint(moves)

    H = len(board)
    W = max(len(x) for x in board)
    brd = np.zeros((H, W), dtype=np.uint8)
    for row in range(H):
        for col in range(W):
            try:
                if board[row][col] == '.':
                    brd[row, col] = 1
                elif board[row][col] == '#':
                    brd[row, col] = 2
            except IndexError:
                continue

    # pprint(brd)
    # import matplotlib.pyplot as plt
    # plt.imshow(brd)
    # plt.savefig('dbg22.png')
    # plt.show()

    print('shape', brd.shape)
    r, c, d = solve(brd, moves, next_pos_on_map)
    print('end', r, c, d)
    r += 1
    c += 1
    print('part1:', 1000*r + 4*c + d)

    print('\n')
    prepare_cube_lookup(brd, 4 if inp.lstrip()[0] == 'e' else 50)
    if inp == EXAMPLE:
        # A to B
        assert next_pos_cube(brd, (5, 11), 0) == ((8, 14), 1)
        # C to D
        print(next_pos_cube(brd, (11, 10), 1))
        assert next_pos_cube(brd, (11, 10), 1) == ((7, 1), 3)
    r, c, d = solve(brd, moves, next_pos_cube)
    print('end', r, c, d)
    r += 1
    c += 1
    print('part2:', 1000*r + 4*c + d)
