# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name ：     screenshots.py
   Description :    用于截图并保存在logs\screenshots目录下
   Author :         FHQI
   date ：          2019-07-19
-------------------------------------------------
"""

import time
import os
from config.varConfig import parentDirPath
from util.log import Log


def get_screenshots(driver):
    try:
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
        screenshots_name = os.path.join(screenshots_path, 'error_%s.png' % current_time)
        driver.get_screenshot_as_file(screenshots_name)
        Log.info("截图保存路径：%s" % screenshots_name)
    except Exception as e:
        Log.error("截图失败：%s" % e)


if __name__ == '__main__':
    from util.browser import browser
    dr = browser()
    get_screenshots(dr)
    time.sleep(1)
    dr.quit()
