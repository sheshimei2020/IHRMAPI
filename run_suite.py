# 导包
import os
import time
import unittest
import HTMLTestRunner_PY3
import app
from script.test_ihrm_login import UnittestTestIHRM
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(UnittestTestIHRM))

# 定义测试报告的目录和报告的名称
report_path = BASE_DIR + "/report/IHRM{}.html".format(time.strftime('%Y%m%d%H%M%S'))
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_path,'wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title='IHRM登录接口功能测试',
                                               description='ihrm登录模块测试报告')
    runner.run(suite)