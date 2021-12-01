#!/usr/bin/env python3
# 2021-12-01

def main(values):
    prev = values[0]
    increased = 0
    for y in values[1:]:
        if y > prev:
            increased += 1
        # if prev < y:
        prev = y
    return increased


if __name__ == '__main__':
    inp_values = open('1-input', 'r').read().splitlines()
    print(f'{len(inp_values)} lines')
    answ = main([int(x) for x in inp_values])
    print(f'Answer: {answ}')
    # 775 -> too low
