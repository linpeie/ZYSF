# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-03-02 17:02
# description:首页业务脚本

from config.varConfig import url, url_hiszysf, url_zysf
from pageObjects.mainPage import MainPage
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainAction(object):
    def __init__(self):
        print("访问首页....")

    @staticmethod
    def loginOut(driver):
        try:
            driver.get(url)
            main = MainPage(driver)
            main.logoutBtn().click()
        except Exception as e:
            raise e

    @staticmethod
    def inoutManager(driver):
        try:
            driver.get(url)
            main = MainPage(driver)
            main.inoutManager().click()
        except Exception as e:
            raise e

    @staticmethod
    def admissionCancell(driver):
        try:
            driver.get(url)
            main = MainPage(driver)
            main.admissionCancell().click()
        except Exception as e:
            raise e