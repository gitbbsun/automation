#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:50
# @Author  : bbsun
# @File    : demo2.py
# @Software: PyCharm

import unittest, time, os
from selenium import webdriver
from MyProjects.common.util import set_log
import win32con
import win32api
path = os.getcwd().split('cases')[0]


class Test_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://pre.svocloud.com")
        set_log("=====================测试截图包括console内容开始=====================")

        #https: // blog.csdn.net / xie_0723 / article / details / 51456266

        win32api.keybd_event(123, 0, 0, 0)
        win32api.keybd_event(123, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)

        set_log("F12按起来")
        time.sleep(10)

    def test_login1(self):
        """1：正确用户名、密码，登录成功"""
        self.driver.find_element_by_xpath("//input[@type='text']").clear()
        self.driver.find_element_by_xpath("//input[@type='text']").send_keys("12508781@qq.com")
        self.driver.find_element_by_xpath("//input[@type='password']").click()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys("1112333")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)

        self.driver.get_screenshot_as_file(path + '\\resultpang\\测试.png')
        self.driver.quit()

    # def tearDown(self):
    #     self.driver.quit()
