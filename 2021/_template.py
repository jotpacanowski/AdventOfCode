#!/usr/bin/env python3
# 2021-12-

import io
from pprint import pprint


def main1(values) -> int:
    return


def main2(values) -> int:
    return


EXAMPLE_IN = io.StringIO("""

""")

if __name__ == '__main__':
    USE_EXAMPLE_IN = False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [int(x) for x in inp_values]
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'Answer: {answ}')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2, Answer: {answ2}')
    # Correct answer for my input:
