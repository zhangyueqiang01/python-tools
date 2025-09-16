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

def print_scp_cmd():
    scp_cmd = """
scp（secure copy）是 Linux/Unix 系统中用来 在本地和远程主机之间进行安全复制 文件或目录的命
令。它基于 SSH 协议，因此具有加密传输的特点，安全性较高。

########################## basic synopsis #################################

scp [参数] 源路径 目标路径

  参数	含义
  -r	递归复制整个目录
  -P	指定远程主机的端口（注意大写）
  -p	保留文件的修改时间、访问时间等属性
  -q	静默模式，不显示传输进度
  -v	显示详细调试信息（常用于排错）
  -C	启用压缩
  -l	限制传输速度
  -v	查看执行过程中的详细信息
  -vvv	看更详细的调试信息


########################## instance #####################################

# 复制整个目录
scp -r /path/to/local/dir user@remote:/path/to/remote/

# 指定端口号
scp -P 2222 file.txt user@remote:/path/

# 限制速度为 100KB/s（即 800 Kbit/s）
scp -l 800 file.txt user@remote:/path/


########################## caution #####################################

scp 无法断点续传（如需支持断点续传推荐使用 rsync）。
要查看 scp 执行过程中的详细信息（例如连接过程、认证、文件传输状态等），可以使用参数 -v（verbose，冗长模式）。
   """
    print(scp_cmd) 

def print_ps_cmd():
    ps_cmd = """
############################## tips #########################################

按内存/CPU 占用排序
ps aux --sort=-%mem | head
ps aux --sort=-%cpu | head

按用户名筛选进程
ps -U root -u root u 或者 ps aux | grep root

输出字段定制
ps -eo pid,user,%cpu,%mem,vsz,rss,tty,stat,start,time,command
| 字段    | 含义
| ------- | ------------- 
| pid     | 进程 ID
| user    | 所属用户
| %cpu    | CPU 占比
| %mem    | 内存占比
| vsz     | 虚拟内存使用量（KB）   
| rss     | 实际物理内存使用量（KB）
| tty     | 终端
| stat    | 进程状态
| start   | 启动时间
| time    | 占用 CPU 时间
| command | 启动命令


查看某个父进程的所有子进程
ps --ppid 1234

查看整个进程树
ps axjf

查看所有用户的进程总数
ps -eo user= | sort | uniq -c | sort -nr

查看某个用户的进程总内存占用
ps -u username -o rss= | awk '{sum+=$1} END {print sum/1024 " MB"}'

显示线程（其中 L 表示线程，f 表示全格式。每个线程都会显示一行。）
ps -eLf

显示完整命令行参数（避免被截断）
ps -eo args | grep kvm
   """
    print(ps_cmd) 

def print_dmidecode_cmd():
    dmidecode_cmd = """
###################################### DESCRIPTION #################################################

dmidecode 是 Linux 系统中用于查看 DMI（Desktop Management Interface）/SMBIOS（System Management BIOS） 
信息的命令行工具，它可以显示很多底层硬件的信息，比如 BIOS、主板、CPU、内存、系统序列号等。

############################## option #########################################
| 选项  | 全写形式   | 说明
| ---- | ----------- | ------------------------------ 
| `-h` | `--help`    | 显示帮助信息
| `-q` | `--quiet`   | 安静模式，隐藏描述文字（只输出字段值）
| `-s` | `--string`  | 仅输出指定字符串（需要配合字段名）
| `-t` | `--type`    | 指定要查询的类型编号或名称
| `-H` | `--handle`  | 仅显示指定的 Handle（如 `0x0100`）
| `-u` | `--dump`    | 以十六进制和ASCII形式显示原始数据
| `-d` | `--dev-mem` | 指定 `dev/mem` 路径（默认 `/dev/mem`）
| `-V` | `--version` | 显示版本信息

############################ instance #########################################

查看系统摘要信息
sudo dmidecode -t system

查看 BIOS 信息
sudo dmidecode -t bios

查看主板信息
sudo dmidecode -t baseboard

查看 CPU 信息
sudo dmidecode -t processor

查看内存插槽信息（包括空插槽）
sudo dmidecode -t memory

查看所有支持的类型（Type）
sudo dmidecode -t
    例如：
	0：BIOS
	1：System
	2：Baseboard
	4：Processor
	17：Memory Device

############################## tips #########################################
| 任务             | 命令
| -----------------| ---------------------------------------- 
| 获取服务器型号   | `sudo dmidecode -t system`
| 查看序列号       | `sudo dmidecode -s system-serial-number`
| 查看 BIOS 版本   | `sudo dmidecode -t bios`
| 查看内存插槽数量 | `sudo dmidecode -t memory`
| 检查内存是否满插 | 查看 memory 中有多少条非 “No Module Installed”


只输出某一项
sudo dmidecode -s system-serial-number

| 字段名                    | 含义                     
| ------------------------- | ---------------------- 
| `bios-vendor`             | BIOS 厂商
| `bios-version`            | BIOS 版本
| `bios-release-date`       | BIOS 发布日期
| `system-manufacturer`     | 系统制造商
| `system-product-name`     | 系统产品名
| `system-version`          | 系统版本
| `system-serial-number`    | 系统序列号
| `system-uuid`             | 系统 UUID
| `baseboard-manufacturer`  | 主板厂商
| `baseboard-product-name`  | 主板产品名
| `baseboard-version`       | 主板版本
| `baseboard-serial-number` | 主板序列号
| `baseboard-asset-tag`     | 主板资产标签
| `chassis-manufacturer`    | 机箱制造商
| `chassis-type`            | 机箱类型（如 Laptop、Desktop）
| `chassis-serial-number`   | 机箱序列号
| `processor-family`        | 处理器家族
| `processor-version`       | 处理器型号
   """
    print(dmidecode_cmd) 

