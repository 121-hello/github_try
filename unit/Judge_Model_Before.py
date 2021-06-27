# -*- coding: utf-8 -*-

'''
# @Time    : 2020-10-26 15:49
# @Author  : jiangsh
# @FileName: Judge_Model_Before.py
# @Software: PyCharm

'''
import os
import re
import sys
sys.path.append("/bs_bidata")
import pymysql
from bs_bidata.utils.MysqlConnection import get_mysqlconn
#打开数据库连接
conn = get_mysqlconn().get_conn("113_dba")

class juddeModel:


    def __init__(self):
        pass

    def date_before(self,tb_name_bf,db,tb_name):
        sql = "select 1 from {}.{} where date(sys_time) = date(now()) limit 1".format(db,tb_name)
        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchone()
        res = str(result).replace("(","").replace(",)","").replace("None","0")
        print("{} {}.{}".format(int(res),db,tb_name))
        if int(res) == 0:
            print(tb_name_bf + "上级项目：" + db + "_" + tb_name + "执行失败")
            os._exit()
            b = os.popen('ps -aux | grep {}'.format(tb_name_bf)).read()
            ls = b.split('\n')
            for i in ls:
                if 'listviewsite' in i:
                    c = re.search('(?sm)\w*\s*(\d*)', i)
                    # os.system() 运行 Linux 命令没有返回值,直接运行
                    os.system('kill -9 %s' % c.group(1))
                    print(c.group(1), 'kill')


    def find_bfmd(self,db,tb_name):
        sql = "select db_bf,tab_name_bf from tracking.table_relationship_111 where db_fin = '{}' and tab_name_fin = '{}'".format(db,tb_name)
        cursor = conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()
        for i in result:
            if i[1][:2] != "x_" and i[1][:4] != "dic_" and i[1][:3] != "xt_":
                self.date_before(tb_name,i[0],i[1])

if __name__ == '__main__':
    juddeModel().find_bfmd('ods','u8_sales_dispatch_list')



