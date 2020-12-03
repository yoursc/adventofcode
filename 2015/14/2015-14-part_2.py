#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/3
"""

# 麋鹿信息
REINDEER_INFO_LIST = {}
# 计分板
SCOREBOARD = []
# 距离实况
DISTANCE = []
# 比赛计时器
MATCH_SECOND = 0
with open("2015-14.data") as f:
    data = f.read().split("\n")
    index = 0
    for line in data:
        info = line.split(" ")
        name = info[0]
        speed = int(info[3])
        duration = int(info[6])
        sleep = int(info[13])
        REINDEER_INFO_LIST[name] = {"speed": speed, "duration": duration, "sleep": sleep}
        SCOREBOARD.append(0)
        DISTANCE.append(0)


def simulation_second():
    index = 0
    for reindeer_info in REINDEER_INFO_LIST.values():
        # 判断状态
        t = MATCH_SECOND % (reindeer_info["duration"] + reindeer_info["sleep"])
        if t < reindeer_info["duration"]:
            DISTANCE[index] += reindeer_info["speed"]
        index += 1
    now_max = max(DISTANCE)
    for i in range(len(REINDEER_INFO_LIST)):
        if DISTANCE[i] == now_max:
            SCOREBOARD[i] += 1


while 1:
    simulation_second()
    MATCH_SECOND += 1
    if MATCH_SECOND >= 2503:
        break
print(max(SCOREBOARD))
