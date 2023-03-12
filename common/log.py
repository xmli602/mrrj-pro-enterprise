#!/usr/bin/env python
#coding:utf-8

"""
@File    :   __init__.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   
"""

import logging
import os
from logging.handlers import RotatingFileHandler
import colorlog

log_colors_config = {
   "DEBUG": "bold_blue",
   "INFO": "bold_green",
   "WARNING": "bold_yellow",
   "ERROR": "bold_red",
   "CRITICAL": "bold_purple",
}

class Log(object):
    """
    日志封装
    """
    def __init__(self, logname='LogFile'):
        self.logname = os.path.join('%s' % logname)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)1.1s %(log_color)s%(asctime)s%(reset)s| %(message_log_color)s%(levelname)-8s %(reset)s| %("
            "log_color)s[%(filename)s%(reset)s:%(log_color)s%(module)s%(reset)s:%(log_color)s%(funcName)s%("
            "reset)s:%(log_color)s%(""lineno)d] %(reset)s- %(log_color)s%(message)s", reset=False, log_colors=log_colors_config,
            secondary_log_colors={
                "message": {
                    "DEBUG": "bold_blue",
                    "INFO": "bold_green",
                    "WARNING": "bold_yellow",
                    "ERROR": "bold_red",
                    "CRITICAL": "bold_purple"
                }
            },
            style="%"
        )  # 日志输出格式

        # 创建一个FileHandler，用于写到本地
        fh = logging.handlers.TimedRotatingFileHandler(self.logname, when='MIDNIGHT', interval=1, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(logging.Formatter('%(asctime)s | %(filename)s[line:%(lineno)d] | %(levelname)s: %(message)s'))
        self.logger.addHandler(fh)
        # 创建一个StreamHandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def get_logger(self):
        """
        获取logger日志对象（栈）
        :return:日志对象
        """
        return self.logger

# 实例化
log = Log().get_logger()