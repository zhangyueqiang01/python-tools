#!/bin/bash

# 检查是否提供了文件名参数
if [ $# -eq 0 ]; then
    echo "用法: $0 文件名"
    echo "示例: $0 names.txt"
    exit 1
fi

file=$1

# 检查文件是否存在
if [ ! -f "$file" ]; then
    echo "错误: 文件 $file 不存在"
    exit 1
fi

# 计算文件行数
line_count=$(wc -l < "$file")

# 确保文件不为空
if [ "$line_count" -eq 0 ]; then
    echo "错误: 文件 $file 为空"
    exit 1
fi

# 生成随机行号 (1到行数之间)
random_line=$((1 + RANDOM % line_count))
# $(( )) - 这是 Bash 的算术扩展语法，用于执行数学计算
# RANDOM - 这是 Bash 的一个内置变量，每次引用时都会返回一个 0 到 32767 之间的随机整数
# % - 这是取模（求余数）运算符
# line_count - 这是文件的总行数（通过之前的 wc -l 命令获得）

# 提取并打印随机行
sed -n "${random_line}p" "$file"

