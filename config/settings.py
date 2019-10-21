import os

# 项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 项目URL
BASE_URL = "http://api.nnzhp.cn"
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
# 定义用例路径
TESTCASE_PATH = os.path.join(BASE_PATH, "testcases")
# 定义测试报告路径
REPORT_PATH = os.path.join(BASE_PATH, "report")
if not os.path.exists(REPORT_PATH):
    os.mkdir(REPORT_PATH)
# 定义Excel路径
EXCEL_PATH = os.path.join(BASE_PATH, "data", "stu_info.xlsx")