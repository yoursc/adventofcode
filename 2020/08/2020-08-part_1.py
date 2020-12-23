#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/8
"""

with open("2020-08.data") as f:
    OXFF = f.read().split("\n")

black_list = []
accumulator = 0
index = 0
while 1:
    if index == len(OXFF):
        break
    if index in black_list:
        break
    else:
        black_list.append(index)
    cmd_split = OXFF[index].split(" ", 1)
    operation = cmd_split[0]
    argument = int(cmd_split[1])
    if operation == "jmp":
        index += argument
        continue
    elif operation == "acc":
        accumulator += argument
    elif operation == "nop":
        pass
    else:
        print(operation)
        raise Exception("未知操作符")
    index += 1

print(accumulator)
