# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-27 9:58
# software: PyCharm


import os

# 获取当前项目所在目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = os.path.join(parentDirPath, "config", "PageElementLocator.ini")

# 获取数据文件存放的绝对路径
dataFilePath = os.path.join(parentDirPath, "testData", "testData.xlsx")

# 测试用例的绝对路径
testPath = os.path.join(parentDirPath, "testScripts")

# url地址
url = "http://10.16.0.78/his-common-test/#/home"
url_zysf = "http://10.16.0.78/his-common-test/#/organization"
url_hiszysf = "http://10.16.0.78/his-common-test/#/commonPannel"

# 单个元素高亮显示的时间（默认0.05秒就行）
highlight_time = 0.05


class Account(object):
    """
    testData.xlsx表的帐号工作表中，每列对应的数字序号
    """
    username = 2
    password = 3
    role = 4
    assertKeyWords = 5
    isExecute = 6
    testResult = 7

