# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-28 9:53
# description: 用于解析存储定位页面元素的定位表达式文件

from configparser import ConfigParser
from config.varConfig import pageElementLocatorPath


class ParsePageElementLocator(object):

    cf = ConfigParser()
    cf.read(pageElementLocatorPath, encoding='UTF-8')

    def getItemsSection(self, sectionName):
        # 获取配置文件中指定section下的所有option键值对
        # 并以字典类型返回给调用者

        # 注意：使用self.cf.items(sectionName)此种方法获取到的配置文件中的options内容均被转换成小写，
        # 比如，loginPage.frame 被转换成loginpage.frame

        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self, sectionName, optionName):
        # 获取指定section下的指定option的值

        value = self.cf.get(sectionName, optionName)
        return value


if __name__ == '__main__':
    pc = ParsePageElementLocator()
    print(pc.getItemsSection("kh_login"))
    print("=======================")
    print(pc.getOptionValue("kh_login", "loginPage.username"))
