# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-27 10:49
# software: PyCharm
import time
import os
from config.varConfig import parentDirPath, highlight_time
from util.log import Log


def highlight(func):
    """单个元素高亮"""
    def apply_style(driver, element):
        js1 = "arguments[0].style.border='3px solid red'"
        js2 = "arguments[0].style.border=''"
        # 定位到元素后，执行js样式
        driver.execute_script(js1, element)
        time.sleep(highlight_time)
        driver.execute_script(js2, element)

    def wrapper(*args, **kwargs):
        element = func(*args, **kwargs)
        apply_style(args[0], element)
        return element

    return wrapper


def highlights(func):
    """多个元素高亮"""
    def apply_style(driver, elements):
        js1 = "arguments[0].style.border='3px solid red'"
        js2 = "arguments[0].style.border=''"
        for element in elements:
            driver.execute_script(js1, element)
            driver.execute_script(js2, element)

    def wrapper(*args, **kwargs):
        elements = func(*args, **kwargs)
        apply_style(args[0], elements)
        return elements

    return wrapper


def screenshots(func):
    """元素截图装饰器"""
    def screen_shot(driver, middle_name):
        screenshots_path = os.path.join(parentDirPath, 'logs\\screenshots')
        # 如果不存在这个screenshots文件夹，就自动创建一个
        if os.path.exists(screenshots_path) and os.path.isdir(screenshots_path):
            pass
        else:
            os.mkdir(screenshots_path)
        # 文件的命名
        now = int(time.time())  # 显示为时间戳
        time_array = time.localtime(now)
        current_time = time.strftime("%Y%m%d%H%M%S", time_array)
        screenshots_name = os.path.join(screenshots_path, 'element_%s_%s.png' % (middle_name, current_time))
        driver.save_screenshot(screenshots_name)
        Log.info("截图保存路径：%s" % screenshots_name)

    def wrapper(*args, **kwargs):
        try:
            element = func(*args, **kwargs)
            return element
        except Exception as e:
            screen_shot(args[0], args[-1])
            raise e
    return wrapper
