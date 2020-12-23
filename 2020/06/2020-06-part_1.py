#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/6
"""

with open("2020-06.data") as f:
    DATA = f.read().split("\n\n")


def group_count(answer: str):
    g = []
    for char in answer.replace("\n", ""):
        g.append(char)
    return len(set(g))


COUNT = 0
for answer in DATA:
    COUNT += group_count(answer)
print(COUNT)
