import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


def blink_for_new_setup(stones, n):
    def insert_or_update(s, key, val):
        if key in s:
            s[key] += val
        else:
            s[key] = val

    while n > 0:
        new = {}
        for k, v in stones.items():
            if k == 0:
                insert_or_update(new, 1, v)
            elif len(str(k)) % 2 == 0:
                mid = len(str(k)) // 2
                first, second = int(str(k)[:mid]), int(str(k)[mid:])
                insert_or_update(new, first, v)
                insert_or_update(new, second, v)
            else:
                insert_or_update(new, k * 2024, v)
        n -= 1
        stones = new

    res = sum(stones.values())
    return res



def calc1(stones):
    new_stones_count = blink_for_new_setup(stones, 25)
    return new_stones_count


def calc2(stones):
    new_stones_count = blink_for_new_setup(stones, 75)
    return new_stones_count


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    l = raw[0].replace('\n', '').split(' ')
    l = {int(_): 1 for _ in l}

    if args.task == 1:
        res = calc1(l)
        print('Total stones num: ', res)

    if args.task == 2:
        res = calc2(l)
        print('Total stones num: ', res)
