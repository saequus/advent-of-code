import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


def blink_for_new_setup(stones, n):
    if n == 0:
        return stones
    
    new = []
    for i in range(len(stones)):
        stone = stones[i]
        if int(stone) == 0:
            new.append('1')
        elif len(stone) % 2 == 0:
            st_len = len(stone) // 2
            first, second = int(stone[:st_len]), int(stone[st_len:])
            new.append(str(first))
            new.append(str(second))
        else:
            new.append(str(int(stone) * 2024))
    
    return blink_for_new_setup(new, n - 1)
    


def calc1(l):
    stones = l.split(' ') 

    new_stones_setup = blink_for_new_setup(stones, 25)

    return len(new_stones_setup)


def calc2(s):
    pass


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    for line in raw:
        l = line.replace('\n', '')

    if args.task == 1:
        res = calc1(l)
        print('Total stones num: ', res)

    if args.task == 2:
        res = calc2(l)
        print('[Wrong] Checksum reworked: ', res)


