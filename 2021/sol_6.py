#!/usr/bin/env python3
# 2021-12-06

import io
import time
from collections import Counter
from pprint import pprint


def main1(values_, days) -> int:
    values = values_.copy()
    t1 = time.time()
    for d in range(days):
        t2 = time.time()
        if d > 80:
            print(f'main1, day {d:5d}   {t2-t1:5.1f} s   {len(values)}')
        no_fishes = len(values)
        t1 = time.time()
        for i in range(no_fishes):
            values[i] -= 1
            if values[i] < 0:
                values[i] = 6
                values.append(8)
    return len(values)


def main2(values, days) -> int:
    prev_gen = Counter(values)  # copy
    # print(prev_gen)
    gen = Counter()
    for d in range(days):
        gen.clear()
        for k, v in prev_gen.items():
            # print(k,v); breakpoint()
            if k == 0:
                gen[6] += v
                gen[8] += v
            else:
                gen[k-1] += v
        prev_gen = gen.copy()
    # print(gen)
    return sum(v for k, v in gen.items())


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
    print(f'After 80 days: {main2(inp_values, DAYS)}')

    # main1, day   109     0.4 s   4511546  -- it would take too much time
    # print(f'After 256 days: {main1(inp_values, 256)}')

    print(f'After 256 days: {main2(inp_values, 256)}')
    # Correct answer for my input:
