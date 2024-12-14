import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


def calc(expected: int, params: list[int], index: int) -> bool:
    if index < 0:
        return False
    last = params[index]
    if index == 0:
        return expected == last
    if expected % last == 0 and calc(expected // last, params, index - 1):
        return True
    if expected > last and calc(expected - last, params, index - 1):
        return True
    return False


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    breakpoint_reached = False
    calibration = {}
    for line in raw:
        res, operands = line.replace('\n', '').split(':')
        res = int(res)
        operands = [int(_) for _ in operands.strip().split(' ')]
        calibration[res] = operands

    if args.task == 1:
        res = 0
        for expected_sum, values in calibration.items():
            if calc(expected_sum, values, len(values) - 1):
                res += expected_sum

        print('Total calibration result: ', res)

    if args.task == 2:
        pass
