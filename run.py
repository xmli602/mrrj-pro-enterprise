#!/usr/bin/env python
#coding:utf-8

"""
@File    :   run.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   执行测试
"""
import pytest
import time
import os
import shutil
from common.log import log
from common.fileActionLib import GetFilePath
from common.printInfo import GetInfo

def custom_reports():
    log.info('==========开始定制报告==========')
    path = GetFilePath.get_file_all_path('reports/reports/Perfectresult/index.html')
    if os.path.exists(path):
        os.remove(path)
    initpath = GetFilePath.get_file_all_path('testdata/index.html')
    movePath = GetFilePath.get_file_all_path('reports/reports/Perfectresult/')
    shutil.copy(initpath, movePath)
    log.info('==========定制报告成功==========')

def run():
	try:
		log.info(GetInfo.get_start_info("茂日软件Pro企业版"))
		pytest.main(['-sv', './testcase/enterprise/base_information/test_base_information_dept.py', '--alluredir',
		             './reports/temp_allurefile', '--clean-alluredir'])
		'''
		pytest.main()：main中传入不同的指令用以执行指定测试用例
		-s: 显示程序中的print/logging输出
		-v: 丰富信息模式, 输出更详细的用例执
		-q: 安静模式, 不输出环境信息
		-k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）s
		-s,py文件路径：指定py执行
		--alluredir ./temp_allurefile  创建allure原json文件目录的位置
		'''
		time.sleep(3)
		os.system('allure generate ./reports/temp_allurefile -o ./reports/reports --clean')
		os.system('allure generate ./reports/temp_allurefile -o ./reports/reports/Perfectresult ./reports/reports --clean')
		'''
		allure generate：生成命令
		../temp：原Json文件
		-o：输出
		../reports：新生产报告的位置
		--clean：每次生成前都会清除之前的报告
		../reports/Perfectresult  本地可以出趋势图：如果要部署到jenkins可以删除掉
		'''
		# 定制报告
		custom_reports()
	except Exception as e:
		# 如有异常，相关异常发送钉钉
		log.error("执行接口自动化失败，失败原因：{}".format(e))
		# erdingtalk()
		raise

		

if __name__ == '__main__':
	
    # 执行测试
    run()