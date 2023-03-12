#!/usr/bin/env python
#coding:utf-8

"""
@File    :   printInfo.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   打印信息
"""

class PrintInfo(object):
	def get_start_info(self,project_name):
		info = """
			                             _    _         _      _____         _
			              __ _ _ __ (_)  / \\  _   _| |_ __|_   _|__  ___| |_
			             / _` | '_ \\| | / _ \\| | | | __/ _ \\| |/ _ \\/ __| __|
			            | (_| | |_) | |/ ___ \\ |_| | || (_) | |  __/\\__ \\ |_
			             \\__,_| .__/|_/_/   \\_\\__,_|\\__\\___/|_|\\___||___/\\__|
			                  |_|
			                  开始执行{}...
			                """.format(project_name)
		return info
	
GetInfo = PrintInfo()