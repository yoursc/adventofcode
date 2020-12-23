#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/8
"""
JMP = "jmp"
ACC = "acc"
NOP = "nop"

with open("2020-08.data") as f:
    OXFF = f.read().split("\n")


def check_loop(cmd_list: list):
    black_list = []
    accumulator = 0
    index = 0
    while 1:
        if index == len(cmd_list):
            return accumulator
        if index in black_list:
            raise Exception("Loop Error!!")
        else:
            black_list.append(index)
        cmd_split = cmd_list[index].split(" ", 1)
        operation = cmd_split[0]
        argument = int(cmd_split[1])
        if operation == JMP:
            index += argument
            continue
        elif operation == ACC:
            accumulator += argument
        elif operation == NOP:
            pass
        else:
            print(operation)
            raise Exception("未知操作符")
        index += 1


for replace_index in range(0, len(OXFF)):
    op = OXFF[replace_index][0: 3]
    if op not in [JMP, NOP]:
        continue
    OXFF_FIX = OXFF.copy()
    if op == JMP:
        OXFF_FIX[replace_index] = OXFF_FIX[replace_index].replace(JMP, NOP)
    if op == NOP:
        OXFF_FIX[replace_index] = OXFF_FIX[replace_index].replace(NOP, JMP)
    try:
        rtrn = check_loop(OXFF_FIX)
        print(rtrn)
    except Exception:
        pass
