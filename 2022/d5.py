import re
from copy import deepcopy
# from pprint import pprint


def parse_input(lines: list[str]):
    stackmat = []
    i = 0
    while lines[i][1] != '1':
        assert lines[i][1] != '1'
        stackmat.append(lines[i][1::4])
        i += 1

    print(f'stack_max_height = {i}')
    print(*stackmat, sep='\n')

    stacks = []
    for st in zip(*stackmat):
        a = [x for x in reversed(st) if x.strip()]
        print(a)
        stacks.append(a)

    assert lines[i][1] == '1'
    assert lines[i+1].strip() == ''
    lines = lines[i+2:]
    regex = re.compile(r'move (\d+) from (\d+) to (\d+)')

    instr = [
        tuple(map(int, regex.match(x).groups()))
        for x in lines
    ]
    return stacks, instr


def solve1(stacks: list[list[int]], instr: list[tuple[int, ...]]):
    N = len(stacks)
    for count, s, t in instr:
        s -= 1
        t -= 1
        # assert 0 <= count < N
        assert 0 <= s < N
        assert 0 <= t < N
        assert s != t
        for i in range(count):
            el = stacks[s].pop()
            stacks[t].append(el)

    print('part1:', ''.join([st[-1] for st in stacks]))


def solve2(stacks: list[list[int]], instr: list[tuple[int, ...]]):
    N = len(stacks)
    for count, s, t in instr:
        s -= 1
        t -= 1
        # assert 0 <= count < N
        assert 0 <= s < N
        assert 0 <= t < N
        assert s != t

        els = stacks[s][-count:]
        stacks[s] = stacks[s][:-count]
        stacks[t].extend(els)

    print('part2:', ''.join([st[-1] for st in stacks]))


if __name__ == '__main__':
    lines = open('in5.txt').read().splitlines()

    stacks, instr = parse_input(lines)
    solve1(deepcopy(stacks), instr)
    solve2(deepcopy(stacks), instr)
