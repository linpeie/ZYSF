# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:LPE
# datetime:2020-02-27 10:52
# description: 封装了日志输出方法
from config.varConfig import parentDirPath
import logging
import time
import os

class Log(object):

    def __init__(self):
        # 日志路径拼接
        log_path = os.path.join(parentDirPath, 'logs')
        # 如果不存在这个logs文件夹，就自动创建一个
        if os.path.exists(log_path) and os.path.isdir(log_path):
            pass
        else:
            os.mkdir(log_path)
        # 文件的命名
        self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 定义日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')
        # self.formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.log_name, encoding='utf-8')
        fh.setLevel(logging.DEBUG)      # 日志级别：DEBUG -> INFO -> WARNING -> ERROR
        # 给handler添加formatter
        fh.setFormatter(self.formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 给handler添加formatter
        ch.setFormatter(self.formatter)
        # 给logger添加handler
        self.logger.addHandler(ch)

        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    @staticmethod
    def debug(message):
        Log().__console('debug', message)

    @staticmethod
    def info(message):
        Log().__console('info', message)

    @staticmethod
    def warning(message):
        Log().__console('warning', message)

    @staticmethod
    def error(message):
        Log().__console('error', message)


if __name__ == '__main__':
    Log.debug("this is debug")
    Log.info("this is info")
    Log.warning("this is warning")
    Log.error("this is error")
