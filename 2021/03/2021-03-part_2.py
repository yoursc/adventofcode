#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-10
"""

# 数组过滤器（数据数组，前序过滤词）
import numpy


def data_filter(base, keys):
    if len(base) <= 1 or len(keys) == 0:
        return base
    tmp_data_filter = []
    for i in range(0, len(base)):
        if base[i][0:len(keys)] == keys:
            tmp_data_filter.append(base[i])
    return tmp_data_filter


# 数位汇总器（数据数组）
def data_summer(base):
    if len(base) == 0:
        return base
    base_line = len(base)
    base_row = len(base[0])
    data_data_summer = numpy.zeros((base_line, base_row), dtype=numpy.int)
    for i in range(0, base_line):
        for j in range(0, base_row):
            data_data_summer[i, j] = base[i][j]
    return numpy.sum(data_data_summer, axis=0)


# 加载数据文件
with open('2021-03.data') as f:
    data = f.read().split("\n")
# data = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

# 数据总量
len_line = len(data)
# 数据长度
len_row = len(data[0])

rating_oxygen = ""
for i in range(0, len_row):
    tmp_data = data_filter(data, rating_oxygen)
    sum_1 = data_summer(tmp_data)
    if 2 * sum_1[i] >= len(tmp_data):
        rating_oxygen += "1"
    else:
        rating_oxygen += "0"
print(int(rating_oxygen, 2))

rating_co2 = ""
for i in range(0, len_row):
    tmp_data = data_filter(data, rating_co2)
    sum_2 = data_summer(tmp_data)
    if int(sum_2[i]) in (0, len(tmp_data)):
        rating_co2 += str(tmp_data[0][i])
    elif 2 * sum_2[i] >= len(tmp_data):
        rating_co2 += "0"
    else:
        rating_co2 += "1"
print(int(rating_co2, 2))
print(int(rating_oxygen, 2) * int(rating_co2, 2))
