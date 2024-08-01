#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_hexdump_cmd():
    print("hexdump usage command:")
    hexdump_cmd = """
		#########
		#hexdump#
		#########

hexdump 是 Linux 系统中的一个命令行工具，用于以十六进制格式查看文件内容。
它可以将文件内容以十六进制、八进制、ASCII 等多种格式输出，非常适合用来调试和分析二进制文件。


hexdump 常用的选项包括：
	-C：输出内容以十六进制和 ASCII 格式显示。
	-b：以八进制格式显示每个字节。
	-c：以字符格式显示每个字节。
	-d：以十进制格式显示每个字节。
	-o：以八进制格式显示每个字节。
	-x：以十六进制格式显示每个字。


#输出内容以十六进制和 ASCII 格式显示
hexdump -C example.txt


#如果你只想查看文件的前 512 个字节，可以使用 -n 选项（查看MBR）
hexdump -C -n 512 /dev/vda


#查看MBR中的启动代码
hexdump -C -n 440 /dev/vda

   """
    print(hexdump_cmd) 

