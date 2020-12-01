#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/1/15
"""
import numpy


class Part:

    def __init__(self):
        self.light_map = numpy.zeros((1000, 1000))
        self.file_path = "2015-06.data"

    def deal_cmd(self, cmd: str):
        cmd_s1 = cmd.split(" ")
        action = str(cmd_s1[0])
        x0, y0 = cmd_s1[1].split(",")
        x1, y1 = cmd_s1[3].split(",")
        for x in range(int(x0), int(x1) + 1):
            for y in range(int(y0), int(y1) + 1):
                self.actioner(action, x, y)

    def actioner(self, action: str, x: int, y: int):
        brightness = self.light_map[x, y]
        if action == "toggle":
            brightness += 2
        if action == "on":
            brightness += 1
        if action == "off":
            brightness -= 1
        if brightness == -1:
            brightness = 0
        self.light_map[x, y] = brightness


if __name__ == '__main__':
    pa = Part()
    with open(pa.file_path, 'r', encoding='utf8') as file:
        file_str = file.read()
    cmd_list = file_str.replace("turn on", "on").replace("turn off", "off").split("\n")
    for cmd in cmd_list:
        if cmd == "":
            break
        pa.deal_cmd(cmd)
    print(pa.light_map)
    print(pa.light_map.sum())
