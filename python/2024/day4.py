import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help="Task number which assosiated function need to perform ", type=int)
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


def find_xmas_occurrences(raw: str) -> int:
    n = 0
    for row in range(len(raw)):
        for col in range(len(raw[row])):
            n += count_words(raw, "XMAS", row, col)
    return n



if __name__ == '__main__':
    raw = open(args.filename).readlines()

    if args.task == 1:
        res = find_xmas_occurrences(raw)
        print('Xmas occurrencies: ', res)
    if args.task == 2:
        pass

