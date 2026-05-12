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

################################################################ what ##########################################################################
################################################################ why ###########################################################################
################################################################ how ###########################################################################
############################################################### config #########################################################################
############################################################## overview ########################################################################
############################################################### option #########################################################################
############################################################## instance ########################################################################
############################################################## caution #########################################################################
############################################################## others #########################################################################@

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
############################################################## 基本特性 #########################################################################

地址长度：128 位二进制（IPv4 仅 32 位）
地址总量：2¹²⁸ ≈ 3.4×10³⁸个，理论上可为每粒沙子编址
表示格式：8 组 4 位十六进制数，冒号分隔（X:X:X:X:X:X:X:X）
例：2001:0db8:85a3:0000:0000:8a2e:0370:7334

############################################################# 简化表示规则 ########################################################################

省略前导零：每组前导的 0 可去掉
	0db8 → db8；0000 → 0
零段压缩（::）：连续全零段可用双冒号代替，整个地址只能用一次
	原地址：2001:0db8:85a3:0000:0000:8a2e:0370:7334
	压缩后：2001:db8:85a3::8a2e:370:7334
大小写不敏感：A与a等效

环回地址（::1）
	本机自环，对应 IPv4 的127.0.0.1

############################################################## instance ########################################################################

# 测试
ping6 ::1
ping6 2408:871a:2100:186c:0:ff:b07e:3fbc
telnet ipv6 22
telnet ipv6 80
curl http://[ipv6]:8080
curl -6 http://www.baidu.com:80
ssh ipv6 22

# 局域网需加网卡名称
ssh fe80::7652:1ff:fe01:201%eth0

# 查路由
ip -6 route show
ip -6 r
route -6 -n

# 抓包
tcpdump -i eth0 ip6
tcpdump ip6 port 80
tcpdump ip6 port 443
tcpdump icmp6

############################################################## caution #########################################################################

1、 Linux网卡上看到的类似inet6 fe80::7652:1ff:fe01:203/64的地址，叫做链路本地地址（Link-Local Address）
        IPv6 协议规范强制: 每个启用ipv6的网卡接口，必须自带一个 fe80 链路本地地址，是基础通信刚需，删不掉、关不掉。
        fe80::/10: 固定前缀，只在当前局域网二层链路生效（路由器坚决不转发这种地址的数据包，出不了局域网、访问不了公网 IPv6）
        /64: 子网掩码前缀，局域网标准网段
        后面一截: 网卡自动生成的接口 ID
        fe80:: 是网卡链路本地，必须带网卡名才能正常 ping（自己ping自己，或者同局域网另一台机器 ping 自己）
		ping6 fe80::7652:1ff:fe01:203%eth0

2、 ping 公网ipv6 网卡必须要有公网可用的ipv6地址

3、 云平台的环境下，一般是将ECS网卡开启ipv6功能，并将网卡绑定到共享带宽中实现ipv6功能

4、 Linux连接手机热点，并且Linux上网卡开启了ipv6功能，那么该该网卡就会获得一个公网ipv6地址，别人可以直接访问该ipv6（客户端也必须有公网可用的ipv6地址才行）

############################################################### others #########################################################################

# 查询百度ipv6 地址
nslookup -q=AAAA www.baidu.com

aa --show nslookup
   """
    print(ipv6_cmd) 

def print_asm_cmd_cmd():
    asm_cmd_cmd = """
########################################################## x86 汇编指令速查表 ####################################################################


| 类别      | 指令        | 作用            | 示例
| --------- | ----------- | --------------  | ----------------------------
| 数据传送  | `MOV`       | 数据传送        | `MOV EAX, 5` → 把立即数 5 送到 EAX
|           | `XCHG`      | 交换数据        | `XCHG EAX, EBX`
|           | `PUSH`      | 压栈            | `PUSH EAX`
|           | `POP`       | 出栈            | `POP EBX`
|           | `LEA`       | 获取地址        | `LEA EAX, [EBX+4]`
| 算术运算  | `ADD`       | 加法            | `ADD EAX, EBX`
|           | `SUB`       | 减法            | `SUB EAX, 1`
|           | `MUL`       | 无符号乘法      | `MUL EBX`
|           | `IMUL`      | 有符号乘法      | `IMUL ECX`
|           | `DIV`       | 无符号除法      | `DIV EBX`
|           | `IDIV`      | 有符号除法      | `IDIV EBX`
|           | `INC`       | 自增            | `INC EAX`
|           | `DEC`       | 自减            | `DEC EBX`
|           | `NEG`       | 取负            | `NEG EAX`
| 逻辑与移位| `AND`       | 按位与          | `AND EAX, 0xFF`
|           | `OR`        | 按位或          | `OR EAX, 1`
|           | `XOR`       | 按位异或        | `XOR EAX, EAX` (清零技巧)
|           | `NOT`       | 按位取反        | `NOT EAX`
|           | `SHL`/`SAL` | 左移            | `SHL EAX, 1`
|           | `SHR`       | 逻辑右移        | `SHR EAX, 1`
|           | `SAR`       | 算术右移        | `SAR EAX, 1`
|           | `ROL`       | 循环左移        | `ROL EAX, 1`
|           | `ROR`       | 循环右移        | `ROR EAX, 1`
|           | `TEST`      | 按位与(只改标志位) | `TEST EAX, EAX`
|           | `CMP`       | 比较            | `CMP EAX, 10`
| 控制转移  | `JMP`       | 无条件跳转      | `JMP label`
|           | `CALL`      | 调用子程序      | `CALL func`
|           | `RET`       | 返回            | `RET`
|           | `JE/JZ`     | 等于/零跳转     | `JE equal`
|           | `JNE/JNZ`   | 不等于跳转      | `JNE notequal`
|           | `JG/JNLE`   | 大于跳转        | `JG greater`
|           | `JL/JNGE`   | 小于跳转        | `JL less`
|           | `JGE`       | 大于等于跳转    | `JGE ge`
|           | `JLE`       | 小于等于跳转    | `JLE le`
|           | `JC`        | 进位时跳转      | `JC carry`
|           | `JNC`       | 无进位跳转      | `JNC nocarry`
|           | `LOOP`      | 循环（ECX递减） | `LOOP loop_start`
| 字符串操作| `MOVS`      | 内存块传送      | `MOVSB` (字节)
|           | `STOS`      | 存储寄存器值到字符串 | `STOSB`
|           | `LODS`      | 加载字符串元素  | `LODSB`
|           | `SCAS`      | 扫描字符串      | `SCASB`
|           | `CMPS`      | 比较字符串      | `CMPSB`
| 处理器控制| `NOP`       | 空操作          | `NOP`
|           | `HLT`       | 停止CPU         | `HLT`
|           | `CLC`       | 清除进位标志    | `CLC`
|           | `STC`       | 设置进位标志    | `STC`
|           | `CLI`       | 禁止中断        | `CLI`
|           | `STI`       | 开中断          | `STI`
|           | `INT n`     | 软件中断        | `INT 0x80`
|           | `IRET`      | 从中断返回      | `IRET`


