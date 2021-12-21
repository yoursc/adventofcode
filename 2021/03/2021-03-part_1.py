#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-09
"""
import numpy

with open('2021-03.data') as f:
    rf = f.read().split("\n")
    len_line = len(rf)
    len_row = len(rf[0])
    data = numpy.zeros((len_line, len_row), dtype=numpy.int)
    for i in range(0, len_line):
        for j in range(0, len_row):
            data[i, j] = rf[i][j]

# 去数量的一半作为除数
len_line_half = numpy.floor_divide(len_line, 2)
# 统计每位1出现的次数
hh = numpy.sum(data, axis=0)
# 整除，获得伽马值，并打印
gamma_rate = numpy.floor_divide(hh, len_line_half)
print(gamma_rate)
# 剩下的手动算吧，位运算太繁琐
