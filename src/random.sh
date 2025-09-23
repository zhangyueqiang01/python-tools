#!/bin/bash

# Bash 没有 random 命令，但通过 $RANDOM 变量或其他工具可以实现随机数生成功能。

# $RANDOM 会返回一个 0 到 32767 之间的随机整数，例如：
echo $RANDOM

# 生成 1 到 100 之间的随机数
echo $((1 + RANDOM % 100))


