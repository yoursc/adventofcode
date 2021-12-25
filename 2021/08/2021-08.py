#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-25
"""


# 字幕排序
def str_sort(str_random):
    tmp = ""
    for a in 'abcdefg':
        if str_random.count(a) > 1:
            raise
        elif str_random.count(a) == 1:
            tmp += a
    return tmp


def list_searcher(alphabet, length=0, times=0):
    """
    搜索器
    :param alphabet: 单词表
    :param length:   单词词长   返回首个该词长的单词
    :param times:    字母次数   返回所有该次数的字母
    :return: 字符串
    """
    for word in alphabet:
        if len(word) == length:
            return word
    tmp = ''
    for abc in set(''.join(alphabet)):
        if ''.join(alphabet).count(abc) == times:
            tmp += abc
    return tmp


# 单行解码器
def get_decode(line):
    hex_patterns, hex_outputs = line.split(' | ')
    hex_pattern_list = []
    hex_output_list = hex_outputs.split(' ')
    number_dict = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3',
                   'bcdf': '4', 'abdfg': '5', 'abdefg': '6',
                   'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
    for one in hex_patterns.split(' '):
        hex_pattern_list.append(str_sort(one))
    '''
       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
    ---+---+---+---+---+---+---+---+---+---+---+
     a | * |   | * | * |   | * | * | * | * | * | 8
    ---+---+---+---+---+---+---+---+---+---+---+
     b | * |   |   |   | * | * | * |   | * | * | 6
    ---+---+---+---+---+---+---+---+---+---+---+
     c | * | * | * | * | * |   |   | * | * | * | 8
    ---+---+---+---+---+---+---+---+---+---+---+
     d |   |   | * | * | * | * | * |   | * | * | 7
    ---+---+---+---+---+---+---+---+---+---+---+
     e | * |   | * |   |   |   | * |   | * |   | 4
    ---+---+---+---+---+---+---+---+---+---+---+
     f | * | * |   | * | * | * | * | * | * | * | 9
    ---+---+---+---+---+---+---+---+---+---+---+
     g | * |   | * | * |   | * | * |   | * | * | 7
    ---+---+---+---+---+---+---+---+---+---+---+
         6   2   5   5   4   5   6   3   7   6
    如上表所示
    横行首行表示显示的数字值
    尾行表示该数值显示需要用到的字母数量
    竖列左列表示显示的字母（正确的情况）
    竖列右列表示改字母在十个数字中一共出现的次数
    中间 * 表示横行的某个数字显示需要用到竖列特定的字母
    
    据此，我们可以按顺序逐个推断：
    e：一共出现过4次
    b：一共出现过6次
    f：一共出现过9次
    并缩小范围：
    ac：一共出现过8次
    dg：一共出现过7次
    c：长度为2的只有cf(1)。已知f，故可推c
    a：出现过8次的字母只有ac。已知c，故可推a
    d：长度为4的只有bcdf(4)。已知bcf，故可推d
    g：出现过7次的字母只有dg。已知d，故可推g
    '''
    decode_dict = {}
    code_dict = {}
    # e 一共出现过4次
    str_e = list_searcher(hex_pattern_list, times=4)
    decode_dict[str_e] = "e"
    code_dict['e'] = str_e
    # b 一共出现过6次
    str_b = list_searcher(hex_pattern_list, times=6)
    decode_dict[str_b] = "b"
    code_dict['b'] = str_b
    # f 一共出现过9次
    str_f = list_searcher(hex_pattern_list, times=9)
    decode_dict[str_f] = "f"
    code_dict['f'] = str_f
    # c 长度为2的只有cf(1)。已知f，故可推c
    str_c = list_searcher(hex_pattern_list, length=2) \
        .replace(code_dict['f'], '')
    decode_dict[str_c] = 'c'
    code_dict['c'] = str_c
    # a 出现过8次的字母只有ac。已知c，故可推a
    str_a = list_searcher(hex_pattern_list, times=8) \
        .replace(code_dict['c'], '')
    decode_dict[str_a] = 'a'
    code_dict['a'] = str_a
    # d 长度为4的只有bcdf(4)。已知bcf，故可推d
    str_d = list_searcher(hex_pattern_list, length=4) \
        .replace(code_dict['b'], '') \
        .replace(code_dict['c'], '') \
        .replace(code_dict['f'], '')
    decode_dict[str_d] = 'd'
    code_dict['d'] = str_d
    # g 出现过7次的字母只有dg。已知d，故可推g
    str_g = list_searcher(hex_pattern_list, times=7) \
        .replace(code_dict['d'], '')
    decode_dict[str_g] = 'g'
    code_dict['g'] = str_g
    # 解码完成
    dec_output_list = []
    for hex_output in hex_output_list:
        dec_output = ""
        for hex_output_abc in hex_output:
            dec_output += decode_dict[hex_output_abc]
        dec_output_list.append(number_dict[str_sort(dec_output)])
    return "".join(dec_output_list)


part_1 = 0
part_2 = 0
with open('2021-08.data') as f:
    for single_entry in f.read().split('\n'):
        out = get_decode(single_entry)
        for num in out:
            if num in "1478":
                part_1 += 1
        part_2 += int(out)

print(part_1)
print(part_2)
