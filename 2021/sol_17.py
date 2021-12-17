#!/usr/bin/env python3
# 2021-12-17

from datetime import datetime as dt
import itertools
from pprint import pprint

import j_aoc_common


def sgn(x):
    "Signum function"
    return 1 if x > 0 else -1 if x < 0 else 0


# This function`s run time is crucial
def check_init_vel(iv, tarx, tary):
    pos = [0, 0]
    vel = [iv[0], iv[1]]
    assert tarx[0] > 1 and tarx[1] > 1
    assert tary[0] < 0 and tary[1] < 0

    steps = 0
    reached = False
    max_y = 0

    while not reached and steps < 100_000:
        steps += 1
        # Algorithm to simulate the probe
        pos[0] += vel[0]
        pos[1] += vel[1]
        vel[1] -= 1  # Gravity
        vel[0] -= sgn(vel[0])

        # Stats
        max_y = max(max_y, pos[1])

        if tarx[0] <= pos[0] <= tarx[1] and tary[0] <= pos[1] <= tary[1]:
            # pos[] is inside the target range
            reached = True
            break

        # Check if vel[] points towards target area or not
        if pos[1] < min(*tary):
            break
        if pos[0] < min(*tarx) and vel[0] <= 0:
            break

    return reached, max_y


def find_initial_speed_x(target_left: int, target_right: int) -> range:
    if target_left <= 0 <= target_right:
        return range(0, 0 + 1)
    # What if target is negative? (if it will ever be)

    return range(1, target_right+2)


def find_initial_sp_y(target_down: int, target_up: int) -> range:
    # In y target usually will be negative
    if target_down <= 0 <= target_up:
        return range(0, 0 + 1)

    # in every case a == -1
    # Again, it takes the same amount of time to reach v_y == 0
    # as the initial velocity in y.

    minv = max(target_down, target_down)
    maxv = 150 + 10  # IDK ???
    return range(-100, 200)
    return range(minv-10, maxv+1+10)


def main_both(xrange, yrange):
    solsp_vx = find_initial_speed_x(*xrange)
    solsp_vy = find_initial_sp_y(*yrange[::-1])
    print(f'Solution space: {len(solsp_vx) * len(solsp_vy)}')
    print(f'Vel. range for x: {solsp_vx}')
    print(f'Vel. range for y: {solsp_vy}')

    highest = 0
    count = 0
    for vx, vy in itertools.product(solsp_vx, solsp_vy):
        reached, max_y = check_init_vel([vx, vy], xrange, yrange)
        if reached:
            highest = max(highest, max_y)
            count += 1
    return highest, count


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

    t_start = dt.now()
    answ1, answ2 = main_both(inp_x, inp_y)
    print(f'\x1b[32;1mAnswer: {answ1} \x1b[0m')
    # Correct answer for my input: 4186
    print(f'\x1b[32;1m Answer2: {answ2} \x1b[0m')
    # Correct answer for my input: 2709
    # 1491 was too low
    took = dt.now() - t_start
    print(f'Computing took {took} seconds')
