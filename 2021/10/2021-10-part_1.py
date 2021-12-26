#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-26
"""

matching_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
point_tab = {')': 3, ']': 57, '}': 1197, '>': 25137, '': 0}


def syntax_checker(code_str):
    men = []
    for abc in code_str:
        if abc in '([{<':
            men.append(abc)
            continue
        if abc != matching_dict[men.pop()]:
            return abc
    return ''


with open('2021-10.data') as f:
    code = f.read().split()

count = 0
for line in code:
    count += point_tab[syntax_checker(line)]

print(count)
