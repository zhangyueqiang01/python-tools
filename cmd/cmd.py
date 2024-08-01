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


#hexdump 命令输出的最左边的内容是文件的偏移地址（offset address）
#以十六进制格式表示。这些地址指示每行输出数据在文件中的起始位置。
#例如：
0000000		#从文件的第0个字节开始
0000010		#表示这一行数据从文件的第 16 个字节（0x10）开始
0000020		#偏移地址是 0000020，即第 32 个字节


#查看字符串对应的16进制格式
echo 'hello world' | hexdump -C
00000000  68 65 6c 6c 6f 20 77 6f  72 6c 64 0a              |hello world.|
0000000c

   """
    print(hexdump_cmd) 

