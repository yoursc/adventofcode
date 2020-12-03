#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/3
"""

MAP_DATA = []
with open("2020-03.data")as f:
    MAP_DATA.extend(f.read().split("\n"))
MAP_X = len(MAP_DATA[0])
MAP_Y = len(MAP_DATA)


def read_map(x: int, y: int):
    if y >= MAP_Y:
        raise Exception("Y too big")
    return MAP_DATA[y][x % MAP_X]


def slope(slope_x: int, slope_y: int):
    sharp_count = 0
    index_x = 0
    index_y = 0
    while 1:
        try:
            hh = read_map(index_x, index_y)
        except Exception:
            break
        if hh == "#":
            sharp_count += 1
        index_x += slope_x
        index_y += slope_y
        if index_y == MAP_Y:
            break
    return sharp_count


print("part 1")
answer_1 = slope(3, 1)
print(answer_1)

print("part 2")
answer_2 = slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2)
print(answer_2)
