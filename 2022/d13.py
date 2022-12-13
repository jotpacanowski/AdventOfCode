from functools import cmp_to_key
from itertools import zip_longest

# from pprint import pprint
# from rich.pretty import pprint


def compare_packets(A, B) -> int:
    if isinstance(A, int) and isinstance(B, int):
        if A == B:
            return 0
        return 1 if (A < B) else -1
    elif isinstance(A, list) and isinstance(B, list):
        for a_it, b_it in zip_longest(A, B, fillvalue=None):
            if a_it is None:
                return +1
            elif b_it is None:
                return -1
            cmp = compare_packets(a_it, b_it)
            if cmp != 0:
                return cmp
        return 0
    else:
        if isinstance(A, int):
            return compare_packets([A], B)
        else:
            return compare_packets(A, [B])


def solve1(packets: list[str]):
    r = 0
    for nr, twolines in enumerate(packets, start=1):
        a, b = twolines.splitlines()
        a = eval(a)
        b = eval(b)
        if compare_packets(a, b) == 1:
            r += nr
    print('part1:', r)


DIV1 = "[[2]]"
DIV2 = "[[6]]"


def solve2(packets: list[str]):
    @cmp_to_key
    def _compare(x, y):
        return -compare_packets(x, y)

    # pprint(packets)
    ls = [eval(x) for x in packets]
    # pprint(ls)
    ls.sort(key=_compare)
    # if len(ls) < 20:
    #     pprint(ls)
    p1, p2 = 0, 0
    for i, j in enumerate(ls, 1):
        if str(j) == DIV1:
            p1 = i
        elif str(j) == DIV2:
            p2 = i
    print('part2:', p1*p2)


if __name__ == '__main__':
    inp = open('input/in13.txt').read()
    # inp = EXAMPLE
    inp = inp.replace('\r\n', '\n')
    pairs = inp.split('\n\n')
    print(f'{len(pairs)*2} packets')
    solve1(pairs)

    inp = inp.replace('\n\n', '\n')
    inp = "[[2]]\n[[6]]\n" + inp
    inp = inp.strip().split('\n')
    solve2(inp)
