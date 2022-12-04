#!/usr/bin/python3

Input = list[tuple[tuple[int, int], tuple[int, int]]]


def parse_input(lines: list[str]) -> Input:
    def rang_(atb):
        a, b = atb.split('-', 1)
        assert int(a) <= int(b)
        return int(a), int(b)

    def f1(a):
        l, _, r = a.partition(',')
        return rang_(l), rang_(r)
    return [f1(x) for x in lines if x]


def main1(inp: Input):
    total = 0
    for lr, rr in inp:
        a, b = lr
        c, d = rr
        if a <= c <= d <= b:
            total += 1
        elif c <= a <= b <= d:
            total += 1
    print('part1:', total)


def main2(inp: Input):
    total = 0
    for (a, b), (c, d) in inp:
        if b < c:
            ...
        elif d < a:
            ...
        else:
            total += 1
    print('part2:', total)


if __name__ == '__main__':
    lines = open('in4.txt').read().splitlines()
    inp = parse_input(lines)
    main1(inp)
    main2(inp)
