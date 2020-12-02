#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/2
"""


def rule_1(pswd: str):
    for i in range(len(pswd) - 2):
        w_1 = ord(pswd[i])
        w_2 = ord(pswd[i + 1])
        w_3 = ord(pswd[i + 2])
        if w_1 == w_2 - 1 == w_3 - 2:
            return True
    return False


def rule_2(pswd: str):
    try:
        pswd.index("i")
        pswd.index("o")
        pswd.index("l")
        return False
    except:
        pass
    return True


def rule_3(pswd: str):
    same_1 = -2
    for i in range(len(pswd) - 1):
        if pswd[i] != pswd[i + 1]:
            continue
        if same_1 == -2:
            same_1 = i
            continue
        if pswd[i] == pswd[same_1]:
            continue
        if i == same_1 + 1:
            continue
        return True
    return False


def check_password(pswd: str):
    if rule_1(pswd) and rule_2(pswd) and rule_3(pswd):
        return True
    else:
        return False


def increase_password(pswd: str):
    tmp = list(pswd)
    tmp[-1] = chr(ord(tmp[-1]) + 1)
    for i in range(len(pswd) - 1, -1, -1):
        if i == 0 and tmp[0] == "{":
            raise Exception("溢出")
        if tmp[i] == "{":
            tmp[i] = "a"
            tmp[i - 1] = chr(ord(tmp[i - 1]) + 1)
    return "".join(tmp)


data_1 = "hepxcrrq"

while 1:
    data_1 = increase_password(data_1)
    if check_password(data_1):
        break
print("part_1")
print(data_1)

print("part_2")
data_2 = data_1
while 1:
    data_2 = increase_password(data_2)
    if check_password(data_2):
        break
print(data_2)
