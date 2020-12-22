#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/20
"""

ORI_MAN = "NESW"

with open("2020-12.data") as f:
    NAV = f.read().split("\n")


def instruction(cmd, orientation):
    x, y = 0, 0
    ori = cmd[0]
    distance = int(cmd[1:])
    if ori not in "NSWEFLR":
        raise Exception(f"无法解析的导航命令:{cmd}")
    if ori == "L":
        return x, y, (orientation - distance) % 360
    elif ori == "R":
        return x, y, (orientation + distance) % 360
    elif ori == "F":
        ori = ORI_MAN[orientation % 360 // 90]
    if ori == "N":
        y += distance
    elif ori == "S":
        y -= distance
    elif ori == "W":
        x -= distance
    elif ori == "E":
        x += distance
    return x, y, orientation


# 设定初始方向角
orientation = 90
# 初始坐标
# X轴 正方向:E 反方向:W
X = 0
# Y轴 正方向:N 反方向:S
Y = 0
for nav in NAV:
    x_d, y_d, orientation = instruction(nav, orientation)
    X += x_d
    Y += y_d
    print(nav, X, Y, orientation)
print(abs(X) + abs(Y))
