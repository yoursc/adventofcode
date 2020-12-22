#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/20
"""

ORI_MAN = ["N", "E", "S", "W"]

GLOBAL_LIST = [0, 0, 0, 0]
# 初始坐标
# X轴 正方向:E 反方向:W
GLOBAL_LIST[0] = 0
# Y轴 正方向:N 反方向:S
GLOBAL_LIST[1] = 0
# 初始导航点
# 前进距离
GLOBAL_LIST[2] = 10
# 右偏距离
GLOBAL_LIST[3] = -1

with open("2020-12.data") as f:
    NAV = f.read().split("\n")


def move_ship(nswe, distance):
    x, y = 0, 0
    if nswe == "N":
        y += distance
    elif nswe == "S":
        y -= distance
    elif nswe == "W":
        x -= distance
    elif nswe == "E":
        x += distance
    return x, y


def move_navpoint(ori, distance, orientation):
    ori_tmp = (360 - orientation + 90 * ORI_MAN.index(ori)) % 360
    if ori_tmp == 0:
        GLOBAL_LIST[2] += distance
    elif ori_tmp == 180:
        GLOBAL_LIST[2] -= distance
    elif ori_tmp == 90:
        GLOBAL_LIST[3] += distance
    elif ori_tmp == 270:
        GLOBAL_LIST[3] -= distance


def instruction(cmd, orientation):
    ori = cmd[0]
    distance = int(cmd[1:])
    if ori not in "NSWEFLR":
        raise Exception(f"无法解析的导航命令:{cmd}")
    if ori == "L":
        return 0, 0, (orientation - distance + 360) % 360
    elif ori == "R":
        return 0, 0, (orientation + distance) % 360
    elif ori == "F":
        x1, y1 = move_ship(ORI_MAN[orientation % 360 // 90], distance * GLOBAL_LIST[2])
        x2, y2 = move_ship(ORI_MAN[(orientation + 90) % 360 // 90], distance * GLOBAL_LIST[3])
        return x1 + x2, y1 + y2, orientation
    move_navpoint(ori, distance, orientation)
    return 0, 0, orientation


# 设定初始方向角
orientation = 90
for nav in NAV:
    x_d, y_d, orientation = instruction(nav, orientation)
    GLOBAL_LIST[0] += x_d
    GLOBAL_LIST[1] += y_d
    print(
        f"nav:{nav} X,Y:{GLOBAL_LIST[0:2]} orientation:{ORI_MAN[orientation % 360 // 90]} nav_point:{GLOBAL_LIST[2:]}")
print(abs(GLOBAL_LIST[0]) + abs(GLOBAL_LIST[1]))