############################################################## caution #########################################################################

系统调用指令 ≠ 普通计算/跳转指令，它的特殊之处在于 —— 触发 CPU 特权级切换，把控制权交给内核，让用户态能安全地使用底层资源（文件、网络、内存管理等）


| 指令             | 体系结构          | 作用                          | 示例
| ---------------- | ----------------- | ----------------------------- | -------------------------------
| `INT n`          | x86               | 触发中断，常用于进入内核      | `INT 0x80` (Linux 32 位常用系统调用入口)
| `IRET` / `IRETD` | x86               | 从中断或系统调用返回          | 内核返回用户态时使用
| `SYSCALL`        | x86-64            | 快速进入内核态执行系统调用    | Linux 64 位 `syscall` ABI
| `SYSRET`         | x86-64            | 从内核返回用户态              | 与 `SYSCALL` 配对
| `SYSENTER`       | x86 (Pentium II+) | Intel 提供的快速进入内核指令  | Windows / Linux 32 位都用过
| `SYSEXIT`        | x86               | 从内核快速返回用户态          | 与 `SYSENTER` 配对


系统调用相关指令（INT 0x80、SYSCALL、SYSENTER 等）和普通的汇编指令（比如 MOV、ADD、JMP）有以下几个核心差别：

1. 执行特权级不同
普通指令：
  在 当前特权级（CPL） 下运行，比如用户态 CPL=3。
  → 你用 ADD EAX, 1 就只是修改了寄存器里的值，不会改变 CPU 模式。
系统调用指令：
  触发 从用户态切换到内核态（CPL=0） 的过程，让 CPU 进入操作系统内核。
  → SYSCALL、INT 0x80 会触发硬件控制流转移，自动切换栈、代码段、特权级。
  
2. 是否涉及上下文切换  
普通指令：
  只在用户空间执行，不会切换上下文。
  → 比如 MOV、CMP 这些指令执行非常快，耗费几个 CPU 周期。
系统调用指令：
  执行时 CPU 会保存现场、切换到内核栈、加载内核代码入口地址，属于 异常/陷入（trap），上下文切换成本更高。
  
3. 控制权归属不同
  
普通指令：
  你写什么，CPU就干什么，完全由用户程序决定。 
系统调用指令：
  你只是“敲门”，真正干活的逻辑在内核里。
  → 用户态只能通过 SYSCALL 或 INT 0x80 进入内核，然后执行的是 操作系统提供的服务，比如 read()、write()。
  
4. 性能差异 
普通指令：
  一般只需要几个 CPU 时钟周期。
系统调用指令：
  包含模式切换和内核执行，开销远大得多（几十到几百个 CPU 周期）。
  → 所以内核和编译器经常想办法 减少系统调用次数（比如缓冲、批处理 I/O）。
  
5. 适用范围 
普通指令：
  任意程序都能用，不受限制。 
系统调用指令：
  必须配合操作系统使用（单靠 SYSCALL 进内核是没意义的，因为还需要正确的寄存器参数和内核入口约定）。
   """
    print(asm_cmd_cmd) 

def print_date_cmd():
    date_cmd = """

############################################################## overview ########################################################################

date 命令可以：
    显示当前的日期和时间；
    按指定格式输出日期；
    设置系统日期和时间（需要 root 权限）；
    进行时间格式转换或时间计算。

############################################################### option #########################################################################

| 格式 | 含义         | 示例
| ---- | ------------ | ------
| `%Y` | 年（四位）   | 2025
| `%y` | 年（两位）   | 25
| `%m` | 月（01–12）  | 10
| `%d` | 日（01–31）  | 20
| `%H` | 小时（00–23）| 09
| `%I` | 小时（01–12）| 09
| `%M` | 分（00–59）  | 12
| `%S` | 秒（00–59）  | 45
| `%a` | 星期缩写     | Mon
| `%A` | 星期全称     | Monday
| `%Z` | 时区         | CST

%F	快捷格式（等价于 %Y-%m-%d）	date +%F → 2024-05-20
%T	快捷格式（等价于 %H:%M:%S）	date +%T → 15:30:25

############################################################## instance ########################################################################

命令			时间戳格式		示例
date +%Y%m%d_%H%M%S	年月日_时分秒		20240520_144030
date +%Y-%m-%d_%H-%M-%S	年-月-日_时-分-秒	2024-05-20_14-40-30
date +%Y%m%d		仅年月日		20240520
date +%H%M%S		仅时分秒		144030

# 复制添加时间戳
cp tmp.txt tmp`date +%Y%m%d_%H%M%S`.txt

# 设置具体时间
sudo date -s "2024-05-20 16:00:00"

# 同步系统时间到硬件时钟
sudo hwclock --systohc

# 反之：同步硬件时钟到系统时间
sudo hwclock --hctosys

用 chrony 强制立即对齐
chronyc makestep

手动一次性同步（不依赖服务）
ntpdate ntp.aliyun.com

重启服务后，1～3秒，生效
systemctl restart chronyd

############################################################ timedatectl #######################################################################

[root@zyq ~]# timedatectl
               Local time: Mon 2026-04-13 13:49:56 CST		//当前系统显示的时间,CST = China Standard Time（中国标准时间，东八区）
           Universal time: Mon 2026-04-13 05:49:56 UTC		//UTC 世界标准时间（UTC = Coordinated Universal Time）,比北京时间晚 8 小时，完全正常
                 RTC time: Mon 2026-04-13 05:49:57		//硬件时钟（ RTC = Real-Time 主板上的硬件时钟芯片，断电靠纽扣电池继续走时）,这里按 UTC 存储，和系统时间基本一致，误差 1 秒属正常
                Time zone: Asia/Shanghai (CST, +0800)		//时区：亚洲 / 上海，即北京时间,偏移 +0800，东八区，配置正确
System clock synchronized: yes				//系统时钟已同步，说明时间是准的
              NTP service: active			//NTP 时间同步服务已启用并运行,系统会自动校准时间，不用手动改
          RTC in local TZ: no		//硬件时钟不使用本地时区，而是使用 UTC,这是 Linux 标准且推荐的设置，避免时区切换、夏令时导致时间错乱

