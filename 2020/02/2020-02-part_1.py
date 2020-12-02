#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/2
"""


def check_passwd(line: str):
    hh = line.split(" ")
    num_range = hh[0].split("-")
    num_min = int(num_range[0])
    num_max = int(num_range[1])
    word = hh[1][0]
    pswd = hh[2]
    word_count = 0
    for w in pswd:
        if w == word:
            word_count += 1
    if word_count <= num_max and word_count >= num_min:
        return True
    else:
        return False


valid_count = 0
with open("2020-02.data") as f:
    data = f.read().split("\n")
    for line in data:
        if check_passwd(line):
            valid_count += 1

print(valid_count)
