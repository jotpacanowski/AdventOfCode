#!/usr/bin/env python3
# 2021-12-

from pprint import pprint

import j_aoc_common


def main1(values) -> int:
    return


def main2(values) -> int:
    return


EXAMPLE_1 = """

"""

if __name__ == '__main__':
    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=0)
    with PUZZLE_INPUT as f:
        inp_values = f.read().splitlines()
        inp_values = [int(x) for x in inp_values]
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