############################################################## caution #########################################################################

Linux 的 NTP 有安全保护,如果系统时间和真实时间差 > 1000 秒, NTP 会直接拒绝同步！

若手动同步后，timedatectl 还显示 synchronized：no ，重启服务即可
systemctl restart chronyd
   
配置文件/etc/chrony.conf 实例
server time2.tencentyun.com iburst
iburst 意思：快速同步模式,刚启动时，一次性多发几个包，快速把时间校准对
   """
    print(date_cmd) 


def print_ansible_cmd():
    ansible_cmd = """
# 手动输入密码ping测试远程主机并且临时跳过密钥检查
ansible all -i /etc/ansible/hosts -u root -k -m ping --ssh-common-args='-o StrictHostKeyChecking=no'
   """
    print(ansible_cmd) 


def print_ping_cmd():
    ping_cmd = """

############################################################## overview ########################################################################

# 带源地址进行ping
ping -I <源地址/网卡名> <目标地址> [其他参数]


# 其他常用参数：
-c n：只发送 n 个 ICMP 包后停止（避免持续 ping）。
-s size：指定 ping 包的大小（单位：字节，默认 56 字节，加上 8 字节 ICMP 头共 64 字节）。
-6：使用 IPv6 进行 ping 测试（对应 ping6 命令）。


# 若不确定网卡的具体 IP，可直接指定网卡名，系统会自动使用该网卡的主 IP 作为源地址：
ping -I eth1 223.5.5.5


# 指定 IPv6 源地址，测试到 IPv6 目标的连通性
ping -6 -I 2408:84f7::100 -c 4 2400:3200::1
   """
    print(ping_cmd) 

def print_jobs_cmd():
    jobs_cmd = """
############################################################## overview ########################################################################

进程可以通过&符号丢到后台，后台的进程也可以调度到前台，可以暂停可以继续运行，可以通过这种方法。

############################################################## instance ########################################################################

将多个进程放到后台
sleep 100&
sleep 200&
sleep 300&
sleep 400&

查看后台进程
[root@zyq]# jobs -l
[1]  1596496 Running                 sleep 100 &
[2]  1596497 Running                 sleep 200 &
[3]- 1596498 Running                 sleep 300 &
[4]+ 1596502 Running                 sleep 400 &
[root@zyq]# 


把后台进程调度到前台
fg %1     # 把任务1切前台
fg %2     # 把任务2切前台

前台快速切换后台
按 Ctrl + Z：暂停并丢到后台


暂停的后台程序想后台继续运行：
bg %1


后台恢复运行
输入命令 bg
这会让刚刚暂停的程序在后台继续运行。


彻底脱离终端（进阶）
nohup 你的命令 &


############################################################## caution #########################################################################


fg/bg 只在当前 Shell 有效：如果你退出了终端（exit），再登录进来，这些后台任务就失效了，无法恢复。

如果想让程序关闭终端后也不停止，建议使用 nohup 或 disown。
nohup 你的命令 &

或

在 bg 之后执行
disown %1  # 把任务从当前Shell的作业表中移除，脱离终端管理

再或者用tmux指令也可以
   """
    print(jobs_cmd) 

def print_k8s_cmd():
    k8s_cmd = """
########################################################### Kubernetes 核心组件 #################################################################

控制平面组件
这些控制平面组件（Control Plane Component）管理集群的整体状态：
	kube-apiserver：集群入口、认证授权、资源增删改查，核心中枢
	etcd：集群所有元数据存储（数据库）
	kube-controller-manager：各类控制器（节点、副本、命名空间等）
	kube-scheduler：负责 Pod 调度分配节点
	cloud-controller-manager（可选）：云厂商资源对接（公有云场景常用）

Node 组件
在每个节点上运行，维护运行的 Pod 并提供 Kubernetes 运行时环境：
	kubelet：确保 Pod 及其容器正常运行。
	kube-proxy（可选）：维护节点上的网络规则以实现 Service 的功能。
	容器运行时（Container runtime）：负责运行容器的软件，阅读容器运行时以了解更多信息。

插件（Addons）
插件扩展了 Kubernetes 的功能。一些重要的例子包括：
	DNS：集群范围内的 DNS 解析。
	Web 界面（Dashboard）：通过 Web 界面进行集群管理。
	容器资源监控：用于收集和存储容器指标。
	集群层面日志：用于将容器日志保存到中央日志存储。
############################################################### concept ########################################################################

1. Node
一台机器（物理机 / 虚拟机）
运行 K8s 组件，承载 Pod

2. Pod
K8s 最小调度单位，不是容器
一个 Pod 里可以有一个或多个紧密相关的容器
共享网络、存储、IP

3. Deployment
Deployment 用于管理运行一个应用负载的一组 Pod，通常适用于不保持状态的负载。

############################################################## overview ########################################################################

查看 k8s 集群中有哪些节点
kubectl get nodes

查看所有pod
kubectl get pod -A

查看所有deployment
kubectl get deployment -A


查看某一个 Pod 运行在哪台 Node（机器）上
kubectl get pod gemini-agent-x86-5xc75 -n vm-az1 -o wide

查看所有 Pod 运行在哪些 Node（机器）上
kubectl get pod -A -o wide

查看某一个pod的具体描述信息
kubectl describe pod gemini-agent-x86-5xc75 -n vm-az1

查看某一个pod中都有哪些容器在运行
kubectl get pod gemini-agent-x86-5xc75 -n vm-az1 -o wide
kubectl get pod gemini-agent-x86-5xc75 -n vm-az1 -o jsonpath='{.spec.containers[*].name}'

查看pod所在节点上所有运行的容器
ssh 目标主机 -> crictl ps


############################################################## caution #########################################################################

有的 K8s 用的是 containerd，不是 Docker，所以没有 docker 命令。
在节点上查看容器直接用：
crictl 指令即可，crictl 命令的选项和参数和docker基本一致

   """
    print(k8s_cmd) 

def print_kubectl_cmd():
    kubectl_cmd = """
############################################################## instance ########################################################################
[root@xinan1-region-k8s-master02 ~]# k get node -A -o wide
NAME                                                 STATUS     ROLES                  AGE    VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE        KERNEL-VERSION                      CONTAINER-RUNTIME
xinan1-az1-compute-s7-7e231e192e11                   Ready      <none>                 653d   v1.20.2   7.231.192.11   <none>        ctyunos 2.0.1   4.19.90-2102.2.0.0062.ctl2.x86_64   containerd://1.5.8
xinan1-az1-compute-s7-7e231e192e12                   Ready      <none>                 653d   v1.20.2   7.231.192.12   <none>        ctyunos 2.0.1   4.19.90-2102.2.0.0062.ctl2.x86_64   containerd://1.5.8

