#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-26
"""

matching_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}
point_tab = {')': 1, ']': 2, '}': 3, '>': 4, '': 0}


def auto_complete(code_str):
    run_buffer = []
    fix_buffer = []
    for abc in code_str:
        if abc in '([{<':
            run_buffer.append(abc)
            continue
        if abc != matching_dict[run_buffer.pop()]:
            return ''
    for abc in run_buffer[::-1]:
        fix_buffer.append(matching_dict[abc])
    return fix_buffer


def scorer(code_str):
    score = 0
    for abc in code_str:
        score *= 5
        score += point_tab[abc]
    return score


with open('2021-10.data') as f:
    code_data = f.read().split()

score_board = []

for code_line in code_data:
    adding_code = auto_complete(code_line)
    fix_score = scorer(adding_code)
    if fix_score != 0:
        score_board.append(fix_score)

score_board.sort()
print(score_board[int(len(score_board) / 2)])
