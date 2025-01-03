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

def print_dline_cmd():
    print("合营客户专线信息查看方法:")
    dline_cmd = """
##############################
#合营专线客户相关信息查看方法#
##############################

#专线（dedicated line）
#先在cloudscope上通过客户邮箱找到专线对应的vlan号

//通过接入网关找到对应的pop
网关					pop
169.254.195.11 				10.255.223.191
169.254.195.10 				老68

Info: The max number of VTY users is 5, the number of current VTY users online is 2, and total number of terminal users online is 2.
      The current login time is 2024-09-04 10:44:06+08:00.
      The last login time is 2024-09-04 10:41:25+08:00 from 10.77.51.125 through SSH.
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>display current-configuration | section include 3763		//通过vlan找到vpn-instance
#
ip vpn-instance DLine13
 ipv4-family
  route-distinguisher 3763:3763
  vpn-target 3763:3763 export-extcommunity
  vpn-target 3763:3763 import-extcommunity
#
interface Eth-Trunk1.13
 ip binding vpn-instance DLine13
 ip address 169.254.195.11 255.255.255.0
 dot1q termination vid 3763
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>display ip interface brief | include DLine13		//查看本客户的互联地址，以下均为客户的专线互联地址
*down: administratively down
!down: FIB overload down
^down: standby
(l): loopback
(s): spoofing
(d): Dampening Suppressed
The number of interface that is UP in Physical is 1169
The number of interface that is DOWN in Physical is 10
The number of interface that is UP in Protocol is 1159
The number of interface that is DOWN in Protocol is 20
Interface                   IP Address/Mask    Physical Protocol VPN           
10GE1/0/12                  10.103.0.2/30      up       up       DLine13       
Eth-Trunk1.13               169.254.195.11/24  up       up       DLine13       
Eth-Trunk1.130              169.254.195.11/24  up       up       DLine130      
Eth-Trunk1.131              169.254.195.11/24  up       up       DLine131      
Eth-Trunk1.132              169.254.195.11/24  up       up       DLine132      
Eth-Trunk1.133              169.254.195.11/24  up       up       DLine133      
Eth-Trunk1.134              169.254.195.11/24  up       up       DLine134      
Eth-Trunk1.135              169.254.195.11/24  up       up       DLine135      
Eth-Trunk1.136              169.254.195.11/24  up       up       DLine136      
Eth-Trunk1.137              169.254.195.11/24  up       up       DLine137      
Eth-Trunk1.138              169.254.195.11/24  up       up       DLine138      
Eth-Trunk1.139              169.254.195.11/24  up       up       DLine139      
Eth-Trunk26.2705            10.101.0.13/30     up       up       DLine13       
Eth-Trunk26.2714            10.101.0.9/30      up       up       DLine13       
Eth-Trunk26.2723            10.101.0.18/30     up       up       DLine13       
Eth-Trunk26.2734            10.101.0.26/30     up       up       DLine13       
Eth-Trunk26.2735            10.101.0.22/30     up       up       DLine13       
Eth-Trunk26.2736            10.101.0.6/30      up       up       DLine13       
Eth-Trunk26.2737            10.101.0.34/30     up       up       DLine13       
Eth-Trunk26.2738            10.101.0.46/30     up       up       DLine13       
Eth-Trunk26.2739            10.101.0.42/30     up       up       DLine13       
Eth-Trunk26.2741            10.103.0.29/30     up       up       DLine13       
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>display ip routing-table vpn-instance DLine13 protocol static 			//查看本客户专线的路由条目                  
Proto: Protocol        Pre: Preference
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
DLine13 Routing Table : Static
         Destinations : 58       Routes : 60       Configured Routes : 60        

Static routing table status : <Active>
         Destinations : 58       Routes : 60        

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

        0.0.0.0/0   Static  60   0             RD  169.254.195.201 Eth-Trunk1.13			//专线访问互联网的路由
       10.1.0.0/16  Static  60   0             RD  10.101.0.5      Eth-Trunk26.2736			//以下是访问专线内部网络路由条目
                    Static  60   0             RD  10.103.0.1      10GE1/0/12
       10.2.0.0/16  Static  60   0             RD  10.103.0.1      10GE1/0/12
       10.3.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
       10.5.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
       10.6.2.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
       10.6.4.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
       10.7.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
       10.9.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.10.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.13.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.14.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.21.0.0/24  Static  60   0             RD  10.101.0.33     Eth-Trunk26.2737
      10.21.2.0/23  Static  60   0             RD  10.101.0.33     Eth-Trunk26.2737
      10.21.3.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.21.5.0/24  Static  60   0             RD  10.101.0.33     Eth-Trunk26.2737
      10.21.6.0/23  Static  60   0             RD  10.101.0.33     Eth-Trunk26.2737
     10.21.10.0/23  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.21.11.0/24  Static  60   0             RD  10.101.0.33     Eth-Trunk26.2737
     10.21.12.0/23  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.24.0.0/16  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.30.0.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.30.2.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.30.3.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.30.4.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.30.6.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.11.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.12.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.13.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.14.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.15.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.21.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.22.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.23.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.24.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
     10.30.25.0/24  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.33.0.0/22  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.34.0.0/22  Static  50   0             RD  10.103.0.1      10GE1/0/12
      10.70.0.1/32  Static  60   0             RD  10.101.0.41     Eth-Trunk26.2739
      10.71.2.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
      10.71.3.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.71.10.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.71.11.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.71.12.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.71.20.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.71.21.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.71.30.1/32  Static  60   0             RD  10.103.0.30     Eth-Trunk26.2741
     10.100.0.0/16  Static  60   0             RD  169.254.195.201 Eth-Trunk1.13
    192.168.0.0/24  Static  60   0             RD  10.101.0.21     Eth-Trunk26.2735
                    Static  60   0             RD  10.103.0.1      10GE1/0/12
    192.168.1.0/24  Static  50   0             RD  10.101.0.21     Eth-Trunk26.2735
   192.168.70.0/24  Static  60   0             RD  10.101.0.25     Eth-Trunk26.2734
   192.168.90.0/24  Static  60   0             RD  10.101.0.25     Eth-Trunk26.2734
    192.169.0.0/16  Static  60   0             RD  10.103.0.1      10GE1/0/12
    192.169.1.0/24  Static  60   0             RD  10.101.0.25     Eth-Trunk26.2734
    192.169.3.0/24  Static  60   0             RD  10.101.0.25     Eth-Trunk26.2734
    192.169.8.0/24  Static  60   0             RD  10.101.0.21     Eth-Trunk26.2735
   192.169.21.0/24  Static  60   0             RD  10.101.0.21     Eth-Trunk26.2735
  198.152.254.0/24  Static  60   0             RD  10.103.0.1      10GE1/0/12
                
Static routing table status : <Inactive>
         Destinations : 0        Routes : 0         
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>
<YZYHB214JF-6-8-1&6-6-2-CE6851-1U42-1U43>

   """
    print(dline_cmd) 

