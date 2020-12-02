#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/2
"""


def check_passwd(line: str):
    data = line.split(" ")
    num_range = data[0].split("-")
    num_1 = int(num_range[0])
    num_2 = int(num_range[1])
    word = data[1][0]
    passwd = data[2]
    w_1 = passwd[num_1 - 1]
    w_2 = passwd[num_2 - 1]
    print(word + ":" + w_1 + w_2)
    tmp = (w_1 == word) == (not (w_2 == word))
    print(f"{line}:{tmp}")
    return tmp


test_1 = "1-3 a: abcde"
test_2 = "1-3 b: cdefg"
test_3 = "2-9 c: ccccccccc"
test_4 = "2-4 j: jxnj"
check_passwd(test_1)
check_passwd(test_2)
check_passwd(test_3)
check_passwd(test_4)

valid_count = 0
with open("2020-02.data") as f:
    data = f.read().split("\n")
    for line in data:
        if check_passwd(line):
            valid_count += 1
print(valid_count)
