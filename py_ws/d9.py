# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
'''

列表推导式
0- 1000 ，数的列表
'''

list1 = [i ** 3 for i in range(1001) if i % 2 == 0]


print(list1)
