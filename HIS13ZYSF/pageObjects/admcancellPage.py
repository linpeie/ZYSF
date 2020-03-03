# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-03-03 10:33
# description:封装病人入院取消页面的元素

from util.objectMap import getElement, getElements
from util.parsePageElementLocator import ParsePageElementLocator


class AdmcancelPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parsePEL = ParsePageElementLocator()
        self.Options = self.parsePEL.getItemsSection("admissioncancell_page")

    def zyhInput(self):
        try:
            # 从定位表达式配置文件中读取定位住院号输入框的定位方式和表达式
            locateType, locatorExpression = self.Options["zyhinput".lower()].split(">>")
            # 获取登录页面的住院号输入框页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def readCard(self):
        try:
            # 从定位表达式配置文件中读取读卡控件的定位方式和表达式
            locateType, locatorExpression = self.Options["readcard".lower()].split(">>")
            # 获取登录页面的读卡控件页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def resSet(self):
        try:
            # 从定位表达式配置文件中读取重置按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["reset".lower()].split(">>")
            # 获取登录页面的重置按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def notAdmitt(self):
        try:
            # 从定位表达式配置文件中读取定位未入科按钮
            locateType, locatorExpression = self.Options["notadmitt".lower()].split(">>")
            # 获取登录页面的未入科按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def cancellIn(self):
        try:
            # 从定位表达式配置文件中读取住院取消按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["cancellin".lower()].split(">>")
            # 获取登录页面的住院取消按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def reFresh(self):
        try:
            # 从定位表达式配置文件中读取定位住院收费按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["refresh".lower()].split(">>")
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e


if __name__ == "__main__":
    # 测试代码
    from util.browser import browser
    import time
    driver = browser()
    driver.get("http://10.16.0.78/his-zysf-test/#/cancelHosp")
    admcancell = AdmcancelPage(driver)
    admcancell.zyhInput().send_keys("00007857")
    time.sleep(1)
    admcancell.cancellIn().click()




