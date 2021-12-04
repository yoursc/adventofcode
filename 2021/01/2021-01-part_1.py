#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-04
"""

with open('2021-01.data') as f:
    data = f.read().split("\n")
    size = len(data)
    out = 0
    for i in range(1, size):
        delta = int(data[i]) - int(data[i - 1])
        if delta > 0:
            out += 1
    print(out)
