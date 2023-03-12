# -*- coding: utf-8 -*-


import allure
from common.log import log  # 日志层

class ResponseAssert(object):
    '''
    断言封装
    '''

    @allure.step("相等断言结果")
    def eq(self, Actualresults, Expectedresults):
        '''

        :param Actualresults: 实际结果
        :param Expectedresults: 预期结果
        :return: 返回PASSED或者Fail
        '''

        try:
            log.info(f'Response实际结果为：{Actualresults}')
            log.info(f'Response预期结果为：{Expectedresults}')
            assert str(Actualresults) == str(Expectedresults) # 成立返回TURE，失败返回FALSE
            log.info('*********** 通过! ***********')
        except AssertionError as e:
            log.error(f'断言不通过，Rseponse实际结果为：{Actualresults}，Response预期结果为：{Expectedresults}')
            log.error('*********** 不通过! ***********')
            raise e

    @allure.step("包含断言结果")
    def ct(self, Actualresults, Expectedresults):
        """
        :param ar: 实际结果
        :param er: 预期结果
        :return: 返回PASSED或者Fail
        """
        try:
            log.info(f'Response实际结果为：{Actualresults}')
            log.info(f'Response预期结果为：{Expectedresults}')
            assert str(Actualresults) in str(Expectedresults)  # 成立返回TURE，失败返回FALSE
            log.info('*********** 通过! ***********！')
        except AssertionError as e:
            log.error(f'断言不通过，Response实际结果为：{Actualresults}，Response预期结果为：{Expectedresults}')
            log.error('*********** 不通过! ***********')
            raise e

    @staticmethod
    def assert_str(node, value, exp_value):
        """断言封装 node 为断言的节点, value为节点的值, exp_value 为期望值"""
        str1 = '%s value is :%s ; \n excepted value is : %s' % (node, value, exp_value)
        space_list = [{}, None, "NULL", [], ""]
        if type(value) is float:
            value = float("%.5f" % value)
        if type(exp_value) is float:
            exp_value = float("%.5f" % exp_value)
        if exp_value == '':
            exp_value = space_list
            assert value in exp_value, str1
        else:
            assert value == exp_value, str1
