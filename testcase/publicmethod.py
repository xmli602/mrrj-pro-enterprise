# -*- coding: utf-8 -*-

"""
@File    :   publicmethod.py
@Time    :   2023/03/12
@Author  :   xmL
@Contact :   13996365087@163.com
@Desc    :   公共方法
"""

from common.mysql import *      # 数据库模块
import allure       # allure报告模块
from common.operationExcel import GetExcel
from common.fileActionLib import GetFilePath

@allure.step('连接数据库')
def connectdb():
    """
    连接数据库
    :return: 返回一个数据库实例
    """
    data = eval(GetExcel.RadeCellExcel(GetFilePath.get_file_all_path('testdata/sql_info.xlsx'), 'sqlinfo', 1, 0))
    db = ConnectMysql(**data)
    return db

# connectdb()
