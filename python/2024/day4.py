import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function need to perform ', type=int)
args = parser.parse_args()


def is_word(board, word, row, row_dir, column, column_dir):
    for _, char in enumerate(word):
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[row]):
            return False
        value = board[row][column]
        if value != char:
            return False
        row += row_dir
        column += column_dir
    return True


def count_words(board, word, row, column):
    count = 0
    directions = [-1, 0, 1]
    for row_dir in directions:
        for col_dir in directions:
            if is_word(board, word, row, row_dir, column, col_dir):
                count += 1
    return count


def find_xmas_occurrences(raw: list[str]) -> int:
    n = 0
    for row in range(len(raw)):
        for col in range(len(raw[row])):
            n += count_words(raw, 'XMAS', row, col)
    return n


def is_x_shape(b):
    middle = b[1][1] == 'A'
    lefttop = (b[0][0] == 'M' and b[2][2] == 'S') or (b[0][0] == 'S' and b[2][2] == 'M')
    righttop = (b[0][2] == 'M' and b[2][0] == 'S') or (b[0][2] == 'S' and b[2][0] == 'M')

    if middle and lefttop and righttop:
        return 1
    return 0


def build_sm_boards(board):
    SM_BOARD_SIZE = 3
    rows = len(board)
    cols = len(board[0])
    sm_boards = []

    for i in range(rows - SM_BOARD_SIZE + 1):
        for j in range(cols - SM_BOARD_SIZE + 1):
            sm_board = [[board[i+x][j+y] for y in range(SM_BOARD_SIZE)] for x in range(SM_BOARD_SIZE)]
            sm_boards.append(sm_board)
    return sm_boards


def count_x_mas(board):
    count = 0
    for sm_board in build_sm_boards(board):
        count += is_x_shape(sm_board)
    return count


if __name__ == '__main__':
    raw = open(args.filename).readlines()

    if args.task == 1:
        res = find_xmas_occurrences(raw)
        print('Xmas occurrencies: ', res)
    if args.task == 2:
        res = count_x_mas(raw)
        print('Xmas shape occurrencies: ', res)
