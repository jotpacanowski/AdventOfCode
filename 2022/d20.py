try:
    from rich.pretty import pprint
except ImportError:
    from pprint import pprint

try:
    from tqdm import trange
except ImportError:
    trange = range


def mix_seq(ls, step, j) -> list:
    N = len(ls)
    idx = ls.index(j)  # could be a dict lookup
    i = step[j]
    if i == 0:
        return ls

    lsa = ls[:idx] + ls[idx+1:]
    if i > 0:
        k = (i // N) % (N-1)  # one number less
        lsa = lsa[k:] + lsa[:k]
        i = i % N
    else:
        k = ((-i) // N) % (N-1)  # one number less
        lsa = lsa[N-1-k:] + lsa[:N-1-k]

        # I do not trust modulo / remainder on negative numbers
        # see https://gynvael.coldwind.pl/?id=230 (in Polish, sorry)
        # tl;dr there are two approaches
        i = -((-i) % N)

    # print(f'\n[{j:2}] idx={idx:<3} step={i:<3}  -- {}')
    ls = lsa[:idx] + [j] + lsa[idx:]
    if 0 < idx + i < N and i > 0:
        #      before      after [idx]       step   after move
        ls = ls[0: idx] + ls[idx+1:idx+1+i] + [j] + ls[idx+i+1:]
    elif 0 < idx + i < N and i < 0:
        ls = ls[0: idx+i] + [j] + ls[idx+i: idx] + ls[idx+1:]
    elif idx + i == 0:
        ls = ls[:idx] + ls[idx+1:] + [j]
    elif idx + i < 0:
        split = idx + i
        ls_wo_i = ls[:idx] + ls[idx+1:split]
        ls = ls_wo_i + [j] + ls[split:]
    else:
        split = idx + i - N + 1
        ls_wo_i = ls[split:idx] + ls[idx+1:]
        ls = ls[:split] + [j] + ls_wo_i

    assert len(set(ls)) == len(ls) == N
    return ls


def solve1(inp: list[int]):
    N = len(inp)
    assert len([i for i in range(N) if inp[i] == 0]) == 1

    # list of indices
    ls = [i for i in range(N)]
    step = [x for x in inp]
    assert all(step[ls[i]] == step[i] for i in range(N))

    for j in trange(N):
        ls = mix_seq(ls, step, j)
    if len(ls) < 22:
        pprint(ls)

    zero_org_idx = inp.index(0)
    idx_zero_offset = ls.index(zero_org_idx)
    assert step[ls[idx_zero_offset]] == 0
    r = (
        step[ls[(idx_zero_offset + 1000) % N]],
        step[ls[(idx_zero_offset + 2000) % N]],
        step[ls[(idx_zero_offset + 3000) % N]],
    )
    print(r)
    return sum(r)


def solve2(inp: list[int]):
    N = len(inp)
    ls = [i for i in range(N)]
    step = [x * 811589153 for x in inp]
    for e in trange(10):
        for j in range(N):
            ls = mix_seq(ls, step, j)
    if len(ls) < 22:
        pprint(ls)

    zero_org_idx = inp.index(0)
    idx_zero_offset = ls.index(zero_org_idx)
    assert step[ls[idx_zero_offset]] == 0
    r = (
        step[ls[(idx_zero_offset + 1000) % N]],
        step[ls[(idx_zero_offset + 2000) % N]],
        step[ls[(idx_zero_offset + 3000) % N]],
    )
    print(r)
    return sum(r)


if __name__ == '__main__':
    inp = open('input/in20.txt').read()
    inp = [int(x) for x in inp.split()]
    N = len(inp)
    print(f'{len(inp)} numbers, from {min(inp)} to {max(inp)}')
    if len(inp) < 20:
        pprint(inp)
    else:
        print(inp[:5], '...')
    print('part1:', solve1(inp))
    print('part2:', solve2(inp))
