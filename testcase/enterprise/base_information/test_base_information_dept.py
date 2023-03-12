#!/usr/bin/env python
# coding:utf-8

"""
@File    :   test_base_information_dept.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   数据设置-部门设置
"""

import pytest
import json

from variables.enterprise_variables import *
from common.operationExcel import GetExcel
from common.fileActionLib import GetFilePath
from variables.enterprise_variables import *
from variables.caseDesc import CaseDesc
from common.Assert import * 	# 断言模块
from services.enterpriseService.E_fixture import *
from common.apiCase import 	case	# 参数替换
from common.mysql import *		 # 数据库模块

@allure.epic('茂日Pro企业版：数据设置')  # allure报告一级目录
@allure.feature('部门设置')  # allure报告二级目录
class TestBaseInformationDept(object):
	'''
	数据设置-部门设置
	'''

	@allure.story('新增部门') # story：三级目录，一般描述具体接口功能目录
	# 缺陷等级：blocker：中断缺陷  critical：临界缺陷  normal：普通缺陷  minor：次要缺陷  trivial：轻微缺陷
	@allure.severity(allure.severity_level.BLOCKER)
	# @pytest.mark.parametrize参数化装饰器：传参1：对象名称  2：文件路径
	@pytest.mark.parametrize('case_info', GetExcel.ReadAllExcel(GetFilePath.get_file_all_path('testdata/数据设置/部门管理(基础数据).xlsx'), '新增'))
	def test_dept_add(self,case_info, connectdb, get_deptdata):
		"""
		        部门接口/新增接口
		        :param storetoken： 前置：获取登录门店后的token和门店ID
		        :param connectdb： 前置：连接数据库
		        :param caseinfo： 参数化变量（部门接口/新增接口测试用例）
		        :return: 成功新增部门
		        """
		# ID、模块/接口名称、用例标题、描述、用例性质、优先级、接口地址、请求参数类型、请求方式、前置条件
		# 请求参数、请求头、步骤、预期结果code、预期结果message、预期结果name、预期结果数据库、sql、断言标记assertmarker、postposition后置
		index, api_name, case_title, desc, case_nature, priority, \
		api_url, data_type, method, preconditions, parameter, header, step, except_code, \
		except_message, except_data, sql, assert_mark, post_position = case_info
		allure.dynamic.title(case_title)  # 用例标题
		allure.dynamic.description(desc)  # 用例描述
		db = connectdb
		case.name = "Auto部门"
		case.parentId = "0"
		if preconditions == '1、登陆门店；2、需要一级部门ID':
			case.name = 'Auto部门-l2'
			case.parentId = get_deptdata
		with allure.step(step):
			request_data = baseRequest.set_request(
				apiurl=api_url,
				method=method,
				datatype=data_type,
				body=json.loads(case.replace_data(parameter)))
			response_results = baseRequest.SendRequest(request_data)
			ResponseAssert().eq('{}{}'.format('Code: ', response_results['code']),
								'{}{}'.format('Code: ', except_code))		# 响应断言：code
			ResponseAssert().eq('{}{}'.format('Code: ', response_results['message']),
								'{}{}'.format('Code: ', except_message))  	# 响应断言：message
			if sql == '是' and assert_mark == 0:
				except_data = case.replace_data(except_data)
				except_data = eval(except_data)
				deptdata = db.select(f"SELECT * FROM mrkj_store_service.store_service_dept "
									 f"WHERE id = {response_results['data']['id']} and is_delete = 0 order by create_time desc")
				ResponseAssert().eq('{}{}'.format('部门名称: ', deptdata['name']),
									'{}{}'.format('部门名称: ', except_data['name']))		# 数据库结果校验：部门是否新增成功
				ResponseAssert().eq('{}{}'.format('上级ID: ', deptdata['parent_id']),
									'{}{}'.format('上级ID: ', except_data['parentId']))  # 数据库结果校验：部门父级id是否正确
			# return response_results



# if __name__ == '__main__':
#     pytest.main(['-sv', '/testcase/enterprise/base_information/test_base_information_dept.py'])