from dataclasses import dataclass, field
from datetime import datetime as dt

from rich.pretty import pprint

VERBOSE = False  # enable debugging


@dataclass
class Monkey():
    # consts
    idx: int = -1
    operation: str = ''
    test_mod: int = -1
    if_true: int = -1
    if_false: int = -1
    starting_items: tuple[int] = ()
    # simulation variables
    holds: list[int] = field(default_factory=list)
    inspected: int = 0


def parse_monkey(text: str):
    r = Monkey()
    for line in text.splitlines():
        line = line.strip()
        b, _, e = line.partition(':')
        b = b.strip()
        e = e.strip().lower()
        if b.startswith('Monkey'):
            r.idx = int(line[7:-1])
        elif b.startswith('Starting'):
            r.starting_items = tuple(list(
                map(int, e.split(','))
            ))
        elif b.startswith('Operation'):
            r.operation = e.removeprefix('new = ')
        elif b.startswith('Test'):
            r.test_mod = int(e.removeprefix('divisible by '))
        elif b.startswith('If '):
            if b.startswith('If true'):
                r.if_true = int(e.removeprefix('throw to monkey '))
            elif b.startswith('If false'):
                r.if_false = int(e.removeprefix('throw to monkey '))
            else:
                print("?!", b, e)
        else:
            print(f"??? {b=} {e=}")

    return r


def _nothing(*args, **kwargs):
    ...


def single_turn(monkeys: list[Monkey], idx: int, part1=False):
    """
    Print description similar to the example Advent of Code website.
    """
    p = print if VERBOSE and part1 else _nothing  # too much for 10_000 rounds

    p(f'Monkey {idx}')
    m = monkeys[idx]
    while m.holds:
        item = m.holds.pop(0)
        p(f'  Monkey inspects an item with a worry level of {item}.')
        m.inspected += 1

        item = eval(m.operation.replace('old', str(item)))
        p(f'    Worry level is {m.operation!r} to {item}.')
        if part1:
            item = item // 3
            p(f'    Monkey gets bored with item. Worry level is divided by 3 to {item}.')
        idx_to = (m.if_true
                  if item % m.test_mod == 0
                  else m.if_false)
        p(f'    Current worry level is/not divisible by {m.test_mod}.')
        monkeys[idx_to].holds.append(item)
        p(f'    Item with worry level {item} is thrown to monkey {idx_to}.')


def normalize_items(monkeys: list[Monkey], base: int):
    for m in monkeys:
        it = m.holds
        for i, j in enumerate(it):
            it[i] = j % base
        m.holds = it


TEST = """"""

if __name__ == '__main__':
    lines: str = open('input/in11.txt').read()
    # lines = TEST
    monkeys = list(map(parse_monkey,
                       lines.replace('\r\n', '\n').split('\n\n')))
    for m in monkeys:
        m.holds = list(m.starting_items)
    if VERBOSE:
        pprint(monkeys)

    for round in range(1, 21):
        for i in range(len(monkeys)):
            single_turn(monkeys, i, part1=True)
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}:', ', '.join(map(str, m.holds)))
    g = []
    for i, m in enumerate(monkeys):
        print(f'Monkey {i} inspected', m.inspected)
        g.append(m.inspected)
    g.sort(reverse=True)
    g = g[:2]
    pprint(g)
    print('part1:', g[0] * g[1])

    # reparse just in case
    monkeys = list(map(parse_monkey,
                       lines.replace('\r\n', '\n').split('\n\n')))
    base = 1
    for m in monkeys:
        base *= m.test_mod
    print('    base: ', base)
    for m in monkeys:
        m.holds = list(m.starting_items)
    normalize_items(monkeys, base)

    start = dt.now()
    # for round in range(1, 21):
    for round in range(1, 10_001):
        for i in range(len(monkeys)):
            single_turn(monkeys, i, part1=False)
        normalize_items(monkeys, base)
        if VERBOSE and (round in (1, 20, 1_000, 9_000, 10_000)):
            # or round % 100 == 0):
            print(f'\n== After round {round} ==')
            for i, m in enumerate(monkeys):
                print(f'Monkey {i} inspected items', m.inspected)
            print('-' * 22, f'{dt.now() - start}')

    g = []
    for i, m in enumerate(monkeys):
        print(f'Monkey {i} inspected', m.inspected)
        g.append(m.inspected)
    g.sort(reverse=True)
    g = g[:2]
    pprint(g)
    print('part2:', g[0] * g[1])
    print('-' * 22, f'{dt.now() - start}')
