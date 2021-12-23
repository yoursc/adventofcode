#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-23
"""


def next_day(status_last):
    status_next = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 9):
        status_next[i - 1] = status_last[i]
        status_next[6] = status_last[0] + status_last[7]
        status_next[8] = status_last[0]
    return status_next


with open('2021-06.data') as f:
    rf = f.read().split(',')

status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for one in rf:
    status[int(one)] += 1

print(status)
for day in range(1, 257):
    status = next_day(status)
    if day in [80, 256]:
        print(day, sum(status))
