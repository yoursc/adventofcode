#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2023-06-06
"""

# start = 939
# bus_list_str = "7,13,x,x,59,x,31,19"

start = 1008713
bus_list_str = "13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"

nest_list = []

for a in bus_list_str.split(","):
    if a != "x":
        bus_no = int(a)
        next_ts = (start // bus_no + 1) * bus_no
        nest_list.append(next_ts)
        if next_ts <= min(nest_list):
            print(str(bus_no) + ":" + str(bus_no * (next_ts - start)))
