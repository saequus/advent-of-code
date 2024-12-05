import pandas as pd
from utils import make_reports
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-t', '--task', help='Task number which assosiated function need to perform ', type=int)
args = parser.parse_args()


def detect_safe_reports(reports: pd.DataFrame) -> pd.Series:
    report_diffs = reports.diff()
    null_ok = report_diffs.isna()
    increases = (null_ok | (report_diffs > 0)).all()
    decreases = (null_ok | (report_diffs < 0)).all()
    diff_le_3 = (null_ok | (report_diffs.abs() <= 3)).all()
    safe_reports = (increases | decreases) & diff_le_3
    assert isinstance(safe_reports, pd.Series)
    return safe_reports

def detect_one_lvl_drop_safe_reports(reports: pd.DataFrame) -> pd.Series:
    dropout_results = []
    for i in range(reports.shape[0]):
        dropout = reports.drop(i)
        safe_dropout = detect_safe_reports(dropout)
        dropout_results.append(safe_dropout)
    return dropout_results


if __name__ == '__main__':
    reports = make_reports(args.filename)

    if args.task == 1:
        safe_reports = detect_safe_reports(reports)
        n_safe_reports = safe_reports.sum()
        print('Safe reports number:', n_safe_reports)
    
    if args.task == 2:
        dropout_results = detect_one_lvl_drop_safe_reports(reports)
        safeish_reports = pd.DataFrame(dropout_results).any()
        n_safeish_reports = safeish_reports.sum()
        print('One-level-down safe reports number:', n_safeish_reports)
