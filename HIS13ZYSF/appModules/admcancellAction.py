# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-03-03 10:31
# description:入院取消业务脚本

from config.varConfig import url, url_hiszysf, url_zysf
from pageObjects.admcancellPage import AdmcancelPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time


class admcancellAction(object):
    def __init__(self):
        print("病人入院取消....")

    @staticmethod
    def inputzyhCancle(driver, zyh000):
        """输入住院号入院取消"""
        try:
            driver.get(url)
            admcancel = AdmcancelPage(driver)
            if zyh000:
                admcancel.zyhInput().send_keys(zyh000)
                # 输入住院号后回车返回病人信息
                admcancel.zyhInput().send_keys(Keys.ENTER)
            time.sleep(1)
            admcancel.cancellIn().click()
        except Exception as e:
            raise e

    def readcardCancle(driver):
        """从读卡选择病人进行入院取消"""
        try:

        except Exception as e:
            raise e

    def readcardCancle(driver):
        """从未入科选择病人进行入院取消"""
        try:

        except Exception as e:
            raise e

if __name__ == "__main__":
    from util.browser import browser
    driver = browser()
    LoginAction.loginSuccess(driver, "zysf", "zysf")
    # LoginAction.loginFail(driver, "zysf", "99")
    time.sleep(2)
    driver.quit()






