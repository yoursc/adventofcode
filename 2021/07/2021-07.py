#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-23
"""
import sys

crab_list = []
# load data
with open('2021-07.data') as f:
    for one in f.read().split(','):
        crab_list.append(int(one))

# PART 1
min_arm_1, min_fuel_1 = 0, int(sys.maxsize)
min_arm_2, min_fuel_2 = min_arm_1, min_fuel_1
for arm in range(min(crab_list), max(crab_list) + 1):
    count_1 = 0
    count_2 = 0
    for crab in crab_list:
        delta = abs(crab - arm)
        count_1 += delta
        count_2 += int((1 + delta) * delta / 2)
    # print(arm, count_1, count_2)
    if count_1 < min_fuel_1:
        min_arm_1, min_fuel_1 = arm, count_1
    if count_2 < min_fuel_2:
        min_arm_2, min_fuel_2 = arm, count_2

print('Part-1', min_arm_1, min_fuel_1)
print('Part-2', min_arm_2, min_fuel_2)
