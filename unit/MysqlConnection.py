# -*- coding: utf-8 -*-

'''
# @Time    : 2021-06-01 
# @Author  : sang
# @FileName: MysqlConnection.py
# @Software: PyCharm

'''
import pymysql
import sys
sys.path.append('D:/pythons_test')
from configparser import ConfigParser

"""
@功能：创建数据库连接池
"""
class get_mysqlconn:
    def __init__(self):
        pass

    def get_conn(self,source):
        cp = ConfigParser()
        # 这里使用的是绝对路径，切换到服务器需要修改
        cp.read('D:/pythons_test/unit/db.cfg')
        conn = pymysql.connect(host=cp.get(source,'host'),
                            port=int (cp.get(source,'port')),
                            user=cp.get(source,'user'),
                            passwd=cp.get(source,'passwd'),
                            db=cp.get(source,'db'))					
        return conn
