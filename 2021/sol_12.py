#!/usr/bin/env python3
# 2021-12-12

import io
import sys
from pprint import pprint


def edges_to_graph(edges_list):
    "Convert edges list to adjacency lists"
    G = dict()
    for a, b in edges_list:
        G.setdefault(a, [])
        G.setdefault(b, [])
        G[a].append(b)
        G[b].append(a)
    return G


def main1(values) -> int:
    return


def main2(values) -> int:
    return


EXAMPLE_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
EXAMPLE_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

EXAMPLE_IN = io.StringIO(EXAMPLE_1)

if __name__ == '__main__':
    USE_EXAMPLE_IN = 'ex' in sys.argv  # False
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('12-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [x.split('-') for x in inp_values]
    print(f'{len(inp_values)} edges')

    G = edges_to_graph(inp_values)
    print('  GRAPH: ')
    pprint(G)

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input:

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input:
