#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-04
"""

plant = []
with open('2021-02.data') as f:
    readfile = f.read().split("\n")
    size = len(readfile)
    for i in range(0, size):
        plant.append(readfile[i].split(" "))

position = 0
depth = 0

for i in range(0,size):
    cmd = plant[i]
    if cmd[0] == "forward":
        position += int(cmd[1])
    elif cmd[0] == "up":
        depth -= int(cmd[1])
    elif cmd[0] == "down":
        depth += int(cmd[1])
    else:
        print("WARNING")

print(position * depth)