def print_lspci_cmd():
    lspci_cmd = """
############################## DESCRIPTION ##################################

lspci 是 Linux 系统中用于显示所有 PCI（Peripheral Component Interconnect）总线及其连
接设备信息的命令，常用于硬件排查、识别系统中的硬件设备等操作。
Peripheral Component Interconnect（外围设备组件互连）

############################### option ####################################
| 选项                   | 作用                        
| ---------------------- | ------------------------- 
| `-v`                   | 显示更详细的信息（verbose）
| `-vv`                  | 显示非常详细的信息（very verbose）
| `-k`                   | 显示每个设备所使用的驱动
| `-nn`                  | 显示设备的数字ID（vendor\:device）
| `-t`                   | 以树状结构显示 PCI 设备拓扑结构
| `-s <bus>`             | 指定总线编号，只显示该总线的设备
| `-d <vendor>:<device>` | 只显示指定厂商和设备ID的设备
| `-x`                   | 显示每个设备的配置空间（十六进制）
| `-b`                   | 以总线编号原始形式输出，不解析名称
| `-i <file>`            | 使用指定的 PCI ID 数据库文件

############################### instance ####################################

列出所有 PCI 设备（简略模式）
lspci

列出详细信息
lspci -v

查看每个设备对应的驱动信息
lspci -k

查看设备的厂商ID和设备ID
lspci -nn

查找某个特定设备（例如显示设备）
lspci | grep VGA

以树状结构展示 PCI 拓扑
lspci -t

查看某个具体设备（如总线地址 00:1f.2）
lspci -s 00:1f.2 -vv
   """
    print(lspci_cmd) 

def print_sysctl_cmd():
    sysctl_cmd = """
############################## DESCRIPTION ##################################

sysctl 是 Linux 和其他类 Unix 系统中用于 查看和修改内核参数 的命令。这些内核参数多位
于 /proc/sys/ 目录中，主要用于内存管理、网络设置、安全控制等系统级行为的调优。

基本语法
sysctl [options] [variable[=value]]


############################### option ######################################

| 选项               | 含义                               
| ------------------ | -------------------------------- 
| `-a` 或 `--all`    | 显示所有可用的内核参数及其当前值                 
| `-w` 或 `--write`  | 写入（设置）一个内核参数的值                   
| `-p` 或 `--load`   | 从配置文件（默认 `/etc/sysctl.conf`）加载参数 
| `-e` 或 `--ignore` | 加载配置时忽略无效参数（通常与 `-p` 一起使用）       
| `-n` 或 `--values` | 仅显示参数值，不显示参数名                    
| `-q` 或 `--quiet`  | 静默模式，抑制非错误输出，常用于脚本中              
| `-N`               | 显示所有参数的名称（不显示值）                  
| `-r`               | 显示所有支持正则匹配的参数（参数名匹配）             


############################### instance ####################################

1. 查看某个内核参数的当前值
sysctl net.ipv4.ip_forward
等价于：
cat /proc/sys/net/ipv4/ip_forward


2. 设置某个参数的值（临时）
sudo sysctl -w net.ipv4.ip_forward=1
等价于：
echo 1 > /proc/sys/net/ipv4/ip_forward
⚠️ 这种方式 重启后会失效。


3. 查看所有内核参数
sysctl -a
会列出当前系统中所有支持的参数及其值。


4. 从配置文件加载参数
sudo sysctl -p
默认从 /etc/sysctl.conf 加载。你也可以指定其他文件：
sudo sysctl -p /path/to/file.conf


5. 永久生效的方法
编辑 /etc/sysctl.conf 或 /etc/sysctl.d/xxx.conf 文件，添加例如：
net.ipv4.ip_forward = 1
vm.swappiness = 10
然后执行：
sudo sysctl -p


######################### Common parameter analysis #########################

| 参数                  | 含义
| --------------------- | ------------------------------
| `net.ipv4.ip_forward` | 是否开启 IP 转发（1 为启用，0 为禁用）
| `vm.swappiness`       | 控制内核将内存页换出到 swap 的倾向（范围 0–100）
| `fs.file-max`         | 系统允许打开的最大文件数
| `kernel.shmmax`       | 单个共享内存段的最大大小
| `net.core.somaxconn`  | socket 的 listen 队列最大长度
   """
    print(sysctl_cmd) 

