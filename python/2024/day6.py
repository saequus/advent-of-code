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
    i = j = 0
    line_len = len(board[0])
    found = False
    while i < len(board) and not found:
        while j < line_len and not found:
            if board[i][j] == '^':
                found = True
                return 'top', i, j
            if board[i][j] == '>':
                found = True
                return 'right', i, j
            if board[i][j] == 'v':
                found = True
                return 'bottom', i, j
            if board[i][j] == '<':
                found = True
                return 'left', i, j
            j += 1
        j = 0
        i += 1



def find_paths(board, direction, i, j):
    visited = {}
    visited_with_dir = {}
    border_reached = False
    while len(board) > i > 0 and 0 < j < len(board) - 1 and not border_reached:
        if (i, j) not in visited:
            visited[i, j] = {'times': 1}
            visited_with_dir[i, j, direction] = False
        else:
            visited[i, j] = {'times': visited[i, j]['times'] + 1}
            nxt_dir = DIRECTIONS_NXT_DIR_MAP[direction]
            if (i, j, nxt_dir) in visited_with_dir:
                visited_with_dir[i, j, nxt_dir] = True

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
    return visited, visited_with_dir


def visualize(board: list[str], visited: dict, visited_with_dir: dict):
    output = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            marked = False
            if (i, j, 'top') in visited_with_dir:
                if visited_with_dir[i, j, 'top']:
                    output += 'T'
                    marked = True
            elif (i, j, 'left') in visited_with_dir:
                if visited_with_dir[i, j, 'left']:
                    output += 'L'
                    marked = True
            elif (i, j, 'bottom') in visited_with_dir:
                if visited_with_dir[i, j, 'bottom']:
                    output += 'B'
                    marked = True
            elif (i, j, 'right') in visited_with_dir:
                if visited_with_dir[i, j, 'right']:
                    output += 'R'
                    marked = True

            if (i, j) in visited and not marked:
                output += 'X'
            elif not marked:
                output += board[i][j]

        output += '\n'
    print(output)

def predict_guard(board: list[str]):
    init_direction, init_i, init_j = find_current_position(board)
    visited, visited_with_dir = find_paths(board, init_direction, init_i, init_j)
    # visualize(board, visited, visited_with_dir)

    return len(visited.keys())


def count_loops(board: list[str]):
    init_direction, init_i, init_j = find_current_position(board)
    visited, visited_with_dir = find_paths(board, init_direction, init_i, init_j)
    # visualize(board, visited, visited_with_dir)

    return sum(visited_with_dir.values())


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
        res = count_loops(lines)

        print('Solution not yet found ^-^: ', res)
