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
    if ret:
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
