#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/1/19
"""

cmd_dic = {}
num_dic = {}


def write_cmd_dic(command: str):
    command_split = command.split(" -> ")
    if command_split.__len__() != 2:
        return
    inter: str = command_split[0]
    outer: str = command_split[1]
    cmd_dic[outer] = inter


def f_and(value: str):
    value_split = value.split("AND")
    a: str = value_split[0].strip()
    b: str = value_split[1].strip()
    result: int = int(get_value(a)) & int(get_value(b))
    return str(result)


def f_or(value: str):
    value_split = value.split("OR")
    a: str = get_value(value_split[0].strip())
    b: str = get_value(value_split[1].strip())
    result: int = int(a) | int(b)
    return str(result)


def f_not(value: str):
    value_n: str = value.replace("NOT", "")
    a: str = get_value(value_n.strip())
    result: int = 65536 + ~int(a)
    return str(result)


def f_shift(value: str):
    if "LSHIFT" in value:
        value_split = value.split("LSHIFT")
        a: str = get_value(value_split[0].strip())
        b: str = get_value(value_split[1].strip())
        result: int = int(a) << int(b)
        return str(result)
    elif "RSHIFT" in value:
        value_split = value.split("RSHIFT")
        a: str = get_value(value_split[0].strip())
        b: str = get_value(value_split[1].strip())
        result: int = int(a) >> int(b)
        return str(result)
    else:
        print("Error!!")
        exit(1)


def get_value(key: str):
    try:
        a = int(key)
        return key
    except Exception:
        if key in num_dic:
            return num_dic[key]
        cmd = cmd_dic[key]
        print(f'{key}=[{cmd}]')
        if "AND" in cmd:
            result = f_and(cmd)
        elif "OR" in cmd:
            result = f_or(cmd)
        elif "NOT" in cmd:
            result = f_not(cmd)
        elif "SHIFT" in cmd:
            result = f_shift(cmd)
        else:
            result = get_value(cmd)
        num_dic[key] = result
        return result


with open("2015-07.data", 'r', encoding='utf8') as file:
    file_str = file.read()
cmd_list = file_str.split("\n")
for command in cmd_list:
    write_cmd_dic(command)

print(f'The value of a is {get_value("a")}')
