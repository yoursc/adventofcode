#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-26
"""
import numpy


def set_lowest_gid(x0, y0, gid):
    if int(map_data[x0, y0]) == 9:
        return
    if int(map_lowest[x0, y0]) != 0:
        return
    map_lowest[x0, y0] = gid
    # behind
    if x0 > 0:
        set_lowest_gid(x0 - 1, y0, gid)
    # before
    if x0 + 1 < x_len:
        set_lowest_gid(x0 + 1, y0, gid)
    # left
    if y0 > 0:
        set_lowest_gid(x0, y0 - 1, gid)
    # right
    if y0 + 1 < y_len:
        set_lowest_gid(x0, y0 + 1, gid)


with open('2021-09.data') as f:
    rf = f.read().split('\n')
    x_len, y_len = len(rf), len(rf[0])
    map_data = numpy.zeros((x_len, y_len), numpy.int)
    map_lowest = numpy.zeros((x_len, y_len), numpy.int)
    for x in range(0, x_len):
        for y in range(0, y_len):
            map_data[x, y] = int(rf[x][y])
    del rf

# 生成盆地分组地图
lowest_gid = 0
for x in range(0, x_len):
    for y in range(0, y_len):
        if int(map_data[x, y]) != 9 and int(map_lowest[x, y]) == 0:
            lowest_gid += 1
        set_lowest_gid(x, y, lowest_gid)
print(map_lowest)

# 汇总分组结果
group_count_list = []
for gid in range(1, lowest_gid + 1):
    group_count_list.append(int(numpy.sum(map_lowest == gid)))
group_count_list.sort(reverse=True)
print(group_count_list[0] * group_count_list[1] * group_count_list[2])
