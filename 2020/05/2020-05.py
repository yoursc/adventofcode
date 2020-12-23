#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/6
"""


def trans_pass(passid: str):
    row = passid[0: 7].replace("F", "0").replace("B", "1")
    column = passid[-3:].replace("L", "0").replace("R", "1")
    return int(row, 2) * 8 + int(column, 2)


PASS_LIST = []
with open("2020-05.data") as f:
    data = f.read().split("\n")
    for line in data:
        PASS_LIST.append(trans_pass(line))

print("part 1")
print(max(PASS_LIST))

print("part 2")
for i in range(min(PASS_LIST), max(PASS_LIST)):
    if i not in PASS_LIST:
        print(i)
        break
