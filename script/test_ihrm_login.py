# 导入unittest和requests
import unittest, requests
# 创建测试类
from parameterized import parameterized

from utils import read_login_data


class UnittestTestIHRM(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    # 销毁
    def tearDown(self):
        pass


    @parameterized.expand(read_login_data())
    # 定义测试函数
    def test01_login(self,case_name,request_body,message):

        # 准备请求数据
        data = request_body
        # 发送请求并接受结果
        response = requests.post(url=self.login_url,json=data)
        # 打印结果
        print(response.json())
        # 断言
        self.assertIn(message,response.json().get("message"))
