# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-03-02 9:27
# description: 执行测试主入口：执行测试 —> 生成报告 —> 发送包含测试报告的邮件
import unittest
import os
from config.varConfig import testPath, parentDirPath, dataFilePath
from util.HTMLTestRunner_Chart import HTMLTestRunner
from util.mail import Email


def report_name():
    report_path = os.path.join(parentDirPath, 'report')
    if os.path.exists(report_path) and os.path.isdir(report_path):
        pass
    else:
        os.mkdir(report_path)
    # name = os.path.join(report_path, '%s.html' % time.strftime('%Y-%m-%d_%H%M%S'))
    name = os.path.join(report_path, 'result.html')
    return name


if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(testPath, pattern='test*.py', top_level_dir=None)
    with open(report_name(), 'wb') as reportFile:
        runner = HTMLTestRunner(stream=reportFile,
                                verbosity=2,
                                title="新版HIS住院收费报告",
                                description=None,
                                retry=1,
                                save_last_try=True)
        runner.run(discover)

    # 发送邮件
    email = Email(server="smtp.qq.com",
                  sender="477600080@qq.com",
                  password="wrwbgenqxymscaia",
                  receiver="746346983@qq.com",
                  title="新版HIS住院收费测试报告",
                  message="这是本次的测试报告，请查收！",
                  path=[dataFilePath,
                        os.path.join(parentDirPath, "report", "result.html"),
                        os.path.join(parentDirPath, "report", "result.json")])
    email.send()