def print_ftp_cmd():
    ftp_cmd = """
############################## DESCRIPTION ##################################

FTP（File Transfer Protocol，文件传输协议）常用的指令可以分为客户端操作命令和服务器响应码两
类。以下是FTP客户端常用命令，适用于你在终端使用 FTP 客户端时（例如 Linux 命令行 ftp 工具）

########################### FTP 常用命令（客户端） ###############################

ftp <ftp服务器地址>
系统会提示你输入用户名和密码，输入后即可进入交互模式（无特殊配置，输入Linux中的用户名和密码即可）。


| 命令         | 作用说明                               
| ------------ | ---------------------------------- 
| `open`       | 连接到 FTP 服务器，例如：`open 192.168.1.10` 
| `user`       | 输入用户名（系统自动提示输入）
| `pass`       | 输入密码（系统自动提示输入）
| `ls` / `dir` | 列出远程服务器当前目录的文件列表
| `cd`         | 切换远程服务器的目录，例如：`cd /home`
| `lcd`        | 切换本地客户端的当前目录，例如：`lcd /tmp`
| `pwd`        | 显示远程服务器当前目录
| `binary`     | 以二进制模式传输（适合传输图片、程序等）
| `ascii`      | 以ASCII模式传输（适合传输文本）
| `get`        | 下载文件，例如：`get filename.txt`
| `mget`       | 下载多个文件，例如：`mget *.txt`
| `put`        | 上传文件，例如：`put filename.txt`
| `mput`       | 上传多个文件，例如：`mput *.txt`
| `delete`     | 删除远程文件，例如：`delete test.txt`
| `mkdir`      | 创建远程目录
| `rmdir`      | 删除远程目录（需目录为空）
| `bye`/`quit` | 退出 FTP
| `help`/`?`   | 查看所有 FTP 命令及帮助信息

################################ tips #####################################

默认 Linux 中的 ftp 客户端是交互式的，如需更现代的命令行 FTP 工具，可使用 lftp 或 ncftp
   """
    print(ftp_cmd) 

def print_readelf_cmd():
    readelf_cmd = """
############################## DESCRIPTION ##################################

readelf 是 Linux 系统中用于查看 ELF（Executable and Linkable Format，可执行与可链
接格式） 文件内部结构的重要命令行工具。它由 GNU binutils 提供，主要用于分析二进制文件、可
执行文件、目标文件（.o）、共享库（.so）等。

############################### option ######################################

基本语法：
readelf [选项] <ELF文件>

| 选项       | 说明                          
| ---------- | ------------------------------------------ 
| `-h`       | 显示 ELF 文件头信息（ELF Header）
| `-l`       | 显示程序头表（Program Header Table）
| `-S`       | 显示节区头表（Section Header Table）
| `-s`       | 显示符号表（Symbol Table）
| `-r`       | 显示重定位信息（Relocation Entries）
| `-d`       | 显示动态段信息（Dynamic Section）
| `-V`       | 显示版本信息（版本需求和定义）
| `-a`       | 显示所有可用的信息（相当于组合了多个选项）


############################### instance ####################################

1. 查看 ELF 文件头
readelf -h a.out
# 输出 ELF 文件的基本信息，比如架构、入口地址、字节序等。

2. 查看节区头表（Section Header Table）
readelf -S a.out
# 可以看到所有节区（如 .text, .data, .bss, .symtab, .strtab）的名称、类型、偏移、大小等。

3. 查看程序头表（Program Header Table）
readelf -l a.out
# 用于分析 ELF 是如何被加载进内存的（如 LOAD, INTERP, DYNAMIC 等段）。

4. 查看符号表（Symbol Table）
readelf -s a.out
# 显示函数、变量等符号及其地址、类型、作用域。

5. 查看重定位信息
readelf -r a.out
# 显示编译时生成的重定位条目，常用于分析未完全链接的目标文件。

6. 查看动态段信息（用于共享库）
readelf -d libfoo.so
# 包括动态链接器、依赖库名、符号查找信息等。

7. 查看节区内容
readelf -x .text a.out 或：readelf -x 10 a.out
# 用于查看 .text 节（即机器码段）或指定编号的节的十六进制内容。

8. 查看所有信息
readelf -a a.out
# 相当于把多个选项合在一起全面分析 ELF 文件。

如需更详细帮助：
man readelf


############################# 与 objdump 的区别 ##############################

| 工具      | 功能描述
| --------- | ----------------------------------------------------------------
| `readelf` | 只分析 ELF 格式，输出更为详细，速度更快，适用于 ELF 文件结构研究
| `objdump` | 支持更多文件格式（如 COFF），可反汇编，更适合逆向工程和调试分析
   """
    print(readelf_cmd) 

