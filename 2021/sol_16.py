#!/usr/bin/env python3
# 2021-12-16

from pprint import pprint

import j_aoc_common


def parse_packet(hex):
    "Parse a single packet"
    if isinstance(hex, str):
        hex = bytes.fromhex(hex)
    bits = ''.join(f'{x:08b}' for x in hex)

    print(f'Packet: {hex.hex()}')
    PV, PT, data = bits[0:3], bits[3:6], bits[6:]
    # print(f'{PV}, {PT}, {len(data)} b left')
    PV = int(PV, 2)
    PT = int(PT, 2)

    values = []
    while True:
        val_start = data[0]
        val_val = data[1:1 + 4]
        # values.append(int(val_val, 2))
        values.append(val_val)
        if val_start == '0':
            break
        data = data[5:]
    return int(''.join(values), 2)


def main1(values) -> int:
    return


def main2(values) -> int:
    return


EXAMPLE_1 = """

"""

if __name__ == '__main__':
    parse_packet("D2FE28")

    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=16)
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
