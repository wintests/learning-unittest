import unittest
import time,os
from config.settings import REPORT_PATH,TESTCASE_PATH
from common.HTMLTestRunnerCN import HTMLTestReportCN

def get_all_cases():
    "获取所有测试用例"
    testcases = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=TESTCASE_PATH,
        pattern="test*.py",
        top_level_dir=None
    )
    testcases.addTests(discover)
    return testcases

def run_all_cases(testcases):
    "执行所有用例"
    now_time = time.strftime("%Y%m%d%H%M%S")
    report_file = os.path.join(REPORT_PATH, "Report_{}.html".format(now_time))
    fp = open(report_file, "wb")  # 以二进制写入方式打开
    runner = HTMLTestReportCN(
        stream=fp,
        title="自动化测试报告",
        tester="wintest",
        description="详细描述",
    )
    runner.run(testcases)
    fp.close()

if __name__ == '__main__':
    testcases = get_all_cases()
    run_all_cases(testcases)
