import pandas as pd


def make_reports(file: str) -> pd.DataFrame:
    raw_inputs = [tuple(map(int, line.split())) for line in open(file).readlines()]
    reports = pd.DataFrame(raw_inputs).T
    return reports
