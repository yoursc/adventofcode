#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/1/15
"""
import hashlib

str = "ckczppom"
num = 1

while 1:
    input_str = f'{str}{num}'
    m = hashlib.md5()
    m.update(bytes(input_str, encoding="utf8"))
    hax = m.hexdigest()
    hax_lead = hax[0:5]
    if hax_lead == '00000':
        print(f'{num}:{hax_lead}')
        break
    num += 1
