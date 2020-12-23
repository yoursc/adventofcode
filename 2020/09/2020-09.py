#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/9
"""
import itertools

DATA = []
with open("2020-09.data") as f:
    for n in f.read().split("\n"):
        DATA.append(int(n))


def check_slider(slider, num):
    for combination in itertools.combinations(slider, 2):
        if sum(combination) == num:
            return True
    return False


index = 25
while 1:
    SLIDER = DATA[index - 25:index]
    if not check_slider(SLIDER, DATA[index]):
        break
    index += 1
    if index >= len(DATA):
        break

print("part 1")
NUM = DATA[index]
print(NUM)

print("part 2")
for start_index in range(0, len(DATA)):
    for end_index in range(start_index, len(DATA)):
        SLIDER = DATA[start_index: end_index]
        SUM = sum(SLIDER)
        if SUM > NUM:
            break
        if SUM == NUM:
            print(max(SLIDER) + min(SLIDER))
