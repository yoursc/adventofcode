#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author : Ven
@Date   : 2020/12/21
"""
DIC = []
with open("2020-21.data") as f:
    for line in f.read().split("\n"):
        line_f = line.replace(")", "").split(" (contains ")
        ingredient_set = set(line_f[0].split(" "))
        allergen_set = set(line_f[1].split(", "))
        DIC.append({"ingredients": ingredient_set, "allergens": allergen_set})

# 待推定的 过敏原-[成分] 字典
allergen_ingredient_pending = {}
# 已确定 成分-过敏原 字典
ingredient_allergen_confirmed = {}

# 遍历数据源，过敏原潜在素材名单求交集初步求解
for line in DIC:
    ingredient_set = line["ingredients"]
    allergen_set = line["allergens"]
    for allergen in allergen_set:
        if allergen not in allergen_ingredient_pending:
            allergen_ingredient_pending[allergen] = ingredient_set
        else:
            allergen_ingredient_pending[allergen] = ingredient_set.intersection(allergen_ingredient_pending[allergen])

while 1:
    for (allergen, ingredient_set) in allergen_ingredient_pending.items():
        if len(ingredient_set) == 1:
            ingredient_allergen_confirmed[ingredient_set.pop()] = allergen
            del allergen_ingredient_pending[allergen]
            break
        confirmed_ingredient = ingredient_set.intersection(ingredient_allergen_confirmed.keys())
        if len(confirmed_ingredient) > 0:
            allergen_ingredient_pending[allergen] = ingredient_set.difference(confirmed_ingredient)
            break
    if len(allergen_ingredient_pending) == 0:
        break

for (allergen, ingredient_set) in allergen_ingredient_pending.items():
    print(allergen, ingredient_set)

ANSWER_1 = 0
for line in DIC:
    ingredient_set = line["ingredients"]
    for ingredient in ingredient_set:
        if ingredient not in ingredient_allergen_confirmed:
            ANSWER_1 += 1
print(ANSWER_1)

ANSWER_2 = []
for hh in sorted(ingredient_allergen_confirmed.items(), key=lambda d: d[1], reverse=False):
    ANSWER_2.append(hh[0])
print(",".join(ANSWER_2))