def print_ckernel_cmd():
    print("编译Linux内核:")
    ckernel_cmd = """
		  	    ######################
			    #Compiling the kernel#
			    ######################

###########################################安装依赖环境################################
yum groupinstall Development Tools
yum install ncurses-devel elfutils-libelf-devel openssl-devel bc -y


###########################################配置内核功能##################################
进入源码目录，使用make menuconfig生成内核功能的配置文件.config


###########################################编译内核##################################
make -j 8
#"-j 8" 代表使用8颗cpu同时编译


###########################################安装模块##################################
make modules_install
#安装将内核功能编译成模块的文件，安装完成后在/lib/modules/目录下会生成一个同内核版本号的目录，目录下便是新内核的模块。


###########################################安装内核##################################
make install
#安装完后会在/boot目录下生成新的内核文件、initramfs文件、并更新grub.cfg文件


###########################################验证##################################
reboot
#新的内核不是默认启动选项，手动选择即可
uname -r

		  	    ##################
			    #编译相关内容说明#
			    ##################

###########################################内核功能选择##################################
Arrow keys navigate the menu: 使用箭头键可以在菜单中上下左右移动。
<Enter> selects submenus ---> (or empty submenus ----): 按下回车键可以选择一个子菜单（如果有子菜单的话），或者选择一个没有子菜单的选项。
Highlighted letters are hotkeys: 在菜单选项中，某些字母会被高亮显示，按下相应的字母键可以快速选择该选项。
Pressing <Y> includes, <N> excludes, <M> modularizes features:
	1、按下 Y 键可以将某个功能包括在内核中，标记为 [*] built-in。
	2、按下 N 键可以排除某个功能，不包括在内核中，标记为 [ ] excluded。
	3、按下 M 键可以将某个功能作为模块编译，标记为 <M> module。
Press <Esc><Esc> to exit: 按两次 Esc 键可以退出菜单配置界面。
<? for Help: 按 ? 键可以查看帮助信息。
</ for Search: 按 / 键可以进行搜索。
Legend: [*] built-in [ ] excluded <M> module < > module capable:
	1、[ ] excluded 表示该功能被排除，不会编译进内核。
	2、[*] built-in 表示该功能会被编译进内核，成为内核的一部分。
	3、<M> module 表示该功能会被编译为模块，可以在需要时加载。
	4、< > module capable 表示该功能可以被编译为模块。


###########################################任务类型##################################
CALL：表示调用脚本，例如 CALL scripts/checksyscalls.sh 表示正在调用脚本 checksyscalls.sh 来检查系统调用。
DESCEND：进入一个子目录进行处理，例如 DESCEND objtool 表示进入 objtool 子目录进行编译。
CC：表示使用 C 编译器（通常是 gcc）编译某个 .c 源文件，例如 CC init/main.o 表示正在编译 init/main.c 文件，生成 main.o。
LD：表示链接操作，通常将多个目标文件链接成一个可执行文件，例如 LD /tmp/linux-5.16.14/tools/objtool/libsubcmd-in.o 表示在链接 libsubcmd-in.o。
AR：表示创建静态库（归档操作），例如 AR libsubcmd.a 表示创建归档文件 libsubcmd.a，通常是将多个目标文件打包成一个静态库。
MKDIR：表示创建目录，例如 MKDIR /tmp/linux-5.16.14/tools/objtool/arch/x86/lib/ 表示正在创建目标目录。
GEN：表示生成某个文件，通常通过脚本或工具自动生成的文件，例如 GEN inat-tables.c。
CHK：检查生成的文件是否需要更新，例如 CHK include/generated/compile.h。
UPD：更新生成的文件，例如 UPD include/generated/compile.h。
LINK：表示生成最终的可执行文件，例如 LINK objtool 表示正在链接生成 objtool 可执行文件。
WRAP：表示包装（wrap）某个工具或命令，通常是在编译过程中对某些工具进行包装，方便调用。例如，某些编译工具可能通过 WRAP 处理来生成特定功能的封装脚本。
SHIPPED：表示某个文件是预先准备好的，不需要重新生成，直接使用已经存在的文件。通常是在内核编译过程中，某些资源是以“已交付”（shipped）形式存在的，避免重复生成。
SYSHDR：表示系统头文件（System Header）。这一操作通常涉及系统头文件的处理或生成，可能是复制或创建特定的系统头文件。
SYNC：表示同步操作。在内核编译中，有时需要确保某些文件或过程与其他部分保持同步，例如与主机系统或其他编译步骤同步。
HOSTCC：表示使用主机的 C 编译器来编译目标文件。由于内核可能是为不同的架构编译的，因此主机（编译服务器或本地开发机器）上的编译工具可能与目标系统不同。HOSTCC 表示在主机环境下进行的编译。
HOSTLD：表示使用主机的链接器（Linker）。与 HOSTCC 类似，HOSTLD 负责在主机系统上进行的链接操作。
MKELF：表示创建 ELF 文件格式（Executable and Linkable Format）。ELF 是一种可执行文件和目标文件格式，常用于 Linux 和类 Unix 系统。MKELF 通常涉及将目标文件打包成 ELF 文件。
AS：汇编器（Assembler），用于将汇编代码编译成目标代码。例如，AS arch/x86/kernel/entry_32.o 表示使用汇编器处理汇编代码并生成 entry_32.o。
CPP：C 预处理器（C PreProcessor），用于处理宏定义、头文件包含等预处理操作。例如，CPP somefile.i 表示预处理某个 C 文件生成中间文件 .i。
CXX：C++ 编译器，用于编译 C++ 源文件。例如，CXX somefile.o 表示正在使用 C++ 编译器编译 somefile.cpp。
HOSTAR：用于创建静态库文件的归档操作，与主机系统相关联。例如，HOSTAR 用于主机上的归档操作，类似于 AR，但适用于本地（主机）环境。
INSTALL：表示安装某个目标文件或模块。例如，INSTALL modules 表示将编译好的模块安装到指定目录中。
MODPOST：模块后处理（Module Postprocessing）。在编译完内核模块后，MODPOST 用于检查和处理内核模块，确保其可以在内核中正确加载和使用。
CCLD：链接 C 编译后的文件。CCLD 是 CC 和 LD 的组合，用于处理 C 语言编译的最终链接步骤。
VDSO：表示编译和链接与用户空间有关的可执行代码（虚拟动态共享对象），通常出现在特定的架构代码中。例如，VDSO arch/x86/entry/vdso/vdso.so。
GENHDR：生成头文件（Generate Header），表示通过某个工具或脚本自动生成头文件。例如，GENHDR include/generated/autoconf.h。
HOSTCXX：主机 C++ 编译器，用于在主机系统上编译 C++ 文件，类似于 HOSTCC 但适用于 C++。
DTB：设备树二进制文件（Device Tree Blob），用于嵌入式系统和硬件设备的信息描述。通常用于将设备树文件 .dts 编译为 .dtb。
OBJCOPY：对象文件复制工具，用于将目标文件从一种格式转换为另一种格式。例如，OBJCOPY vmlinux vmlinux.bin。
STRIP：用于去除二进制文件中的符号表和调试信息，生成更小的可执行文件。例如，STRIP vmlinux。
CLEAN：清理生成的文件。执行 make clean 或者其他类似命令时，CLEAN 会删除编译生成的文件，以便重新编译时不产生冲突。
DEPMOD：依赖模块（Dependency Modules），在模块编译之后用于生成模块的依赖信息。
   """
    print(ckernel_cmd) 

