from pathlib import PurePosixPath

from pprint import pprint


def parse_input(lines: list[str]):

    cwd = PurePosixPath('/')

    dirs = []
    files = []

    for line in lines:
        if line.startswith('$ '):
            match line[2:4]:
                case 'cd':
                    newd = line[5:]
                    if newd == '..':
                        cwd = cwd.parent
                    else:
                        cwd = cwd / PurePosixPath(newd)
                    # match newd:
                    #     case '/':
                    #         cwd = PurePosixPath(newd)
                    #     case '..'
                case 'ls':
                    ...  # next lines are only for `ls``
                case _:
                    print("bad line: ", line)
        else:
            size, filename = line.split(' ', 1)
            fullpath = cwd / filename
            if size == 'dir':
                # :)
                dirs.append(fullpath)
            else:
                # file
                size = int(size)
                # print(f'file')
                # filename.relative_to(PurePosixPath('/'))
                files.append((fullpath, size))

    # pprint(dirs)
    # pprint(files)

    # find dirs with total size "of at most 100_000"
    dirsizes = dict()
    for i in sorted(dirs, key=lambda x: -len(x.parts)):
        # print('\ndir ', i)
        sumsz = 0
        for f, fsz in files:
            # if f.is_relative_to(i):
            if i in f.parents:
                # print('file ', f)
                sumsz += fsz
        # for dk, dv in dirsizes.items():
        #     if dk.is_relative_to(i):
        #         sumsz += dv

        dirsizes[i] = sumsz
    dirsizes[PurePosixPath('/')] = sum(fsz for f, fsz in files)
    # pprint(dirsizes)

    r = 0
    for v in dirsizes.values():
        if v <= 100_000:
            r += v
    print('part1:', r)

    return dirs, files, dirsizes


def main2(dirs, files, dirsizes):
    total_sz = 70_000_000
    needed = 30_000_000
    total_new = total_sz - needed
    root = dirsizes[PurePosixPath('/')]
    for k, v in sorted(dirsizes.items(), key=lambda x: x[1]):
        if root - v <= total_new:
            print(k, root-v)
            break
    print('part2:', dirsizes[k])


TEST = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

if __name__ == '__main__':
    lines = open('input/in7.txt').read().splitlines()
    # lines = TEST.splitlines()
    dirs, files, dirsizes = parse_input(lines)
    main2(dirs, files, dirsizes)