def print_lsof_cmd():
    lsof_cmd = """
############################## DESCRIPTION ##################################

lsof（List Open Files）是 Linux/Unix 系统中一个非常有用的命令行工具，用于列出系统当前
打开的文件及其相关进程。因为在 Unix/Linux 中，一切皆文件，所以 lsof 可以查看：

############################### option ######################################

lsof [选项] [文件/目录/端口]

| 选项          | 作用                                      | 示例
| ------------- | ----------------------------------------- | ----------------------- 
| `-p <PID>`    | 查看指定进程打开的文件                    | `lsof -p 1234`
| `-u <用户>`   | 查看指定用户打开的文件                    | `lsof -u root`
| `-i`          | 查看所有网络连接                          | `lsof -i`
| `-i :端口`    | 查看某端口被哪个进程占用                  | `lsof -i :80`
| `-i @IP:端口` | 指定 IP 和端口查看连接                    | `lsof -i @127.0.0.1:22`
| `-c <进程名>` | 查看进程名以指定字符串开头的进程打开的文件| `lsof -c nginx`
| `+D <目录>`   | 查看某目录下被打开的文件（递归）          | `lsof +D /var/log`
| `+d <目录>`   | 查看某目录下被打开的文件（不递归）        | `lsof +d /var/log`
| `<文件名>`    | 查看该文件被谁打开                        | `lsof /tmp/test.log`
| `-n`          | 不解析主机名，提高速度                    | `lsof -n -i`
| `-P`          | 不解析端口名，直接显示端口号              | `lsof -nP -i`
| `-t`          | 只显示进程 PID（可配合 kill 使用）        | `lsof -t -i :80`
| `-r <秒数>`   | 每隔 N 秒刷新一次                         | `lsof -i -r 2`
| `-s`          | 显示文件大小（部分类型）                  | `lsof -s`
| `-l`          | 显示 UID 而不是用户名                     | `lsof -l`

############################## 常见字段解释 ###################################

| 列名     | 含义
| -------- | ---------------------------------------------------------
| COMMAND  | 打开文件的进程名
| PID      | 进程ID
| USER     | 拥有者用户名
| FD       | 文件描述符，如 `cwd`, `txt`, `mem`, `0u`, `1w` 等
| TYPE     | 文件类型，如 REG（普通文件）、DIR（目录）、CHR（字符设备）
| DEVICE   | 设备号
| SIZE/OFF | 文件大小或偏移量
| NODE     | inode编号
| NAME     | 文件名称或路径、IP/端口等

############################### instance ####################################

1. 查看某个文件被谁占用
lsof /var/log/syslog

2. 查看TCP/UDP连接
lsof -i tcp
lsof -i udp

3. 配合 grep 查找指定内容
lsof -i | grep ssh

4. 查看某个目录下被打开的文件（包括子文件）
lsof +D /path/to/directory

5. 列出某个用户打开的所有文件描述符数
lsof -u 用户名 | wc -l

################################## tips #####################################
释放被删除但仍被占用的文件（如日志）
lsof | grep deleted
找到占用的进程 PID 后，用 kill 或 systemctl restart 来释放资源。
   """
    print(lsof_cmd) 

def print_ltrace_cmd():
    ltrace_cmd = """
############################## DESCRIPTION ##################################

ltrace 是一个 Linux 下的调试工具，用于跟踪用户空间程序调用的 库函数（如 libc 中的 printf、
malloc 等） 以及动态链接库的调用情况。
它的作用类似于 strace，但区别在于：
| 工具     | 主要用途      | 跟踪层级    
| -------- | ------------- | ------- 
| `strace` | 系统调用跟踪  | 内核调用    
| `ltrace` | 库函数调用跟踪| 用户空间库函数 

############################### option ######################################
ltrace [选项] 程序名 [参数...]

| 选项         | 说明
| ------------ | ------------------------------------------------------------------
| `-e <表达式>`| **只跟踪匹配的函数**，如 `-e malloc`、`-e malloc+free`、`-e 'strcmp*'`
| `-p <pid>`   | **附加到一个已运行的进程**
| `-f`         | 跟踪子进程（例如通过 `fork` 派生的进程）
| `-t`         | 每行前打印 **绝对时间戳**
| `-r`         | 每行前打印 **相对时间**（从上一行到现在的时间间隔）
| `-T`         | 显示 **每个函数调用耗时**
| `-s <n>`     | 输出字符串最大长度（默认 32 字节），可设大一点，如 `-s 128`
| `-n <深度>`  | 显示调用的嵌套层数（默认无限）
| `-o <文件>`  | 将输出写入指定文件
| `-a <列数>`  | 设置函数参数对齐宽度（默认 30）
| `-l`         | 显示可跟踪的库函数列表，不执行程序

############################### instance ####################################
1. 跟踪一个程序的库函数调用：
ltrace ./test

2. 跟踪指定的库函数（只显示 malloc 和 free 的调用情况）：
ltrace -e malloc,free ./test

3. 跟踪所有符号调用（默认就是）：
ltrace -e '*'

4. 附加到已经运行的进程：
ltrace -p <pid>

5. 打印返回值和时间信息：
ltrace -t ./test       # 打印时间戳
ltrace -r ./test       # 打印相对时间
ltrace -T ./test       # 打印每个函数调用耗时

6. 输出重定向：
ltrace ./test > ltrace.log 2>&1

################################## tips #####################################

ltrace一般适用于：
  逆向工程：分析一个程序到底用了哪些库函数。
  调试程序崩溃：比如怀疑 malloc/free 有问题时。
  性能分析辅助：可以配合 -T 查看耗时长的库调用。
  学习系统和库调用流程。
   """
    print(ltrace_cmd) 

