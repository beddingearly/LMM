#coding=utf-8
'''
@Time    : 2018/12/10 16:48
@Author  : Zt.Wang
@Email   : 137602260@qq.com
@File    : dataClean.py
@Software: PyCharm
'''

import csv
class DataClean():
    def read_file(self):
        with open("‎") as f:
            reader = csv.reader(f)
            print(list(reader))