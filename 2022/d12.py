import matplotlib.pyplot as plt
import numpy as np
# from rich.pretty import pprint


def elevation(x: str) -> int:
    if 'a' <= x <= 'z':
        return ord(x) - ord('a')
    elif x == 'S':
        return 0
    elif x == 'E':
        return ord('z') - ord('a')
    else:
        raise ValueError(f'{x=}')


def solve(input: list[str], part: int):
    inp = np.array([list(y) for y in input])
    # pprint(inp)
    mape = np.array([list(map(elevation, y)) for y in input])
    # pprint(mape)

    fig, ax = plt.subplots(3, 1, constrained_layout=True, sharex=True)
    ax[0].set_title('map elevation')
    ax[0].imshow(mape)
    # plt.show()

    q = []

    pos_S = None
    for ri, r in enumerate(inp):
        for ci, c in enumerate(r):
            if c == 'S':
                pos_S = ri, ci
                print(f'start: {ri} -> {ci}')
            elif c == 'E':
                pos_E = ri, ci
                print(f'  end: {ri} -> {ci}')

            if part != 1 and c in ('a', 'S'):
                q.append((ri, ci))

    if part == 1:
        q = [pos_S]
    visited = set()
    queued = set()
    D = dict.fromkeys(q, 0)  # distance from Start
    prev = dict.fromkeys(q, None)

    while q:  # and pos_E not in D:
        cur = q.pop(0)
        visited.add(cur)
        for (i, j) in ((-1, 0), (1, 0), (0, 1), (0, -1),):
            assert abs(i) + abs(j) == 1
            if not (0 <= cur[0]+i < len(input)
                    and 0 <= cur[1]+j < len(input[0])):
                continue
            n = cur[0]+i, cur[1]+j

            if n in visited or n in queued:
                continue
            if D.get(n, float('inf')) < 1 + D[cur]:
                continue

            if (mape[n] == mape[cur]
                or mape[n] - 1 == mape[cur]
                    or mape[n] < mape[cur]):
                D[n] = 1 + D[cur]
                # push_back()
                q.append(n)
                queued.add(n)
                prev[n] = cur

    print(f'part{part}:', D[pos_E])
    ax[1].set_title(f'Path length from [S]tart'
                    if part == 1 else 'Path length from any [a]')
    ax[1].imshow(np.array([
        [D.get((i, j), -1) for j in range(len(input[0]))]
        for i in range(len(input))
    ]))

    p = pos_E
    path = []
    print(prev[pos_S])
    while p is not None:
        path.append(p)
        p = prev[p]
    path.append(p)
    # if len(path) < 32:
    #     pprint(path)
    ax[2].set_title(f'Path - part {part}')
    ende = D[pos_E]

    def mapi(p):
        try:
            return path.index(p)
        except ValueError:
            return -5
    ax[2].imshow(np.array([
        [mapi((i, j))
         for j in range(len(input[0]))]
        for i in range(len(input))
    ]))
    plt.savefig(f'debug/d12-p{part}.png', dpi=200)
    print(f'# wrote debug/d12-p{part}.png')


TEST = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

if __name__ == '__main__':
    inp = open('input/in12.txt').read()
    # inp = TEST
    inp = inp.splitlines()
    if len(inp) < 15:
        # pprint(inp)
        print(*inp, sep='\n')
    print(f'{len(inp[0])} by {len(inp)}')
    solve(inp, part=1)
    solve(inp, part=2)
