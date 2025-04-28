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
	-b：以八进制方式显示每个字节的数据。
	-c：以字符方式显示每个字节的数据。
	-C：以标准的十六进制+ASCII方式显示数据，这是最常用的选项之一。
	-d：以十进制显示两个字节的数据。
	-o：以八进制显示两个字节的数据。
	-x：以十六进制显示两个字节的数据。
	-e format：根据指定的格式字符串来显示数据。
	-f format_file：从指定的格式文件中读取格式字符串并根据此格式显示数据。
	-n length：只处理输入文件的前 length 字节。
	-s offset：跳过输入文件开头的 offset 个字节后再开始处理。
	-v：显示完整输出，不压缩相同的行。
	-V：显示版本信息然后退出。



#输出内容以十六进制和 ASCII 格式显示
hexdump -C example.txt


#如果你只想查看文件的前 512 个字节，可以使用 -n 选项（查看MBR）
hexdump -C -n 512 /dev/vda


#查看MBR中的启动代码
hexdump -C -n 440 /dev/vda

#查看MBR中的分区表
hexdump -s 446 -n 64 -C /dev/vda
  -s 446：这个选项指定从文件或输入的第446个字节开始（偏移量为446字节）。在MBR（主引导记录）中，分区表从第446字节开始。
  -n 64：这个选项指定只读取64字节的数据。在MBR中，分区表的长度为64字节

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

def print_yum_cmd():
    print("yum usage command:")
    yum_cmd = """
# create ftp repo
/etc/fstab
...
/ISO/rhel-server-7.4-x86_64-dvd.iso /var/ftp/rhel74 iso9660 defaults 0 0
...

[rhel74]
name=rhel74
baseurl=ftp://192.168.2.254/rhel74/
enabled=1
gpgcheck=0
   """
    print(yum_cmd) 

def print_nic_cmd():
    print("nic usage command:")
    nic_cmd = """
[root@ct7_node01 network-scripts]# cat ifcfg-eth1
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
IPADDR=192.168.2.1
NETMASK=255.255.255.0
FROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=eth1
DEVICE=eth1
ONBOOT=yes
   """
    print(nic_cmd) 

def print_process_cmd():
    process_cmd = """
查看进程运行过程的命令主要包括 实时监控进程状态 和 查看历史进程信息 两类。以下是常用的命令和操作：
#####################################实时监控进程运行##################################
top
# 交互操作：
#	P：按 CPU 使用率排序。
#	M：按内存使用率排序。

htop
# 增强版的 top，支持彩色显示和鼠标操作。

# 查看当前进程快照，常用组合：
ps aux               # 显示所有用户的所有进程
ps -ef               # 显示完整格式的进程信息
ps -u username       # 查看指定用户的进程
ps -p PID -o lstart  # 查看进程的启动时间

# 监控进程的 CPU、内存、I/O 等资源使用情况。
pidstat -u -p PID 1   # 每1秒刷新指定进程的CPU使用情况
pidstat -d -p PID     # 查看进程的I/O统计


#####################################查看进程的详细运行历史##################################

# 跟踪进程的系统调用（如文件、网络操作）
strace -p PID         # 实时跟踪运行中进程
strace -o log.txt command  # 将命令的系统调用写入文件

# 跟踪进程的库函数调用（类似 strace，但针对动态库）
ltrace -p PID

# 性能分析工具，可记录进程的调用栈和热点函数
perf stat -p PID      # 统计进程的性能事件
perf record -p PID    # 记录进程运行数据（生成 `perf.data`）
perf report           # 分析记录结果


# 直接读取进程的运行时信息（如环境变量、打开文件等）
cat /proc/PID/environ     # 查看进程的环境变量
cat /proc/PID/cmdline     # 查看进程的启动命令
ls -l /proc/PID/fd        # 查看进程打开的文件描述符


#####################################日志与审计工具##################################

# 查看系统日志（适用于使用 systemd 的系统）
journalctl -u service_name  # 查看某个服务的日志
journalctl -f              # 实时跟踪日志

# 审计进程行为（需配置规则）
auditctl -w /path/to/file -p rwxa  # 监控文件的读写执行
ausearch -p PID                    # 查询特定进程的审计日志


#####################################其他实用命令##################################

# 根据名称查找进程 PID
pgrep -l nginx

# 以树状结构显示进程关系
pstree -p

# 统计命令执行时间
time command
   """
    print(process_cmd) 

