# -*- coding: utf-8 -*-


import pytest
import json
from testcase import publicmethod   # 公共方法
from common.mysql import *      # 数据库模块
from common.fileActionLib import *      # 获取文件路径
from common.operationExcel import *     # excel文件操作
from common.apiCase import *      # 替换传参
from variables.enterprise_variables import *    # 请求封装
from variables.caseDesc import CaseDesc    # case对应列
from common.mysql import *      # 数据库模块



@pytest.fixture(scope='class')
def connectdb():
    """
    连接数据库
    :return: 返回一个数据库的实例对象
    """
    db = publicmethod.connectdb()
    try:
        log.info("**************-Module：开始连接数据库-**************")
        yield db
        # db.ConnectMysql.closemysql()
        db.closemysql()
        log.info("**************-Module：关闭数据库-**************")
    except Exception as e:
        log.error("**************-Module：数据库连接失败并关闭数据库-**************")
        log.error("**************-Module：失败原因：{}-**************".format(e))
        db.connectmysql.closemysql()
        raise e


@pytest.fixture(scope='class')
def get_deptdata():
    """
    新建一个部门，并返回其id
    :return: 一级部门id
    """
    try:
        log.info("===============Class：开始创建部门，并获得部门ID===============")
        get_testcase = GetExcel.ReadOneExcel(GetFilePath.get_file_all_path('testdata/数据设置/部门管理(基础数据).xlsx'), '新增', 1)
        testcase = get_testcase[0]
        parameter = eval(testcase[CaseDesc.parameter_col])
        case.name = "Auto部门-l1"
        case.parentId = "0"
        request_data = baseRequest.set_request(
            apiurl=testcase[CaseDesc.apiurl_col],
            method=testcase[CaseDesc.method_col],
            datatype=testcase[CaseDesc.datatype_col],
            body=json.loads(case.replace_data(testcase[CaseDesc.parameter_col]))
        )
        response_result = baseRequest.SendRequest(request_data)
        log.info("===============Class：成功新增部门并获得ID：{}===============".format(response_result['data']['id']))
        yield response_result['data']['id']
    except Exception as e:
        log.error("===============Class：新增部门失败===============")
        log.error("===============Class：失败原因：{}===============".format(e))
        raise e

# get_deptdata()


