#!/usr/bin/env python3
# 2021-12

import io
import sys
from pprint import pprint
from typing import Tuple


def parse_argv(argv=sys.argv) -> Tuple[bool, int]:
    """Return example number provided in """
    # USING_EXAMPLE_IN = False
    if 'ex' not in ''.join(argv[1:]):
        return False, 0
        # USING_EXAMPLE_IN = True

    # Try to find example number
    example_no = None
    match argv[1:]:
        case ['ex', int(n)]:
            example_no = n
        case ['ex']:
            example_no = 1
        case str(s) if len(s) > 2:
            example_no = int(s[2:])

    if example_no is None:
        raise NotImplementedError(
            "example number should be 1 in this case", sys.argv[1:])
    return True, example_no


def do_common_main(mod_locals: dict, argv=sys.argv, *, day=0):
    """Opens puzzle input for parsing"""
    USE_EXAMPLE_IN, EXAMPLE_NO = parse_argv(argv)

    if USE_EXAMPLE_IN:
        print(f'\x1b[31;1m Using EXAMPLE input \x1b[0m({EXAMPLE_NO})')
    # Set module locals, maybe needed
    mod_locals['USE_EXAMPLE_IN'] = USE_EXAMPLE_IN
    # mod_locals['EXAMPLE_NO'] = EXAMPLE_NO

    if USE_EXAMPLE_IN:
        example_data = mod_locals[f'EXAMPLE_{EXAMPLE_NO}']
        PUZZLE_INPUT = io.StringIO(example_data)
    else:
        PUZZLE_INPUT = open(f'{day}-input', 'r')
    mod_locals['PUZZLE_INPUT'] = PUZZLE_INPUT
    return PUZZLE_INPUT

    # with EXAMPLE_IN if USE_EXAMPLE_IN else  as f:
    #     inp_values = f.read().splitlines()
    #     inp_values = [int(x) for x in inp_values]
    # print(f'{len(inp_values)} lines')


if __name__ == '__main__':
    ...
