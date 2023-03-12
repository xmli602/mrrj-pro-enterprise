#!/usr/bin/env python
#coding:utf-8

"""
@File    :   baseRequests.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   请求封装
"""

import allure
import requests
from common.log import log

class BaseRequests(object):
    def __init__(self,url):
        """
        Session：通过session方法快速关联session
        """
        self.Session = requests.session()
        self.url = url
        self.header = {}
        self.enterprise_id=""

    def _printResponse(self, response):
        """
        :param response: 请求头部信息
        :return: 返回json响应信息（Body）
        """
        try:
            print('------------HTTP Response  *   header ----------')
            print('URL:' + response.url)
            for self.i, self.v in response.headers.items():
                print('{}:{}'.format(self.i, self.v))
            print('Code:' + str(response.status_code))
            print('------------HTTP Response  *   information ----------')
            print('Body：' + response.content.decode('utf-8'))
            log.info('Body：' + response.content.decode('utf-8'))
            print('------------HTTP Response  *   end ----------\n\n')
            return response.json()
        except Exception as e:
            log.error("Request Error：{}".format(e))

    @allure.step('发起请求')
    def SendRequest(self, data: dict):
        """
        开始发起请求
        :param data: 请求参数 来源于request源码方法
        :return:  接口返回数据，所有的接口请求都可以用
        """
        try:
            response = requests.request(**data, timeout=(300, 600), verify=False)  # 传入多个参数**data根据参数进行自动匹配
            log.info(f'SendRequest Success, RequestBody：{data}')
            self._printResponse(response)
            return response.json()
        except Exception as e:
            log.error(f'SendRequest Error, RequestBody：{data}')
            log.error(f'Error Reason：{e}')
            raise e
        
    def set_request(self, apiurl: str, method: str, datatype=None, body=None):
        """
        请求体
        :return: data
        """
        data = {
            'url': self.url + apiurl,
            'method': method,
            'headers': self.header,
            '{}'.format(datatype): body
        }
        return data
    
    def set_header(self,header):
        self.header = header
    
    def set_enterprise_id(self,enterprise_id):
        self.enterprise_id = enterprise_id
        
    