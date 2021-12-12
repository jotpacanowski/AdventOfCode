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


def main1(G, display=False) -> int:
    """
    How many paths through this cave system are there
    that visit small caves at most once?
    """
    total_paths = 0
    # visited = {k: 0 for k in G.keys()}
    stack = []

    def dfs_visit(node):
        nonlocal stack, total_paths
        if node == 'end':
            stack.append('end')
            if display:
                print('New path: ', '-'.join(stack))
            stack.pop()
            total_paths += 1
        stack.append(node)
        for neigh in G[node]:
            if neigh.islower() and neigh not in stack:
                dfs_visit(neigh)
            elif neigh.isupper():
                dfs_visit(neigh)
            else:
                pass  # raise ValueError(f'node name {node!r}')
        stack.pop()

    dfs_visit('start')
    return total_paths


def main2(G, display=False) -> int:
    # Now *single* lowercase cave can be visited at most twice
    # ...and the rest of small caves once
    total_paths = 0
    visited = {k: 0 for k in G.keys()}
    stack = []
    have_twice = False

    def node_enter(node):
        stack.append(node)
        visited[node] = visited.get(node) + 1

    def node_leave():
        n = stack.pop()
        visited[n] = visited.get(n) - 1

    def dfs_visit(node):
        nonlocal stack, visited, total_paths, have_twice
        if node == 'end':
            node_enter('end')
            if display:
                print('New path: ', '-'.join(stack))
            node_leave()
            total_paths += 1
            return

        node_enter(node)
        for neigh in G[node]:
            if neigh == 'start':
                continue
            if neigh.islower() and visited[neigh] < 2:
                if visited[neigh] == 0:
                    dfs_visit(neigh)
                elif visited[neigh] == 1:
                    if not have_twice:
                        have_twice = True
                        dfs_visit(neigh)
                        have_twice = False

            elif neigh.isupper():
                dfs_visit(neigh)
            else:
                pass  # raise ValueError(f'node name {node!r}')
        node_leave()

    dfs_visit('start')
    return total_paths


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
EXAMPLE_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

EXAMPLE_IN = io.StringIO(EXAMPLE_2 if 'ex2' in sys.argv else EXAMPLE_1)
# EXAMPLE_IN = io.StringIO(EXAMPLE_3)

if __name__ == '__main__':
    USE_EXAMPLE_IN = 'ex' in sys.argv or 'ex2' in sys.argv
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('12-input', 'r') as f:
        inp_values = f.read().splitlines()
        inp_values = [x.split('-') for x in inp_values]
    print(f'{len(inp_values)} edges')

    G = edges_to_graph(inp_values)
    print(f'{len(G)} vertices')
    # print('  GRAPH: ')
    # pprint(G)

    answ = main1(G, display=False)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 3369

    answ2 = main2(G)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input: 85883
