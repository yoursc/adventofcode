#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : part01.py
@CreateTime : 2020/12/1 18:19
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
with open('2020-01.data') as f:
    data = f.read()
    data_list = data.split("\n")
    size = len(data_list)
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if int(data_list[i]) + int(data_list[j]) == 2020:
                print(f"Index:{i},{j}")
                print(f"data:{data_list[i]},{data_list[j]}")
                print(int(data_list[i]) * int(data_list[j]))
