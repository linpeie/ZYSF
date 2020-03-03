# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-03-02 17:00
# description:封装首页的对象
from util.objectMap import getElement, getElements
from util.parsePageElementLocator import ParsePageElementLocator


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parsePEL = ParsePageElementLocator()
        self.Options = self.parsePEL.getItemsSection("main_page")

    def logoutBtn(self):
        try:
            # 从定位表达式配置文件中读取定位退出的定位方式和表达式
            locateType, locatorExpression = self.Options["logoutbtn".lower()].split(">>")
            # 获取登录页面的用户名输入框页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def inoutManager(self):
        try:
            # 从定位表达式配置文件中读取住院入出转的定位方式和表达式
            locateType, locatorExpression = self.Options["inoutmanager".lower()].split(">>")
            # 获取登录页面的住院入出转页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

    def admissionCancell(self):
        try:
            # 从定位表达式配置文件中读取病人入院取消的定位方式和表达式
            locateType, locatorExpression = self.Options["admissioncancell".lower()].split(">>")
            # 获取登录页面的病人入院取消页面对象，并返回给调用者
            element = getElement(self.driver, locateType, locatorExpression)
            return element
        except Exception as e:
            raise e