CONTAINER-RUNTIME 是容器运行时，它是 Kubernetes 节点上负责真正启动、管理、销毁容器的核心软件，是 Kubernetes 和容器之间的 “桥梁”。
1. 常见的容器运行时
containerd（你当前在用）
	Kubernetes 1.24+ 版本默认首选，也是生产环境主流选择
	兼容 Docker、Kubernetes 生态
Docker
	早期 Kubernetes 默认运行时
	Kubernetes 1.20+ 已弃用直接支持，现在也可以通过 cri-dockerd 适配
CRI-O
	专为 Kubernetes 设计的轻量运行时

############################################################## instance ########################################################################
[root@xinan1-region-k8s-master02 ~]# k get pod -A -o wide
NAMESPACE              NAME                                                              READY   STATUS         RESTARTS   AGE    IP              NODE                                                 NOMINATED NODE   READINESS GATES
cttg-az1               cttg-monitor-deployment-5bcff6cccd-fsgkb                          1/1     Running        0          632d   10.233.168.2    xinan1-az1-cttg-monitor-7e231e199e76                 <none>           <none>
idrs                   idrs-capacity-service-5984b8bf66-9nh89                            0/1     NodeAffinity   0          653d   <none>          xinan1-region-idrs-7e231e199e45                      <none>           <none>

NAMESPACE:(命名空间可以理解成 K8s 里的分组、文件夹、隔离环境)
NAME(这个 Pod 的完整名字)
READY( 1/1 的意思(1/1 = 这个 Pod 里总共有 1 个容器，其中 1 个已经正常就绪（Ready）))
STATUS(NodeAffinity(这个 Pod 被 “规则限制” 了，只能运行在特定节点上，现在找不到符合条件的节点，所以启动不了))
IP(Pod 的 IP 地址)
RESTARTS(这个 Pod 重启过多少次)
AGE( 就是这个 Pod 已经创建、存在了多长时间)
NOMINATED NODE( 翻译过来就是：被提名的节点)
READINESS GATES(就绪门 / 就绪网关)
   """
    print(kubectl_cmd) 


def print_nslookup_cmd():
    nslookup_cmd = """

nslookup 是一个用来查询 DNS（域名解析）信息的命令行工具，主要用于排查域名解析问题、查看域名对应的 IP、反向解析等。在日常运维、网络排障中非常常用。

############################################################### usage ##########################################################################

1、查询域名对应 IP
nslookup www.baidu.com

2、指定 DNS 服务器查询
nslookup www.baidu.com 8.8.8.8

3、查询 MX（邮件服务器记录）
nslookup -type=mx gmail.com

4、查询 NS（权威 DNS）
nslookup -type=ns baidu.com

4、查询域名的ipv6地址
nslookup -type=AAAA www.baidu.com

############################################################## instance ########################################################################

[root@VM ~]# nslookup www.baidu.com 114.114.114.114
Server:		114.114.114.114			//使用的 DNS：114.114.114.114
Address:	114.114.114.114#53		//端口：53（DNS 标准端口）

Non-authoritative answer:			//返回结果不是权威 DNS ,而是 DNS 缓存服务器（114DNS）返回的结果
www.baidu.com	canonical name = www.a.shifen.com.		//www.baidu.com 不是直接解析 IP,而是先被解析成：www.a.shifen.com,这个叫CNAME（别名记录）
Name:	www.a.shifen.com			//可以理解为,www.baidu.com → www.a.shifen.com → IP地址
Address: 180.101.51.73				//IPv4 地址（A记录）,两个 IPv4,说明：负载均衡 / 多节点部署,客户端可能随机访问其中一个
Name:	www.a.shifen.com
Address: 180.101.49.44
Name:	www.a.shifen.com
Address: 240e:e9:6002:1ac:0:ff:b07e:36c5		//IPv6 地址（AAAA记录）,如果客户端支持 IPv6，可能优先走 IPv6
Name:	www.a.shifen.com
Address: 240e:e9:6002:1fd:0:ff:b0e1:fe69

############################################################## caution #########################################################################

# 对比不同 DNS 结果
nslookup example.com 114.114.114.114
nslookup example.com 8.8.8.8

############################################################### others #########################################################################

在生产环境中快速排查用nslookup,深度分析用dig
aa --show dig
   """
    print(nslookup_cmd) 

def print_docker_run_cmd():
    docker_run_cmd = """
docker run -itd \\
  # 容器基本信息
  --name my-httpd \\
  --hostname httpd-server \\
  --restart unless-stopped \\

  # 权限与用户
  --privileged=false \\
  --user 1000:1000 \\

  # 端口映射
  --publish 8080:80 \\
  --publish 8443:443 \\
  --expose 80 \\
  --expose 443 \\

  # 环境变量
  --env TZ=Asia/Shanghai \\
  --env LANG=C.UTF-8 \\
  --env HTTPD_PREFIX=/usr/local/apache2 \\

  # 数据卷挂载
  --volume /data/httpd/html:/usr/local/apache2/htdocs:ro \\
  --volume /data/httpd/conf:/usr/local/apache2/conf \\
  --volume /data/httpd/logs:/usr/local/apache2/logs \\

  # 临时文件系统
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \\

  # 工作目录
  --workdir /usr/local/apache2 \\

  # 资源限制
  --memory 512m \\
  --memory-swap 1g \\
  --cpus="1.5" \\
  --cpu-shares 512 \\
  --pids-limit 100 \\

  # 文件描述符限制
  --ulimit nofile=65535:65535 \\

  # 日志配置
  --log-driver json-file \\
  --log-opt max-size=10m \\
  --log-opt max-file=3 \\

  # 健康检查
  --health-cmd="curl -f http://localhost/ || exit 1" \\
  --health-interval=30s \\
  --health-timeout=5s \\
  --health-retries=3 \\

  # 网络配置
  --network bridge \\
  --add-host myhost:192.168.1.100 \\
  --dns 8.8.8.8 \\
  --dns-search localdomain \\

  # 安全配置
  --cap-drop ALL \\
  --cap-add NET_BIND_SERVICE \\
  --security-opt no-new-privileges \\
  --read-only \\

  # 镜像
  httpd
  
