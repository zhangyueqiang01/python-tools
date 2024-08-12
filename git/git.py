#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_git_cmd():
    print("git usage command:")
    git_cmd = """
	#添加一个特定的目录，比如my_folder
	git add my_folder

	#添加当前目录及其所有子目录中的所有文件
	git add .

	git commit -m "提交信息"
	git push
	git log
	git status

	# 暂存本地更改
	git stash
	
	# 拉取远程仓库的更新
	git pull origin master
	
	# 恢复暂存的更改（如果需要）
	git stash pop

   """
    print(git_cmd)  


def print_lamp_cmd():
    print("lamp 快速搭建方法:")
    lamp_cmd = """

[root@node07 html]#yum install httpd mariadb-server

[root@node07 html]# rpm -qa | grep -i php
php-pdo-5.4.16-43.el7_4.x86_64
php-common-5.4.16-43.el7_4.x86_64
php-5.4.16-43.el7_4.x86_64
php-mysql-5.4.16-43.el7_4.x86_64
php-cli-5.4.16-43.el7_4.x86_64


[root@node07 html]# cat /var/www/html/index.php 
<?php
phpinfo();
?>


#设置mqriadb账号密码
mysql_secure_installation


#数据库

   """
    print(lamp_cmd) 

def print_objdump_cmd():
    print("objdump usage command:")
    objdump_cmd = """
					#########
					#objdump#
					#########

###########################################简介################################
objdump 是一个用于显示二进制文件（如可执行文件、目标文件、库文件）信息的命令行工具。
它通常用于反汇编程序、查看符号表、检查段信息等。objdump 是 GNU Binutils 工具包的一部分，
广泛用于 Linux 和其他类 Unix 系统。

###########################################用法##################################


1、反汇编代码:
	-d：反汇编代码段。
	-D：反汇编所有段。
objdump -d example.o

2、查看文件头:
	-f：显示文件头信息，包括目标文件的格式、架构、入口点等。
objdump -f example.o

3、查看符号表:
	-t：显示符号表。
objdump -t example.o

4、查看节信息:
	-h：显示各个节的头信息（段信息），包括节名、大小、虚拟地址等。
objdump -h example.o

5、显示调试信息:
	-g：显示调试信息（如果有）。
objdump -g example.o

6、查看重定位表:
	-r：显示重定位信息。
objdump -r example.o

7、查看所有信息:
	-x：显示文件的所有头信息，包括符号表、节信息、重定位表等。
objdump -x example.o

###########################################示例##################################


1、查看一个可执行文件的所有信息，可以使用以下命令：
objdump -a -f -h -r -t -x -d example.o

2、查看MBR的启动代码
objdump -D -b binary -mi386 -Maddr16,data16 mbr.bin
	-b 选项指定输入文件的格式。在这个例子中，指定 mbr.bin 是一个原始的二进制文件（没有特定的文件格式，比如 ELF 或 COFF），通常这种格式用于处理诸如引导扇区、固件镜像等文件。
	-mi386 选项指定目标架构。这里 i386 表示使用 Intel 80386 指令集，这是 x86 架构的早期版本。由于引导扇区通常运行在 x86 架构的低级模式下，所以指定 i386 是合适的。
	-Maddr16,data16
		-M 选项指定反汇编器的特定选项。在这个例子中：
			addr16：表示使用 16 位的地址模式，意味着指令中的地址操作数将被解释为 16 位宽度。
			data16：表示使用 16 位的数据操作模式，意味着数据操作数将被解释为 16 位宽度。
		这些选项通常用于反汇编 16 位的 x86 实模式代码，这在引导扇区（MBR）中非常常见。
	mbr.bin:
		这是要被反汇编的二进制文件。mbr.bin 通常是一个包含主引导记录（Master Boot Record, MBR）的文件。
   """
    print(objdump_cmd) 

