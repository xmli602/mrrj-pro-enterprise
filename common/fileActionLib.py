#!/usr/bin/env python
#coding:utf-8

"""
@File    :   fileActionLib.py
@Time    :   2023/01/28
@Author  :   zhuoyan
@Contact :   18108347985@163.com
@Desc    :   获取文件路径
"""

import os

class FileActionLib(object):

    @staticmethod
    def get_file_all_path(filepath: str):
        """
        :param filepath: 文件相对路径
        :return: 文件的全路径
        """
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 测试数据基础目录
        return os.path.join(project_dir, filepath)

# 实例化
GetFilePath = FileActionLib()