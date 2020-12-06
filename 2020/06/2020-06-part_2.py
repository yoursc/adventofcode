#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/6
"""

with open("2020-06.data") as f:
    DATA = f.read().split("\n\n")


def str_split(hh):
    rtrn = []
    for i in hh:
        rtrn.append(i)
    return rtrn


def group_count(answer: str):
    group_list = answer.split("\n")
    g = set(str_split(group_list[0]))
    for user in group_list:
        g = g & set(str_split(user))
    return len(set(g))


COUNT = 0
for answer in DATA:
    COUNT += group_count(answer)
print(COUNT)