def print_mysql_cmd():
    print("mysql basic operate:")
    mysql_cmd = """

		  	    ###############
			    #mysql基础操作#
			    ###############

####################################基础操作################################

mysql -u your_username -p
CREATE DATABASE 数据库名;
SHOW DATABASES;
USE your_database;
SHOW TABLES;
DROP DATABASE <database_name>;


CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    ...
);

DROP TABLE table_name;


INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

#####################################查询操作################################

SELECT column1, column2, ...
FROM table_name
[WHERE condition]
[ORDER BY column_name [ASC | DESC]]
[LIMIT number];


-- 选择所有列的所有行
SELECT * FROM users;

-- 选择特定列的所有行
SELECT username, email FROM users;

-- 添加 WHERE 子句，选择满足条件的行
SELECT * FROM users WHERE is_active = TRUE;

-- 添加 ORDER BY 子句，按照某列的升序排序
SELECT * FROM users ORDER BY birthdate;

-- 添加 ORDER BY 子句，按照某列的降序排序
SELECT * FROM users ORDER BY birthdate DESC;

-- 添加 LIMIT 子句，限制返回的行数
SELECT * FROM users LIMIT 10;
   """
    print(mysql_cmd) 

def print_nginx_cmd():
    print("nginx usage:")
    nginx_cmd = """
# 客户端通过域名访问服务器时会将域名与被解析的ip一同放在请求中。当请求到了nginx中时。nginx会先去匹配ip，如果listen中
# 没有找到对应的ip，就会通过域名进行匹配，匹配成功以后，再匹配端口。当这三步完成，就会找到对应的server的location对应的资源。

server {
        listen       ip:端口;
        # 当listen出现了ip时，server_name就失去了意义。所以不配置也罢了。
        #server_name  域名;
 
        access_log   日志地址1;
        error_log    日志地址2;
 
        location / {
            root   /data/www/151;
            index  index.html index.htm;
        }
    }
	

# 在测试机本地上监听8080、8081、8082三个端口，模拟三台主机分别处理来自客户端访问picture、video、text的请求

[root@node9 ~]# vim /etc/nginx/nginx.conf
server {
        listen       80;
        server_name  192.168.2.19;
 
        access_log   /usr/local/nginx/test/data/logs/www.test151.com.log;
        error_log    /usr/local/nginx/test/data/logs/www.test151.com.error.log;
 
        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
 
        location / {
            root   /usr/share/nginx/html;
            index  index.html index.htm;
        }
 
        location ~ /picture/ {
            proxy_pass  http://127.0.0.1:8080;
        }
       
        location ~ /video/ {
            proxy_pass  http://127.0.0.1:8081;
        }
       
        location ~ /text/ {
	    proxy_pass http://127.0.0.1:8082;
        }
 
        error_page 404 /404.html;
        location = /404.html {
        }
 
        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
   }
}


# location 指令说明
# 该指令用于匹配 URL， 语法如下：

location [ = | ~ | ~* | ^~] uri {
 
}

= ：用于不含正则表达式的 uri 前，要求请求字符串与 uri 严格匹配， 如果匹配成功，就停止继续向下搜索并立即处理该请求。
~：用于表示 uri 包含正则表达式，并且区分大小写。
~*：用于表示 uri 包含正则表达式，并且不区分大小写。
^~：用于不含正则表达式的 uri 前，要求 Nginx 服务器找到标识 uri 和请求

   """
    print(nginx_cmd) 


