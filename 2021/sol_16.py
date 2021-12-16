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
    return 6 + 5 * len(values), int(''.join(values), 2)


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
    if len(bits) <= 6:
        print('??? Packet shorter than 6 bits')
        return 0, float('nan')

    # print(f'Packet: {hex.hex()}')
    PV, PT, data = bits[0:3], bits[3:6], bits[6:]
    # print(f'{PV}, {PT}, {len(data)} b left')
    if not data:
        print('??? empty data', PT, PV)
        return 0, float('nan')

    PV = int(PV, 2)   # packet version
    PT = int(PT, 2)   # packet type ID
    print(f' * {"Value packet" if PT == 4 else "Operator"} ver. {PV},  {len(data)} bits')
    GLBL_SUM_ALL_PV += PV

    if PT == 4:
        bits, val = parse_literal_value(data)
        print(f' -> Has VALUE {val},  ({bits=})')
        return bits, val

    # operators
    length_type_id = data[0]
    if length_type_id == '0':
        length = int(data[1:1 + 15], 2)
        data = data[16: 16 + length]
        print(f' -- Inside packet i=0, L={length}')
        while len(data) > 6:
            # print(f'Another inside packet', len(data)//4, data)
            print(f'about to parse ({len(data)} b):')  # , data)
            that_c, _ = parse_packet(data, str_bits=True)
            # if that_c > 11:
            #     print('!!! !!!!')
            # that_c = math.ceil(that_c / 4)
            data = data[that_c:]
        if len(data) != 0 and len(data) > 6:
            print('! Unconsumed', len(data), 'bits')
        return 6 + 1 + 15 + length, 'LT-len'
    else:
        sub_pack = int(data[1:1 + 11], 2)
        print(f' -- Inside packet i=1 with {sub_pack} sub-packets')
        data = data[12:]
        # data = data[:sub_pack * 11]
        rlen = 12
        for i in range(sub_pack):
            print(f'about to parse {i}/{sub_pack}:')  # , data)
            that_c, _ = parse_packet(data, str_bits=True)
            data = data[that_c:]
            rlen += that_c
        print(f'{i}/{sub_pack} -- ver {PV}')
        if len(data) != 0:
            # rlen += len(data)
            print('@ Unconsumed', len(data), 'bits')
        return 6 + rlen, 'LT_sub'

    raise NotImplementedError()


def main1(values) -> int:
    # data = values
    # pprint(values)
    data = ''.join(f'{int(x,16):04b}' for x in values)
    # print(data)
    # "The BITS transmission contains a single packet at its outermost layer"
    while len(data) > 7:
        print(f'Parsing {int(data[:4*2],2):02x}... {len(data)} bits left\n')
        bits, v = parse_packet(data, str_bits=True)
        # bits += 6  # header
        hexd = math.ceil(bits / 4)
        print(f"\nAte {bits} -> {hexd} digits, {v=}")
        print('   CURRENT SUM IS ', GLBL_SUM_ALL_PV)
        data = data[bits:]  # data[hexd:]
        # BITS transmission might encode few 0 at the end - ignore
        print('data left:')
        print(data)
    return GLBL_SUM_ALL_PV


def main2(values) -> int:
    return


EXAMPLE_1 = "8A004A801A8002F478"  # 4,1,5,6 -> 16
EXAMPLE_2 = '620080001611562C8802118E34'  # 12
EXAMPLE_3 = 'C0015000016115A2E0802F182340'  # 23
EXAMPLE_4 = 'A0016C880162017C3686B18A3D4780'  # 31

if __name__ == '__main__':
    if False:
        assert parse_packet("D2FE28") == (15 + 6, 2021)     # integer value
        print('assertions succ1')
        assert parse_packet("38006F45291200")[0] - 6 == 43  # I=0
        print('assertions succ2')
        print('\n\n\n', parse_packet("EE00D40C823060"))
        assert parse_packet("EE00D40C823060")[0] == 45 + 6 + 5  # I=1, 5 at the end
        print('assertions succ3')
        GLBL_SUM_ALL_PV = 0

    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=16)
    with PUZZLE_INPUT as f:
        inp_values = f.read().strip()
    print(f'{len(inp_values)} hex digits == {4*len(inp_values)} bits')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 904

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
