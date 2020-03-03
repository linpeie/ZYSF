# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-28 10:55
# description:登录页面业务脚本

from config.varConfig import url, url_hiszysf, url_zysf
from pageObjects.loginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginAction(object):
    def __init__(self):
        print("登录....")

    def loginSuccess(driver, username, password):
        try:
            driver.get(url)
            login = LoginPage(driver)
            # main = MainPage(driver)
            if username:
                login.userNameObj().send_keys(username)
            if password:
                login.passwordObj().send_keys(password)
            login.loginBtn().click()
            time.sleep(1)
            login.loginCon().click()
            time.sleep(1)
            # 判断是否进入住院收费处的页面url_zysf,是则增加一步
            if driver.current_url == url_zysf:
                login.loginfirstSys().click()
                time.sleep(1)
                ActionChains(driver).double_click(login.loginSys()).perform()
            elif driver.current_url == url_hiszysf:
                # 鼠标双击新版His住院收费
                ActionChains(driver).double_click(login.loginSys()).perform()
            # login.userNameObj().clear()
            # login.passwordObj().clear()
            # driver.quit()
        except Exception as e:
            raise e

    def loginFail(driver, username, password):
        try:
            driver.get(url)
            login = LoginPage(driver)
            if username:
                login.userNameObj().send_keys(username)
            if password:
                login.passwordObj().send_keys(password)
            login.loginBtn().click()
            time.sleep(1)
            login.errorClose().click()
            login.userNameObj().clear()
            login.passwordObj().clear()
            # driver.quit()
        except Exception as e:
            raise e


if __name__ == "__main__":
    from util.browser import browser
    driver = browser()
    LoginAction.loginSuccess(driver, "zysf", "zysf")
    # LoginAction.loginFail(driver, "zysf", "99")
    time.sleep(2)
    driver.quit()






