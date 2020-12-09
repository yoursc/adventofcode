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
            value[child_name] = int(child_numb)
        BAG_RULES[key] = value


def bag_sum(bag):
    BAG_CHILD = BAG_RULES[bag]
    if len(BAG_CHILD) == 0:
        return 0
    COUNT = 0
    for child in BAG_CHILD.keys():
        child_numb = BAG_CHILD[child]
        COUNT += child_numb * (1 + bag_sum(child))
    return COUNT


hh = bag_sum("shiny gold")
print(hh)
