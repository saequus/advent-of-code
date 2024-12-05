
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function need to perform ', type=int)
args = parser.parse_args()


def sum_valid_pages_median(rules: list[str], pages: list[str]) -> int:
    store = {}
    for rule in rules:
        rule = rule.replace('\n', '')
        key1, key2 = rule.split('|')
        key = (key1, key2)
        if key not in store:
            store[key] = 1

    valid_pages = []
    for page in pages:
        arr = page.replace('\n', '').split(',')
        i = 0
        invalid_page = False
        while i < len(arr) - 1 and not invalid_page:
            j = i + 1
            while j < len(arr) and not invalid_page:
                if (arr[j], arr[i]) in store:
                    invalid_page = True
                j += 1
            i += 1
        if not invalid_page:
            valid_pages.append(arr)

    total = 0
    for page in valid_pages:
        total += int(page[len(page) // 2])

    return total


if __name__ == '__main__':
    raw = open(args.filename).readlines()
    breakpoint_reached = False
    rules = []
    pages = []
    for line in raw:
        if line == '\n':
            breakpoint_reached = True
            continue
        if breakpoint_reached:
            pages.append(line)
        else:
            rules.append(line)

    if args.task == 1:

        res = sum_valid_pages_median(rules, pages)

        print('Valid pages median sum: ', res)

    if args.task == 2:
        pass
