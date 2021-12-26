#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-26
"""
import numpy


def check_lowest(x0, y0):
    point = map_data[x0, y0]
    other_point = []
    # behind
    if x0 > 0:
        other_point.append(map_data[x0 - 1, y0])
    # before
    if x0 + 1 < x_len:
        other_point.append(map_data[x0 + 1, y0])
    # left
    if y0 > 0:
        other_point.append(map_data[x0, y0 - 1])
    # right
    if y0 + 1 < y_len:
        other_point.append(map_data[x0, y0 + 1])
    # CHECK
    if point < min(other_point):
        return int(point)
    else:
        return -1


with open('2021-09.data') as f:
    rf = f.read().split('\n')
    x_len, y_len = len(rf), len(rf[0])
    map_data = numpy.zeros((x_len, y_len), numpy.int)
    for x in range(0, x_len):
        for y in range(0, y_len):
            map_data[x, y] = int(rf[x][y])
    del rf

lowest_list = []
for x in range(0, x_len):
    for y in range(0, y_len):
        check = check_lowest(x, y)
        if check >= 0:
            lowest_list.append(check)
print(sum(lowest_list) + len(lowest_list))
