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

def find_antennas(board, max_row, max_col):
    antennas = {}
    for row in range(max_row):
        for col in range(max_col):
            value = board[row][col]
            if value != '.':
                antennas.setdefault(value, []).append(Antenna(value, Position(row, col)))
    return antennas


def mirror(a, b, radius):
    dx = b.row - a.row
    dy = b.col - a.col
    pos_a = Position(b.row + radius * dx, b.col + radius * dy)
    pos_b = Position(a.row - radius * dx, a.col - radius * dy)
    return pos_a, pos_b


def find_anti_nodes1(antennas, max_row, max_col, anti_nodes):
    pair_of_antennas = combinations(antennas, 2)
    for pair in pair_of_antennas:
        a, b = mirror(pair[0].position, pair[1].position, 1)
        if is_in_boundaries(a.row, a.col, max_row, max_col):
            anti_nodes[(a.row, a.col)] = True
        if is_in_boundaries(b.row, b.col, max_row, max_col):
            anti_nodes[(b.row, b.col)] = True


def find_anti_nodes_in_line(antennas, max_row, max_col, anti_nodes):
    pairs = combinations(antennas, 2)
    for pair in pairs:
        radius = 1
        first_out_of_range = False
        second_out_of_range = False
        init_a, init_b = pair[0].position, pair[1].position
        anti_nodes[(init_a.row, init_a.col)] = True
        anti_nodes[(init_b.row, init_b.col)] = True
        while not first_out_of_range or not second_out_of_range:
            a, b = mirror(init_a, init_b, radius)
            if is_in_boundaries(a.row, a.col, max_row, max_col):
                anti_nodes[(a.row, a.col)] = True
            else:
                first_out_of_range = True
            if is_in_boundaries(b.row, b.col, max_row, max_col):
                anti_nodes[(b.row, b.col)] = True
            else:
                second_out_of_range = True
            radius += 1


def calc1(board: list[str]):
    result = 0
    max_row = len(board)
    max_col = len(board[0])
    antennas = find_antennas(board, max_row, max_col)
    anti_nodes = {}
    for sub_antennas in antennas.values():
        find_anti_nodes1(sub_antennas, max_row, max_col, anti_nodes)

    result += len(anti_nodes)
    return result

def calc2(board: list[str]):
    anti_nodes = {}
    max_row = len(board)
    max_col = len(board[0])
    antennas = find_antennas(board, max_row, max_col)
    for sub_antennas in antennas.values():
        find_anti_nodes_in_line(sub_antennas, max_row, max_col, anti_nodes)

    return len(anti_nodes)



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
        res = calc2(board)
        print('Total anti nodes number expanding lines: ', res)
