# -*- coding: utf-8 -*-

'''
# @Time    : 2020-06-01
# @Author  : sang
# @FileName: WriteFile.py
# @Software: PyCharm

'''

# 这里的饿写入文件，需要连接数据库返回云西状态
import time
import sys
from MysqlConnection import get_mysqlconn


class writefile():
    # 系统时间获取



    def write_file_day(self,LOG_FILE,sql_commands,start_dt):
        sysCurDate=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))

        #打开数据库连接
        db = get_mysqlconn().get_conn("local")

        #创建游标对象
        cursor = db.cursor()
        fo = open(LOG_FILE, "a")
        fo.write(('\n{}开始执行{}数据加载日志:\n').format(sysCurDate,start_dt))
        for sql_command in sql_commands:
            fo.write(sql_command+';\n')
            fo.flush()
            result = cursor.execute(sql_command+';\n')
            fo.flush()
            if result == 'error':
                 sys.exit()
        fo.close()
        db.commit()
        print('is ok')
        db.close()

    def write_file_total(selef,LOG_FILE,sql_commands):
        sysCurDate=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        start_dt = time.strftime('%Y.%m.%d',time.localtime(time.time()))
        #打开数据库连接
        db = get_mysqlconn().get_conn("local")

        #创建游标对象
        cursor = db.cursor()
        fo = open(LOG_FILE, "a")

        for sql_command in sql_commands:
            # print(sql_command)
            fo.write(('\n{}开始执行{}数据加载日志:\n').format(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())),start_dt))
            fo.write(sql_command+';\n')
            fo.flush()
            # try:
            result = cursor.execute(sql_command+';\n')
            db.commit()
            fo.write(('\n{}结束执行{}数据加载日志:\n').format(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())),start_dt))
            fo.flush()
            # print(result)
        # sys.exit()
            # except pymysql.Error as e:
            #     print(e)
            #     fo.write(str(e)+';\n')
            #     fo.flush()
            #     sys.exit()
        # print('is ok')
        db.close()
        fo.close()

