# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-27 16:55
# description:封装定位页面元素的方法

from selenium.webdriver.support.ui import WebDriverWait
from util.wrappers import *

@screenshots
@highlight
def getElement(driver, locateType, locatorExpression):
    """获取单个页面元素对象"""
    try:
        elemet = WebDriverWait(driver, 5).until(
            lambda x: x.find_element(by=locateType, value=locatorExpression))
        return elemet
    except Exception as e:
        raise e

def getElements(driver, locateType, locatorExpression):
    """获取多个页面元素对象"""
    try:
        elements = WebDriverWait(driver, 5).until(
            lambda x: x.find_elements(by=locateType, value=locatorExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == "__main__":
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    print(searchBox.tag_name)
    aList = getElements(driver, "tag name", "a")
    print(len(aList))
    time.sleep(1)
    driver.quit()
