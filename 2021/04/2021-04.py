#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2021-12-21
"""
import numpy


def check(draw_list, board_one):
    # row
    for r in range(0, 5):
        if set(draw_list) >= set(board_one[r, :].tolist()):
            return True
    # column
    for r in range(0, 5):
        if set(draw_list) >= set(board_one[:, r].tolist()):
            return True
    return False


# load data file
with open('2021-04.data') as f:
    rf = f.read().split('\n\n')
    # draw numbers
    draw = []
    for st in rf[0].split(','):
        draw.append(int(st))
    # random set of boards
    boards = []
    for board_base in rf[1:]:
        board_tmp = numpy.zeros((5, 5), dtype=numpy.int)
        i, j = 0, 0
        for row in board_base.split('\n'):
            for column in row.strip().replace('  ', ' ').split(' '):
                board_tmp[i, j] = int(column)
                j += 1
            i += 1
            j = 0
        boards.append(board_tmp)

# Part 1
draw_final = []
board_final = []
for draw_len in range(5, len(draw)):
    for board in boards:
        c = check(draw[0:draw_len], board)
        if c:
            draw_final = draw[0:draw_len]
            board_final = board
            break
    if draw_final:
        P2 = set(board_final.reshape((1, 25))[0].tolist()).difference(set(draw_final))
        print(draw_final[-1] * sum(P2))
        break

# Part 2
board_final = []
for draw_len in range(5, len(draw)):
    draw_final = draw[0:draw_len]
    for board in boards:
        c = check(draw[0:draw_len], board)
        if not c:
            draw_final = []
            break
    if not draw_final:
        continue
    for board in boards:
        c = check(draw_final[0: -1], board)
        if not c:
            P2 = set(board.reshape((1, 25))[0].tolist()).difference(set(draw_final))
            print(draw_final[-1] * sum(P2))
            break
    break
