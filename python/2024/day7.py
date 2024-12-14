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


def calc2(expected: int, params: list[int], index: int) -> bool:
    if index < 0:
        return False
    last = params[index]
    if index == 0:
        return expected == last
    if expected % last == 0 and calc2(expected // last, params, index - 1):
        return True
    if expected > last and calc2(expected - last, params, index - 1):
        return True

    expected_as_str = str(expected)
    lastparam_as_str = str(last)

    if len(expected_as_str) > len(lastparam_as_str) and expected_as_str.endswith(lastparam_as_str):
        new_target = int(expected_as_str[:-len(lastparam_as_str)])
        return calc2(new_target, params, index - 1)

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
        res = 0
        for expected_sum, values in calibration.items():
            if calc2(expected_sum, values, len(values) - 1):
                res += expected_sum

        print('Total calibration result with concatenation operator: ', res)




