import numpy as np
try:
    from rich.pretty import pprint
except ImportError:
    # TODO: mypy "error" about "incompatible" pprint functions
    from pprint import pprint


def solve1(mat):
    p1 = len(mat)*2 + len(mat[0])*2 - 4

    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[0])-1):
            up = mat[:i, j].max()
            down = mat[i+1:, j].max()
            left = mat[i, :j].max()
            right = mat[i, j+1:].max()
            if min(up, down, left, right) < mat[i, j]:
                p1 += 1
    print('part1:', p1)


def solve2(mat: np.ndarray):
    def line_of_sight(trees: np.ndarray, h: int) -> int:
        r = 0
        m = 0
        for t in trees:
            r += 1
            if t >= h:
                break
        return r

    def p2_score(r: int, c: int) -> int:
        # nonlocal mat
        up = mat[:r, c][::-1]
        down = mat[r+1:, c]
        left = mat[r, :c][::-1]
        right = mat[r, c+1:]
        if False and (r, c) == (3, 2):
            print((r, c))
            print(up, down, left, right)
            print('')
            print(line_of_sight(up, mat[r, c]))
            print(line_of_sight(down, mat[r, c]))
            print(line_of_sight(left, mat[r, c]))
            print(line_of_sight(right, mat[r, c]))

        return (1
                * line_of_sight(up, mat[r, c])
                * line_of_sight(down, mat[r, c])
                * line_of_sight(left, mat[r, c])
                * line_of_sight(right, mat[r, c])
                )

    print('part2:', max(p2_score(i, j)
                        for i in range(1, len(mat)-1)
                        for j in range(1, len(mat[0])-1)
                        ))


TEST = """30373
25512
65332
33549
35390"""

if __name__ == '__main__':
    lines = open('input/in8.txt').read().splitlines()
    # lines = TEST.splitlines()
    mat = np.array([
        [int(x) for x in ln]
        for ln in lines
    ])
    pprint(mat)
    solve1(mat)
    solve2(mat)
