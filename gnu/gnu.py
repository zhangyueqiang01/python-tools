#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_gnu_cmd():
    gnu_cmd = """
##################################### GNU简介 ################################

GNU项目（GNU Project）是一个自由软件运动的重要组成部分，由自由软件基金会（FSF）的创始人理查德·斯托曼（Richard Stallman）
于1983年9月27日发起。GNU是递归缩写，意思是“GNU's Not Unix”，表示它是一个与Unix兼容但完全自由的软件操作系统。

##################################### GNU项目的宗旨 ################################

GNU项目的目标是创建一个完全自由的类Unix操作系统，用户可以自由使用、修改、分享该系统的所有组成部分，不受专有软件许可的限制。
自由在这里指的是：
	自由运行程序的自由，无论目的为何。
	研究程序如何工作并根据需要修改它的自由（前提是可以获得源代码）。
	重新分发副本的自由，帮助他人。
	发布你修改后的程序版本的自由，让社区受益。


##################################### GNU系统的组成 ################################

GNU项目开发了一整套自由软件工具，这些工具构成了类Unix操作系统的主要部分，包括：
	GNU编译器套件（GCC）：强大的C/C++等语言的编译器。
	GNU调试器（GDB）：程序调试工具。
	GNU Bash：著名的Shell解释器。
	GNU Coreutils：如 ls、cp、rm 等基础命令工具。
	GNU Make：构建工具。
	GNU Emacs：强大的文本编辑器。
	glibc：GNU的C语言标准库。


##################################### 与Linux的关系 ################################

虽然GNU项目开发了大部分用户空间的工具，但一直没有完全实现自己的内核（GNU Hurd开发进度缓慢）。1991年，林纳斯·托瓦兹（Linus Torvalds）
发布了Linux内核，这给了GNU项目一个可以结合的内核。
于是，很多人使用GNU工具 + Linux内核，形成了完整的操作系统。这就是我们今天常说的“Linux系统”，实际上应该更准确地称为 GNU/Linux系统。


##################################### 头文件和库文件存放路径 ################################

# GNU 项目中的头文件和库文件（GNU C Library/glibc 为代表）在 Linux 系统中的存放位置

常见头文件：
路径				说明
/usr/include/			主系统头文件路径，包含大多数标准 C 头文件，如 stdio.h、unistd.h
/usr/include/linux/		内核相关的头文件，如 linux/fs.h、linux/limits.h 等
/usr/include/x86_64-linux-gnu/	在某些多架构支持的系统中（如 Debian/Ubuntu），一些平台特定的 glibc 头文件会放在这里

常见动态库（.so） 和 静态库（.a）：
路径				说明
/lib/ 或 /lib64/		系统引导级别的共享库（如 libc.so.6，ld-linux-x86-64.so.2）
/usr/lib/ 或 /usr/lib64/	常规用户空间程序依赖的库
/usr/lib/x86_64-linux-gnu/	多架构支持的系统会把不同架构的库放这里（比如 Ubuntu/Debian）

类型			常见路径
头文件（.h）		/usr/include/、/usr/include/linux/
动态库（.so）		/lib/、/lib64/、/usr/lib/、/usr/lib64/
架构相关扩展路径	/usr/include/x86_64-linux-gnu/、/usr/lib/x86_64-linux-gnu/
   """
    print(gnu_cmd) 

def print_gcc_cmd():
    print("gcc usage command:")
    gcc_cmd = """
gcc 是 GNU 编译器套件（GNU Compiler Collection）中用于编译 C 程序的命令行工具。
官网： https://gcc.gnu.org/mirrors.html
获取 GCC 的源代码：
	wget https://ftp.gnu.org/gnu/gcc/gcc-13.2.0/gcc-13.2.0.tar.gz
	tar -xvzf gcc-13.2.0.tar.gz
	或者：
	yum install gcc
	yum install gcc-devel
	yum install gcc-source  # 如果有此包

源码内容简介：
	gcc/：核心编译器代码
	libgcc/：运行时支持库
	include/：内部头文件
	config/：不同平台的配置文件
	cp/、c/：不同语言前端（比如 C++）

############################## gcc基本操作 ##################################

# 查看gcc编译时使用的内部文件
gcc -print-search-dirs
gcc -v


# 常用选项
	选项	含义
	-o file	指定输出文件名
	-c	只编译为目标文件（.o 文件），不链接
	-Wall	打开所有常见的警告
	-Werror	将所有警告当作错误处理
	-g	生成调试信息
	-O2	开启优化等级 2
	-I<dir>	添加头文件搜索路径
	-L<dir>	添加库文件搜索路径
	-l<lib>	链接名为 lib<lib>.so 或 lib<lib>.a 的库

############################## 示例用法 ##################################

gcc source.c -o output	# 基本用法
gcc -c hello.c   		# 生成 hello.o
gcc main.c util.c -o app	#链接多个源文件
gcc -g test.c -o test		#开启调试信息（用于 gdb 调试）
gcc -O2 main.c -o main		#开启优化（适合发布版本）

动态库（.so）的生成步骤：
	1. 编写源文件，例如 add.c
	2. gcc -fPIC -c add.c	# 使用 -fPIC 生成位置无关代码（必须）
	3. gcc -shared -o libmymath.so add.o	# 使用 -shared 生成动态库
	4. gcc main.c -L. -lmymath -o main		# 使用动态库编译其他程序
	5. export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH && ./main	# 运行时指定动态库路径（否则可能找不到）


静态库（.a）的生成步骤
1. 编写源文件，例如 add.c
2. gcc -c add.c  	# 生成 add.o 目标文件
3. ar rcs libmymath.a add.o		# 使用 ar 工具生成静态库
	r：插入文件；
	c：创建库；
	s：创建符号索引。
4. gcc main.c -L. -lmymath -o main		# 使用静态库编译其他程序
	-L.：表示当前目录；
	-lmymath：链接名为 libmymath.a 的库（省略前缀 lib 和扩展名 .a）；
   """
    print(gcc_cmd) 

