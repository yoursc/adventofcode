#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/3
"""
import json


class RedException(Exception):
    pass


def open_list(cell_list: list):
    count = 0
    for cell in cell_list:
        try:
            count += deal(cell)
        except RedException:
            continue
    return count


def open_dict(cell_dict: dict):
    count = 0
    for cell in cell_dict.values():
        try:
            count += deal(cell)
        except RedException:
            return 0
    return count


def deal(cell):
    if type(cell) == int:
        return cell
    elif type(cell) == dict:
        return open_dict(cell)
    elif type(cell) == list:
        return open_list(cell)
    elif type(cell) == str:
        if cell == "red":
            raise RedException
        else:
            return 0
    else:
        raise Exception("未预见类型")


test_str = '{"a":2,"b":4}'
test_data = json.loads(test_str)
test_rtrn = deal(test_data)
print(f"Test: {test_rtrn}")

with open("2015-12.data") as f:
    INPUT = f.read()
    data = json.loads(INPUT)
    print(deal(data))
