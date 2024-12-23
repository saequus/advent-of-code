

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


def get_anti_notes_positions(board: list[str], x: int, y: int, i: int, j: int):
    l_col = len(board)
    l_row = len(board[0])
    x_bigger = x > i
    y_bigger = y > j
    x_dist = x - i if x_bigger else i - x
    y_dist = y - j if y_bigger else j - y

    if x_bigger:
        a = x + x_dist
        c = i - x_dist
    else:
        a = x - x_dist
        c = i + x_dist
    if y_bigger:
        b = y + y_dist
        d = j - y_dist
    else:
        b = y - y_dist
        d = j + y_dist

    first = a, b,
    second = c, d
    if a < 0 or b < 0 or a >= l_row or b >= l_col:
        first = None, None,
    if c < 0 or d < 0 or c >= l_row or d >= l_col:
        second = None, None

    return *first, *second


def build_frequency_map(board: list[str]):
    m = {}
    col_len = len(board[0])
    for i in range(len(board)):
        for j in range(col_len):
            frequency = board[i][j]
            if frequency == '.':
                continue
            if frequency not in m:
                m[frequency] = [(i, j)]
            else:
                m[frequency].append((i, j))
    return m


def find_anti_nodes_positions_on_board(board: list[str], m: dict):
    anti_nodes_arr = []
    for fr, pos_arr in m.items():
        s1 = 0
        s2 = 0
        while s1 < len(pos_arr) - 1:
            while s2 < len(pos_arr):

                if s2 == s1:
                    pass
                else:
                    x, y = pos_arr[s1]
                    i, j = pos_arr[s2]
                    ps = get_anti_notes_positions(board, x, y, i, j)
                    if ps[0] and [ps[0], ps[1]] not in anti_nodes_arr:
                        anti_nodes_arr.append([ps[0], ps[1]])
                    if ps[2] and [ps[2], ps[3]] not in anti_nodes_arr:
                        anti_nodes_arr.append([ps[2], ps[3]])
                s2 += 1
            s1 += 1
            s2 = s1 + 1
    return anti_nodes_arr


def calc1(board: list[str]) -> int:
    frequency_map = build_frequency_map(board)
    anti_nodes_arr = find_anti_nodes_positions_on_board(board, frequency_map)
    # print('m: ', frequency_map)
    # print('anti_nodes_arr: ', anti_nodes_arr, len(anti_nodes_arr))
    return len(anti_nodes_arr)


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



