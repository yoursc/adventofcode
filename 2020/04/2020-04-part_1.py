#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/4
"""
ID_FORMAT = []
with open("2020-04.data") as f:
    data = f.read().split("\n\n")
    for passport in data:
        one = {}
        for kv in passport.replace("\n", " ").split(" "):
            kvs = kv.split(":")
            one[kvs[0]] = kvs[1]
        ID_FORMAT.append(one)

FULL = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
answer_1 = 0
for passport in ID_FORMAT:
    if len(set(passport.keys()).intersection(FULL)) == 7:
        answer_1 += 1
print(answer_1)