def print_smartctl_cmd():
    smartctl_cmd = """
############################## DESCRIPTION ##################################

smartctl 是 smartmontools 工具包中的一个命令行工具，用于监控和控制硬盘的 S.M.A.R.T.
（Self-Monitoring, Analysis and Reporting Technology）功能。它可以帮助你检测磁盘是
否即将出现故障，对 HDD 和 SSD 都适用。

############################### option ######################################

smartctl [选项] 设备
| 选项          | 说明
| ------------- | ---------------------------------------- 
| `-i`          | 显示设备信息
| `-a` 或 `-x`  | 显示所有可用信息（包括设备信息、SMART 状态、日志等）
| `-H`          | 显示健康状况（SMART overall-health）
| `-c`          | 显示SMART功能支持情况
| `-A`          | 显示SMART属性（例如通电时间、坏道计数等）
| `-t short`    | 执行短时自检
| `-t long`     | 执行长时自检
| `-l error`    | 显示错误日志
| `-l selftest` | 显示自检日志
| `-s on/off`   | 开启或关闭 SMART 功能
| `-d`          | 指定设备类型（如 RAID 控制器后的磁盘）
| `--scan`      | 扫描所有支持的设备


############################### instance ####################################

1. 查看磁盘是否支持 SMART，并查看设备信息
smartctl -i /dev/sda

2. 检查磁盘健康状况
smartctl -H /dev/sda

3. 显示所有SMART信息
smartctl -a /dev/sda

4. 启动短自检
smartctl -t short /dev/sda
执行后可以通过以下命令查看自检结果：
smartctl -l selftest /dev/sda

5. 启用 SMART 功能（如果未启用）
smartctl -s on /dev/sda

6.查看 NVMe 盘的SMART
smartctl -a -d nvme /dev/nvme0n1


################################## tips #####################################

1.有些RAID控制器后的硬盘不支持直接通过/dev/sdX访问，需要加 -d 参数指定类型（如 -d megaraid,N）。
2.smartctl 需要 root 权限运行。
3.如果是 NVMe 设备，要加 -d nvme 参数，否则可能无法读取信息。
	常见磁盘设备路径
		/dev/sda、/dev/sdb：SATA/SAS 硬盘
		/dev/nvme0n1：NVMe 固态硬盘（需使用 -d nvme）
   """
    print(smartctl_cmd) 

def print_lsscsi_cmd():
    lsscsi_cmd = """
############################## DESCRIPTION ##################################

lsscsi 是 Linux 系统中用于列出当前系统中所有 SCSI 设备（包括 SATA、SAS、光驱等）的命令。
它基于 /sys 文件系统，能够清晰地展示每个设备的 SCSI 地址、类型、厂商、型号等信息，是系统管
理和排障中常用的工具之一。

############################### option ######################################
lsscsi [选项]
| 选项 | 作用说明
| ---- | ------------------------------
| `-s` | 显示设备的 SCSI 地址（默认行为）
| `-v` | 显示更详细信息，包括设备路径
| `-t` | 显示设备类型
| `-d` | 显示设备的 major/minor 号
| `-c` | 显示设备的通道（Channel）信息
| `-l` | 显示设备与块设备的链接路径
| `-g` | 显示对应的 sg 设备（如 `/dev/sg0`）


############################### instance ####################################
1. 查看所有 SCSI 设备（默认）：
lsscsi

2. 查看详细信息：
lsscsi -v

3. 显示设备的类型：
lsscsi -t

4. 显示对应的 SG 设备（如用于smartctl等工具）：
lsscsi -g

5. 显示块设备链接路径：
lsscsi -l

############################# 常见输出格式说明： ###############################

$ lsscsi
[0:0:0:0]    disk    ATA      ST1000DM010-2EP1 CC43  /dev/sda
[1:0:0:0]    cd/dvd  TSSTcorp CDDVDW SH-224DB   SB00  /dev/sr0

各字段含义如下：
| 字段       | 说明
| ---------- | ------------------------------------- 
| \[0:0:0:0] | SCSI 地址（Host\:Channel\:Target\:LUN）
| disk       | 设备类型（磁盘 disk、光驱 cd/dvd 等）
| ATA        | 厂商标识
| ST1000...  | 型号
| CC43       | 固件版本
| /dev/sda   | 对应的设备文件
   """
    print(lsscsi_cmd) 

