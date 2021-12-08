#!/usr/bin/env python3
# 2021-12-08

import io
import itertools
from pprint import pprint


SEVENSEG = {
    0: 'ABCEFG',
    1: 'CF',
    2: 'ACDEG',
    3: 'ACDFG',
    4: 'BCDF',
    5: 'ABDFG',
    6: 'ABDEFG',
    7: 'ACF',
    8: 'ABCDEFG',
    9: 'ABCDFG'
}

NUM_SEGMENTS = {k: len(v) for k, v in SEVENSEG.items()}
# NUM_SEGMENTS = {
#     0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
#     5: 5, 6: 6, 7: 3, 8: 7, 9: 6
# }
POSSIBLE_DIGITS = {v: [k for k in NUM_SEGMENTS if NUM_SEGMENTS[k] == v]
                   for v in NUM_SEGMENTS.values()}
# digits 1, 4, 7, 8
UNIQUE_SEG = {v: k for k, v in NUM_SEGMENTS.items()
              if list(NUM_SEGMENTS.values()).count(v) == 1}


def single_line(line: list[str]) -> str:
    signal_patterns, output_value = line

    knowledge = []
    # easy digits:
    for d in itertools.chain(signal_patterns, output_value):
        if len(d) in UNIQUE_SEG.keys():
            it_is = UNIQUE_SEG[len(d)]
            knowledge.append((d, SEVENSEG[it_is], it_is))
    pprint(knowledge)


def main1(lines: list[list[str]]) -> int:
    "In the output values, how many times do digits 1, 4, 7, or 8 appear?"
    total = 0
    for _, output_values in lines:
        for x in output_values:
            if UNIQUE_SEG.get(len(x), -1) > -1:
                total += 1
    return total


def main2(lines: list[list[str]]) -> int:
    "What do you get if you add up all of the output values?"


EXAMPLE_IN = io.StringIO("""be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
""".replace('|\n', '|'))

if __name__ == '__main__':
    print('Example single line:')
    single_line(['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split(),
                'cdfeb fcadb cdfeb cdbaf'.split()])
    print('')

    USE_EXAMPLE_IN = False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('8-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [list(map(lambda y: y.split(), x.split('|')))
                      for x in inp_values]
    print(f'{len(inp_values)} lines')

    # single_line(inp_values[0])
    # raise NotImplementedError

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
