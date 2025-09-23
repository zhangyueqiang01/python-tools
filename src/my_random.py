#!/usr/bin/python
# -*- coding: utf-8 -*-


import random

print(random.random()) # 生成 [0.0, 1.0) 之间的随机浮点数
print(random.uniform(1, 10))  # 示例输出：3.14159
print(random.randint(1, 6))  # 生成 [a, b] 之间的整数（包含 a 和 b）
print(random.randrange(0, 10, 2))  # 0-10之间的偶数，从指定范围按步长生成随机整数

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))  # 从序列中随机选择一个元素

