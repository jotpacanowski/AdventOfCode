#!/usr/bin/python3

def parse_input(inp):
    st = []
    r = []
    for line in inp.splitlines():
        if line.strip():
            st.append(int(line))
        else:
            r.append(st)
            st = []
    return r


def main(inp):
    print(max(sum(x) for x in inp))
    seq = [sum(x) for x in inp]
    seq.sort(reverse=True)
    print(seq[:3])
    print(sum(seq[:3]))


if __name__ == '__main__':
    inp = open('in1.txt').read()

    main(parse_input(inp))
