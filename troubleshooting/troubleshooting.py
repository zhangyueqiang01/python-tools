#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_diskio_cmd():
    print("Disk writing and writing detailed process:")
    diskio_cmd = """
###############################
#Linux从磁盘读取数据的详细过程#
###############################

在Linux系统中，进程从磁盘读取数据的过程涉及多个层次和组件，包括硬件、操作系统内核、文件系统、缓冲区缓存等。下面是详细的步骤：

### 1. 用户进程发起读取请求
用户进程通过系统调用（如 `read()`）请求从文件读取数据。这个系统调用会触发从用户空间到内核空间的上下文切换。

### 2. 文件系统层处理
内核接收到读取请求后，通过文件系统接口（VFS，Virtual File System）进行处理。VFS是一个抽象层，它能够支持不同类型的文件系统。

### 3. 检查页缓存
内核首先检查页缓存（page cache），这是内存中的一块区域，用于缓存最近访问过的数据块。如果请求的数据已经在页缓存中，内核会直接从缓存中返回数据，避免了磁盘I/O操作。这一步骤大大提高了读取操作的效率。

### 4. 缺少缓存情况下的处理
如果数据不在页缓存中，内核会发起块I/O操作从磁盘读取数据。这个过程如下：

#### a. 文件系统查找
文件系统查找请求的数据块的位置。这通常涉及通过文件的inode（索引节点）查找具体的物理块地址。

#### b. 提交块I/O请求
内核通过块设备层向相应的块设备（如硬盘）提交I/O请求。块设备层负责将文件系统请求转化为具体的设备I/O操作。

### 5. 块设备驱动处理
块设备驱动接收到I/O请求后，负责与实际的硬件设备进行通信。驱动程序将请求排入I/O队列，并根据硬盘调度算法（如电梯算法、CFQ调度算法）优化I/O操作的顺序。

### 6. 硬件设备读取数据
硬盘接收到I/O请求后，控制器会定位到请求的物理块地址，并将数据读取到硬盘的缓存中。然后通过DMA（直接内存访问）或PIO（编程输入输出）方式将数据传输到内核空间的缓冲区。

### 7. 数据返回到内核空间
数据从硬盘传输到内核空间后，内核将数据拷贝到页缓存中，以便未来的读取请求能够快速访问到这部分数据。

### 8. 数据返回到用户空间
最后，内核将数据从页缓存或直接从内核缓冲区拷贝到用户进程的地址空间中，完成整个读取过程。

### 总结
上述步骤涉及多个层次的协调与优化，包括缓存管理、文件系统查找、I/O调度、硬件交互等。通过这些机制，Linux系统能够高效地处理磁盘读取请求，并尽量减少磁盘I/O带来的性能瓶颈。


#############################
#Linux向磁盘写数据的详细过程#
#############################
在Linux系统中，进程向磁盘写入数据的过程也涉及多个层次和组件，包括硬件、操作系统内核、文件系统、缓冲区缓存等。下面是详细的步骤：

### 1. 用户进程发起写入请求
用户进程通过系统调用（如 `write()`）请求向文件写入数据。这个系统调用会触发从用户空间到内核空间的上下文切换。

### 2. 文件系统层处理
内核接收到写入请求后，通过文件系统接口（VFS，Virtual File System）进行处理。VFS是一个抽象层，它能够支持不同类型的文件系统。

### 3. 更新页缓存
内核首先将数据写入到页缓存（page cache）中，而不是立即写入磁盘。这种机制被称为“写缓存”或“延迟写”，能够提高写入操作的效率。

### 4. 标记脏页
被写入数据的页缓存页被标记为“脏页”（dirty page），表示这些数据需要在未来的某个时间点被写入磁盘。

### 5. 脏页回写到磁盘
内核通过以下机制将脏页回写到磁盘：

#### a. 回写机制
回写机制（write-back mechanism）负责定期将脏页写回到磁盘。这个机制包括两种主要方式：
- **pdflush守护进程**：定期扫描脏页并将其写回磁盘。
- **同步操作**：用户进程可以调用 `fsync()` 或 `sync()` 强制将数据写入磁盘。

#### b. 提交块I/O请求
在回写过程中，内核通过块设备层向相应的块设备（如硬盘）提交I/O请求。块设备层负责将文件系统请求转化为具体的设备I/O操作。

### 6. 块设备驱动处理
块设备驱动接收到I/O请求后，负责与实际的硬件设备进行通信。驱动程序将请求排入I/O队列，并根据硬盘调度算法（如电梯算法、CFQ调度算法）优化I/O操作的顺序。

### 7. 硬件设备写入数据
硬盘接收到I/O请求后，控制器会将数据写入到指定的物理块地址。写入操作可以通过DMA（直接内存访问）或PIO（编程输入输出）方式完成。

### 8. 更新元数据
文件系统还需要更新相关的元数据（如文件大小、时间戳等）。这些更新通常也是通过块设备层提交到磁盘的。

### 9. 数据一致性与持久化
为了保证数据一致性，Linux提供了多种机制（如日志文件系统、事务机制等）来确保数据在写入过程中不会丢失或损坏。

### 总结
上述步骤涉及多个层次的协调与优化，包括缓存管理、文件系统管理、I/O调度、硬件交互等。通过这些机制，Linux系统能够高效地处理磁盘写入请求，并尽量减少磁盘I/O带来的性能瓶颈，同时确保数据的完整性和一致性。

################################
#磁盘IO缓慢可能是哪些原因造成的#
################################


磁盘I/O缓慢可能由多种原因引起，涉及硬件、软件、配置等多个方面。以下是一些常见的原因及其可能的解决方案：

### 1. 硬件问题
- **磁盘老化或故障**：磁盘使用时间长久或出现物理损坏，会导致I/O速度变慢。解决方法是检查磁盘健康状态（如使用 `smartctl` 工具）并考虑更换磁盘。
- **接口问题**：磁盘接口（如SATA、SAS）的速率限制或接口线缆问题。解决方法是检查并更换接口线缆，或升级到更高性能的接口（如从SATA升级到NVMe）。
- **控制器问题**：磁盘控制器性能不足或出现故障。解决方法是检查控制器状态，必要时更换控制器。

### 2. 系统配置问题
- **I/O调度算法不合适**：Linux支持多种I/O调度算法（如CFQ、deadline、noop），选择不当可能影响性能。解决方法是尝试不同的调度算法以找到最佳配置。
- **文件系统问题**：文件系统类型或配置不当会影响I/O性能。解决方法是优化文件系统配置或选择更适合的文件系统类型（如ext4、XFS）。
- **磁盘分区对齐问题**：分区未对齐会导致I/O操作效率低下。解决方法是确保磁盘分区与扇区对齐，使用工具（如 `fdisk` 或 `parted`）重新分区。

### 3. 软件问题
- **操作系统配置**：操作系统的I/O缓冲设置或内存管理配置不当。解决方法是调整操作系统的I/O缓冲设置，优化内存管理。
- **驱动程序问题**：磁盘驱动程序有问题或未更新。解决方法是检查并更新磁盘驱动程序。

### 4. 负载问题
- **高I/O负载**：系统负载过高，I/O请求过多，导致磁盘瓶颈。解决方法是分析负载情况（如使用 `iostat` 工具），减轻系统负载或升级硬件。
- **竞争资源**：多个进程同时访问磁盘，导致资源竞争。解决方法是优化应用程序的I/O操作，合理调度任务。

### 5. 网络存储问题（如NFS、SAN）
- **网络延迟**：网络存储系统的网络延迟过高。解决方法是检查网络连接状态，优化网络配置。
- **存储服务器性能**：存储服务器的性能不足。解决方法是升级存储服务器或优化其配置。

### 6. 缓存问题
- **缓存未命中**：页缓存或块缓存未命中，导致频繁的磁盘I/O操作。解决方法是增加内存，优化缓存配置。
- **缓存污染**：不合理的缓存策略导致缓存命中率低。解决方法是调整缓存策略，清理不必要的缓存。

### 7. 磁盘碎片化
- **文件碎片化**：文件碎片化严重，导致I/O操作效率低下。解决方法是对文件系统进行碎片整理（注意，现代文件系统如ext4一般不需要手动整理碎片）。

### 8. RAID配置问题
- **RAID阵列问题**：RAID配置不当或阵列故障。解决方法是检查RAID配置，修复或重建RAID阵列。

### 9. 热量和散热问题
- **散热不足**：磁盘温度过高会导致性能下降。解决方法是检查散热系统，确保磁盘温度在正常范围内。

通过系统性地检查上述各个方面，可以找出导致磁盘I/O缓慢的具体原因，并采取相应的解决措施。
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

