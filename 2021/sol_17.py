#!/usr/bin/env python3
# 2021-12-17

from pprint import pprint

import j_aoc_common


def sgn(x):
    "Signum function"
    return 1 if x > 0 else -1 if x < 0 else 0


def check_init_vel(iv, tarx, tary):
    pos = [0, 0]
    vel = [iv[0], iv[1]]
    steps = 0
    reached = False
    max_y = 0
    while not reached and steps < 1000:
        steps += 1
        # Algorithm to simulate the probe
        pos[0] += vel[0]
        pos[1] += vel[1]
        vel[1] -= 1  # Gravity
        vel[0] -= sgn(vel[0])

        max_y = max(max_y, pos[1])

        if tarx[0] <= pos[0] <= tarx[1] and tary[0] <= pos[1] <= tary[1]:
            reached = True

        # TODO: Check if it is outside using some vector math
    return reached, max_y


def main1(xrange, yrange) -> int:
    ...


def main2(xrange, yrange) -> int:
    ...


EXAMPLE_1 = "target area: x=20..30, y=-10..-5"
EXAMPLE_17 = "target area: x=277..318, y=-92..-53"  # puzzle input

if __name__ == '__main__':
    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=None)
    with PUZZLE_INPUT as f:
        inp_values = f.read().strip()
    _, _, inp_values = inp_values.partition('target area: ')
    inp_x, _, inp_y = inp_values.partition(', ')
    inp_x = inp_x[2:]
    inp_y = inp_y[2:]
    inp_x = tuple([int(x) for x in inp_x.split('..')])
    inp_y = tuple([int(x) for x in inp_y.split('..')])
    print(f'Target X: {inp_x}')
    print(f'Target Y: {inp_y}')
    assert inp_x[0] <= inp_x[1]
    assert inp_y[0] <= inp_y[1]

    answ = main1(inp_x, inp_y)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_x, inp_y)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
