import pandas as pd


def make_reports(file: str) -> pd.DataFrame:
    raw_inputs = [tuple(map(int, line.split())) for line in open(file).readlines()]
    reports = pd.DataFrame(raw_inputs).T
    return reports


def is_in_boundaries(row, col, max_rows, max_cols):
    return 0 <= row < max_rows and 0 <= col < max_cols


def combinations(arr, size):
    combs = []
    def generate(current, start, combination):
        if len(combination) == size:
            combs.append(combination[:])
            return
        for i in range(start, len(current)):
            generate(current, i+1, combination + [current[i]])
    generate(arr, 0, [])
    return combs
