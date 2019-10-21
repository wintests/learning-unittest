import requests
import urllib3
urllib3.disable_warnings()
from config.settings import BASE_URL

class StudentLogin():

    def __init__(self):
        self.baseUrl = BASE_URL
        # 设置请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    # 模拟登录，并返回 response
    def student_login(self, username, passwd):
        login_url = self.baseUrl + "/api/user/login"
        body = {
            "username": username,
            "passwd": passwd
        }
        res = requests.post(login_url, headers = self.headers, data = body)
        return res.json()

if __name__ == '__main__':
    stu = StudentLogin()
    res = stu.student_login(username="用户名", passwd="密码")
    print(res)