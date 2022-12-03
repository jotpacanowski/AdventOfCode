#!/usr/bin/python3


def priority(letter: str) -> int:
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    if 'A' <= letter <= 'Z':
        return ord(letter) - ord('A') + 27
    raise NotImplementedError(f'{letter=}')


def single_line_common(line: str) -> set[str]:
    assert len(line) % 2 == 0
    a = line[:len(line)//2]
    b = line[len(line)//2:]
    assert len(a) == len(b)
    pr = set(a).intersection(set(b))
    return pr


def main1(inp: list[str]):
    total = 0
    for line in inp:
        pr = single_line_common(line)
        total += sum(priority(x) for x in pr)
    print('part1: ', total)


def main2(inp: list[str]):
    total = 0
    for a, b, c in zip(
        inp[0:len(inp):3],
        inp[1:len(inp):3],
        inp[2:len(inp):3],
    ):
        a = set(a)
        b = set(b)
        c = set(c)
        pr = a.intersection(b).intersection(c)
        total += sum(priority(x) for x in pr)

    print('part2: ', total)


if __name__ == '__main__':
    inp = open('in3.txt').read().splitlines()
    main1(inp)
    main2(inp)
