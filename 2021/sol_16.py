#!/usr/bin/env python3
# 2021-12-16

import math
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


def parse_packet(hex, str_bits=False):
    "Parse a single packet, return (consumed_bits, value)"
    global GLBL_SUM_ALL_PV

    if str_bits:
        bits = hex
    else:
        if isinstance(hex, str):
            if len(hex) % 2 == 1:
                hex += '0'
            hex = bytes.fromhex(hex)
            bits = ''.join(f'{x:08b}' for x in hex)
        else:
            raise NotImplementedError

    # org_data_len = len(bits)

    # print(f'Packet: {hex.hex()}')
    PV, PT, data = bits[0:3], bits[3:6], bits[6:]
    # print(f'{PV}, {PT}, {len(data)} b left')
    PV = int(PV, 2)
    PT = int(PT, 2)

    if not data:
        return 0, float('nan')
    print(f' * Packet {PT == 4} w/ ver. {PV}   {len(data)}')
    GLBL_SUM_ALL_PV += PV

    if PT == 4:
        return parse_literal_value(data)

    # operators
    length_type_id = data[0]
    if length_type_id == '0':
        length = int(data[1:1 + 15], 2)
        data = data[16:]
        while len(data) // 4 > 0 and len(data) > 6:
            # print(f'Another inside packet', len(data)//4, data)
            that_c, _ = parse_packet(data, str_bits=True)
            that_c = math.ceil(that_c / 4)
            data = data[that_c:]
        return 1 + 15 + length, 'LT-len'
    else:
        sub_pack = int(data[1:1 + 11], 2)
        data = data[12:]
        data = data[:sub_pack * 11]
        return 12 + len(data), 'LT_sub'

    raise NotImplementedError()


def main1(values) -> int:
    # data = values
    data = ''.join(f'{int(x,16):08b}' for x in values)
    while len(data) > 0:
        print(f'Parsing {data[:5]!r} ... {len(data)} d. left')
        bits, v = parse_packet(data, str_bits=True)
        bits += 6  # header
        hexd = math.ceil(bits / 4)
        print(f"cosdumed {bits} -> {hexd} digits, {v=}")
        print('current sum', GLBL_SUM_ALL_PV)
        data = data[hexd:]
        # BITS transmission might encode few 0 at the end - ignore
    return GLBL_SUM_ALL_PV


def main2(values) -> int:
    return


EXAMPLE_1 = "8A004A801A8002F478"  # 4,1,5,6 -> 16
EXAMPLE_2 = '620080001611562C8802118E34'  # 12

if __name__ == '__main__':
    if False:
        assert parse_packet("D2FE28") == (15, 2021)     # integer value
        print('assertions succ1')
        assert parse_packet("38006F45291200")[0] == 43  # I=0
        print('assertions succ2')
        assert parse_packet("EE00D40C823060")[0] == 45  # I=1
        print('assertions succ3')
        GLBL_SUM_ALL_PV = 0

    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=16)
    with PUZZLE_INPUT as f:
        inp_values = f.read().strip()
    print(f'{len(inp_values)} hex digits')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:
    # 2545 - too high
    # 45 - wrong

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
