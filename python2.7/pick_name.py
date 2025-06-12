# -*- coding: utf-8 -*-
import random

# 打开文件并读取所有行
with open('names.txt', 'r') as f:
    names = [line.strip() for line in f if line.strip()]

# 随机选择一个名字
selected_name = random.choice(names)

print "选中的人名是：%s" % selected_name

