# -*- coding: utf-8 -*-

'''
# @Time    : 2020-06-01
# @Author  : sang
# @FileName: ExecuteTotal.py
# @Software: PyCharm

'''

# 全量执行脚本，需要传入表名参数
import sys
import datetime
sys.path.append("/github_try/unit")
from ReadFile import getsqlfile
from WriteFile import writefile

# 参数入口
tb_name = sys.argv[1]
# tb_name = 'test'


SQL_FILE = "github_try/sql/{}.sql".format(tb_name)
print('---------------------------------------------------------') # 分割线
LOG_FILE = "github_try/log/{}.log".format(tb_name)
# print(SQL_FILE)



# 输出开始时间
dt_start = datetime.datetime.now()
print('start time :{}'.format(dt_start.strftime('%Y-%m-%d %H:%M:%S')))

# 先获取文件
tar_sql_commands = getsqlfile().get_sqlfile_total(SQL_FILE)

# print(tar_sql_commands)
# 执行脚本
writefile().write_file_total(LOG_FILE,tar_sql_commands)

# 输出结束时间
dt_end = datetime.datetime.now()
print('end time :{}'.format(dt_end.strftime('%Y-%m-%d %H:%M:%S')))

# 输出运行时长
time_used = dt_end - dt_start
print('time : {} seconds'.format(time_used.seconds))
print('{}已经完成dm层加工'.format(tb_name))
print('脚本路径: {}'.format(SQL_FILE))
print('------------------------------------------------------------------------------------------------')
