import unittest
import ddt
from api.student_login import StudentLogin
from common.logger import log
from common.read_excel import excelUtil

ddt_data = excelUtil.read_excel()

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stu = StudentLogin()

    @classmethod
    def tearDownClass(cls):
        pass

    @ddt.data(*ddt_data)
    # @ddt.unpack
    def test_stu_login(self, dict_data):
        """测试数据：{0}"""
        description, userId, username, passwd = dict_data["description"], dict_data["userId"], \
                                                dict_data["username"], dict_data["passwd"]
        result = self.stu.student_login(username, passwd)
        log.logger.debug("【用例名】 {} == >> 用户ID ：{}, 用户名 ：{}，密码 ：{}".format(description, userId, username, passwd))
        log.logger.debug("error_code ==>> 期望结果：{}， 实际结果：{}".format(0, result["error_code"]))
        try:
            self.assertEqual(result["error_code"], 0)
            self.assertEqual(result["login_info"]["userId"], int(userId))
            log.logger.debug("登录成功")
        except AssertionError as e:
            log.logger.debug("登录失败")
            raise AssertionError

if __name__ == '__main__':
    unittest.main()