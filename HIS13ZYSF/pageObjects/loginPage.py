# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-27 10:11
# description:封装了登录页面的对象
from util.objectMap import getElement, getElements
from util.parsePageElementLocator import ParsePageElementLocator


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parsePEL = ParsePageElementLocator()
        self.Options = self.parsePEL.getItemsSection("login_page")

    def userNameObj(self):
        try:
            # 从定位表达式配置文件中读取定位用户名输入框的定位方式和表达式
            locateType, locatorExpression = self.Options["username".lower()].split(">>")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            # 从定位表达式配置文件中读取定位密码输入框的定位方式和表达式
            locateType, locatorExpression = self.Options["password".lower()].split(">>")
            # 获取登录页面的密码输入框页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def loginBtn(self):
        try:
            # 从定位表达式配置文件中读取定位登录按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["loginbtn".lower()].split(">>")
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def errorClose(self):
        try:
            # 从定位表达式配置文件中读取定位关闭登录错误的关闭按钮
            locateType, locatorExpression = self.Options["errorclose".lower()].split(">>")
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def loginCon(self):
        try:
            # 从定位表达式配置文件中读取定位登录按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["logincon".lower()].split(">>")
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def loginfirstSys(self):
        try:
            # 从定位表达式配置文件中读取定位住院收费按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["enterzysf".lower()].split(">>")
            # 获取登录页面的登录按钮页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def loginSys(self):
        try:
            # 从定位表达式配置文件中读取定位HIS13住院收费按钮的定位方式和表达式
            locateType, locatorExpression = self.Options["enterhiszysf".lower()].split(">>")
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
    driver.get("http://10.16.0.78/his-common-test/#/home")
    login = LoginPage(driver)
    login.userNameObj().send_keys("9999")
    login.passwordObj().send_keys("")
    time.sleep(2)
    login.loginBtn().click()
    time.sleep(2)
    login.loginCon().click()
    time.sleep(2)
    login.loginfirstSys().click()
    time.sleep(2)
    login.loginSys().click()
    driver.quit()