def print_arp_cmd():
    arp_cmd = """
############################## DESCRIPTION ##################################

arp 命令用于查看和操作系统的 ARP (Address Resolution Protocol) 缓存表，该表存储
了 IP 地址到 MAC 地址的映射关系。

############################### option ######################################

| 选项       | 说明
| ---------- | ------------------------------
| `-a`       | 显示所有 ARP 缓存条目（默认格式）
| `-n`       | 不解析主机名（只显示 IP 地址），加快显示速度
| `-v`       | 显示详细信息（verbose 模式）
| `-d`       | 删除一条 ARP 缓存条目（需配合 IP 地址使用）
| `-s`       | 添加静态 ARP 条目（需指定 IP 和 MAC 地址）
| `-i [接口]`| 指定网络接口（如 `eth0`）用于查看或设置 ARP 条目

############################### instance ####################################

1. 显示 ARP 表（IP + MAC）
arp -a

2. 显示 ARP 表（纯 IP，不解析主机名）
arp -n
arp -an

3. 添加静态 ARP 条目
sudo arp -s 192.168.1.100 00:11:22:33:44:55

4. 删除指定 IP 的 ARP 条目
sudo arp -d 192.168.1.100

5. 指定接口查看 ARP
arp -i eth0 -a
   """
    print(arp_cmd) 


def print_iperf3_cmd():
    iperf3_cmd = """

iperf 是一个网络性能测试工具，常用于测量主机间的 网络带宽，支持 TCP、UDP、SCTP 协议。
它分为 客户端 和 服务器端 两部分运行。

############################### install #####################################

sudo yum install iperf3
sudo apt install iperf3

############################## 基本使用方法 ###################################

1. 启动服务端（表示开启监听，默认端口为 5201，等待客户端连接）
iperf3 -s

2. 启动客户端进行测试（将连接服务端并进行默认 10 秒的带宽测试）
iperf3 -c <server-ip>

################################ option #####################################

| 参数              | 含义
| ----------------- | --------------------------------
| `-s`              | 作为服务端运行
| `-c <ip>`         | 指定服务端 IP，作为客户端连接
| `-t <时间>`       | 设置测试时长（秒），默认 10 秒
| `-p <端口>`       | 指定端口，默认 5201
| `-u`              | 使用 UDP（默认是 TCP）
| `-b <带宽>`       | 指定带宽（仅用于 UDP 模式）如 `-b 100M`
| `-i <间隔>`       | 每隔几秒输出一次中间结果
| `-P <并发数>`     | 启用多个并发连接，测试最大带宽能力
| `--logfile <文件>`| 把结果保存到指定文件中
| `-R`              | 反向模式（客户端接收、服务端发送）

################################ 结果解读 ####################################

测试结果一般类似如下：
[ ID] Interval           Transfer     Bandwidth
[  5]   0.00-10.00 sec   112 MBytes   94.1 Mbits/sec

Transfer：总传输数据量
Bandwidth：平均带宽（实际传输速率）

############################### caution #####################################

测试建议在非高峰时段执行，避免影响业务
UDP 模式可用于测试网络质量（如丢包、抖动）
防火墙或安全组需放通端口（默认 TCP/UDP 5201）

测试客户端的上下行带宽，建议：
  iperf3 -c <server-ip>      # 测上行
  iperf3 -c <server-ip> -R   # 测下行
   """
    print(iperf3_cmd) 

def print_eg_cmd():
    eg_cmd = """
introduce

############################################################## overview ########################################################################
############################################################### option #########################################################################
############################################################## instance ########################################################################
############################################################## caution #########################################################################

※ ← ↑ → ↓ ↔ ↕
   """
    print(eg_cmd) 

