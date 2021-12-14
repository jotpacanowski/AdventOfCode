#!/usr/bin/env python3
# 2021-12-14

import io
import sys
from collections import Counter
from pprint import pprint


def next_polymer(rules, start):
    n2 = []
    for a, b in zip(start, start[1:]):
        r = rules[a + b]
        n2.append(a)
        n2.append(r)
        # n2.append(b)
    n2.append(start[-1])
    return n2
    return ''.join(n2)   # the same, but readable


def main1(rules, start) -> int:
    n = start
    for i in range(10):
        n2 = next_polymer(rules, n)
        n = n2.copy()
    ctr = Counter(n)
    ctri = list(ctr.items())
    ctri.sort(key=lambda x: x[1])  # by value / frequency
    return ctri[-1][1] - ctri[0][1]
    return ''.join(n2)


def main2(rules, start) -> int:
    return


EXAMPLE_IN = io.StringIO("""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""")

if __name__ == '__main__':
    USE_EXAMPLE_IN = 'ex' in sys.argv  # False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('14-input', 'r') as f:
        inp_start, inp_rules = f.read().replace('\r\n', '\n').split('\n\n')
        inp_start = inp_start.strip()
        inp_rules = dict(x.partition(' -> ')[::2]
                         for x in inp_rules.splitlines())
    print(f'{len(inp_rules)} rules')

    answ = main1(inp_rules, inp_start)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 3095

    answ2 = main2(inp_rules, inp_start)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
