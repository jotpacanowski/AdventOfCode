#!/usr/bin/env python3
# 2021-12-16

from pprint import pprint

import j_aoc_common


def parse_literal_value(data) -> int:
    values = []
    while True:
        val_start = data[0]
        val_val = data[1:1 + 4]
        # values.append(int(val_val, 2))
        values.append(val_val)
        if val_start == '0':
            break
        data = data[5:]
    return 5 * len(values), int(''.join(values), 2)


GLBL_SUM_ALL_PV = 0


def parse_packet(hex):
    "Parse a single packet, return (consumed_bits, value)"
    global GLBL_SUM_ALL_PV

    if isinstance(hex, str):
        hex = bytes.fromhex(hex)
    bits = ''.join(f'{x:08b}' for x in hex)
    org_data_len = len(bits)

    # print(f'Packet: {hex.hex()}')
    PV, PT, data = bits[0:3], bits[3:6], bits[6:]
    # print(f'{PV}, {PT}, {len(data)} b left')
    PV = int(PV, 2)
    PT = int(PT, 2)
    GLBL_SUM_ALL_PV += PV

    if PT == 4:
        return parse_literal_value(data)

    # operators
    length_type_id = data[0]
    if length_type_id == '0':
        length = int(data[1:1 + 15], 2)
        data = data[16:]
        return 1 + 15 + length, None
    else:
        sub_pack = int(data[1:1 + 11], 2)
        data = data[12:]
        data = data[:sub_pack * 11]
        return 12 + len(data), None

    raise NotImplementedError()


def main1(values) -> int:
    parse_packet(values)
    return GLBL_SUM_ALL_PV


def main2(values) -> int:
    return


EXAMPLE_1 = """

"""

if __name__ == '__main__':
    assert parse_packet("D2FE28") == (15, 2021)     # integer value
    assert parse_packet("38006F45291200")[0] == 43  # I=0
    assert parse_packet("EE00D40C823060")[0] == 45  # I=1

    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=16)
    with PUZZLE_INPUT as f:
        inp_values = f.read().strip()
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