def print_virsh_cmd():
    print("virsh usage command:")
    virsh_cmd = """

				#########
				# virsh #
				#########

virsh 是 KVM/Libvirt 环境下的一个强大的管理工具，能够通过命令行方式管理虚拟机。除了查看虚拟机的
资源使用情况，virsh 还提供了许多常用的命令，涵盖虚拟机的生命周期管理、存储、网络等操作。以下是
一些常用的 virsh 命令及其用法：

####################################虚拟机生命周期管理################################

启动虚拟机：
virsh start <虚拟机名称>

关闭虚拟机：
virsh shutdown <虚拟机名称>

强制关闭虚拟机：
virsh destroy <虚拟机名称>

挂起虚拟机：
virsh suspend <虚拟机名称>
暂停虚拟机的运行，类似于将物理机挂起。

恢复虚拟机：
virsh resume <虚拟机名称>
恢复之前挂起的虚拟机。

重启虚拟机：
virsh reboot <虚拟机名称>

销毁虚拟机：
virsh undefine <虚拟机名称>
从 KVM 中永久删除虚拟机的定义，不会影响虚拟机的磁盘数据。


####################################查看虚拟机状态和信息################################

查看所有虚拟机：
virsh list --all
列出所有虚拟机，包括正在运行的和已关闭的虚拟机。

查看虚拟机的详细信息：
virsh dominfo <虚拟机名称>
显示指定虚拟机的详细信息，如 UUID、CPU、内存、状态等。

查看虚拟机的控制台输出：
virsh console <虚拟机名称>
进入虚拟机的控制台，适用于没有 GUI 的虚拟机（可以按 Ctrl+] 退出控制台）。

获取虚拟机的XML配置：
virsh dumpxml <虚拟机名称>
输出虚拟机的 XML 配置文件，可以用于备份或修改虚拟机配置。

编辑虚拟机配置：
virsh edit <虚拟机名称>
使用文本编辑器编辑虚拟机的 XML 配置文件，适用于高级配置修改。


####################################虚拟机快照管理################################

创建虚拟机快照：
virsh snapshot-create-as <虚拟机名称> <快照名称>
为虚拟机创建一个快照，可以指定快照的名称和描述。

列出虚拟机的快照：
virsh snapshot-list <虚拟机名称>
查看指定虚拟机的所有快照。

恢复虚拟机到某个快照：
virsh snapshot-revert <虚拟机名称> <快照名称>
将虚拟机恢复到指定快照的状态。

删除虚拟机快照：
virsh snapshot-delete <虚拟机名称> <快照名称>
删除指定的快照。


####################################网络管理################################


列出虚拟网络：
virsh net-list --all
列出所有虚拟网络。

查询某个网络的 DHCP 租约信息：
virsh net-dhcp-leases <网络名称>

启动虚拟网络：
virsh net-start <网络名称>
启动指定的虚拟网络。

关闭虚拟网络：
virsh net-destroy <网络名称>
关闭指定的虚拟网络。

创建网络：
virsh net-create <网络.xml>
根据 XML 文件创建一个虚拟网络。

编辑网络配置：
virsh net-edit <网络名称>
编辑现有虚拟网络的 XML 配置文件。

查看虚拟机的 MAC 地址：
virsh domiflist <虚拟机名称>

通过 arp 命令查找该 MAC 地址对应的 IP：
arp -n | grep <MAC 地址>


####################################存储管理################################


列出存储池：
virsh pool-list --all
列出所有的存储池。

创建存储池：
virsh pool-create <存储池.xml>
根据 XML 文件创建一个存储池。

启动存储池：
virsh pool-start <存储池名称>
启动指定的存储池。

关闭存储池：
virsh pool-destroy <存储池名称>
关闭指定的存储池。

删除存储池：
virsh pool-delete <存储池名称>
删除存储池中的数据，并移除该存储池的定义。

查看存储卷：
virsh vol-list <存储池名称>
列出指定存储池中的所有存储卷。

####################################虚拟机磁盘管理################################


挂载磁盘：
virsh attach-disk <虚拟机名称> <磁盘镜像路径> <目标设备>
动态为虚拟机添加一个磁盘。

卸载磁盘：
virsh detach-disk <虚拟机名称> <目标设备>
从虚拟机中卸载磁盘。

####################################虚拟机迁移################################

热迁移虚拟机：
virsh migrate --live <虚拟机名称> <目标URI>
实时迁移虚拟机到另一台主机，不需要关闭虚拟机。


####################################其他################################
virt-top 是一个专门用于监控虚拟机资源使用情况的工具，类似于 top，但专注于虚拟机。

sudo yum install virt-top   # Red Hat 系列系统
sudo apt-get install virt-top  # Debian/Ubuntu 系列系统

使用 virt-top 命令来监控所有虚拟机的负载：
sudo virt-top
   """
    print(virsh_cmd) 

