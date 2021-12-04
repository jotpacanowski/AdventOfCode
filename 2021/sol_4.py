#!/usr/bin/env python3
# 2021-12-04

import io
from pprint import pprint


def is_winning(board, nums) -> bool:
    """Check if the board is winning when nums are marked."""
    for row in board:
        if all(x in nums for x in row):
            return True
    for col in zip(*board):
        if all(x in nums for x in col):
            return True
    # Diagonals don't count
    return False


def minimum_marked_bs(board, nums) -> int:
    """Return minimum number of marked numbers for a board to be winning."""
    l_, r = 3, len(nums)
    while r - l_ > 1:
        m = (l_+r) // 2
        if is_winning(board, nums[:m]):
            r = m
        else:
            l_ = m+1
    return l_


def minimum_marked(board, nums) -> int:
    """Return minimum number of marked numbers for a board to be winning."""
    i = 1
    while not is_winning(board, nums[:i]):
        i += 1
    return i


def board_sum_unmarked(board, nums):
    total = 0
    for row in board:
        for x in row:
            if x not in nums:
                total += x
    return total


def main1(boards, rand):
    rand.append(None)
    rand.append(None)
    need_nums = dict()
    for i in range(len(boards)):
        need_nums[i] = minimum_marked(boards[i], rand)
    # pprint(need_nums)
    best_i, best_n = min(need_nums.items(), key=lambda x: x[1])
    print(f'{best_i}-th board, {best_n} numbers')
    print('Last number was', rand[best_n-1], rand[:best_n][-1])
    return rand[best_n-1] * board_sum_unmarked(boards[best_i], rand[:best_n])


def main2(boards, rand):
    rand.append(None)
    rand.append(None)
    need_nums = dict()
    for i in range(len(boards)):
        need_nums[i] = minimum_marked(boards[i], rand)

    best_i, best_n = max(need_nums.items(), key=lambda x: x[1])
    print(f'{best_i}-th board, {best_n} numbers')
    print('Last number was', rand[best_n-1], rand[:best_n][-1])
    return rand[best_n-1] * board_sum_unmarked(boards[best_i], rand[:best_n])


EXAMPLE_IN = io.StringIO("""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""")

if __name__ == '__main__':
    USE_EXAMPLE_IN = False
    rand = None
    bingo_ln = []
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('4-input', 'r') as f:
        for line in f:
            if not len(line.strip()):
                continue
            if not rand:
                rand = [int(x) for x in line.split(',')]
                continue
            bingo_ln.append([int(x) for x in line.split()])

    boards = [bingo_ln[i:i+5] for i in range(0, len(bingo_ln), 5)]
    # pprint(boards[99])

    print(f'{len(rand)} numbers and {len(bingo_ln) / 5:g} boards')

    answ = main1(boards, rand)
    print(f'Answer: {answ}')
    # 39902 - right answer

    answ2 = main2(boards, rand)
    print(f'Part 2: {answ2}')
    #