def print_fio_cmd():
    fio_cmd = """

fio 是一个用于测试存储性能的开源命令行工具，全称为 "Flexible I/O Tester"。它被广泛用于评
估硬盘（HDD）、固态硬盘（SSD）、NVMe、文件系统以及整个存储子系统的性能。

############################### overview ####################################

工具安装:
  sudo yum install libaio -y
  sudo yum install libaio-devel -y
  sudo yum install fio –y

fio VS dd
  若需进行专业的存储性能评估（如选购硬盘、优化存储子系统），优先用 fio。
  若仅需快速检查存储的顺序读写速度（如验证新硬盘是否正常），可用 dd 临时测试。

天翼云参考网址:
https://www.ctyun.cn/document/10027696/10381488

################################ option #####################################

一、全局基础选项
  --name=JOB_NAME：定义测试任务名称（必填，可用于区分多个任务）。
  --filename=PATH：指定测试文件或设备路径（如 /tmp/test.fio 或 /dev/sdb）。
  --size=SIZE：测试数据总量（如 1G、500M，若不指定则默认使用整个文件 / 设备）。
  --direct=1|0：是否绕过操作系统缓存（1 为直接 I/O，测试真实存储性能；0 为使用缓存，默认 0）。
  --runtime=SECONDS：测试持续时间（如 60 表示运行 60 秒，超时后自动停止）。
  --time_based：即使达到 --size 设定的总量，仍按 --runtime 持续测试（确保时长准确）。
  --numjobs=N：启动 N 个并行任务（模拟多线程 / 进程并发，如 --numjobs=8）。
  
二、I/O 模式与类型
  --rw=MODE：指定读写模式（核心参数）：
    read：顺序读
    write：顺序写
    randread：随机读
    randwrite：随机写
    rw,readwrite：混合随机读写（默认 50% 读 / 50% 写，可通过 --rwmixread 调整比例）
    trim：测试 SSD trim 功能（仅支持特定设备）
  --bs=SIZE：I/O 块大小（如 4k、128k、1m，可指定范围如 4k-64k 表示随机块大小）。
  --rwmixread=PERCENT：混合模式下读操作的比例（如 70 表示 70% 读、30% 写）。
  --iodepth=N：异步 I/O 队列深度（仅对 libaio 等异步引擎有效，如 --iodepth=32）。
  
三、I/O 引擎选项
  --ioengine=ENGINE：指定 I/O 引擎（决定 fio 如何与存储交互）：
    libaio：Linux 异步 I/O（支持异步操作，需配合 --iodepth 使用）。
    sync：同步 I/O（默认值，每次 I/O 需等待完成）。
    psync：POSIX 同步 I/O。
    mmap：通过内存映射文件进行 I/O。
    net：网络 I/O（测试网络存储如 NFS、CIFS）。
    posixaio：POSIX 异步 I/O（兼容性好，但性能可能不如 libaio）。
	
四、性能与输出选项
  --iodepth_batch_submit=N：每次提交的 I/O 数量（用于控制批量提交）。
  --iodepth_batch_complete=N：每次完成的 I/O 数量。
  --group_reporting：当 --numjobs>1 时，汇总所有任务的结果（而非单独显示每个任务）。
  --output=FILE：将测试结果输出到指定文件（默认打印到终端）。
  --bandwidth-log：记录吞吐量变化日志。
  --latency-log：记录延迟分布日志（可用于绘制延迟直方图）。
  
五、文件与设备选项
  --nrfiles=N：每个任务使用的文件数量（默认 1 个）。
  --filesize=SIZE：单个文件的大小（当 --nrfiles>1 时使用）。
  --delete=1：测试结束后删除测试文件（默认不删除，避免重复测试受旧数据影响）。
  --fsync=FREQ：每 FREQ 次写操作后执行一次 fsync（模拟需要持久化的场景，如数据库）。
  
六、其他常用选项
  --dry-run：仅检查配置是否有效，不实际执行测试。
  --help：查看所有选项的简要说明。
  --version：显示 fio 版本。

############################### instance ####################################

以下命令中，filename参数指定的设备名为/dev/test_device，请您根据实际情况替换为磁盘设备名称（如/dev/vdb），或文件地址（如/opt/fiotest/fiotest.txt）。      

# 测试硬盘的随机写IOPS：
fio -direct=1 -iodepth=32 -rw=randwrite -ioengine=libaio -bs=4k -size=1G -numjobs=4 -runtime=1000 -group_reporting -filename=/dev/test_device -name=RandWrite_Testing

# 测试硬盘的随机读IOPS：
fio -direct=1 -iodepth=32 -rw=randread -ioengine=libaio -bs=4k -size=1G -numjobs=4 -runtime=1000 -group_reporting -filename=/dev/test_device -name=RandRead_Testing

# 测试硬盘的顺序写吞吐量：
fio -direct=1 -iodepth=64 -rw=write -ioengine=libaio -bs=1024k -size=1G -numjobs=1 -runtime=1000 -group_reporting -filename=/dev/test_device -name=Write_Testing

# 测试硬盘的顺序读吞吐量：
fio -direct=1 -iodepth=64 -rw=read -ioengine=libaio -bs=1024k -size=1G -numjobs=1 -runtime=1000 -group_reporting -filename=/dev/test_device -name=Read_Testing

# 测试硬盘的随机写时延：
fio -direct=1 -iodepth=1 -rw=randwrite -ioengine=libaio -bs=4k -size=1G -numjobs=1 -group_reporting -filename=/dev/test_device -name=RandWrite_Latency_Testing

# 测试硬盘的随机读时延：
fio -direct=1 -iodepth=1 -rw=randread -ioengine=libaio -bs=4k -size=1G -numjobs=1 -group_reporting -filename=/dev/test_device -name=RandRead_Latency_Testing

############################### caution #####################################

1、 进行磁盘性能测试前，建议做好数据备份，避免造成数据丢失
2、 测试时需指定正确的文件路径或设备（如 /dev/sda），直接测试物理设备可能会覆盖数据，需谨慎！
3、 --direct=1 表示绕过操作系统缓存，测试真实存储性能；--direct=0 则使用缓存。
4、 可通过 man fio 查看完整参数说明，或访问 官方文档 了解更多高级用法。
   """
    print(fio_cmd) 

