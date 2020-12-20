#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import product
import hashlib

"""
@Author : Ven
@Date   : 2020/12/11
"""

# 下面数据将不以行列的方式保存而是直接保存成字符串（或数组）
# 行列坐标通过公式转换获取

BASE_MAP = []
# 行
X_BASE = 0
# 列
Y_BASE = 0

with open("2020-11.data") as f:
    TMP_MAP = ""
    for hh in f.read().split("\n"):
        X_BASE += 1
        TMP_MAP += hh
        if Y_BASE == 0:
            Y_BASE = len(hh)
        elif Y_BASE != len(hh):
            raise Exception("数据文件内容非行列式")
    BASE_MAP = list(TMP_MAP)
    del TMP_MAP
    print("数据加载完成")


# 行列坐标与单索引的转换方法
def xy_2_i(x, y):
    if x >= X_BASE or y >= Y_BASE:
        raise Exception("x y 指定值过大")
    return x * Y_BASE + y


def i_2_xy(i):
    x = i % Y_BASE
    y = i // Y_BASE
    return x, y


def hash_list(the_map):
    md5 = hashlib.md5()
    md5.update("".join(the_map).encode("utf-8"))
    return md5.hexdigest()


# 查看特定坐标下回合的情况
def check(x: int, y: int, seat_map: list):
    center = seat_map[xy_2_i(x, y)]
    if center == ".":
        return center
    count_seat = 0
    count_person = 0
    x0 = x - 1 if x >= 1 else 0
    y0 = y - 1 if y >= 1 else 0
    x1 = x + 1 if x < X_BASE - 1 else X_BASE - 1
    y1 = y + 1 if y < Y_BASE - 1 else Y_BASE - 1
    for piece_x, piece_y in product(range(x0, x1 + 1), range(y0, y1 + 1)):
        if piece_x == x and piece_y == y:
            continue
        point = seat_map[xy_2_i(piece_x, piece_y)]
        if point == "#":
            count_person += 1
        elif point == "L":
            count_seat += 1
    if center == "L" and count_person == 0:
        return "#"
    if center == "#" and count_person >= 4:
        return "L"
    return center


# 生成下回合的地图
def round(seat_map: list):
    seat_new = seat_map.copy()
    for x, y in product(range(0, X_BASE), range(0, Y_BASE)):
        seat_new[xy_2_i(x, y)] = check(x, y, seat_map)
    return seat_new


index = 1
last_md5 = "0"
while 1:
    BASE_MAP = round(BASE_MAP)
    md5 = hash_list(BASE_MAP)
    peo_num = "".join(BASE_MAP).count("#")
    if last_md5 == md5:
        break
    print(f"INDEX:{index}  MD5:{md5}  PEOPLE:{peo_num}")
    index += 1
    last_md5 = md5
print(peo_num)
