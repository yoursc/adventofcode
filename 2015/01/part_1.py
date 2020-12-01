#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : part_1.py
@CreateTime : 2020/12/1 18:46
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
with open("2015-01.data") as f:
    data = f.read()
    size = len(data)
    count = 0
    for i in range(0, size):
        zi = data[i]
        if zi == "(":
            count += 1
        elif zi == ")":
            count -= 1
        else:
            raise Exception
    print(count)
