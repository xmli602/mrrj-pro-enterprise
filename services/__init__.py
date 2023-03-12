#!/usr/bin/env python
#coding:utf-8

"""
@File    :   __init__.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   特定功能模块方法
"""

# from enterpriseService.E_login.e_login_service import *
from services.enterpriseService.E_login.e_login_service import *


def token():
    """
    获取认证信息（鉴权）
    :return: token and storid
    """

    # 账号密码登录
    user_token = e_login_by_password(ENTERPRISE_MOBILE, ENTERPRISE_PWD)

    # 获取最后一次登录企业id、token
    enterprise_id, enterprise_token = e_get_last_enterprise(user_token)

    baseRequest.set_header({'Authorization': enterprise_token})
    baseRequest.set_enterprise_id(enterprise_id)


token()