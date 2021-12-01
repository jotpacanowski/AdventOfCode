#!/usr/bin/env python3
# 2021-12-01

def main1(values):
    prev = values[0]
    increased = 0
    for y in values[1:]:
        if y > prev:
            increased += 1
        # if prev < y:
        prev = y
    return increased


# (part 2) Instead, consider sums of
# a three-measurement sliding window.
def main2(values: list[int]) -> int:
    w1 = (a+b+c for a, b, c in zip(values, values[1:], values[2:]))
    w2 = (a+b+c for a, b, c in zip(values[1:], values[2:], values[3:]))
    increased = 0
    for prev, next in zip(w1, w2):
        if next > prev:
            increased += 1
    return increased


if __name__ == '__main__':
    inp_values = open('1-input', 'r').read().splitlines()
    inp_values = [int(x) for x in inp_values]
    print(f'{len(inp_values)} lines')
    answ = main1(inp_values)
    print(f'Answer: {answ}')
    # 775 -> too low, correct: 1374

    answ2 = main2(inp_values)
    print(f'Part 2: {answ2}')
    # 1418
