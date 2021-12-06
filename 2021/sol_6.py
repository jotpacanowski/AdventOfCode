#!/usr/bin/env python3
# 2021-12-06

import io
from pprint import pprint


def main1(values_, days) -> int:
    values = values_.copy()
    for d in range(days):
        no_fishes = len(values)
        for i in range(no_fishes):
            values[i] -= 1
            if values[i] < 0:
                values[i] = 6
                values.append(8)
    return len(values)


def main2(values, days) -> int:
    return


EXAMPLE_IN = io.StringIO("3,4,3,1,2\n")

if __name__ == '__main__':
    DAYS = 80
    USE_EXAMPLE_IN = False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('6-input', 'r') as f:
        inp_values = f.read().strip().split(',')
        inp_values = [int(x) for x in inp_values]
    print(f'{len(inp_values)} fishes')

    answ = main1(inp_values, DAYS)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 365131

    print(f'After 256 days: {main1(inp_values, 256)}')

    answ2 = main2(inp_values, DAYS)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
