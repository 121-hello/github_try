# -*- coding: utf-8 -*-

'''
# @Time    : 2020-06-01
# @Author  : sang
# @FileName: ReadFile.py
# @Software: PyCharm

'''

from string import Template
import time

class getsqlfile():


    def get_sqlfile_day(self,SQL_FILE,start_dt):
        #全局变量调用
        sysCurDate=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        # 参数列表,这里的参数需要传入sql文件中的、，替换时间参数，执行增量脚本需要使用
        conf_dict = {
            'start_dt':start_dt,
            'sysCurDate':sysCurDate
        }

        tar_sql_commands = []
        with open(SQL_FILE,encoding='UTF-8') as f:
                sql_command=''
                for line in f:
                    if not line.strip().startswith('--'):
                            if line.strip().endswith(b';'):
                                    sql_command = sql_command + line[:line.index(';')] + '\n'
                                    # 这里是吧参数列表传入，Template方法替换
                                    tar_sql_commands.append(Template(sql_command).substitute(conf_dict))
                                    sql_command = ''
                            else:
                                    sql_command = sql_command + line
        return tar_sql_commands

# 针对存储过程，分割进行优化
    def get_sqlfile_total(self,SQL_FILE):
        #全局变量调用
        sysCurDate=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        # 参数列表,这里的参数需要传入sql文件中的、，替换时间参数，执行增量脚本需要使用
        conf_dict = {
            'sysCurDate':sysCurDate
        }

        tar_sql_commands = []
        tar_sql_commands_new = []
        with open(SQL_FILE,encoding='UTF-8') as f:
                sql_command=''
                for line in f:
                    if not line.strip().startswith('--'):
                        if line.strip().endswith('//'):
                            sql_command = sql_command + line[:line.index('//')] + '\n'
                            # 这里是吧参数列表传入，Template方法替换
                            tar_sql_commands.append(Template(sql_command).substitute(conf_dict))
                            sql_command = ''
                        else:
                            sql_command = sql_command + line
                tar_sql_commands.append(sql_command)
        if len(tar_sql_commands) == 1:
            for i in tar_sql_commands[0].split(';'):
                tar_sql_commands_new.append(i)
            tar_sql_commands_new.pop()
        else:
            for sql_list in range(len(tar_sql_commands)):
                # 这里是除以2余数的判断，之前//用来获取是数组奇数还是偶数位
                if sql_list %  2 == 0:
                    for i in tar_sql_commands[sql_list].split(';'):
                        tar_sql_commands_new.append(str(i).replace("delimiter",""))
                    tar_sql_commands_new.pop()
                else:
                    tar_sql_commands_new.append(str(tar_sql_commands[sql_list]).replace("delimiter",""))

        tar_sql_commands_old = []
        for j in range(len(tar_sql_commands_new)):
            if str(tar_sql_commands_new[j]).replace(" ","") != "":
                tar_sql_commands_old.append(tar_sql_commands_new[j])
        return tar_sql_commands_old



