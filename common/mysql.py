# -*- coding: utf-8 -*-


# 导入模块
import pymysql
import random
from common.log import log  # 日志层
import allure
from pymysql import converters


class ConnectMysql(object):
    @allure.step('连接数据库')
    def __init__(self, **kwargs: dict):
        """
        连接数据库
        :param kwargs: 需要的参数
        """
        try:
            converions = converters.conversions
            converions[pymysql.FIELD_TYPE.BIT] = lambda data: '1' if data == '\x01' else '0'
            self.connectmysql = pymysql.connect(charset='utf8', conv=converions, **kwargs)
            self.cursor = self.connectmysql.cursor(cursor=pymysql.cursors.DictCursor)  # 游标
            log.info(f'数据库连接成功，连接参数为：{kwargs}')
        except Exception as e:
            log.error(f'数据库连接失败，连接参数为：{kwargs}')
            log.error(f'错误原因：{e}')
            raise e

    @allure.step('操作数据库：插入数据')
    def insert(self, sql: str):
        """
        :param sql: 插入数据sql语句 -->   insert into 表名(字段) values(值)
        :return: 新增数据
        """
        try:
            log.info(f"insert sql:{sql}")
            self.cursor.execute(sql)  # 操作
            self.connectmysql.commit()  # 进行提交保存
        except Exception as e:
            log.error(f'error Reason：{e}')
            raise e

    @allure.step('操作数据库：插入数据（多条）')
    def insert_many(self, sql: str, args: str):
        """
        :param sql: 插入多条数据sql语句 -->   insert into 表名(字段) values(值)
        :param args: values(值)
        :return: 新增数据
        """
        try:
            log.info(f"insert_many sql:{sql}")
            self.cursor.executemany(query=sql, args=args)  # 操作
            self.connectmysql.commit()  # 进行提交保存
        except Exception as e:
            log.error(f'error Reason：{e}')
            raise e

    @allure.step('操作数据库：更新数据')
    def update(self, sql: str):
        """
        :param sql: update数据sql语句 -->   UPDATE 表名 SET Sname=%s（args） WHERE Sno = %s（args）
        :return:    更新数据
        """
        try:
            log.info(f"update sql:{sql}")
            self.cursor.execute(sql)  # 操作
            self.connectmysql.commit()  # 进行提交保存
        except Exception as e:
            log.error(f'error Reason：{e}')
            raise e

    @allure.step('操作数据库：删除数据')
    def delete(self, sql: str):
        """
        :param sql: 删除delete数据sql语句 -->   DELETE FROM 表 WHERE Sno = %s（args）
        :return:    删除数据
        """
        try:
            log.info(f"delete sql:{sql}")
            self.cursor.execute(sql)  # 操作
            self.connectmysql.commit()  # 进行提交保存
        except Exception as e:
            log.error(f'error Reason：{e}')
            raise e

    @allure.step('操作数据库：查询数据（单个数据）')
    def select(self, sql: str):
        """
        :param sql: 查询select数据sql语句 -->   SELECT * FROM 表
        :return:    查询数据
        """
        try:
            log.info(f"select sql:{sql}")
            self.connectmysql.commit()  # 进行提交保存
            self.cursor.execute(sql)  # 操作
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            log.error(f'error Reason：{e}')
            raise e

    @allure.step('操作数据库：查询数据（多个数据）')
    def selects(self, sql: str):
        """
        :param sql: 查询select数据sql语句 -->   SELECT * FROM 表
        :return:    查询数据
        """
        try:
            log.info(f"selects sql:{sql}")
            self.connectmysql.commit()  # 进行提交保存
            self.cursor.execute(sql)  # 操作
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            log.error(f'error Reason：{e}')
            raise e

    @allure.step('关闭数据库')
    def closemysql(self):
        """
        关闭数据库
        :return: 关闭数据库
        """
        self.cursor.close()
        self.connectmysql.close()
        log.info("Success Close Mysql")

# 实例化
# connectmysql = ConnectMysql()