#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/10
"""

DATA = []
with open("2020-10.data") as f:
    for i in f.read().split("\n"):
        DATA.append(int(i))

DATA.append(0)
DATA.append(max(DATA) + 3)
DATA.sort()
DIC = {"1": 0, "2": 0, "3": 0}

for i in range(0, len(DATA) - 1):
    cha = DATA[i + 1] - DATA[i]
    DIC[str(cha)] += 1

print(DIC)
print(DIC["1"] * DIC["3"])
