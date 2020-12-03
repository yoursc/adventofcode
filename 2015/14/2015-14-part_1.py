#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/3
"""


def simulation_batch(speed: int, duration: int, sleep: int, limit: int):
    distance_count = 0
    cycle = duration + sleep
    distance_count += speed * duration * (limit // cycle)
    remainder_time = limit % cycle
    remainder_time = duration if remainder_time > duration else remainder_time
    distance_count += remainder_time * speed
    return distance_count


winner_distance = 0
with open("2015-14.data") as f:
    data = f.read().split("\n")
    for line in data:
        info = line.split(" ")
        name = info[0]
        speed = int(info[3])
        duration = int(info[6])
        sleep = int(info[13])
        winner_distance = max(winner_distance, simulation_batch(speed, duration, sleep, 2503))
print(winner_distance)

