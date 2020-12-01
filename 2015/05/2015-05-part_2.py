#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/1/15
"""

file_path = "2015-05.data"


def check_a(line: str):
    line_l = len(line)
    if line_l == 0:
        return False
    index = 0
    str_new = ""
    while 1:
        str_new = line[index:index + 2]
        if len(line.split(str_new)) >= 3:
            return True
        # next index
        index += 1
        if index >= line_l - 1:
            break
    return False


def check_b(line: str):
    line_l = len(line)
    if line_l == 0:
        return False
    index = 0
    while 1:
        word = line[index:index + 3]
        if word[0] == word[2]:
            return True
        index += 1
        if index >= line_l - 2:
            break
    return False


with open(file_path, 'r', encoding='utf8') as file:
    file_str = file.read()
file_list = file_str.split("\n")

nice_count = 0
for line in file_list:
    if check_a(line) and check_b(line):
        nice_count += 1
print(nice_count)
