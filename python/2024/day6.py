import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function to execute', type=int)
args = parser.parse_args()

DIRECTIONS_NXT_DIR_MAP = {
    'top': 'right',
    'right': 'bottom',
    'bottom': 'left',
    'left': 'top'
}


def find_current_position(board):
    direction = None
    i = j = cur_i = cur_j = 0
    line_len = len(board[0])
    found = False
    while i < len(board) and not found:
        while j < line_len and not found:
            if board[i][j] == '^':
                direction = 'top'
                found = True
                cur_i, cur_j = i, j
            if board[i][j] == '>':
                direction = 'right'
                found = True
                cur_i, cur_j = i, j
            if board[i][j] == 'v':
                direction = 'bottom'
                found = True
                cur_i, cur_j = i, j
            if board[i][j] == '<':
                direction = 'left'
                found = True
                cur_i, cur_j = i, j
            j += 1
        j = 0
        i += 1
    return direction, cur_i, cur_j


def find_paths(board, direction, i, j):
    visited = {}
    border_reached = False
    while len(board) > i > 0 and 0 < j < len(board) - 1 and not border_reached:
        visited[i, j] = ''
        match direction:
            case 'top':
                border_reached = i <= 0
                if border_reached:
                    pass
                elif board[i-1][j] == '#':
                    direction = DIRECTIONS_NXT_DIR_MAP[direction]
                    j += 1
                else:
                    i -= 1
            case 'right':
                border_reached = j + 1 > len(board[i]) - 1
                if border_reached:
                    pass
                elif board[i][j+1] == '#':
                    direction = DIRECTIONS_NXT_DIR_MAP[direction]
                    i += 1
                else:
                    j += 1
            case 'bottom':
                border_reached = i + 1 > len(board) - 1
                if border_reached:
                    pass
                elif board[i+1][j] == '#':
                    direction = DIRECTIONS_NXT_DIR_MAP[direction]
                    j -= 1
                else:
                    i += 1
            case 'left':
                border_reached = j <= 0
                if border_reached:
                    pass
                elif board[i][j-1] == '#':
                    direction = DIRECTIONS_NXT_DIR_MAP[direction]
                    i -= 1
                else:
                    j -= 1
    return visited


def visualize(board: list[str], visited: dict):
    output = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) in visited:
                output += 'X'
            else:
                output += board[i][j]
        output += '\n'


def predict_guard(board: list[str]):
    init_direction, init_i, init_j = find_current_position(board)
    visited = find_paths(board, init_direction, init_i, init_j)
    # visualize(board, visited)

    return len(visited.keys())


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    breakpoint_reached = False
    lines = []
    for line in raw:
        lines.append(line.replace('\n', ''))

    if args.task == 1:
        res = predict_guard(lines)

        print('The guard visited tiles: ', res)

    if args.task == 2:
        pass
