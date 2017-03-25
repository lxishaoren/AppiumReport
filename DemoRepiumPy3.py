#!/usr/bin/env python3
# coding=utf-8
from appium import webdriver
from nose.tools import *
import time
from time import sleep
import unittest
import HtmlTestRunner #生成HTML格式的测试报告

#装饰器
class take_screen_shot():
    def __init__(self,func):
        self.func = func
        # date_time = time.strftime('%Y-%m-%d_%H-%M',time.localtime(time.time()))
        self.name = func.__name__ + ' (__main__.EduTestCase).png'
        

    def __call__(self,*args):
        try:
            self.func(self,*args)
        finally:
            driver.get_screenshot_as_file(self.name)

class EduTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        desired_caps = {}
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'WEY6R16426001169'
        desired_caps['appPackage'] = 'com.leoet.edu'
        desired_caps['appActivity'] = 'com.leoet.edu.ui.LoginActivity'
        # desired_caps['app'] = PATH("E:\Test_pad\Cepin_PAD\Tests_akp\Debug-20170215.apk")
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        sleep(3)
        # 名密码点击登录
        # name = self.driver.find_element_by_id("com.leoet.edu:id/et_account")
        # name.click()
        # name.send_keys('zhuzhe')
        # psw = self.driver.find_element_by_id("com.leoet.edu:id/et_pwd")
        # psw.send_keys('123456')
        # self.driver.find_element_by_id("com.leoet.edu:id/btn_login").click()
        # driver.find_element_by_id('com.leoet.edu:id/btn_test').click()
    @classmethod
    def tearDown(self):
        driver.quit()

    @take_screen_shot  #每条测试用例使用截图装饰器
    def test_login(self):
        name = driver.find_element_by_id("com.leoet.edu:id/et_account")
        name.click()
        name.send_keys('zhuzhe')
        psw = driver.find_element_by_id("com.leoet.edu:id/et_pwd")
        psw.send_keys('123456')
        driver.find_element_by_id('btn_login').click()
        sleep(10)
        text = driver.find_element_by_id('tv_admin').text()
        assertEqual(text,u'你好，管理员')



if __name__ == '__main__':   
    suite = unittest.TestLoader().loadTestsFromTestCase(EduTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)                                     
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='EduLoginReport',report_title='MyReport'))