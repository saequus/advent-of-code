import pandas as pd
from utils import make_reports
from day2 import detect_safe_reports, detect_one_lvl_drop_safe_reports

DAY2_TEST_FILE_PATH = './data/day2_01_test.txt' 

def test_day2():
    reports = make_reports(DAY2_TEST_FILE_PATH)
    safe_reports = detect_safe_reports(reports)
    assert 2 == safe_reports.sum()
    dropout_results = detect_one_lvl_drop_safe_reports(reports)
    safeish_reports = pd.DataFrame(dropout_results).any()
    assert 6 ==  safeish_reports.sum()

