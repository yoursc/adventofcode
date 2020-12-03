#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/3
"""
import itertools

FAMILY_LIST = []
HAPPINESS_TAB = {}
with open("2015-13.data") as f:
    data = f.read().split("\n")
    for line in data:
        hh = line.split(" ")
        master = hh[0]
        slave = hh[10].replace(".", "")
        if master not in FAMILY_LIST:
            FAMILY_LIST.append(master)
        if slave not in FAMILY_LIST:
            FAMILY_LIST.append(slave)
        num = int(hh[3])
        if hh[2] == "gain":
            dire = 1
        elif hh[2] == "lose":
            dire = -1
        else:
            raise Exception
        key = f"{master}-{slave}"
        value = dire * num
        HAPPINESS_TAB[key] = value


def get_happiness_count(layout: list):
    count = 0
    for i in range(0, len(layout) - 1):
        name_1 = layout[i]
        name_2 = layout[i + 1]
        count += HAPPINESS_TAB[f"{name_1}-{name_2}"] + HAPPINESS_TAB[f"{name_2}-{name_1}"]
    count += HAPPINESS_TAB[f"{layout[0]}-{layout[-1]}"] + HAPPINESS_TAB[f"{layout[-1]}-{layout[0]}"]
    return count


def get_max_happiness(family_list: list):
    max_happiness = 0
    for arrangement in itertools.permutations(family_list, len(family_list)):
        happiness = get_happiness_count(arrangement)
        max_happiness = max(happiness, max_happiness)
    return max_happiness


print("part 1")
print(get_max_happiness(FAMILY_LIST))

print("part 1")
for name in FAMILY_LIST:
    HAPPINESS_TAB[f"Santa-{name}"] = 0
    HAPPINESS_TAB[f"{name}-Santa"] = 0
FAMILY_LIST.append("Santa")
print(get_max_happiness(FAMILY_LIST))
