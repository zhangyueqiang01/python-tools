#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_kernel_compose():
    print("kernel compose:")
    kernel_compose = """
                        Linux kernel space - major subsystems and blocks

            +----+       +----+         Processes, Threads,        +----+
            | P1 |       | P2 |         Librarles, Daemons         | Pn |
            +----+       +----+               ...                  +----+
     User Space
=====================================================================================================
     Kernel Space

+----------------------------------------------------------------------+     +-------+  +----------+
|  +-------------------------------------------------+ +-------------+ |     | init  |  | security |
|  |                       Kernel                    | |   Memory    | |     +-------+  +----------+
|  |  [(user and kernel) thread creation/destruction | | managerment | |
|  |    CPU scheduling, synchronization primitives   | +-------------+ |     +---------------------+
|  |   signalling,timers, interrupt handling,        |    +-----+      |     |                     |
|  |  namespaces, cgroups, module support, etc       |    | VFS |      |     |                     |
|  +-------------------------------------------------+    +-----+      |     |     arch-specific   |
|  +------------+ +------+ +-------+ +-----+ +----------+              |     |                     |
|  | networking | | virt | | sound | | IPC | | Block IO |              |     |                     |
|  +------------+ +------+ +-------+ +-----+ +----------+              |     |                     |
+----------------------------------------------------------------------+     +--^------------^-----+
                                                                                |            |
       +-------------------------------------------------+                      |            |
       |              Device Drivers                     |                +-----v----+  +----v-----+
       |   +---------------+ +-----------+ +---------+   |                |  CPU(s)  |  | MMU/RAM  |
       |   | Network (NIC) | | Character | | Storage |   |                +----------+  +----------+
       |   +-------^-------+ +------^----+ +------^--+   |
       +-----------|----------------|-------------|------+
                   |                |             |
         +---------|----------------|-------------|----+
         |    +----v----+   +-------v-+    +------v--+ |
         |    | ....... |   | ******* |    |  Disk   | |
         |    +---------+   +---------+    +---------+ |
         +---------------------------------------------+
               """
    print(kernel_compose)  


def print_kerneldir_cmd():
    print("kernel directory info:")
    kerneldir_cmd = """

##############################Linux 内核源码目录##################################

目录				作用
Documentation/	存放内核相关文档，包括开发指南、子系统说明等。
arch/			与 CPU 体系结构相关的代码，如 x86、ARM、RISC-V 等。
block/			块设备层相关代码，包括 I/O 调度、缓冲管理等。
certs/			证书管理相关，支持 Secure Boot、模块签名等安全机制。
crypto/			内核加密框架，包括加密、哈希、压缩算法等。
drivers/		设备驱动程序，如网卡、显卡、存储设备、输入设备等。
fs/			文件系统实现，包括 ext4、xfs、btrfs 及 VFS（虚拟文件系统）层。
include/		头文件目录，定义内核 API 及各种子系统的接口。
init/			内核初始化代码，包括 start_kernel()。
ipc/			进程间通信（IPC）机制，如信号量、消息队列、共享内存等。
kernel/			核心代码，包括调度器、信号处理、软中断等。
lib/			内核通用库函数，如哈希、位操作、字符串处理等。
mm/			内存管理相关代码，如分页、交换、Slab 分配器等。
net/			网络协议栈，包括 TCP/IP、UDP、IPv4/IPv6、socket 实现等。
security/		安全机制，如 SELinux、LSM（Linux Security Module）。
sound/			音频子系统，如 ALSA（Advanced Linux Sound Architecture）。
tools/			内核工具，如 perf、bpftool、cpupower 等。
usr/			早期用户态引导相关，如 initramfs 处理。
virt/			虚拟化相关，如 KVM（Kernel-based Virtual Machine）。

##############################arch/ 目录结构##################################
arch/ 目录是 Linux 内核源码中与特定 CPU 体系结构（架构）相关的代码存放位置。不同的 CPU 体
系结构可能有不同的指令集、寄存器、内存管理方式，因此 Linux 内核需要针对不同架构进行适配。

目录			说明
alpha/		适用于 Alpha 处理器（DEC 早期的 64 位架构）。
arc/		适用于 Synopsys ARC 处理器（嵌入式 CPU）。
arm/		32 位 ARM 体系结构代码（ARMv7 及更早）。
arm64/		64 位 ARM（ARMv8 及更新的架构）。
csky/		适用于中科芯（C-SKY）架构的处理器。
hexagon/	高通 Hexagon DSP 处理器（主要用于嵌入式和 AI 计算）。
ia64/		Intel Itanium 64 位架构（已被淘汰）。
loongarch/	适用于龙芯 LoongArch 体系结构。
m68k/		Motorola 68k 系列 CPU（如 68000 处理器）。
microblaze/	Xilinx MicroBlaze 软核处理器。
mips/		适用于 MIPS 架构的处理器（如 Loongson 早期产品）。
nds32/		Andes Technology 的 32 位架构（已逐步被 RISC-V 替代）。
nios2/		Intel（Altera）Nios II 软核处理器。
openrisc/	OpenRISC 处理器架构（开源 RISC 架构）。
parisc/		HP PA-RISC 处理器架构（已过时）。
powerpc/	适用于 PowerPC 架构的处理器（如 IBM Power 服务器）。
riscv/		适用于 RISC-V 开源指令集架构。
s390/		适用于 IBM System Z（大型机架构）。
sh/		适用于 SuperH 处理器架构（如 SH-4）。
sparc/		适用于 SPARC 架构（Solaris 服务器等）。
um/		User-Mode Linux（运行在用户态的 Linux 内核）。
x86/		适用于 x86 和 x86_64 架构（Intel/AMD 处理器）。
xtensa/		适用于 Xtensa 处理器（常用于 DSP 设备）。

##############################arch/ 目录中的关键文件与子目录##########################
每个架构子目录下通常包含以下关键文件和子目录：

文件/目录		作用
boot/		处理架构特定的引导流程。
configs/	该架构支持的默认内核配置。
include/	该架构的专有头文件，如 CPU 特定寄存器定义。
kernel/		该架构的核心实现，如中断处理、进程切换等。
mm/		该架构的内存管理代码，如页表、TLB 处理等。
Kconfig		该架构的内核配置选项。
Makefile	该架构的编译规则和编译参数。

##############################重点架构解析##################################
1. x86（arch/x86/）
适用于 Intel 和 AMD 的 x86（32 位）和 x86_64（64 位）处理器。

arch/x86/
├── boot/        # 早期引导代码
├── crypto/      # 加密相关
├── entry/       # 入口代码（中断、异常处理）
├── include/     # 头文件
├── kernel/      # 体系结构相关的内核实现
├── mm/          # 内存管理
├── platform/    # 不同平台适配（Intel、AMD）
├── Kconfig      # 该架构的内核配置
├── Makefile     # 编译规则
└── ...          # 其他子目录

关键文件：
entry.S：汇编级入口代码，如系统调用、异常处理。
setup.c：处理 CPU 初始化。

##############################arch/ 目录小结##################################
arch/ 目录是 Linux 内核源码中最重要的部分之一，负责适配不同 CPU 体系结构。
每种 CPU 架构都有自己的子目录，其中包含：
	boot/：		启动相关代码。
	kernel/：	体系结构相关的内核代码（如调度、中断）。
	mm/：		内存管理相关代码。
	include/：	头文件，定义架构特定的数据结构。

   """
    print(kerneldir_cmd) 

