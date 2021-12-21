#!/usr/bin/env python3
# 2021-12-21

from pprint import pprint

import j_aoc_common


def move_pawn(pos: int, steps: int) -> int:
    pos -= 1
    pos = (pos + steps) % 10
    return pos + 1


def add_modulo_p1(a: int, b: int, /, mod: int) -> int:
    """Perform addition modulo `mod` of $a+b-1$ and add 1 to the result."""
    return ((a + b - 1) % mod) + 1
    # a -= 1
    # a += b
    # while a > mod:
    #     a -= mod
    # return a + 1


def main1(inp_values) -> int:
    p1pos, p2pos = inp_values  # Positions on the board 1..10
    p1sc = p2sc = 0
    dice_id = 1
    rolled_times = 0

    while p1sc < 1000 and p2sc < 1000:
        roll = 3 * dice_id + 3
        # print(f'P1 rolls {dice_id},{dice_id+1},{dice_id+2} == {roll} ', end='')
        dice_id = add_modulo_p1(dice_id, 3, 100)
        rolled_times += 3

        p1pos = move_pawn(p1pos, roll)
        p1sc += p1pos
        # print(f'and goes to', p1pos, 'w/', p1sc, 'points')

        if p1sc >= 1000:
            break

        # Same thing
        roll = 3 * dice_id + 3
        # print(f'P2 rolls {dice_id},{dice_id+1},{dice_id+2} == {roll} ', end='')
        dice_id = add_modulo_p1(dice_id, 3, 100)
        rolled_times += 3

        p2pos = move_pawn(p2pos, roll)
        p2sc += p2pos
        # print(f'and goes to', p2pos, 'w/', p2sc, 'points')

    print(f' * Dice has been rolled {rolled_times} times.')
    if p1sc >= 1000:
        print(f'-- Player 1 won with {p1sc} points  > {p2sc}')
        return p2sc * rolled_times
    elif p2sc >= 1000:
        print(f'-- Player 2 won with {p2sc} points  > {p1sc}')
        return p1sc * rolled_times
    else:
        return NotImplemented


def main2(values) -> int:
    return


EXAMPLE_1 = """Player 1 starting position: 4
Player 2 starting position: 8
"""

# My puzzle input
EXAMPLE_21 = """Player 1 starting position: 10
Player 2 starting position: 2
"""

if __name__ == '__main__':
    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=21)
    with PUZZLE_INPUT as f:
        inp_values = f.read().splitlines()
        inp_values = [int(x.partition(':')[2]) for x in inp_values if x]
        assert len(inp_values) == 2
    print(f'Positions: {inp_values[0]} and {inp_values[1]}')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 916083

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input: