#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_diskio_cmd():
    diskio_cmd = """
########################## 读取数据的详细过程 ######################################

1. 用户进程发起读取请求
2. 文件系统层处理
3. 检查页缓存
4. 缺少缓存情况下的处理
  a. 文件系统查找
  b. 提交块I/O请求
5. 块设备驱动处理
6. 硬件设备读取数据
7. 数据返回到内核空间
8. 数据返回到用户空间

########################## 写数据的详细过程 ######################################

1. 用户进程发起写入请求
2. 文件系统层处理
3. 更新页缓存
4. 标记脏页
5. 脏页回写到磁盘
  a. 回写机制
     pdflush守护进程**：定期扫描脏页并将其写回磁盘。
     同步操作**：用户进程可以调用 `fsync()` 或 `sync()` 强制将数据写入磁盘。
  b. 提交块I/O请求
6. 块设备驱动处理
7. 硬件设备写入数据
8. 更新元数据
9. 数据一致性与持久化

########################## IO缓慢可能是哪些原因造成的 #################################

磁盘I/O缓慢可能由多种原因引起，涉及硬件、软件、配置等多个方面。以下是一些常见的原因及其可能的解决方案：

1. 硬件问题
2. 系统配置问题
3. 软件问题
4. 负载问题
5. 网络存储问题（如NFS、SAN）
6. 缓存问题
7. 磁盘碎片化
8. RAID配置问题
9. 热量和散热问题

########################## 常见磁盘读写速度对比 ######################################

| 磁盘类型                      | 接口类型     | 理论顺序读写速度 | 特点
| ----------------------------- | ------------ | ---------------- | -------------
| **机械硬盘（HDD）**           | SATA3        | 80 - 200 MB/s    | 大容量、低成本，随机访问慢
| **2.5" SATA 固态硬盘（SSD）** | SATA3        | 450 - 550 MB/s   | 普通消费级 SSD
| **M.2 SATA SSD**              | SATA3        | 450 - 550 MB/s   | 接口变小，速度同上
| **NVMe SSD（PCIe 3.0 x4）**   | PCIe 3.0 x4  | 1500 - 3500 MB/s | 高速顺序访问
| **NVMe SSD（PCIe 4.0 x4）**   | PCIe 4.0 x4  | 5000 - 7000 MB/s | 高端台式机、服务器使用
| **企业级 SAS HDD**            | SAS 12Gbps   | 200 - 300 MB/s   | 多用于服务器、高可靠性
| **企业级 SSD（U.2 / NVMe）**  | PCIe/SAS/U.2 | 3000+ MB/s       | 高负载读写、寿命长
| **机械 RAID（如 RAID5）**     | SATA/SAS     | 500 - 1000 MB/s+ | 多盘并发可提升吞吐
| **RAM Disk（内存盘）**        | 内存         | 5000+ MB/s       | 用于极高性能需求或测试

   """
    print(diskio_cmd)  

def print_netio_cmd():
    print("netio usage command:")
    netio_cmd = """
css -s
   """
    print(netio_cmd)  

def print_cputop10_cmd():
    print("cputop10 usage command:")
    cputop10_cmd = """
css -s
   """
    print(cputop10_cmd)  

def print_memtop10_cmd():
    print("memtop10 usage command:")
    memtop10_cmd = """
css -s
   """
    print(memtop10_cmd)  

def print_sar_cmd():
    print("sar usage command:")
    sar_cmd = """
在 Linux 中，sar 是 System Activity Reporter 的缩写，是一个系统性能监控工具。
sar 工具可以收集、报告和保存系统活动的信息，包括 CPU 使用率、内存和交换空间的利用率、I/O 和网络性能等。sar 通常是 sysstat 软件包的一部分。

# 查看 CPU 使用情况：
sar -u

# 查看内存使用情况：
sar -r

# 查看设备 I/O 活动：
sar -b

# 查看磁盘I/O的详细信息
sar -d
这个命令下的dev对应的设备可以通过lsblk第二列的输出MAJ:MIN进行匹配

# 查看网络活动：
sar -n DEV

# 指定时间间隔和次数：
sar -u 5 3
这个命令每隔 5 秒报告一次 CPU 使用情况，总共报告 3 次。

# 查看历史数据：
sar -f /var/log/sa/sa10
这个命令从指定的历史文件中读取数据。通常，/var/log/sa/ 目录中存储着 sar 的历史数据文件。


# 在centos7中配置sar服务
sudo yum install sysstat
sudo systemctl start sysstat
sudo systemctl enable sysstat

# sysstat 套件的其他工具，例如 iostat、mpstat 和 pidstat，也用于不同方面的系统监控，可以与 sar 配合使用以提供更全面的系统性能分析。
   """
    print(sar_cmd) 

