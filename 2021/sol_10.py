#!/usr/bin/env python3
# 2021-12-10

import io
import itertools
import sys
from pprint import pprint


MATCHING_BR = '() {} [] <>'.split()
MATCHING_BR = dict(itertools.chain(
    ((x[0], x[1]) for x in MATCHING_BR),
    ((x[1], x[0]) for x in MATCHING_BR)
))


def parse_line(ln: str, verbose=False) -> int:
    stack = []
    for i, x in enumerate(ln.strip()):
        if verbose:
            print('Got', x)
        if x in '([{<':
            stack.append(x)
        elif x in ')]}>':
            if len(stack) == 0:
                return 'Unmatched', i, x
            y = stack.pop()
            if MATCHING_BR[x] != y:
                return 'Expected', i, y, x
            # else:
            #     pass
        else:
            raise ValueError(f'Found character {x!r}')
        if verbose:
            print(' stack: ', ' '.join(stack))

    if len(stack) == 0:
        return 'good', None, None
    else:
        return 'incomplete', i, stack


def main1(values) -> int:
    illegal_closing = dict.fromkeys(')]}>', 0)
    for ln in values:
        msg, i, *br = parse_line(ln)
        match msg:
            # case 'Unmatched':
            #     pass
            case 'Expected':
                should, but_is = br
                illegal_closing[but_is] += 1
            case _:
                pass
    total = 0
    total += illegal_closing[')'] * 3
    total += illegal_closing[']'] * 57
    total += illegal_closing['}'] * 1197
    total += illegal_closing['>'] * 25137
    return total


def main2(values) -> int:
    scores = []
    for ln in values:
        msg, i, *br = parse_line(ln)
        if msg != 'incomplete':
            continue
        stack = br[0]
        complete = [MATCHING_BR[x] for x in stack[::-1]]

        VAL = ' )]}>'
        score = 0
        for c in complete:
            score *= 5
            score += VAL.index(c)

        scores.append(score)
        # print('line', ln, 'compete w/', ' '.join(complete), score, 'points')
    scores.sort()
    return scores[len(scores) // 2]


EXAMPLE_IN = io.StringIO("""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""")

if __name__ == '__main__':
    TEST_VALID = "() [] ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], (((((((((())))))))))"
    for t in TEST_VALID.replace(',', '').split():
        print(f'Testing line  {t!r}')
        parse_line(t)
    TEST_WRONG = "(], {()()()>, (((()))}, <([]){()}[{}])"
    for t in TEST_WRONG.replace(',', '').split():
        print(f'Testing {t!r}\n  ', parse_line(t))
    print('Done testing.')

    USE_EXAMPLE_IN = 'ex' in sys.argv
    if USE_EXAMPLE_IN:
        print('\x1b[31;1m Using EXAMPLE input! \x1b[0m')
    with EXAMPLE_IN if USE_EXAMPLE_IN else open('10-input', 'r') as f:
        inp_values = f.read().splitlines()
    print(f'{len(inp_values)} lines')

    # parse_line(inp_values[0])
    # raise SystemExit(0)

    answ = main1(inp_values)
    print(f'\x1b[32;1mAnswer: {answ} \x1b[0m')
    # Correct answer for my input: 394647

    answ2 = main2(inp_values)
    print(f'Part 2,\x1b[32;1m Answer: {answ2} \x1b[0m')
    # Correct answer for my input: 2380061249
