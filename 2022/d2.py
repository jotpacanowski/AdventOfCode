#!/usr/bin/python3
from pprint import pprint


winning = (
    # ('A', 'Y'),  # paper wins with scissors
    # ('B', 'Z'),
    # ('C', 'X')
    (0, 1),
    (1, 2),
    (2, 0),
)

# X means you need to lose,
# Y means you need to end the round in a draw,
# and Z means you need to win. Good luck!"


def main1(inp: list[tuple[str, ...]]):
    total = 0
    for i, m in inp:
        i = ord(i) - ord('A')
        m = ord(m) - ord('X')
        if i == m:  # draw
            total += 3 + (m+1)
        elif (i, m) in winning:
            total += 6 + (m+1)
        else:
            total += 0 + (m+1)
    print('part1: ', total)


def main2(inp: list[tuple[str, ...]]):
    total = 0
    for i, t in inp:
        i = ord(i) - ord('A')
        if t == 'X':
            # LOSE
            m = (i-1) % 3
            total += 0 + (m+1)

        elif t == 'Y':
            # draw
            m = i
            total += 3 + (m+1)
        elif t == 'Z':
            # win
            m = (i+1) % 3
            total += 6 + (m+1)
        else:
            print('!?')
    print('part2: ', total)


if __name__ == '__main__':
    inp = open('in2.txt').read().splitlines()
    inp = [tuple(x.split()) for x in inp]
    # pprint(inp)

    main1(inp)
    main2(inp)
