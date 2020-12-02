#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/2
"""

# 城市列表
CITY = ["Arbre", "AlphaCentauri", "Faerun", "Norrath", "Straylight", "Snowdin", "Tambi", "Tristram"]
# 距离列表
DISTANCE_TAB = {}

# 加载数据
with open("2015-09.data") as f:
    for line in f.read().split("\n"):
        hh = line.split(" ")
        index_1 = CITY.index(hh[0])
        index_2 = CITY.index(hh[2])
        distance = int(hh[4])
        k = f"{min(index_1, index_2)}-{max(index_1, index_2)}"
        DISTANCE_TAB[k] = distance


def distance(sort: list):
    sum_distance = 0
    for i in range(0, len(sort) - 1):
        key = f"{min(sort[i], sort[i + 1])}-{max(sort[i], sort[i + 1])}"
        sum_distance += DISTANCE_TAB[key]
    return sum_distance


def deal_one(sort: list):
    this_distance = distance(sort)
    distance_list.append(this_distance)
    print(f"{sort}:{this_distance}")


def rec(unsort: list, sort: list):
    if len(unsort) == 0:
        deal_one(sort)
    else:
        for i in range(0, len(unsort)):
            p_unsort = unsort.copy()
            p_sort = sort.copy()
            p_sort.append(p_unsort.pop(i))
            rec(p_unsort, p_sort)


tmp_unsort = [0, 1, 2, 3, 4, 5, 6, 7]
tmp_sort = []
distance_list = []
rec(tmp_unsort, tmp_sort)

print("part_1")
print(min(distance_list))

print("part_2")
print(max(distance_list))