def print_strace_cmd():
    strace_cmd = """
strace 是一个强大的调试工具，适用于 Linux 平台的程序
故障排查和系统调用分析。通过 strace，可以：
	监视程序执行过程中所有的系统调用
	发现文件权限、依赖库、网络通信等问题
	统计系统调用的时间，优化性能

############################## 基本用法 #####################################

# 跟踪程序的系统调用
strace ./your_program

# 跟踪已运行进程
strace -p <PID>

# 记录输出到文件
strace -o output.txt ./my_program


############################## 过滤系统调用 ##################################

# 仅跟踪 open、read、write 相关的系统调用
strace -e open,read,write ./my_program

# 仅跟踪网络相关系统调用
strace -e trace=network ./my_program
strace -e socket,connect,send,recv ./your_program

# 仅跟踪文件相关系统调用
strace -e trace=file ./my_program

# 仅跟踪进程管理相关的系统调用：
strace -e fork,execve,exit ./your_program


############################## 进阶使用 ######################################

# 统计每个系统调用的执行次数、时间占比等信息
strace -c ./my_program

# 跟踪 my_program 及其所有子进程
strace -f ./my_program

# 在每个系统调用前显示时间戳
strace -t ./my_program

# 显示每个系统调用与前一个调用的时间间隔
strace -r ./my_program


############################## 典型应用场景 ##################################

1. 排查程序崩溃原因
	strace ./crash_program
	观察最后几个系统调用，可能会看到 open() 失败、write() 失败或 segfault 相关信息
2. 分析程序卡顿
	strace -T -p <PID>
	观察哪些系统调用花费的时间最多，可能是 read() 或 poll()，可以进一步优化
3. 检查程序是否正确访问了某个文件：
	strace -e open,access ./your_program
	看到 open() 返回 EACCES（权限不足）或 ENOENT（文件不存在）可以帮助修复问题
4. 监测网络连接
	strace -e trace=network ./my_program
	如果程序涉及网络通信，可跟踪 connect、sendto、recvfrom 等调用
5. 找出进程依赖的文件
	strace -e open,stat ./your_program
	这可以帮助排查程序为何找不到某些文件


################################# tips #####################################

程序的运行一般分为三个阶段(以 hello world 举例)

1. 程序加载阶段
execve: 加载并运行你的可执行文件。比如你运行 ./hello，其实 shell 最终调用了 execve("./hello", argv, envp)。
brk / mmap: 分配堆内存、加载动态链接库（如 libc.so），mmap 用于映射库文件到内存。
open, read, mmap: 打开和读取 ELF 文件本身（可执行文件格式），加载所需的动态库，比如 /lib64/libc.so.6，/lib64/ld-linux-x86-64.so.2。


2. 程序运行阶段
write: printf 最终会调用 write 系统调用，把字符串 "Hello, World!\\n" 写到标准输出（通常是终端，文件描述符 1）。
printf -> puts -> fputs -> 底层 write。
（可选）fstat: 程序有时会查询标准输出是终端还是文件，用来决定是否启用缓冲。
（可选）read, close: 如果程序或标准库需要读取配置文件（比如 locale 设置），会有额外的 read/close。


3. 程序退出阶段
exit_group: 程序结束时调用 exit 或 return 0，最终内核调用 exit_group，通知操作系统进程终止，并清理资源。
   """
    print(strace_cmd) 

def print_top_cmd():
    top_cmd = """

top 是 Linux 系统中非常常用的性能监控命令之一，用于实时查看系统的资源使用情况，比如 CPU、内
存、进程等，是系统运维和性能调优必备的工具。

############################## 系统整体信息（前几行） ##############################

top - 18:07:40 up  8:30,  1 user,  load average: 0.00, 0.01, 0.05
Tasks: 216 total,   1 running, 215 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 32520788 total, 29491284 free,   663552 used,  2365952 buff/cache
KiB Swap: 10481660 total, 10481660 free,        0 used. 31328904 avail Mem

load average：1分钟、5分钟、15分钟的平均负载
Tasks：任务总数（正在运行、睡眠、僵尸等）
%Cpu(s)：CPU 各种使用情况
   us：用户态占用 CPU 的百分比（不含 nice 优先级进程）
   sy：内核态（系统）占用 CPU 的百分比
   ni：用户进程中调整过 nice 值的进程占用的 CPU 百分比
   id：空闲 CPU 百分比
   wa：等待 I/O（磁盘、网络）占用的 CPU 百分比
   hi：硬中断占用 CPU 百分比
   si：软中断占用 CPU 百分比
   st：虚拟机偷取的 CPU 百分比（如你是虚拟机中运行）
Mem：物理内存使用情况
Swap：交换分区使用情况

############################## 各进程信息（后面多行） ##########################

常见字段含义如下：
	PID：进程ID
	USER：进程所属用户
	PR/NI：优先级/Nice值
	VIRT：虚拟内存使用量
	RES：实际物理内存使用量
	%CPU：占用的CPU百分比（如果显示值为400%意味着，这个进程中的线程完全占用了4个核心）
	%MEM：占用的内存百分比	
	TIME+：进程累计占用CPU时间
	COMMAND：启动该进程的命令

ps： 一个进程本身不会同时在多个 CPU 上运行，但它的多个线程可以并发地运行在多个 CPU 上

############################## shortcut key #################################

快捷键 | 功能
 P     | 按 CPU 使用率排序（默认）
 M     | 按内存使用率排序（Shift + M）
 m     | 图形化展示内存使用率
数字1  | 显示每个 CPU 核心的使用情况
 T     | 按时间排序
 k     | 杀掉一个进程（输入 PID）
 r     | 修改进程优先级（renice）
 h     | 查看帮助
 q     | 退出 top
 H     | 切换线程显示（可以在头几行看到Tasks变成Threads）
 f     | 查看展示进程的哪些属性，上下箭头移动，”空格“选择
h / ?  | 查看更多的快捷键

ps： 可以使用 ps 命令查看线程列表
	ps -T -p <PID>
		-T：显示线程
		-p：指定进程 PID
	查看所有线程
		ps -eLf（L：显示线程）

############################## tips #########################################

1、 查看某个用户的进程：
	top -u username

2、 设置刷新间隔（默认 3 秒）： 按 d 然后输入秒数。

3、 将输出重定向为静态快照：
	top -b -n 1 > top_snapshot.txt

4、 查看高负载的进程中的线程使用了哪些cpu 
	top -H -p <PID>
	在 top 界面中：
		按 f → 选择 j 选项（显示 P 列：Last used CPU）
		按 P 或 Shift+P：按 CPU 使用率排序
		P 列代表线程最近运行在哪个 CPU 上（例如 CPU 0、CPU 3 等）
   """
    print(top_cmd) 

