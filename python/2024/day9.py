import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


def get_checksum(arr, end) -> int:
    checksum = 0
    for i in range(end+1):
        checksum += arr[i] * i
    return checksum


def build_memory(s):
    mem = []
    for i in range(len(s)):
        repeats = int(s[i])
        if i % 2 == 0:
            mem += repeats * [i // 2]
        else:
            mem += repeats * [-1]
    return mem


def calc1(s):
    mem = build_memory(s)

    end = len(mem) - 1
    start = 0
    while start < end:
        val = mem[start]
        if val == -1:
            while start < end and mem[end] == -1:
                end -= 1
            if start < end:
                mem[start], mem[end] = mem[end], -1
            end -= 1
        start += 1

    return get_checksum(mem, end)


def calc2(s):
    mem = build_memory(s)
    end = len(mem) - 1
    start = 0
    while start < end:
        val = mem[start]
        if val == -1:
            while start < end and mem[end] == -1:
                end -= 1
            if start < end:
                start_i, end_i = start, end
                cur = mem[end_i]
                check = True
                while mem[start_i] == -1 and check:
                    if mem[end_i] == cur:
                        start_i += 1
                        end_i -= 1
                    else:
                        check = False
                if mem[end_i] != cur:
                    for k in range(start, start_i):
                        mem[k] = cur
                    for k in range(end_i+1, end+1):
                        mem[k] = -1
                    
            end -= 1
        start += 1
    return get_checksum(mem, end)


if __name__ == '__main__':

    raw = open(args.filename).readlines()[0]

    if args.task == 1:
        res = calc1(raw)
        print('Checksum: ', res)

    if args.task == 2:
        res = calc2(raw)
        print('[Wrong] Checksum reworked: ', res)


