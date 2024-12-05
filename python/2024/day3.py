import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-t', '--task', help='Task number which associated function need to perform ', type=int)
args = parser.parse_args()


def sum_of_multiplications_extra_istructions(s: str) -> int:
    total = 0
    index = 0
    execute = True
    while index < len(s):
        if s[index:index+7] == "don't()":
            execute = False
        if s[index:index+4] == 'do()':
            execute = True

        if s[index:index+4] == 'mul(':
            start = index + 4
            end = start
            comma_encountered = False
            max_end = end + 7  # 2 * 3 digits numbers + comma 
            consecutive_digits = 0
            while (s[end] == ',' or s[end].isdigit()) and consecutive_digits < 4 and s[end] != ')' and end < max_end:
                if s[end] == ',':
                    consecutive_digits = 0
                    comma_encountered = True
                else:
                    consecutive_digits += 1
                end += 1
            if s[end] == ')' and comma_encountered:
                numbers_str = s[start:end]
                numbers = [int(num) for num in numbers_str.split(',')]
                total += numbers[0] * numbers[1] if execute else 0
        index += 1
    return total


def sum_of_multiplications(s: str) -> int:
    total = 0
    index = 0
    while index < len(s):
        if s[index:index+4] == 'mul(':
            start = index + 4
            end = start
            comma_encountered = False
            max_end = end + 7  # 2 * 3 digits numbers + comma 
            consecutive_digits = 0
            while (s[end] == ',' or s[end].isdigit()) and consecutive_digits < 4 and s[end] != ')' and end < max_end:
                if s[end] == ',':
                    consecutive_digits = 0
                    comma_encountered = True
                else:
                    consecutive_digits += 1
                end += 1
            if s[end] == ')' and comma_encountered:
                numbers_str = s[start:end]
                numbers = [int(num) for num in numbers_str.split(',')]
                total += numbers[0] * numbers[1]
        index += 1
    return total


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    if isinstance(raw, list):
        raw = ''.join(raw)

    if args.task == 1:
        res = sum_of_multiplications(raw)
        print('Multiplications sum after deciphering: ', res)
    if args.task == 2:
        res = sum_of_multiplications_extra_istructions(raw)
        print('Multiplications sum with extra instruction after deciphering: ', res)

    

