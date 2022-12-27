TO_SNAFU = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2',
}
TO_DEC = {v: k for k, v in TO_SNAFU.items()}


def to_dec(snafu: str) -> int:
    r = 0
    b = 1
    for digit in snafu[::-1]:
        r += b * TO_DEC[digit]
        b *= 5
    return r


def to_snafu(num: int) -> str:
    ret = ''
    while num > 0:
        q, r = divmod(num, 5)
        if r <= 2:
            ret = TO_SNAFU[r] + ret
            num = num - r
        else:
            ret = TO_SNAFU[r - 5] + ret
            num = num - (r-5)
        assert num % 5 == 0
        num //= 5
    return ret


if __name__ == '__main__':
    inp = open('input/in25.txt').read()
    # inp = EXAMPLE
    nums = [to_dec(x.strip()) for x in inp.splitlines()]
    print('p1 sum:', sum(nums))
    for i in range(0, 100):
        assert i == to_dec(to_snafu(i))
    print('part1:', to_snafu(sum(nums)))
