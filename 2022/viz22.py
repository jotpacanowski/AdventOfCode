from datetime import datetime as dt

import numpy as np
from d22 import *

try:
    from rich.pretty import pprint
except ImportError:
    from pprint import pprint

import matplotlib.animation as animation
import matplotlib.pyplot as plt


def solve_ani(board: np.ndarray, moves: list[str | int], next_pos_func, title: str):
    start = find_start(board)
    r, c = start
    dir = 0  # right=0 down left up
    snake = []
    snake.append((r, c))
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
                if board[nextmove[0]] == 2:
                    print('!W!', (r, c), dir)
                    print('to:', nextmove[0], nextmove[1])
                (r, c), dir = nextmove
                snake.append((r, c))
                assert board[r, c] != 0
    # pprint(snake)
    print('snake len: ', len(snake))
    # raise SystemExit()
    t1 = dt.now()

    fig, ax = plt.subplots(figsize=(8, 8), dpi=128)
    fig.tight_layout()

    wall_img = np.zeros((board.shape))
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            if board[y, x] == 2:
                wall_img[y, x] = 1
    walls = ax.imshow(wall_img, cmap='Greys', alpha=1.0,
                      vmin=0, vmax=1)

    # ax.plot(np.array(snake[0:50]).T[0], np.array(snake[0:50]).T[1])
    # ax.scatter(np.array(snake[0:50]).T[0], np.array(snake[0:50]).T[1])
    snake_img = np.zeros((board.shape), np.uint8)
    snake_a = np.zeros((board.shape))
    one = np.uint8(1)
    for i, (c, r) in enumerate(snake[:50], 1):
        snake_img[c, r] = one
        snake_a[c, r] = (i / 50)
    sc2 = ax.imshow(snake_img, cmap='viridis', alpha=snake_a,
                    vmin=0, vmax=1)
    # plt.show()

    def init():
        return []
        # return walls, sc2

    def animate(i):
        nonlocal snake_img, snake_a
        T = 50
        if i % 100 == 0:
            print(f'frame  {i:<5}  ', end='\r', flush=True)
        # snake_img = np.zeros((board.shape), np.uint8)
        # snake_a = np.zeros((board.shape))
        snake_img *= np.uint8(0)
        snake_a *= 0
        for i, (c, r) in enumerate(snake[i+1:i+1+T], 1):
            # snake_img[c, r] = i
            # snake_a[c, r] = 1
            snake_img[c, r] = one
            snake_a[c, r] = i / T
        sc2.set_alpha(snake_a)
        sc2.set_data(snake_img)
        # return sc2,
        return walls, sc2

    ani = animation.FuncAnimation(
        fig, animate,
        init_func=init,
        interval=50,  # 20 fps
        blit=True,  # save_count=50,
        frames=len(snake)
        # frames=4000
    )
    plt.show()
    # plt.rcParams['animation.ffmpeg_args'].append('-')
    # writer = animation.FFMpegWriter(
    #     fps=30, bitrate=1800,
    #     codec='h264',)
    # ani.save(f"{title}.mp4", writer=writer)
    # print(f'saved {title}.mp4, took {dt.now() - t1}')


if __name__ == '__main__':
    inp = open('input/in22.txt').read()
    # inp = EXAMPLE
    board, moves = inp.replace('\r\n', '\n').split('\n\n')
    board = board.rstrip().splitlines()
    board = [ln for ln in board if ln.strip()]
    moves = parse_moves(moves.strip())

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
    print('shape', brd.shape)

    # pprint(brd)
    # import matplotlib.pyplot as plt
    # plt.imshow(brd)
    # plt.savefig('dbg22.png')
    # plt.show()

    r, c, d = solve(brd, moves, next_pos_on_map)
    print('end', r, c, d)
    r += 1
    c += 1
    print('part1:', 1000*r + 4*c + d)
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

    print('\nviz part 1')
    solve_ani(brd, moves, next_pos_on_map, 'ani22-part1')
    print('\nviz part 2')
    solve_ani(brd, moves, next_pos_cube, 'ani22-part2')

    # pprint([
    #     [float(x[0]) for x in ls_positions],
    #     [float(x[1]) for x in ls_positions],
    # ])
    # import matplotlib.pyplot as plt
    # b = brd.copy()
    # start = ls_positions[0]
    # b[start[0], start[1]] = 9
    # for i, (y, x) in enumerate(ls_positions[1:], 10):
    #     for a in range(start[0], y+1):
    #         for aa in range(start[1], x+1):
    #             b[a, aa] = i
    #     # b[y, x] = i
    # plt.imshow(brd)
    # plt.scatter(
    #     [float(x[1]) for x in [start] + ls_positions],
    #     [float(x[0]) for x in [start] + ls_positions],
    # )
    # # plt.savefig('dbg22-pt1.png')
    # plt.show()
    ...
