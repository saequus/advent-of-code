import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('-t', '--task', help='Task number which associated function need to execute', type=int)
args = parser.parse_args()


def prepare_rules(rules: list[str]) -> dict:
    rules_storage = {}
    for rule in rules:
        rule = rule.replace('\n', '')
        key1, key2 = rule.split('|')
        key = (key1, key2)
        if key not in rules_storage:
            rules_storage[key] = 1
    return rules_storage


def compare(left, right, rules):
    return rule_valid(left, right, rules)


def sort_items(itms, rules):
    for init in range(len(itms) - 1):
        for inner in range(len(itms) - init - 1):
            if not compare(itms[inner], itms[inner + 1], rules):
                itms[inner], itms[inner + 1] = itms[inner + 1], itms[inner]


def rule_valid(left: int, right: int, rules: list[list[int]]):
    for i in range(len(rules)):
        if left == rules[i][0] and right == rules[i][1]:
            return True
    return False


def is_in_order(input: list, rules: list):
    for i in range(len(input)-1):
        left, right = input[i], input[i + 1]
        if not rule_valid(left, right, rules):
            return False
    return True


def sum_fixed_pages_median(rules: list[str], pages: list[str]) -> int:
    result = 0
    itms = []
    for page in pages:
        a = [int(_) for _ in page.replace('\n', '').split(',')]
        itms.append(a)

    rules_as_arr = []
    for rule in rules:
        prev, nxt = [int(_) for _ in rule.split("|")]
        rules_as_arr.append([prev, nxt])

    for i in range(len(itms)):
        if not is_in_order(itms[i], rules_as_arr):
            sort_items(itms[i], rules_as_arr)
            mid = len(itms[i]) // 2
            result += itms[i][mid]

    return result


def sum_valid_pages_median(rules: list[str], pages: list[str]) -> int:
    rules = prepare_rules(rules)
    valid_pages = []
    for page in pages:
        arr = page.replace('\n', '').split(',')
        i = 0
        invalid_page = False
        while i < len(arr) - 1 and not invalid_page:
            j = i + 1
            while j < len(arr) and not invalid_page:
                if (arr[j], arr[i]) in rules:
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
        res = sum_fixed_pages_median(rules, pages)

        print('Fixed pages median sum: ', res)
