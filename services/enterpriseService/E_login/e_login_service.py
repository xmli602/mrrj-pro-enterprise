#!/usr/bin/env python
#coding:utf-8

"""
@File    :   e_login_service.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   注册登录
"""
import allure
import json
from common.operationExcel import GetExcel
from variables.caseDesc import CaseDesc
from common.fileActionLib import GetFilePath
from common.operationExcel import GetExcel
from common.apiCase import case
from variables.enterprise_variables import *

@allure.step('企业：账号密码登录')
def e_login_by_password(username,password):
	'''
	账号密码登录
	:param username: 账号
	:param password: 密码
	:return: 用户登录token
	'''
	try:
		log.info("**************账号密码登录：开始-**************")
		case_info = GetExcel.ReadOneExcel(GetFilePath.get_file_all_path("testdata/注册登录/注册登录.xlsx"), "账号密码登录", 1)[0]
		case.mobile = username
		case.password = password
		request_data = baseRequest.set_request(
			apiurl=case_info[CaseDesc.apiurl_col],
			method=case_info[CaseDesc.method_col],
			datatype=case_info[CaseDesc.datatype_col],
			body=json.loads(case.replace_data(case_info[CaseDesc.parameter_col])))
		response_results = baseRequest.SendRequest(request_data)
		user_token= response_results["data"]["access_token"]
		log.info("**************-账号密码登录成功，返回用户登录token-**************->{}".format(user_token))
		return user_token
	except Exception as e:
		log.error("**************-账号密码登录失败-**************=")
		log.error("**************-失败原因：{}-**************".format(e))
		raise e
	

@allure.step('企业：获取最后登录企业id与token')
def e_get_last_enterprise(user_token):
	'''
	获取最后登录企业id与token
	:param user_token:
	:return: 企业id、企业token
	'''
	try:
		log.info("**************开始获取最后登录企业id与token-**************")
		baseRequest = BaseRequests(url=ENTERPRISE_URL)
		baseRequest.set_header({'Authorization': user_token})
		case_info = GetExcel.ReadOneExcel(GetFilePath.get_file_all_path("testdata/注册登录/注册登录.xlsx"), "获取最后一次登录的企业", 1)[0]
		request_data = baseRequest.set_request(
			apiurl=case_info[CaseDesc.apiurl_col],
			method=case_info[CaseDesc.method_col],
			datatype=case_info[CaseDesc.datatype_col],
			body=json.loads(case.replace_data(case_info[CaseDesc.parameter_col])))
		response_results = baseRequest.SendRequest(request_data)
		enterprise_id = response_results["data"]["enterpriseInfo"]["id"]
		enterprise_token = response_results["data"]["token"]["access_token"]
		log.info("**************成功获取最后登录企业id与token-**************{}->{}".format(enterprise_id, enterprise_token))
		return enterprise_id, enterprise_token
	except Exception as e:
		log.error("**************获取最后登录企业id与token失败-**************=")
		log.error("**************失败原因：{}-**************".format(e))
		raise e