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
    def most_least_comm(bits: list[str], bitnum: int, filter=''):
        ctr = Counter()
        for x in bits:
            if x.startswith(filter):
                ctr.update([x[bitnum]])
        # print(ctr.items())
        c_0 = ctr['0']
        c_1 = ctr['1']
        if c_1 > c_0:
            return '1', '0', False
        else:
            return '0', '1', c_0 == c_1

    def cnt_nums(start=''):
        return sum(1 for x in values if x.startswith(start))

    def mlc_subset(bits: list[str], start=''):
        return (
            [most_least_comm(bits, b, start) for b in range(len(bits[0]))],
            cnt_nums(start))

    common_bits = mlc_subset(values, '1')
    import pprint
    pprint.pprint(common_bits)

    oxygen_pref = ''
    while cnt_nums(oxygen_pref) > 1:
        most_cm, _, eq = most_least_comm(values, len(oxygen_pref), oxygen_pref)
        print(f'{oxygen_pref:13s} {len(oxygen_pref):2} {most_cm} '
              f'  count={cnt_nums(oxygen_pref)}')
        if eq:
            oxygen_pref += '1'
        else:
            oxygen_pref += most_cm
    print(f'{oxygen_pref:13s} {len(oxygen_pref):2} - {"":5}   '
          f'count={cnt_nums(oxygen_pref)}')
    oxygen_nums = [x for x in values if x.startswith(oxygen_pref)]
    oxygen_num = [x for x in values if x.startswith(oxygen_pref)][0]
    oxygen_rating = int(oxygen_pref, 2)
    # print(f'{oxygen_nums=} {oxygen_num}')
    print(f'{oxygen_num} = {int(oxygen_num,2)}')
    print('')

    CO2_pref = ''
    # while len(CO2_pref) < len(values[0]):
    while cnt_nums(CO2_pref) > 1:
        _, least_cm, eq = most_least_comm(values, len(CO2_pref), CO2_pref)
        print(f'{CO2_pref:13s} {len(CO2_pref):2} {least_cm} {eq:5}   '
              f'count={cnt_nums(CO2_pref)}')
        if eq:
            CO2_pref += '0'
        else:
            CO2_pref += least_cm
    print(f'{CO2_pref:13s} {len(CO2_pref):2} - {"":5}   '
          f'count={cnt_nums(CO2_pref)}')
    CO2_rating = int(CO2_pref, 2)
    CO2_nums = [x for x in values if x.startswith(CO2_pref)]
    CO2_num = CO2_nums[0]
    # print(f'{CO2_nums=} {CO2_num}')
    print(f'{CO2_num} = {int(CO2_num,2)}')

    return int(oxygen_num, 2) * int(CO2_num, 2)
    return oxygen_rating * CO2_rating

    # 866761 - too low
    # 3370220 - too high
    # 3368358 OK


if __name__ == '__main__':
    inp_values = open('3-input', 'r').read().splitlines()
    inp_values = [x for x in inp_values]
    print(f'{len(inp_values)} lines')

    answ = main(inp_values)
    print(f'Answer: {answ}')

    answ = main2(inp_values)
    print(f'\n Pt 2 Answer: {answ}')