def print_uname_cmd():
    uname_cmd = """
############################### overview ####################################

uname 是一个轻量命令，主要用于快速获取 内核、系统架构、主机名 等基础信息。
如果要更详细的系统版本信息，可以配合使用：

cat /etc/redhat-release   # RHEL/CentOS 版本
lsb_release -a            # 需要安装 redhat-lsb-core

################################ option #####################################

| 选项 | 含义                                      | 示例输出
| ---- | ----------------------------------------- | ---------------------------------------------------------------------------
| `-s` | 显示内核名称（默认）                      | `Linux`
| `-r` | 显示内核发行版本号                        | `3.10.0-693.el7.x86_64`
| `-v` | 显示内核编译版本（构建日期、编译器等信息）| `#1 SMP Tue Aug 22 21:09:27 UTC 2017`
| `-n` | 显示主机名（nodename）                    | `zyq`
| `-m` | 显示硬件架构（机器类型）                  | `x86_64`
| `-p` | 显示处理器类型（可能输出 `unknown`）      | `x86_64` 或 `unknown`
| `-i` | 显示硬件平台（可能输出 `unknown`）        | `x86_64`
| `-o` | 显示操作系统名称                          | `GNU/Linux`
| `-a` | 显示所有信息，等价于 `-snrvmo`            | `Linux zyq 3.10.0-693.el7.x86_64 #1 SMP ... x86_64 x86_64 x86_64 GNU/Linux`

############################### instance ####################################

[zyq@zyq linux]$ uname -r
3.10.0-693.el7.x86_64

3.10.0
  表示 Linux 内核主版本号。
  3：主版本号（Major），表示大的内核系列。
  10：次版本号（Minor），代表内核的功能更新。
  0：修订号（Patch level），表示该内核的第几次小修改。
  → 这说明这是 Linux 3.10 系列内核。
-693
  表示该内核在 **Red Hat 系列发行版（RHEL / CentOS / Oracle Linux 等）**中的 打包或补丁版本号。
  数字越大，说明 Red Hat 官方为该内核修复、增强、加固的次数越多。
  693 就是 CentOS/RHEL 7.4（2017年发布）所对应的内核版本。
.el7
  el = Enterprise Linux。
  7 = 适配于 RHEL/CentOS 7 系列。
  → 所以这是 RHEL/CentOS 7 的内核版本。
.x86_64
  表示该内核是为 **64位 x86 架构（即 AMD64/Intel64）**编译的。
  如果是 32 位系统则可能显示为 i686 或 i386。

############################### caution #####################################

内核版本的命名规则：
  主版本号.次版本号.修订版本号-附加标识

1. 主版本号（Major）
  代表内核的重大变更，比如架构或核心子系统的更新。
  例如 2.x → 3.x → 4.x → 5.x → 6.x，都是大版本迭代。

2. 次版本号（Minor）
  在早期（2.x 时代），奇偶号有特殊含义：
  偶数：稳定版（Stable）
  奇数：开发版（Development）
  从 2.6 开始，奇偶数的区分取消，次版本号就是普通的子版本迭代。
  例如 5.10、5.15 都是稳定版。

3. 修订版本号（Patchlevel / Point Release）
  表示在某个次版本的基础上发布的小更新，主要是 Bug 修复、安全补丁、驱动更新。
  例如 5.10.1、5.10.25。

4. 附加标识（Build/Distribution Tag）
  由 Linux 发行版维护者添加，标记补丁、构建环境或发行版特性。
  比如在 Red Hat / CentOS 中：
    3.10.0-693.el7.x86_64
      各部分含义：
      3.10.0 → 上游内核主线版本
      693 → Red Hat 在此版本上的补丁代号（内部维护版本号）
      el7 → Enterprise Linux 7（即 RHEL7 / CentOS7）
      x86_64 → 平台架构
    在 Debian/Ubuntu 中可能看到 -generic、-lowlatency 等后缀，分别代表通用内核、低延迟内核。


如果要下载这个版本（3.10.0-693.el7.x86_64）的内核源码；
3.10.0（比如 RHEL 7 自带的 3.10.0-xxx.el7），那是 Red Hat 在 3.10 基础上打了大量补丁的定制版本，在 kernel.org 是没有的。

# 安装对应的源码包
yum install kernel-devel-$(uname -r) kernel-headers-$(uname -r) kernel-source

源码会放在 /usr/src/kernels/ 或者 /usr/src/debug/ 下。
如果你只要 RPM 包，可以去 CentOS Vault 找对应的 7.x 版本下载。
   """
    print(uname_cmd) 

def print_port_cmd():
    port_cmd = """
############################### Scan port ###################################

TCP

tcping localhost 22
telnet localhost 2222
nc -zv localhost 2222
nmap -sV -p 2222 localhost

# 临时在TCP 端口监听（需保持终端运行）
python -m SimpleHTTPServer 8080 / python3 -m http.server 80

UDP

nc -zv -u 8.8.8.8 53
nmap -sU -p 161 localhost

# 临时在UDP 5353端口监听（需保持终端运行）
nc -ul 5353

############################### instance ####################################

ssh root@localhost -p 2222
ssh localhost -p 2222

############################### advance ####################################

如果经常需要连接到这个特定端口的服务器，可以在 ~/.ssh/config 文件中添加配置，避免每次输入端口号：

Host myserver
    HostName 192.168.1.100
    User root
    Port 2222

之后只需使用 ssh myserver 即可连接到该服务器。
   """
    print(port_cmd) 

def print_ipv6_cmd():
    ipv6_cmd = """
ping6 www.baidu.com
ping6 self_ipv6
telnet ipv6 22
telnet ipv6 80
curl http://[ipv6]:8080
curl -6 http://www.baidu.com:80
   """
    print(ipv6_cmd) 

