#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/1/26
"""


def count(line: str):
    num = 0
    for i in line:
        if i in ("\\", "\""):
            num += 1
    return num


with open("2015-08.data", 'r', encoding='utf8') as file:
    file_str = file.read()
str_list = file_str.split("\n")

num = 0
for line in str_list:
    num += count(line) + 2

print(num)
