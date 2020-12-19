#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/10
"""

INPUT = []
with open("2020-10.data") as f:
    for i in f.read().split("\n"):
        INPUT.append(int(i))
INPUT.append(0)
INPUT.append(max(INPUT) + 3)
INPUT.sort()
print(INPUT)
VAR_1 = ""
for i in range(0, len(INPUT) - 1):
    VAR_1 += str(INPUT[i + 1] - INPUT[i])
VAR_2 = VAR_1.split("3")
print(VAR_2)


def check(cha):
    length = len(cha)
    if length < 2:
        return 1
    elif length == 2:
        return 2
    elif length == 3:
        return 4
    elif length == 4:
        return 7
    else:
        raise Exception(length)


answer = 1
for one in VAR_2:
    answer *= check(one)
    print(answer)
