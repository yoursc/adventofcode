#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/2
"""


def get_lwh(line: str):
    int_list = []
    for str_num in line.split("x"):
        int_list.append(int(str_num))
    if len(int_list) != 3:
        raise Exception
    int_list.sort()
    return int_list[0], int_list[1], int_list[2]


with open("2015-02.data") as f:
    file = f.read()
    data_list = file.split("\n")
    summary = 0
    for line in data_list:
        a, b, c = get_lwh(line)
        sing = 3 * a * b + 2 * b * c + 2 * a * c
        summary += sing
    print(summary)
