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

def print_assembly_cmd():
    assembly_cmd = """
		  	    #######################
			    #Assembly instructions#
			    #######################

###########################################简介################################
汇编语言是一种底层编程语言，直接操作计算机硬件。以下是一些常用的汇编指令，主要基于x86架构：


###########################################常用指令##################################

数据传输指令
	MOV - 将数据从一个位置传送到另一个位置。例如：MOV AX, BX将BX寄存器中的值复制到AX寄存器。
	PUSH - 将数据压入堆栈。例如：PUSH AX将AX寄存器中的值压入堆栈。
	POP - 从堆栈中弹出数据。例如：POP AX从堆栈中弹出一个值并存储在AX寄存器中。
	LEA - 获取有效地址。例如：LEA AX, [BX+SI]将BX+SI的内存地址加载到AX中。
	
算术运算指令
	ADD - 加法运算。例如：ADD AX, BX将AX和BX中的值相加，结果存储在AX中。
	SUB - 减法运算。例如：SUB AX, BX将BX从AX中减去，结果存储在AX中。
	MUL - 无符号乘法。例如：MUL BX用AX中的值乘以BX中的值，结果存储在AX和DX中。
	DIV - 无符号除法。例如：DIV BX用AX中的值除以BX，商存储在AX中，余数存储在DX中。
	INC - 自增运算。例如：INC AX将AX中的值加1。
	DEC - 自减运算。例如：DEC AX将AX中的值减1。
	
逻辑运算指令
	AND - 位与操作。例如：AND AX, BX对AX和BX中的值进行位与操作，结果存储在AX中。
	OR - 位或操作。例如：OR AX, BX对AX和BX中的值进行位或操作，结果存储在AX中。
	XOR - 位异或操作。例如：XOR AX, BX对AX和BX中的值进行位异或操作，结果存储在AX中。
	NOT - 位非操作。例如：NOT AX对AX中的值进行位取反。
	
控制转移指令
	JMP - 无条件跳转。例如：JMP LABEL跳转到LABEL处执行代码。
	JE/JZ - 如果相等或零，则跳转。例如：JE LABEL当上一次计算结果为零时跳转到LABEL。
	JNE/JNZ - 如果不相等或不为零，则跳转。例如：JNE LABEL当上一次计算结果不为零时跳转到LABEL。
	CALL - 调用子程序。例如：CALL SUBROUTINE跳转到子程序SUBROUTINE执行，并在完成后返回调用点。
	RET - 从子程序返回。例如：RET从子程序返回到调用点。
	
数据比较指令
	CMP - 比较两个操作数。例如：CMP AX, BX比较AX和BX的值，并设置标志寄存器。
	TEST - 测试操作数。例如：TEST AX, BX对AX和BX进行位与操作，但不存储结果，仅设置标志寄存器。



###########################################备注##################################

这些指令是x86汇编语言中的基础，掌握它们有助于理解底层计算机操作和编写高效的低级代码。
   """
    print(assembly_cmd) 

