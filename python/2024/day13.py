import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Combination:
    def __init__(self, button_a, button_b, result_x, result_y):
        self.button_a = button_a
        self.button_b = button_b
        self.result_x = result_x
        self.result_y = result_y


def solve(eq):
    part_a1 = eq.button_b.y * eq.result_x - eq.button_b.x * eq.result_y
    part_a2 = eq.button_a.x * eq.button_b.y - eq.button_a.y * eq.button_b.x
    mul_a = part_a1 // part_a2
    part_b1 = eq.button_a.y * eq.result_x - eq.button_a.x * eq.result_y
    partB2 = eq.button_a.y * eq.button_b.x - eq.button_a.x * eq.button_b.y
    mul_b = part_b1 // partB2

    new_point_a = Pos(eq.button_a.x * mul_a, eq.button_a.y * mul_a)
    new_point_b = Pos(eq.button_b.x * mul_b, eq.button_b.y * mul_b)
    new_point = Pos(new_point_a.x + new_point_b.x, new_point_a.y + new_point_b.y)

    if new_point.x == eq.result_x and new_point.y == eq.result_y:
        return mul_a, mul_b
    return 0, 0


def calc1(combs):
    res = 0
    for comb in combs:
        x, y = solve(comb)
        res += x * 3 + y

    return res


def calc2(combs):
    pass

if __name__ == '__main__':
    raw = open(args.filename).read()
    combs = [] 
    pattern = r'X[+=](\d+), Y[+=](\d+)'
    arr = raw.split('\n\n')

    for a in arr:
        values = re.findall(pattern, a)
        values = [(int(v[0]), int(v[1])) for v in values]

        aX, aY = values[0]
        bX, bY  = values[1]
        rX, rY = values[2]
        combination = Combination(
            button_a=Pos(aX, aY),
            button_b=Pos(bX, bY),
            result_x=rX,
            result_y=rY
        )
        combs.append(combination)

    if args.task == 1:
        res = calc1(combs)
        print('Total tokens: ', res)

    if args.task == 2:
        res = calc2()
        print('Total tokens: ', res)