def print_htop_cmd():
    htop_cmd = """

htop 是 Linux 系统中一个非常实用的交互式进程查看工具，它是传统 top 命令的增强版。相比 top，
htop 界面更加美观、直观，并且支持更多的操作方式，比如使用键盘方向键进行导航、筛选和排序等。

############################## 基本特点 ##############################

1、 彩色界面，更易阅读
2、 交互性强
3、 多核CPU支持
4、 支持进程树
5、 动态刷新

yum install htop -y   # 或者在新版本中使用 dnf

############################## shortcut key ##########################

快捷键 	| 功能描述
F1 	| 帮助
F2 	| 设置选项
F3 	| 搜索进程
F4 	| 过滤进程
F5 	| 显示进程树
F6 	| 更改排序方式
F7/F8 	| 改变 nice 值（优先级）
F9 	| 杀死选中的进程
F10 	| 退出 htop

P     	| 按 CPU 使用率排序（默认）
M     	| 按内存使用率排序（Shift + M）
   """
    print(htop_cmd) 

def print_shell_cmd():
    shell_cmd = """

##################### cmd exec process ##################################

	用户输入命令
	     ↓
	Shell解析命令
	     ↓
	查找可执行文件路径
	     ↓
	fork() 创建子进程
	     ↓
	子进程调用 execve()
	     ↓
	内核加载新程序，执行
	     ↓
	父Shell等待子进程结束

小补充：
	如果是内建命令（比如 cd），就不会 fork，Shell自己执行。
	如果命令不存在或没有执行权限，execve 会失败，shell会显示 command not found 或 permission denied。

########################## advanced #####################################

基于 GNU Bash：
	bash 调用的是 glibc 提供的 execve 函数，
	然后 glibc 里面的 execve 才真正去触发 CPU 的 syscall 指令


glibc（比如 /lib64/libc.so.6）里真正的 execve 函数（伪代码）大概是这样：
long sys_execve(const char *pathname, char *const argv[], char *const envp[])
{
    // 使用 syscall 指令，系统调用号 __NR_execve
    return syscall(__NR_execve, pathname, argv, envp);
}


完整流程：
bash源码：调用 execve(path, argv, envp)
   ↓
glibc库：实现了 execve()，内部通过 syscall(__NR_execve, ...)
   ↓
CPU执行 syscall 指令
   ↓
内核态 syscall 表：根据 rax=59，找到 sys_execve() 函数
   ↓
内核内部实现 execve（加载新程序、替换地址空间）


对应的汇编程序：
mov rax, __NR_execve    ; 把系统调用号（execve）放入 rax
mov rdi, pathname       ; 第一个参数，程序路径
mov rsi, argv           ; 第二个参数，argv数组
mov rdx, envp           ; 第三个参数，环境变量
syscall                 ; 触发软中断，进入内核模式


Summarize:
    bash 调用 glibc的execve函数；
    glibc 发出真正的 syscall指令；
    CPU切换到内核态，执行 59号系统调用；
    内核根据 sys_execve() 完成新程序的加载和运行！
   """
    print(shell_cmd) 

