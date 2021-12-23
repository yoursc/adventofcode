#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-22
"""

import numpy


def get_line(x1, y1, x2, y2, diagonal=False):
    line_map = numpy.zeros((max_y, max_x), dtype=numpy.int)
    if x1 == x2 and y1 == y2:
        print('not move')
        return line_map
    elif x1 == x2 or y1 == y2:
        # straight line
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                line_map[y, x] = 1
    elif (abs(x2 - x1) == abs(y2 - y1)) and diagonal:
        # diagonal line
        delta_x = 1 if (x2 > x1) else -1
        delta_y = 1 if (y2 > y1) else -1
        for x, y in zip(range(x1, x2 + delta_x, delta_x), range(y1, y2 + delta_y, delta_y)):
            line_map[y, x] = 1
    else:
        pass
    return line_map


# load data file
with open('2021-05.data') as f:
    rf = f.read().replace(' -> ', ',').split('\n')
    # empty data
    data = numpy.zeros((len(rf), 4), dtype=numpy.int)
    for line_index in range(0, len(rf)):
        column_index = 0
        for column in rf[line_index].split(','):
            data[line_index, column_index] = int(column)
            column_index += 1
max_data = data.max(axis=0, initial=None)
max_x = max(max_data[0], max_data[2]) + 1
max_y = max(max_data[1], max_data[3]) + 1

# PART 1
point_map_1 = numpy.zeros((max_y, max_x), dtype=numpy.int)
for line in data:
    point_map_1 += get_line(line[0], line[1], line[2], line[3])
print(point_map_1)
print((point_map_1 >= 2).sum())

# PART 2
point_map_2 = numpy.zeros((max_y, max_x), dtype=numpy.int)
for line in data:
    point_map_2 += get_line(line[0], line[1], line[2], line[3], True)
print(point_map_2)
print((point_map_2 >= 2).sum())
