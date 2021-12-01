#!/usr/bin/env python3
# 2021-12-01

def main(values):
    x = values[0]
    increased = 0
    for y in values[1:]:
        if y > x:
            increased += 1
        if x < y:
            x = y
    return increased


if __name__ == '__main__':
    inp_values = open('1-input', 'r').read().splitlines()
    print(f'{len(inp_values)} lines')
    answ = main([int(x) for x in inp_values])
    print(f'Answer: {answ}')
