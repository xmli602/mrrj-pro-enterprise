#!/usr/bin/env python
#coding:utf-8

"""
@File    :   __init__.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   
"""

class CaseDesc(object):
	index_col = 0 # ID
	apiname_col=1 # 模块/接口名称
	casetitle_col=2 # 用例标题
	desc_col=3 # 描述
	casenature_col=4 # 用例性质
	priority_col=5 # 优先级
	apiurl_col=6 # 接口地址
	datatype_col=7 # 请求参数类型
	method_col=8 # 请求方式
	preconditions_col=9 # 前置条件
	parameter_col=10 # 请求参数
	header_col=11 # 请求头
	step_col=12 # 步骤
	Epresulets_code_col=13 # 预期结果code
	Epresulets_msg_col=14 # 预期结果message
	Epresulets_db_col=15 # 预期结果数据库
	whether_sql_col=16 # 是否需要执行数据库
	assertsign_col=17 # 断言标记assertmarker
	whether_postposition=18	# 是否需要后置
	