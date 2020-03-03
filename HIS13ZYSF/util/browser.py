# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-27 14:43
# description:封装了启动浏览器的方法

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def browser():
    """启动谷歌浏览器"""
    # 创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    # 向Options实例中添加禁用扩展插件的设置参数项
    chrome_options.add_argument("--disable-extensions")
    # 添加屏蔽 --ignore-certificate-errors 提示信息的设置参数项
    chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    # 添加浏览器最大化的设置参数项，一启动就是最大化
    chrome_options.add_argument("--start-maximized")
    # 启动带有自定义设置的浏览器
    driver = webdriver.Chrome(options=chrome_options)
    # 设置一个隐性等待时间
    driver.implicitly_wait(2)
    return driver

if __name__ == "__main__":
    import time
    driver = browser()
    driver.get("http://baidu.com")
    time.sleep(2)
    driver.quit()

