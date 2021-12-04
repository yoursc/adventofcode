#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-04
"""

d = []

with open('2021-01.data') as f:
    data = f.read().split("\n")
    size = len(data)
    for i in range(0, size):
        d.append(int(data[i]))


def get_slide(index):
    slide_now = d[index: index + 3]
    slide_next = d[index + 1: index + 4]
    return sum(slide_next) - sum(slide_now)


size = len(d)
out = 0
for i in range(0, size - 3):
    delta = get_slide(i)
    if delta > 0:
        out += 1
print(out)
