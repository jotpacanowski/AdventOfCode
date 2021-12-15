# Advent of code test

import sys
import pathlib
from pprint import pprint

sys.path.append(pathlib.Path(__file__).parent.parent.absolute().as_posix())
# pprint(sys.path)
import j_aoc_common


def main1(values) -> int:
    pprint(values)
    return 1337


def main2(values) -> int:
    print(hex(int(values[1])))
    return 0xc0ffee


EXAMPLE_1 = """o.n.e.s
1111
"""

EXAMPLE_2 = """t.w.o.s
2222
"""

if __name__ == '__main__':
    PUZZLE_INPUT = j_aoc_common.do_common_main(locals(), day=0)
    with PUZZLE_INPUT as f:
        inp_values = f.read().splitlines()
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
elif do_the_test:
    ...
    PUZZLE_INPUT = j_aoc_common.do_common_main(
        locals(), argv=do_the_test, day=0)
    with PUZZLE_INPUT as f:
        inp_values = f.read().splitlines()
    print(f'{len(inp_values)} lines')

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