def print_reboot_cmd():
    reboot_cmd = """
以下内容为查询Linux重启原因的一般方法

############################## 重启的常见原因 ######################################

1、内核崩溃 (OOM Killer)
2、硬件问题 (过热、电源故障)
3、计划内的系统更新
4、手动重启 (可能是其他用户)


############################## 确定Linux系统重启的原因 ######################################

journalctl --list-boots 
# 列出所有启动记录

journalctl --since "2025-04-01 10:00:00" --until "2025-04-03 15:00:00"
# 如果知道大概的重启时间，可以查看特定时间段的日志：

journalctl -b -1 
# 查看上一次启动的完整日志

egrep -i "reboot|shutdown" /var/log/syslog 
egrep -i "reboot|shutdown" /var/log/messages
# 查看传统的系统日志

last -x | grep reboot -9 
last -x | grep shutdown -9
# 查看最后登录记录

ll /var/crash/
# 检查是否有内核崩溃转储

uptime
# 查看开机时间

############################## 查看是否有手动重启的记录 ######################################

# 查看认证日志中的重启记录
grep -i "shutdown\|reboot\|halt\|poweroff" /var/log/auth.log

# 检查root用户的命令历史
sudo cat /root/.bash_history | grep -i "reboot\|shutdown"

# 查看是否有定时重启任务
sudo grep -r "reboot\|shutdown" /etc/cron*

# 如果是手动重启，命令记录中会有明确的reboot、shutdown、init 6等命令   
   """
    print(reboot_cmd) 

def print_boot_fail_cmd():
    boot_fail_cmd = """
############################## emergency mode ######################################

在 Linux 系统中，开机进入 emergency mode（紧急模式） 表示系统启动过程中发生了严重错误，导致无法正
常进入多用户或图形界面模式，只能进入一个非常基本的修复环境。这种模式下，系统只挂载了最基本的文件系统，
并启动了最少的服务，提供一个 root shell 用于排查和修复问题。

通常可以看到如下提示：
Welcome to emergency mode! After logging in, type "journalctl -xb" to view system logs, 
"systemctl reboot" to reboot, "systemctl default" to try again to boot into default mode.

常见导致进入 emergency mode 的原因：
	/etc/fstab 配置错误
		比如挂载了不存在的分区或格式不正确。
	磁盘或分区损坏
		系统启动时无法挂载某些必要的文件系统。
	内核参数错误
		比如 grub 配置了错误的 root 分区。
	权限或 SELinux 问题
		某些关键目录权限不对，或者 SELinux 策略阻止正常启动。
	系统文件缺失或损坏
		比如 /bin/bash 或 /lib 目录损坏。

典型的排查步骤：
	查看错误日志：
		journalctl -xb
	检查 /etc/fstab 是否有错误挂载项：
		cat /etc/fstab
	尝试挂载文件系统看是否报错：
		mount -a
	使用 fsck 修复分区错误：
		fsck /dev/sdX
	修复后重启系统：
		reboot

		
############################## grub error ######################################

./mytool --show  grub
   """
    print(boot_fail_cmd) 

def print_core_dump_cmd():
    core_dump_cmd = """

############################## 概念（conception） ##########################################

“Core dump”（核心转储，也叫core文件）是操作系统在程序崩溃（通常是段错误 segmentation fault）时，保存程序在崩溃瞬间内存内
容的一种方式。它会把程序当时的内存、寄存器、调用栈等信息写入一个文件，通常叫 core 或 core.<pid>。

这个文件的主要用途是 调试，开发者可以通过调试器（比如 gdb）查看程序在崩溃时的状态，找到 bug 的根源。

############################## instance ###################################################

#include <stdio.h>

int main() {
	int *p = NULL;
	*p = 10;  // 访问了空指针

        return 0;
}

# 这时候程序就会崩溃，并生成 core 文件。你可以用 gdb 来分析它：

############################## caution #####################################################

core 文件的默认生成路径：通常在当前目录，也可能由 /proc/sys/kernel/core_pattern 控制。
是否允许生成 core dump：
	有时候系统或用户限制了 core 文件的生成，比如：
		ulimit -c 0  # 表示不生成 core 文件
	改成：
		ulimit -c unlimited
	永久生效：
		修改 /etc/security/limits.conf
程序崩溃常见信号：如 SIGSEGV, SIGABRT，收到这些信号时可能会生成 core 文件。
   """
    print(core_dump_cmd) 

