from MyProjects.common import util
from MyProjects.page.Login_Page import *
from selenium import webdriver
import unittest, os, win32api, win32con
from ddt import data, ddt

path = os.getcwd().split('cases')[0]
case_path = path + '\\data\\case.xlsx'
case_datas = util.get_case_data(case_path, 0)
print(case_datas)



# TODO 优化代码   元素定位

# TODO 需要深入学习ddt、yaml、pytest   12：31
# TODO 1 截图将浏览器console中内容截图下来
@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_fun = Login_test(self.driver)
        time.sleep(3)
        win32api.keybd_event(123, 0, 0, 0)
        win32api.keybd_event(123, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
        time.sleep(3)

    def login_verify(self, name, pwd, assert_value):
        self.re_data = self.login_fun.login(name, pwd)
        if (self.re_data == "账号或密码有误"):
            util.set_log("账号或密码有误")
            time.sleep(2)
            self.driver.get_screenshot_as_file(path + '\\resultpang\\%s.png' % self.name)
        else:
            self.re_data = "登录成功"
            util.set_log("登录成功")
        self.assertEqual(self.re_data, assert_value)

    @data(*case_datas)
    def test_login(self, case_data):
        if (case_data['skip'] == 0):
            self.name = case_data['username']
            self.pwd = case_data['pwd']
            self.assert_value = case_data['assert']
            self.login_verify(self.name, self.pwd, self.assert_value)
        else:
            unittest.TestCase.skipTest(self, "skip this case")

    # def test_loginB(self):
    #     """2：用户登录-错误用户名，正确密码，登录失败"""
    #     if (case_datas[1]['skip'] == 0):
    #         self.name = case_datas[1]['username']
    #         self.pwd = case_datas[1]['pwd']
    #         self.assert_value = case_datas[1]['assert']
    #         self.login_verify(self.name, self.pwd, self.assert_value)
    #     else:
    #         unittest.TestCase.skipTest(self, "skip this case")
    #
    # def test_loginC(self):
    #     """3：用户登录-正确用户名，错误密码，登录失败"""
    #     if (case_datas[2]['skip'] == 0):
    #         self.name = case_datas[2]['username']
    #         self.pwd = case_datas[2]['pwd']
    #         self.assert_value = case_datas[2]['assert']
    #         self.login_verify(self.name, self.pwd, self.assert_value)
    #     else:
    #         unittest.TestCase.skipTest(self, "skip this case")

    def tearDown(self):
        self.driver.quit()
