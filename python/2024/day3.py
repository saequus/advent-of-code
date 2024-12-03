import sys

def sum_of_multiplications(s: str) -> int:
    print(len(s))
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
    file = sys.argv[1]

    raw = open(file).readlines()
    if isinstance(raw, list):
        raw = ''.join(raw)

    res = sum_of_multiplications(raw)
    
    print('Multiplications sum after deciphering: ', res)

