#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/2
"""


def look_and_say(input: str):
    output = ""
    start_index = 0
    for index in range(len(input)):
        if index != start_index and input[index] != input[start_index]:
            output += f"{index - start_index}{input[start_index]}"
            start_index = index
    output += f"{len(input) - start_index}{input[start_index]}"
    return output


print("part_1")
data_1 = "3113322113"
for i in range(40):
    data_1 = look_and_say(data_1)
print(len(data_1))

print("part_2")
data_2 = "3113322113"
for i in range(50):
    data_2 = look_and_say(data_2)
print(len(data_2))
