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


def main1(inp_values, /, stopping_points=1000, *, verbose=False) -> int:
    p1pos, p2pos = inp_values  # Positions on the board 1..10
    p1sc = p2sc = 0
    dice_id = 1
    rolled_times = 0

    while p1sc < stopping_points and p2sc < stopping_points:
        roll = 3 * dice_id + 3
        # print(f'P1 rolls {dice_id},{dice_id+1},{dice_id+2} == {roll} ', end='')
        dice_id = add_modulo_p1(dice_id, 3, 100)
        rolled_times += 3

        p1pos = move_pawn(p1pos, roll)
        p1sc += p1pos
        # print(f'and goes to', p1pos, 'w/', p1sc, 'points')

        if p1sc >= stopping_points:
            break

        # Same thing
        roll = 3 * dice_id + 3
        # print(f'P2 rolls {dice_id},{dice_id+1},{dice_id+2} == {roll} ', end='')
        dice_id = add_modulo_p1(dice_id, 3, 100)
        rolled_times += 3

        p2pos = move_pawn(p2pos, roll)
        p2sc += p2pos
        # print(f'and goes to', p2pos, 'w/', p2sc, 'points')

    if verbose:
        print(f' * Dice has been rolled {rolled_times} times.')
    if p1sc >= stopping_points:
        if verbose:
            print(f'-- Player 1 won with {p1sc} points  > {p2sc}')
        return p2sc * rolled_times
    elif p2sc >= stopping_points:
        if verbose:
            print(f'-- Player 2 won with {p2sc} points  > {p1sc}')
        return p1sc * rolled_times
    else:
        return NotImplemented


# def enum_dice_roll_possibilities():
    # Computed this way:
    # dd = dict()
    # for i,j,k in itertools.product(range(1,3+1), repeat=3):
    #     dd[i+j+k] = dd.get(i+j+k, 0) + 1
    # return dd

DIRAC_DICE = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}.items()


# RECURSIVE_CALLS = 0

def rek(pl_pos, other_pos, pl_sc=0, other_sc=0, *, lvl=0):
    # global RECURSIVE_CALLS
    # RECURSIVE_CALLS += 1
    # if lvl < 2:
    #     print(f'{" "*lvl}* {RECURSIVE_CALLS} calls')
    this_wins, other_wins = 0, 0
    for rollsum, universes in DIRAC_DICE:
        new_pos = move_pawn(pl_pos, rollsum)  # add_modulo_p1(pl_pos, rollsum, 10)
        new_score = pl_sc + new_pos
        if new_score >= 21:
            this_wins += universes
            continue

        # Now other player takes turn
        rec_result = rek(other_pos, new_pos, other_sc, new_score, lvl=lvl+1)
        other_wins += rec_result[0] * universes
        this_wins += rec_result[1] * universes
    return this_wins, other_wins


def main2(values) -> int:
    result = rek(values[0], values[1])
    print('Recursion result: ', result)
    return max(result)


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

    answ = main1(inp_values, verbose=True)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 916083

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input: 49982165861983
