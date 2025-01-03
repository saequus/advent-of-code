import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()


def find_start_positions(board):
    positions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                positions += [[i, j]]
    return positions


def is_in_range(row, col, board):
    return 0 <= row < len(board) and 0 <= col < len(board[0])


def find_trails(cur, row, col, board, trails, init_row, init_col):
    if cur == 9:
        init_key = (init_row, init_col)
        key = (row, col)
        trails.setdefault(init_key, {}).setdefault(key, True)
        return
    for (c1, c2) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if not is_in_range(row + c1, col + c2, board):
            continue
        val = board[row + c1][col + c2]
        if val == cur + 1:
            find_trails(cur + 1, row + c1, col + c2, board, trails, init_row, init_col)


def calc1(board):
    trails = {}
    positions = find_start_positions(board)
    for row, col in positions:
        find_trails(0, row, col, board, trails, row, col)

    total = 0
    for _, trail in trails.items():
        score = len(trail.keys())
        total += score

    return total


def calc2(s):
    pass


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    board = []
    for line in raw:
        l = line.replace('\n', '')
        board.append([int(_) for _ in l])

    if args.task == 1:
        res = calc1(board)
        print('Total score: ', res)

    if args.task == 2:
        res = calc2(board)
        print('[Wrong] Checksum reworked: ', res)


