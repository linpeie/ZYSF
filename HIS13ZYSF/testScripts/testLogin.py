# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-28 11:24
# description:登录的测试脚本
import traceback
import unittest
from util.log import Log
from util.browser import browser
from util.parseExcel import ParseExcel
from appModules.loginAction import LoginAction
from config.varConfig import dataFilePath, Account


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.excelObj = ParseExcel()                 # 创建解析Excel对象
        cls.excelObj.loadWorkBook(dataFilePath)     # 将Excel数据文件加载到内存
        cls.driver = browser()

    def setUp(self):
        self.status = ""        # 用来存放断言失败信息，如果同种类型用例中有一个用例执行失败，则整个test置为失败！
        self.isExecuteNum = 0   # 存放总共执行的用例数
        self.successNum = 0     # 存放成功执行的用例数

    def tearDown(self):
        # self.driver.quit()
        Log.info(f"本模块共执行用例 {self.isExecuteNum} 条，其中成功 {self.successNum} 条!")
        if self.status != "":
            raise self.status

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_loginSuccess(self):
        """登录成功用例"""
        Log.info("登录成功测试开始")
        try:
            accountSheet = self.excelObj.getSheetByName("登录成功")
            isExecuteAccount = self.excelObj.getColumn(accountSheet, Account.isExecute)
            for id, data in enumerate(isExecuteAccount[1:]):
                if data.value == "y":
                    accountRow = self.excelObj.getRow(accountSheet, id + 2)
                    username = accountRow[Account.username - 1].value
                    password = accountRow[Account.password - 1].value
                    assertKeyWords = accountRow[Account.assertKeyWords - 1].value
                    Log.info("启动浏览器，访问url")
                    LoginAction.loginSuccess(self.driver, username, password)
                    try:
                        assert assertKeyWords in self.driver.page_source
                        Log.info("用户 %s 登录后，断言页面关键字“%s”成功" % (username, assertKeyWords))
                        self.isExecuteNum = self.isExecuteNum+1
                        self.successNum = self.successNum+1
                        self.excelObj.writeCell(accountSheet, "测试通过", rowNo=id+2, colNo=Account.testResult)
                    except AssertionError as e:
                        Log.warning("用户 %s 登录后，断言页面关键字“%s”失败" % (username, assertKeyWords))
                        self.isExecuteNum = self.isExecuteNum + 1
                        self.excelObj.writeCell(accountSheet, "测试不通过", rowNo=id + 2, colNo=Account.testResult)
                        raise e
        except Exception as e:
            Log.error("主程序执行过程发生异常，异常信息：%s" % traceback.format_exc())
            raise e

    def test_02_loginFail(self):
        """登录失败用例"""
        Log.info("登录失败测试开始")
        try:
            accountSheet = self.excelObj.getSheetByName("登录失败")
            isExecuteAccount = self.excelObj.getColumn(accountSheet, Account.isExecute)
            for id, data in enumerate(isExecuteAccount[1:]):
                if data.value == "y":
                    accountRow = self.excelObj.getRow(accountSheet, id + 2)
                    username = accountRow[Account.username - 1].value
                    password = accountRow[Account.password - 1].value
                    assertKeyWords = accountRow[Account.assertKeyWords - 1].value
                    Log.info("启动浏览器，访问url")
                    LoginAction.loginFail(self.driver, username, password)
                    try:
                        assert assertKeyWords in self.driver.page_source
                        Log.info("用户 %s 登录失败，断言页面关键字“%s”成功" % (username, assertKeyWords))
                        self.isExecuteNum = self.isExecuteNum + 1
                        self.excelObj.writeCell(accountSheet, "测试通过", rowNo=id + 2, colNo=Account.testResult)
                    except AssertionError as e:
                        Log.warning("用户 %s 登录失败，断言页面关键字“%s”失败" % (username, assertKeyWords))
                        self.isExecuteNum = self.isExecuteNum + 1
                        self.excelObj.writeCell(accountSheet, "测试不通过", rowNo=id + 2, colNo=Account.testResult)
                        raise e
        except Exception as e:
            Log.error("主程序执行过程发生异常，异常信息：%s" % traceback.format_exc())
            raise e