def print_xxd_cmd():
    print("xxd usage command:")
    xxd_cmd = """
		  	    ##################
			    # xxd 命令的使用 #
			    ##################


# xxd 是一个非常实用的命令行工具，用于在十六进制格式和二进制格式之间转换数据。
# 它通常用于查看和编辑二进制文件内容，也可以用作调试工具来分析文件的底层数据结构。

#####################################基本功能################################
1、十六进制转储
将二进制文件以十六进制和ASCII的可视化形式显示，方便分析文件内容。

2、生成可编辑的十六进制文本
将二进制文件转换为十六进制文本（hexdump），可以用文本编辑器修改后再转换回二进制。

3、反转转换
将编辑后的十六进制文件重新转换为二进制文件。


#####################################常见选项################################
选项	功能
-p	仅显示纯十六进制，不带偏移量和ASCII部分（“plain hexdump”）。
-r	将十六进制转储文本恢复成二进制文件（与 -p 通常一起使用）。
-s <offset>	从指定偏移量处开始显示内容。
-l <length>	显示指定长度的数据。
-c <columns>	每行显示的字节数（默认为 16）。
-u	将十六进制显示为大写（默认是小写）。


#####################################示例################################

# 将bitmap中的0修改为全1
# 假设 Block Bitmap 位于 block 122
dd if=/root/disk.img bs=1024 count=1 skip=122 of=bitmap.bin
xxd bitmap.bin > bitmap.hex


# 修改bitmap.hex中的相应位
sed -i s/0000/ffff/g bitmap.hex
sed -i s/ffff/0000/ bitmap.hex


# 写回修改
xxd -r bitmap.hex bitmap.bin
dd if=bitmap.bin of=/root/disk.img bs=1024 count=1 seek=122 conv=notrunc
   """
    print(xxd_cmd) 