def print_gdb_cmd():
    gdb_cmd = """

############################## 概念（conception） #########################################

gdb（GNU Debugger）是一个强大的调试工具，主要用于调试 C/C++ 等语言编写的程序。


############################## 准备工作 ###################################################

1. 编译程序时添加调试信息
	在使用 gdb 调试前，需要在编译程序时加入 -g 选项：
		gcc -g test.c -o test

2. 启动 gdb
	gdb ./test

############################## gdb 常用命令分类整理 #########################################

（1）运行控制命令
	命令 		| 作用
	run 或 r 	| 运行程序
	start 		| 从 main() 函数开始运行
	continue 或 c 	| 继续执行（如遇断点会停下）
	next 或 n 	| 单步执行（不进入函数）
	step 或 s 	| 单步执行（进入函数）
	finish 		| 执行完当前函数并返回调用处
	until 		| 运行直到当前循环结束或下一行
	kill 		| 停止正在运行的程序
	quit 或 q 	| 退出 gdb

（2）断点操作命令
	命令 			   | 作用
	break 行号 或 b 行号 	   | 在某行设置断点（如：b 25）
	break 函数名 		   | 在函数入口设置断点
	info breakpoints 或 i b    | 查看当前所有断点
	delete 			   | 删除所有断点
	delete 编号 		   | 删除指定编号断点
	disable 编号 / enable 编号 | 禁用/启用某个断点
	clear 行号 		   | 清除指定行的断点

（3）查看变量与表达式
	命令 			 | 作用
	print 变量名 或 p 变量名 | 查看变量的值（如：p x）
	display 表达式 		 | 每次中断自动显示表达式的值
	undisplay 		 | 取消自动显示
	set var 变量=值 	 | 修改变量的值（如：set var x=10）
	info locals 		 | 查看当前函数中的局部变量
	info args 		 | 查看当前函数的参数

（4）栈和函数调用
	命令 		| 作用
	backtrace 或 bt | 查看函数调用栈
	frame 编号 	| 切换到指定帧（函数调用层）
	info frame 	| 查看当前帧信息
	up / down 	| 在调用栈中向上/向下移动

（5）查看源代码
	命令 		| 作用
	list 或 l 	| 查看当前代码（默认显示10行）
	list 行号 	| 查看指定行附近的代码
	list 函数名 	| 查看某函数的源代码

（6）调试核心转储文件
	gdb ./test core
		可用于分析程序崩溃原因。
		core 文件可通过 ulimit -c unlimited 启用生成。
		
		
############################## 调试小技巧 #############################################

1、使用 tab 自动补全命令。
2、可使用 set pagination off 禁止翻页，避免查看信息被暂停。
3、用 info registers 查看寄存器值（用于底层调试）。

############################## instance #############################################

// test.c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int x = 3, y = 4;
    int result = add(x, y);
    printf("Result = %d\\n", result);
    return 0;
}


# 调试流程如下：
gcc -g test.c -o test
gdb ./test
(gdb) break main
(gdb) run
(gdb) next
(gdb) print x
(gdb) break add
(gdb) continue
(gdb) step
(gdb) print a
(gdb) quit
   """
    print(gdb_cmd) 

def print_launch_ipv6_cmd():
    launch_ipv6_cmd = """

Linux上开启ipv6功能

############################# 修改内核参数 #######################################

编辑 /etc/sysctl.conf，加上这两行：
net.ipv6.conf.all.disable_ipv6 = 0
net.ipv6.conf.default.disable_ipv6 = 0

第一条是开启整体的IPv6支持。
第二条是让新创建的网络接口也支持IPv6。

sudo sysctl -p


############################ 修改网卡配置文件 #####################################

sudo vi /etc/sysconfig/network-scripts/ifcfg-ens33
IPV6INIT=yes
DHCPV6C=yes
IPV6_AUTOCONF=yes


sudo nmcli connection reload
sudo nmcli connection up ens33


############################## caution #########################################


1、（如果是CentOS/RHEL的话）有时候还需要确认grub的启动参数里，没有禁用IPv6，比如：
查看 /etc/default/grub 文件，有没有 ipv6.disable=1 这样的参数，如果有的话，要删掉或者改成 ipv6.disable=0。

修改完后，更新grub并重启：
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
sudo reboot

2、 如果是虚拟机，注意宿主机网络也要支持IPv6。

3、 有些情况下（比如防火墙规则、网络管理器设置）还需要进一步确保IPv6是允许的，不然虽然内核支持IPv6，但网络上收发不了。

   """
    print(launch_ipv6_cmd) 

