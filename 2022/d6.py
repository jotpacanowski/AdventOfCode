
def start_of_packet(packet: str):
    for i in range(len(packet) - 4+1):
        chunk = packet[i:i+4]
        assert len(chunk) == 4
        if len(set(chunk)) == len(chunk):
            print(f'part1:', i+4)
            return


def start_of_message(packet: str):
    for i in range(len(packet) - 14+1):
        chunk = packet[i:i+14]
        assert len(chunk) == 14
        if len(set(chunk)) == len(chunk):
            print(f'part2:', i+14)
            return


if __name__ == '__main__':
    lines = open('input/in6.txt').read().splitlines()
    start_of_packet(lines[0])
    start_of_message(lines[0])
