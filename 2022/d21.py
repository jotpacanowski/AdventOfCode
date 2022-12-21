import math
from dataclasses import dataclass


try:
    from rich.pretty import pprint
except ImportError:
    from pprint import pprint


@dataclass
class Monkey:
    name: str
    expr: str
    ref: list

    def resolve_refs(self, monkeys):
        if self.expr.isdigit():
            self.expr = int(self.expr)
            return
        a, b, c = self.expr.split()
        assert b in '+-*/'
        aa = [x for x in monkeys if x.name == a]
        cc = [x for x in monkeys if x.name == c]
        assert len(aa) == len(cc) == 1
        self.ref = [aa[0], cc[0]]
        self.expr = (b, a, c)


def parse_input(lines: list[str]) -> list[Monkey]:
    r: list[Monkey] = []
    for ln in lines:
        n, _, e = ln.partition(':')
        m = Monkey(name=n.strip(), expr=e.strip(), ref=[])
        r.append(m)
    for m in r:
        m.resolve_refs(r)
    return r


def solve1(root: Monkey):
    if isinstance(root.expr, int) or isinstance(root.expr, float):
        return root.expr
    match root.expr[0]:
        case '+':
            return solve1(root.ref[0]) + solve1(root.ref[1])
        case '-':
            return solve1(root.ref[0]) - solve1(root.ref[1])
        case '*':
            return solve1(root.ref[0]) * solve1(root.ref[1])
        case '/':
            return solve1(root.ref[0]) / solve1(root.ref[1])
    return 'xd'


def solve2(monk: Monkey, must_be_eq: int, path: list[Monkey]):
    assert not math.isnan(must_be_eq)
    if monk.name == 'humn':
        return must_be_eq
    match monk.expr[0]:
        case '+':
            if monk.ref[0].name == path[0].name:
                var = solve1(monk.ref[1])
                return solve2(monk.ref[0], must_be_eq - var, path[1:])
            else:
                var = solve1(monk.ref[0])
                return solve2(monk.ref[1], must_be_eq - var, path[1:])
        case '-':
            if monk.ref[0].name == path[0].name:
                var = solve1(monk.ref[1])
                return solve2(monk.ref[0], must_be_eq + var, path[1:])
            else:
                var = solve1(monk.ref[0])
                return solve2(monk.ref[1], var - must_be_eq, path[1:])
        case '*':
            if monk.ref[0].name == path[0].name:
                var = solve1(monk.ref[1])
                return solve2(monk.ref[0], must_be_eq / var, path[1:])
            else:
                var = solve1(monk.ref[0])
                return solve2(monk.ref[1], must_be_eq / var, path[1:])
        case '/':
            if monk.ref[0].name == path[0].name:
                var = solve1(monk.ref[1])
                return solve2(monk.ref[0], must_be_eq * var, path[1:])
            else:
                var = solve1(monk.ref[0])
                return solve2(monk.ref[1], var / must_be_eq, path[1:])
    return 'XD?'


def solve2_root(root: Monkey, humn: Monkey):
    assert isinstance(humn.expr, int)
    oldexpr = humn.expr
    humn.expr = float('nan')  # NaN propagation
    lhs = solve1(root.ref[0])
    rhs = solve1(root.ref[1])
    if not math.isnan(lhs):
        root.ref = root.ref[::-1]
        lhs, rhs = rhs, lhs
    print('lhs is nan:', lhs)
    print('rhs:', rhs)

    path = []
    x = root
    while x.name != 'humn':
        if math.isnan(solve1(x.ref[0])):
            x = x.ref[0]
        elif math.isnan(solve1(x.ref[1])):
            x = x.ref[1]
        else:
            print('???')
        path.append(x)
    # pprint([x.name for x in path])

    return solve2(root.ref[0], rhs, path[1:])


if __name__ == '__main__':
    inp = open('input/in21.txt').read()
    # inp = EXAMPLE
    inp = inp.splitlines()
    monkeys = parse_input(inp)
    root = [x for x in monkeys if x.name == 'root'][0]
    humn = [x for x in monkeys if x.name == 'humn'][0]
    if len(inp) < 16:
        pprint(root)
    print('part1:', int(solve1(root)))
    print('part2:', int(solve2_root(root, humn)))
