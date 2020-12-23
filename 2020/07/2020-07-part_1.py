#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/7
"""

BAG_RULES = {}
with open("2020-07.data") as f:
    rule_list = f.read().split("\n")
    for rule in rule_list:
        rule_spl = rule.replace(".", "").split(" contain ")
        key = rule_spl[0].replace(" bags", "")
        value = {}
        for child_bag in rule_spl[1].replace(" bags", "").replace(" bag", "").split(", "):
            if child_bag == "no other":
                continue
            child_info = child_bag.split(" ", 1)
            child_name = child_info[1]
            child_numb = child_info[0]
            value[child_name] = child_numb
        BAG_RULES[key] = value


def check(parents, child, grand=None, depth=0):
    # 自己查自己
    if child == parents:
        return True
    # 子项包含
    bag = BAG_RULES[parents].keys()
    if child in bag:
        return True
    # 套娃预防
    if grand == parents:
        return False
    if grand is None:
        grand = parents
    # 递归
    for rec in bag:
        if check(rec, child, grand, depth + 1):
            return True
    return False


COUNT_1 = -1
for hh in BAG_RULES.keys():
    if check(hh, "shiny gold"):
        COUNT_1 += 1
print(COUNT_1)