# 加工后再运行,更具自己的需求进行调整  
aa --show docker_run | grep '\\\\'
   """
    print(docker_run_cmd) 

def print_dnf_cmd():
    dnf_cmd = """

################################################################ what ##########################################################################

DNF (Dandified YUM) 是 YUM (Yellowdog Updater, Modified) 的下一代替代品，是目前 RHEL 8+/CentOS 8+/Fedora/Rocky Linux 等系统的默认包管理器。语法高度兼容 YUM，
可以把它理解为 “升级版 yum”。

YUM：传统 RPM 包管理器（CentOS 7/RHEL 7 及更早默认）
DNF：新一代包管理器（CentOS 8+/RHEL 8+/Fedora 默认）
	基于 libsolv 依赖解析库，更快、更准、更稳定
	支持模块化、事务回滚、API 更健壮
	多数命令 直接替换 yum → dnf 即可使用

################################################################ why ###########################################################################

依赖解析更强
	YUM 用老的递归算法，复杂依赖容易慢 / 出错
	DNF 用 libsolv，求解速度、准确性大幅提升
性能更好
	内存占用更低、下载更快、缓存更干净
	大系统 / 大量包时差异明显
功能更现代
	支持 模块化（module）
	事务可 撤销 / 重做
	自动清理无用依赖（clean_requirements_on_remove 默认开启）
完全兼容旧用法
	几乎所有 yum 指令都能直接改成 dnf
	很多系统里 yum 本身就是指向 dnf 的软链接

################################################################ how ###########################################################################

1. 安装 / 卸载 / 更新
功能	            YUM 命令	        DNF 命令
安装包	            yum install nginx	dnf install nginx
reinstall	    yum reinstall nginx	dnf reinstall nginx
卸载包	            yum remove nginx	dnf remove nginx
更新所有包	    yum update	        dnf update
更新单个包	    yum update nginx	dnf update nginx
检查可更新	    yum check-update	dnf check-update
升级系统（含废弃）  yum upgrade	        dnf upgrade

2. 查询 / 搜索
功能	        YUM 命令	                DNF 命令
搜索包	        yum search nginx	        dnf search nginx
包详情	        yum info nginx	                dnf info nginx
列出已安装	yum list installed	        dnf list --installed
列出可用包	yum list available	        dnf list --available
哪个包提供文件	yum provides /bin/ls	        dnf provides /bin/ls
列出软件组	yum grouplist	                dnf group list
安装组	        yum groupinstall "Web Server"	dnf group install "Web Server"

3. 仓库 / 缓存
功能	        YUM 命令	        DNF 命令
查看仓库	yum repolist	        dnf repolist
生成缓存	yum makecache	        dnf makecache
清理缓存	yum clean all	        dnf clean all
查看历史	yum history	        dnf history
撤销历史事务	yum history undo 编号	dnf history undo 编号

############################################################### option #########################################################################

常用选项
-y：自动确认（yum -y install → dnf -y install）
--nogpgcheck：跳过 GPG 检查
--enablerepo / --disablerepo：临时启用 / 禁用仓库
   """
    print(dnf_cmd) 

def print_rpm_cmd():
    rpm_cmd = """

################################################################ what ##########################################################################

RPM 最初叫 Red Hat Package Manager，现在官方名称一般写成 RPM Package Manager。
它是 Red Hat 在 Linux 上推出的一套：
    软件打包格式
    软件安装管理系统
    包数据库管理机制
你可以把它理解成 Linux 世界里的：
“软件安装包 + 软件登记系统 + 软件依赖管理基础设施”

RPM 的本质是什么?
比如：httpd-2.4.6-99.el7.x86_64.rpm
| 部分    | 含义
| ------- | ------
| httpd   | 软件名
| 2.4.6   | 软件版本
| 99.el7  | 发布版本
| x86_64  | CPU架构
| rpm     | 包格式

RPM 工作原理
  RPM 安装时会：
    解压软件包
    执行预安装脚本
    拷贝文件到系统
    更新 RPM 数据库
    执行安装后脚本
  RPM 数据库默认位置：(/var/lib/rpm/)
  里面记录：
    安装了哪些包
    每个包有哪些文件
    版本信息
    依赖关系
    安装时间
  rpm -q httpd,其实就是查数据库。

################################################################ why ###########################################################################

在早期 Linux 里，安装软件非常麻烦。
问题很多：
    不知道装了哪些文件
    无法统一卸载
    依赖关系混乱
    软件版本难管理
    运维无法标准化
RPM 解决了：
|    问题     | RPM 的解决方式
| ----------- | --------------
| 软件文件分散| 统一打包
| 无法追踪    | 建立 RPM 数据库
| 无法验证    | 提供签名校验
| 依赖复杂    | 记录依赖关系
| 升级困难    | 支持版本升级
| 企业运维困难 | 可自动化部署

################################################################ how ###########################################################################
一、安装与升级
| 命令               | 作用
| ------------------ | ---------------
| `rpm -ivh xxx.rpm` | 安装 RPM 包
| `rpm -Uvh xxx.rpm` | 升级 RPM 包（没有则安装）
| `rpm -Fvh xxx.rpm` | 仅升级已安装的软件
| `rpm -e 包名`      | 卸载 RPM 包

二、查询类（最常用）
| 命令                    | 作用
| ----------------------- | --------------
| `rpm -q 包名`           | 查询软件是否安装
| `rpm -qa`               | 查询所有已安装 RPM 包
| `rpm -qi 包名`          | 查看软件详细信息
| `rpm -ql 包名`          | 查看软件安装了哪些文件
| `rpm -qc 包名`          | 查看配置文件
| `rpm -qd 包名`          | 查看文档文件
| `rpm -qR 包名`          | 查看依赖关系
| `rpm -q --scripts 包名` | 查看安装/卸载脚本
| `rpm -qf 文件路径`      | 查看文件属于哪个 RPM 包

三、校验与检查
| 命令             | 作用
| ---------------- | ------------
| `rpm -V 包名`    | 校验软件文件是否被修改
| `rpm -Va`        | 校验系统所有 RPM 包
| `rpm -K xxx.rpm` | 检查 RPM 包签名

四、查询 RPM 包文件（未安装时）
| 命令                        | 作用
| --------------------------- | ------------
| `rpm -qpi xxx.rpm`          | 查看 RPM 包信息
| `rpm -qpl xxx.rpm`          | 查看 RPM 包文件列表
| `rpm -qpR xxx.rpm`          | 查看 RPM 包依赖
| `rpm -qp --scripts xxx.rpm` | 查看安装脚本

