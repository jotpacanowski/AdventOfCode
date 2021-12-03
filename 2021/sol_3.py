# 2021-12-03
from collections import Counter


def most_least_common(bits: list[str], bitnum: int):  # -> (int,int):
    ctr = Counter()
    for x in bits:
        ctr.update([x[bitnum]])
    # print(ctr.items())
    c_0 = ctr['0']
    c_1 = ctr['1']
    if c_1 > c_0:
        return '1', '0'
    else:
        return '0', '1'


def main(values: list[str]) -> int:
    # print(f'{most_least_common(values, 0)}')
    gamma = ''
    epsilon = ''
    for b in range(0, len(values[0])):
        most, least = most_least_common(values, b)
        gamma += most
        epsilon += least
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def main2(values: list[str]) -> int:
    gamma = ''
    epsilon = ''
    for b in range(0, len(values[0])):
        most, least = most_least_common(values, b)
        gamma += most
        epsilon += least
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


if __name__ == '__main__':
    inp_values = open('3-input', 'r').read().splitlines()
    inp_values = [x for x in inp_values]
    print(f'{len(inp_values)} lines')

    answ = main(inp_values)
    print(f'Answer: {answ}')

    answ = main2(inp_values)
    print(f'\n Pt 2 Answer: {answ}')
