import argparse
from utils import is_in_boundaries, combinations

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col


class Antenna:
    def __init__(self, name, position):
        self.name = name
        self.position = position


def mirror(a, b, radius):
    dx = b.row - a.row
    dy = b.col - a.col
    pos_a = Position(b.row + radius * dx, b.col + radius * dy)
    pos_b = Position(a.row - radius * dx, a.col - radius * dy)
    return pos_a, pos_b


def print_matrix(anti_nodes, max_rows, max_cols):
    for row_idx in range(max_rows):
        for col_idx in range(max_cols):
            if Position(row_idx, col_idx) in anti_nodes:
                print("#", end="")
            else:
                print(".", end="")
        print()


def find_anti_nodes1(antennas, max_rows, max_cols, anti_nodes):
    pair_of_antennas = combinations(antennas, 2)
    for pair in pair_of_antennas:
        a, b = mirror(pair[0].position, pair[1].position, 1)
        if is_in_boundaries(a.row, a.col, max_rows, max_cols):
            anti_nodes[(a.row, a.col)] = True
        if is_in_boundaries(b.row, b.col, max_rows, max_cols):
            anti_nodes[(b.row, b.col)] = True


def calc1(board: list[str]):
    result = 0
    antennas = {}
    max_rows = len(board)
    max_cols = len(board[0])
    for row in range(max_rows):
        for col in range(max_cols):
            value = board[row][col]
            if value != ".":
                antennas.setdefault(value, []).append(Antenna(value, Position(row, col)))
    anti_nodes = {}
    for sub_antennas in antennas.values():
        find_anti_nodes1(sub_antennas, max_rows, max_cols, anti_nodes)

    result += len(anti_nodes)
    return result


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    board = []
    for line in raw:
        l = line.replace('\n', '')
        board.append(l)

    if args.task == 1:
        res = calc1(board)
        print('Total anti nodes number: ', res)

    if args.task == 2:
        pass


