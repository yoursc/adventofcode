#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/1
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
