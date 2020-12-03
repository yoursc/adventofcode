#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/3
"""
import json


def open_list(cell_list: list):
    count = 0
    for cell in cell_list:
        count += deal(cell)
    return count


def open_dict(cell_dict: dict):
    count = 0
    for cell in cell_dict.values():
        count += deal(cell)
    return count


def deal(cell):
    if type(cell) == int:
        return cell
    elif type(cell) == dict:
        return open_dict(cell)
    elif type(cell) == list:
        return open_list(cell)
    elif type(cell) == str:
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
