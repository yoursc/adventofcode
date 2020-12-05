#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/4
"""
ID_FORMAT = []
with open("2020-04.data") as f:
    data = f.read().split("\n\n")
    for passport in data:
        one = {}
        for kv in passport.replace("\n", " ").split(" "):
            kvs = kv.split(":")
            one[kvs[0]] = kvs[1]
        ID_FORMAT.append(one)


def check_passport(passport: dict):
    try:
        byr = int(passport["byr"])
        if byr < 1920 or 2002 < byr:
            return False
        iyr = int(passport["iyr"])
        if iyr < 2010 or 2020 < iyr:
            return False
        eyr = int(passport["eyr"])
        if eyr < 2020 or 2030 < eyr:
            return False
        hgt = passport["hgt"]
        hgt_num = int(hgt[:-2])
        if hgt[-2:] == "in":
            if hgt_num < 59 or 76 < hgt_num:
                return False
        elif hgt[-2:] == "cm":
            if hgt_num < 150 or 193 < hgt_num:
                return False
        else:
            return False
        hcl = passport["hcl"]
        if hcl[0] != "#" or len(hcl) != 7:
            return False
        for a in hcl[1:]:
            if a not in "0123456789abcdef":
                return False
        ecl = passport["ecl"]
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        pid = passport["pid"]
        if len(pid) != 9:
            return False
        for a in pid:
            if a not in "0123456789":
                return False
        return True
    except:
        return False


valid_count = 0
for one in ID_FORMAT:
    if check_passport(one):
        valid_count += 1

print(valid_count)