五、数据库相关
RPM 有自己的数据库(/var/lib/rpm/)：
| 命令              | 作用
| ----------------- | -----------
| `rpm --rebuilddb` | 重建 RPM 数据库
| `rpm --initdb`    | 初始化 RPM 数据库

六、强制操作（危险）
| 命令                        | 作用
| --------------------------- | --------
| `rpm -ivh --force xxx.rpm`  | 强制安装
| `rpm -e --nodeps 包名`      | 忽略依赖强制卸载
| `rpm -ivh --nodeps xxx.rpm` | 忽略依赖安装

############################################################### option #########################################################################
| 参数   | 含义
| ---- | ------------
| `-i` | install
| `-U` | upgrade
| `-F` | freshen
| `-e` | erase
| `-q` | query
| `-a` | all
| `-l` | list
| `-i` | info
| `-f` | file
| `-R` | requires
| `-V` | verify
| `-p` | package file
| `-h` | hash进度条
| `-v` | verbose

############################################################## caution #########################################################################

这些参数危险：

--nodeps
可能导致：
    软件无法运行
    系统依赖断裂

--force
可能覆盖系统文件。
企业环境慎用。

############################################################## others #########################################################################@

RPM
├── 安装
│   ├── -ivh
│   ├── -Uvh
│   └── -e
│
├── 查询
│   ├── -qa
│   ├── -qi
│   ├── -ql
│   ├── -qf
│   └── -qR
│
├── 校验
│   ├── -V
│   └── -K
│
├── 数据库
│   └── --rebuilddb
│
└── 强制
    ├── --force
    └── --nodeps
   """
    print(rpm_cmd) 

def print_yum_cmd():
    yum_cmd = """
################################################################ what ##########################################################################
YUM 全称是 Yellowdog Updater, Modified，是早期 Red Hat Red Hat 官方网站系 Linux（比如 Red Hat Enterprise Linux、CentOS）最核心的软件包管理工具之一。

它的本质：
    基于 RPM 包管理
    自动解决依赖关系
    自动从软件仓库下载软件
    自动安装、升级、删除软件

YUM 工作流程：
    用户执行 yum install nginx
            ↓
    读取 repo 配置
            ↓
    访问仓库 metadata
            ↓
    分析依赖关系
            ↓
    下载 RPM
            ↓
    调用 rpm 安装
            ↓
    更新本地数据库
################################################################ why ###########################################################################

因为安装一个软件时，经常会报：
    软件之间互相依赖
    一个软件可能依赖几十个库
    需要手动下载
    顺序还不能错
于是 YUM 出现了。

YUM 的核心价值：
1. 自动解决依赖
2. 统一软件仓库
3. 批量更新系统

############################################################### config #########################################################################

主配置：/etc/yum.conf
仓库配置：/etc/yum.repos.d/*.repo

yum.conf 配置项速查表
| 配置项                | 示例                                    | 作用说明                 | 企业环境常见设置
| --------------------- | --------------------------------------- | -------------------- | -----------
| `cachedir`            | `cachedir=/var/cache/yum`               | YUM 缓存目录             | 默认即可
| `keepcache`           | `keepcache=1`                           | 是否保留下载的 RPM 包        | 离线环境常设 `1`
| `debuglevel`          | `debuglevel=2`                          | 日志详细级别               | 通常 `2`
| `logfile`             | `logfile=/var/log/yum.log`              | YUM 日志文件路径           | 默认即可
| `exactarch`           | `exactarch=1`                           | 是否严格匹配架构             | 通常开启
| `obsoletes`           | `obsoletes=1`                           | 是否允许废弃包替换            | 通常开启
| `gpgcheck`            | `gpgcheck=1`                            | 是否检查 RPM 签名          | 生产必须开启
| `plugins`             | `plugins=1`                             | 是否启用插件               | 通常开启
| `installonly_limit`   | `installonly_limit=3`                   | 保留的内核数量              | 常设 3~5
| `bugtracker_url`      | `bugtracker_url=http://...`             | Bug 提交地址             | 默认即可
| `distroverpkg`        | `distroverpkg=centos-release`           | 决定 `$releasever` 的来源 | 默认即可
| `reposdir`            | `reposdir=/etc/yum.repos.d`             | repo 仓库配置目录          | 默认即可
| `exclude`             | `exclude=kernel*`                       | 排除某些软件包              | 生产常排除内核
| `proxy`               | `proxy=http://ip:port`                  | 使用代理访问仓库             | 内网常见
| `proxy_username`      | `proxy_username=admin`                  | 代理用户名                | 代理认证环境
| `proxy_password`      | `proxy_password=123456`                 | 代理密码                 | 代理认证环境
| `timeout`             | `timeout=30`                            | 下载超时时间（秒）            | 常设 30~60
| `retries`             | `retries=3`                             | 下载失败重试次数             | 常设 3
| `metadata_expire`     | `metadata_expire=6h`                    | metadata 缓存过期时间      | 常设数小时
| `multilib_policy`     | `multilib_policy=best`                  | 多架构包策略               | 通常 `best`
| `ip_resolve`          | `ip_resolve=4`                          | 指定 IPv4 或 IPv6       | 网络问题时常用
| `sslverify`           | `sslverify=1`                           | 是否验证 SSL 证书          | 生产建议开启
| `http_caching`        | `http_caching=packages`                 | HTTP 缓存策略            | 默认即可
| `assumeyes`           | `assumeyes=1`                           | 自动 yes               | 自动化环境常用
| `tolerant`            | `tolerant=1`                            | 忽略轻微错误               | 特殊环境使用
| `diskspacecheck`      | `diskspacecheck=1`                      | 检查磁盘空间               | 建议开启
| `installroot`         | `installroot=/mnt/sysroot`              | 指定安装根目录              | chroot/救援环境
| `persistdir`          | `persistdir=/var/lib/yum`               | YUM 持久数据目录           | 默认即可
| `usercache`           | `usercache=0`                           | 是否允许用户缓存             | 一般关闭
| `enablegroups`        | `enablegroups=1`                        | 是否启用软件组              | 通常开启
| `group_package_types` | `group_package_types=mandatory,default` | 软件组安装策略              | 默认即可


例如：
[base]
name=CentOS-$releasever - Base
baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
enabled=1
gpgcheck=1

含义：
| 参数     | 作用
| -------- | ------
| [base]   | 仓库ID
| name     | 仓库名称
| baseurl  | 仓库地址
| enabled  | 是否启用
| gpgcheck | 是否检查签名

############################################################### option #########################################################################
| 选项               | 完整写法      | 作用说明            | 常见示例
| ------------------ | ------------- | --------------- | -----------------------------------------------------
| `-y`               | `--assumeyes` | 自动回答 yes        | `yum -y install nginx`
| `-q`               | `--quiet`     | 静默模式，减少输出       | `yum -q install nginx`
| `-v`               | `--verbose`   | 显示详细信息          | `yum -v repolist`
| `-h`               | `--help`      | 查看帮助            | `yum -h`
| `--nogpgcheck`     | —             | 不检查 GPG 签名      | `yum --nogpgcheck install nginx`
| `--enablerepo=`    | —             | 临时启用仓库          | `yum --enablerepo=epel install htop`
| `--disablerepo=`   | —             | 临时禁用仓库          | `yum --disablerepo=base install nginx`
| `--disableplugin=` | —             | 禁用插件            | `yum --disableplugin=fastestmirror install nginx`
| `--downloadonly`   | —             | 仅下载，不安装         | `yum install --downloadonly nginx`
| `--downloaddir=`   | —             | 指定下载目录          | `yum install --downloadonly --downloaddir=/tmp nginx`
| `-c`               | `--config=`   | 指定配置文件          | `yum -c myyum.conf install nginx`
| `--installroot=`   | —             | 指定安装根目录         | `yum --installroot=/mnt/sysroot install bash`
| `--releasever=`    | —             | 指定发行版版本         | `yum --releasever=7 install nginx`
| `--setopt=`        | —             | 临时修改配置参数        | `yum --setopt=keepcache=1 install nginx`
| `--skip-broken`    | —             | 跳过损坏依赖          | `yum update --skip-broken`
| `--exclude=`       | —             | 排除某软件           | `yum update --exclude=kernel*`
| `--security`       | —             | 仅安装安全更新         | `yum update --security`
| `--bugfix`         | —             | 仅安装 bug 修复更新    | `yum update --bugfix`
| `--obsoletes`      | —             | 启用 obsolete 包处理 | `yum update --obsoletes`
| `--showduplicates` | —             | 显示所有版本          | `yum list nginx --showduplicates`
| `--color=`         | —             | 设置颜色输出          | `yum --color=never list`
| `--assumeno`       | —             | 自动回答 no         | `yum --assumeno update`
| `--cacheonly`      | —             | 只使用缓存           | `yum --cacheonly list`
| `--refresh`        | —             | 强制刷新缓存          | `yum --refresh update`
| `--best`           | —             | 安装最佳版本（DNF 常见）  | `yum --best install nginx`
| `--allowerasing`   | —             | 允许替换冲突包（DNF 常见） | `yum --allowerasing update`

############################################################## instance ########################################################################
| 分类     | 命令                                     | 作用说明
| -------- | -------------------------------------- | ----------------
| 软件安装 | `yum install nginx`                    | 安装软件
| 软件安装 | `yum -y install nginx`                 | 自动确认安装
| 软件安装 | `yum install nginx httpd`              | 安装多个软件
| 软件安装 | `yum localinstall xxx.rpm`             | 安装本地 RPM，并自动解决依赖
| 软件删除 | `yum remove nginx`                     | 删除软件
| 软件删除 | `yum erase nginx`                      | 删除软件（等同 remove）
| 软件更新 | `yum update`                           | 更新所有软件
| 软件更新 | `yum update openssl`                   | 更新指定软件
| 软件更新 | `yum check-update`                     | 检查可更新的软件
| 软件更新 | `yum upgrade`                          | 升级系统软件
| 软件查询 | `yum search nginx`                     | 搜索软件
| 软件查询 | `yum info nginx`                       | 查看软件详细信息
| 软件查询 | `yum list installed`                   | 查看已安装软件
| 软件查询 | `yum list updates`                     | 查看可更新软件
| 软件查询 | `yum list available`                   | 查看可安装软件
| 软件查询 | `yum list installed nginx`             | 查看某软件是否安装
| 仓库管理 | `yum repolist`                         | 查看启用的仓库
| 仓库管理 | `yum repolist all`                     | 查看所有仓库
| 仓库管理 | `yum --enablerepo=epel install htop`   | 临时启用某仓库
| 仓库管理 | `yum --disablerepo=epel install nginx` | 临时禁用某仓库
| 缓存管理 | `yum makecache`                        | 生成缓存
| 缓存管理 | `yum clean all`                        | 清理全部缓存
| 缓存管理 | `yum clean metadata`                   | 清理仓库元数据
| 缓存管理 | `yum clean packages`                   | 清理 RPM 缓存包
| 依赖分析 | `yum deplist nginx`                    | 查看软件依赖
| 依赖分析 | `yum provides /usr/sbin/nginx`         | 查看文件属于哪个 RPM
| 依赖分析 | `yum whatprovides ifconfig`            | 查看命令由哪个包提供
| 软件组   | `yum grouplist`                        | 查看软件组
| 软件组   | `yum groupinstall "Development Tools"` | 安装开发工具组
| 软件组   | `yum groupremove "Development Tools"`  | 删除开发工具组
| 历史记录 | `yum history`                          | 查看历史操作
| 历史记录 | `yum history info 10`                  | 查看某次事务详情
| 历史记录 | `yum history undo 10`                  | 回滚某次操作
| RPM 下载 | `yum install --downloadonly nginx`     | 只下载不安装
| 自动化   | `yum -y install wget vim`              | 自动确认安装多个软件
| 自动化   | `yum -q install nginx`                 | 静默安装
| 自动化   | `yum --nogpgcheck install nginx`       | 忽略 GPG 检查
| 自动化   | `yum -c xxx.conf install nginx`        | 指定配置文件
| 企业运维 | `yum -y update`                        | 企业批量更新系统
| 企业运维 | `yum -y install wget vim net-tools`    | 安装基础运维工具
| 企业运维 | `yum clean all && yum makecache`       | 修复缓存问题
   """
    print(yum_cmd) 

def print_curl_cmd():
    curl_cmd = """
############################################################### option #########################################################################
| 选项 | 长选项              | 作用               | 示例
| ---- | ------------------- | ------------------ | ----------------------------------
| `-o` | `--output`          | 保存为指定文件     | `curl -o a.html URL`
| `-O` | —                   | 使用远程文件名保存 | `curl -O URL`
| `-L` | `--location`        | 跟随重定向         | `curl -L URL`
| `-I` | `--head`            | 只获取响应头       | `curl -I URL`
| `-i` | `--include`         | 显示响应头+正文    | `curl -i URL`
| `-v` | `--verbose`         | 显示详细调试信息   | `curl -v URL`
| `-s` | `--silent`          | 静默模式           | `curl -s URL`
| `-k` | `--insecure`        | 忽略 HTTPS 证书    | `curl -k URL`
| `-X` | `--request`         | 指定请求方法       | `curl -X POST URL`
| `-d` | `--data`            | 发送 POST 数据     | `curl -d "a=1"`
| `-F` | `--form`            | 表单上传           | `curl -F file=@a.txt`
| `-H` | `--header`          | 添加请求头         | `curl -H "token:1"`
| `-A` | `--user-agent`      | 指定 User-Agent    | `curl -A "Chrome"`
| `-e` | `--referer`         | 指定 Referer       | `curl -e URL`
| `-u` | `--user`            | 用户认证           | `curl -u admin:123`
| `-x` | `--proxy`           | 使用代理           | `curl -x proxy:8080`
| `-b` | `--cookie`          | 发送 Cookie        | `curl -b "a=1"`
| `-c` | `--cookie-jar`      | 保存 Cookie        | `curl -c cookie.txt`
| `-C` | `--continue-at`     | 断点续传           | `curl -C - -O URL`
| `-T` | `--upload-file`     | 上传文件           | `curl -T a.txt ftp://`
| `-r` | `--range`           | 范围下载           | `curl -r 0-1024 URL`
| `-m` | `--max-time`        | 最大执行时间       | `curl -m 10 URL`
| —    | `--connect-timeout` | 连接超时           | `curl --connect-timeout 5`
| —    | `--retry`           | 失败重试           | `curl --retry 3 URL`
| —    | `--limit-rate`      | 限速               | `curl --limit-rate 1M`
| —    | `--interface`       | 指定网卡           | `curl --interface eth0`
| `-4` | —                   | 强制 IPv4          | `curl -4 URL`
| `-6` | —                   | 强制 IPv6          | `curl -6 URL`
| —    | `--dns-servers`     | 指定 DNS           | `curl --dns-servers 8.8.8.8`
| —    | `--resolve`         | 自定义域名解析     | `curl --resolve a.com:443:1.1.1.1`
| `-w` | `--write-out`       | 输出格式化信息     | `curl -w "%{http_code}"`

############################################################## instance ########################################################################
| 功能            | 示例                                                        | 说明
| --------------- | ----------------------------------------------------------- | ---------------
| 访问网页        | `curl https://www.baidu.com`                                | 获取网页源码
| 下载文件        | `curl -O https://test.com/a.iso`                            | 使用原文件名下载
| 指定文件名下载  | `curl -o test.iso https://test.com/a.iso`                   | 自定义保存文件名
| 显示响应头      | `curl -I https://www.baidu.com`                             | 查看 HTTP Header
| 显示详细过程    | `curl -v https://www.baidu.com`                             | 调试网络请求
| 跟随重定向      | `curl -L http://test.com`                                   | 自动跳转 301/302
| POST 请求       | `curl -X POST https://api.test.com`                         | 发送 POST
| POST 表单       | `curl -d "name=tom&age=20" URL`                             | 提交表单数据
| POST JSON       | `curl -H "Content-Type: application/json" -d '{"a":1}' URL` | 提交 JSON
| 上传文件        | `curl -F "file=@a.txt" URL`                                 | multipart 上传
| 指定请求头      | `curl -H "token:123"`                                       | 自定义 Header
| 使用 Basic 认证 | `curl -u user:pass URL`                                     | HTTP Basic Auth
| 指定代理        | `curl -x http://proxy:8080 URL`                             | 使用代理
| 限速下载        | `curl --limit-rate 1M -O URL`                               | 限制下载速度
| 断点续传        | `curl -C - -O URL`                                          | 继续下载
| 忽略 HTTPS 证书 | `curl -k URL`                                               | 跳过证书验证
| 指定超时时间    | `curl --connect-timeout 5 URL`                              | 连接超时
| 查看公网 IP     | `curl ifconfig.me`                                          | 查询公网 IP
| 仅获取状态码    | `curl -o /dev/null -s -w "%{http_code}" URL`                | 获取 HTTP 状态码

############################################################ HTTP 请求示例 ######################################################################

1、GET 请求
curl https://api.test.com/users

2、POST 表单
curl -X POST \\
     -d "username=admin&password=123456" \\
     https://api.test.com/login

3、POST JSON
curl -X POST \\
     -H "Content-Type: application/json" \\
     -d '{"name":"tom","age":20}' \\
     https://api.test.com/user

4、PUT 请求
curl -X PUT \\
     -H "Content-Type: application/json" \\
     -d '{"name":"new"}' \\
     https://api.test.com/user/1

5、DELETE 请求
curl -X DELETE https://api.test.com/user/1

############################################################# 文件下载相关 ########################################################################
| 功能           | 示例
| -------------- | -------------------------------
| 下载文件       | `curl -O URL`
| 指定文件名     | `curl -o file.iso URL`
| 后台下载       | `curl -O URL &`
| 断点续传       | `curl -C - -O URL`
| 限速下载       | `curl --limit-rate 500K -O URL`
| 多线程下载（需 aria2） | `aria2c URL`


############################################################# HTTPS 与证书 ######################################################################
| 功能         | 示例
| ------------ | ---------------------------------------------
| 忽略证书检查 | `curl -k URL`
| 指定 CA 证书 | `curl --cacert ca.pem URL`
| 双向证书认证 | `curl --cert client.pem --key client.key URL`

######################################################### 调试网络非常有用的选项 ###################################################################
| 命令                           | 作用
| ------------------------------ | ------------------
| `curl -v URL`                  | 查看 TCP/SSL/HTTP 过程
| `curl --trace trace.log URL`   | 保存完整调试日志
| `curl -I URL`                  | 查看响应头
| `curl -w "%{http_code}" URL`   | 查看状态码
| `curl --connect-timeout 5 URL` | 测试连接超时
| `curl -k -v https://IP`        | 调试 HTTPS

########################################################### 运维场景经典用法 #######################################################################
检查网站状态
curl -I https://www.baidu.com

获取 HTTP 状态码
curl -o /dev/null -s -w "%{http_code}\\n" https://www.baidu.com

查看公网 IP
curl ifconfig.me

测试 IPv6
curl -6 ifconfig.me

测试接口耗时
curl -o /dev/null -s -w "time:%{time_total}\\n" URL
   """
    print(curl_cmd) 

