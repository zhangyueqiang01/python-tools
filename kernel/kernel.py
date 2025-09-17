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

def print_syscall_cmd():
    syscall_cmd = """

############################################################ syscall ##################################################################################

在 Linux 中，系统调用（System Call） 是用户空间程序和内核空间之间交互的主要方式。
简单来说：
	用户写的程序通常运行在用户态（User Mode），权限受限，不能直接操作硬件或者访问敏感资源。
	**内核态（Kernel Mode）**则拥有最高权限，能够直接操作硬件、内存、文件系统、网络等。
	系统调用就是用户程序请求内核帮它做事的一种机制，比如读文件、写网络、分配内存等。


例子：
	printf()-----> C 库中的printf() ------> C库中的wirite()------> wirte()系统调用
	应用程序 ————————————————————————> C库 —————————————————————————————> 内核

这个 printf 其实最终会通过一次系统调用，让内核来完成将字符打印到屏幕上的工作。
整个过程大致是：
	用户程序准备好参数。
	触发一个特殊的指令（比如 int 0x80、syscall 等）切换到内核态。
	内核根据系统调用号找到对应的内核函数。
	执行完后，把结果返回给用户程序。


#################################################### int 0x80、syscall ########################################################################

int 是 interrupt（中断） 的缩写。
int 0x80 是在早期32位x86架构Linux系统中，用来触发系统调用的一个指令。
int 0x80 会产生一次软中断，让CPU跳到内核的中断向量表中的第 0x80（也就是128号）条目，去执行与之对应的系统调用处理逻辑。


syscall 是在x86_64（64位）架构引入的新的、更高效的系统调用指令。
相比 int 0x80，syscall 切换内核态的过程更快、开销更小，因为它是专门为系统调用优化设计的，减少了不必要的中断处理步骤。


############################################ 常见的系统调用和与之对应的系统调用号 ####################################################

内核中相关的文件：
	文件路径 					| 作用
	arch/x86/entry/syscalls/syscall_64.tbl 		| 定义系统调用号及对应实现（64位）
	arch/x86/include/generated/uapi/asm/unistd_64.h | 编译后生成的系统调用号头文件
	include/linux/syscalls.h 			| 声明系统调用函数（原型）
	kernel/sys.c（或其他子模块） 			| 系统调用函数的具体实现

常见系统调用函数的具体实现位置:
	系统调用 		| 主要源码文件 			 | 简单说明
	read, write, open, close| fs/read_write.c, fs/open.c 	 | 文件操作相关
	stat, fstat, lstat 	| fs/stat.c 			 | 获取文件状态
	mmap, munmap, mprotect  | mm/mmap.c, mm/mprotect.c 	 | 内存管理
	fork, vfork, clone 	| kernel/fork.c 		 | 进程创建
	execve 			| fs/exec.c 			 | 执行程序
	exit, _exit 		| kernel/exit.c 		 | 退出进程
	wait4, waitid 		| kernel/exit.c 		 | 等待子进程
	kill, tkill 		| kernel/signal.c 		 | 发送信号
	getpid, getppid, getuid | kernel/sys.c 			 | 获取基本进程信息
	brk 			| mm/mmap.c（早期在 mm/memory.c）| 调整堆空间
	uname 			| kernel/sys.c 			 | 获取系统信息
	ioctl 			| fs/ioctl.c 			 | 设备控制接口
	select, poll, epoll 	| fs/select.c, fs/eventpoll.c    | I/O多路复用

系统调用号在操作系统中查看：
	cat /usr/include/asm/unistd_64.h

| 系统调用号|  系统调用    | 功能说明
|  -------  | ------------ | -----------------------------
|  **0**    | `read`       | 从文件描述符读取数据
|  **1**    | `write`      | 向文件描述符写数据
|  **2**    | `open`       | 打开文件
|  **3**    | `close`      | 关闭文件
|  **4**    | `stat`       | 获取文件状态
|  **5**    | `fstat`      | 获取文件描述符对应文件的状态
|  **6**    | `lstat`      | 获取符号链接的状态
|  **9**    | `mmap`       | 建立内存映射
|  **10**   | `mprotect`   | 设置内存访问权限
|  **11**   | `munmap`     | 解除内存映射
|  **12**   | `brk`        | 调整堆内存（进程数据段末尾）
|  **39**   | `getpid`     | 获取进程号
|  **57**   | `fork`       | 创建子进程
|  **59**   | `execve`     | 执行新程序
|  **60**   | `exit`       | 退出进程
|  **61**   | `wait4`      | 等待子进程结束
|  **62**   | `kill`       | 向进程发送信号
|  **63**   | `uname`      | 获取系统信息
|  **78**   | `getdents`   | 读取目录项
|  **79**   | `getcwd`     | 获取当前工作目录
|  **80**   | `chdir`      | 改变工作目录
|  **202**  | `futex`      | Fast Userspace Mutex（高性能用户态锁）
|  **231**  | `exit_group` | 结束线程组（多线程进程退出）


############################################ 添加一个新的系统调用到Linux内核 ##########################################################

流程：
	第一步：写系统调用实现函数
	第二步：注册系统调用号
	第三步：声明系统调用原型（可选）
	第四步：重新编译内核
	第五步：用户态调用测试

步骤 | 内容
 1   | 写内核函数（用 SYSCALL_DEFINE 宏）
 2   | 修改 syscall_64.tbl，分配系统调用号
 3   | （可选）修改 syscalls.h，声明原型
 4   | 重新编译内核并安装
 5   | 写用户态程序用 syscall() 测试

详细方法：
	./mytool.py --show syscall_instance


############################################################ caution ##################################################################################

添加新系统调用，必须重新编译内核，不能单靠插入模块实现。
	系统调用（System Call）是用户态到内核态的标准接口，它的入口在内核的"系统调用表"里（比如 sys_call_table）
   

   """
    print(syscall_cmd) 

def print_syscall_instance_cmd():
    syscall_instance_cmd = """

我们的新系统调用叫 sys_hello，它的功能就是简单打印一句 "Hello from kernel!"。

########################## 写系统调用实现函数 #####################################

在 kernel/sys.c 文件最后，加上：
#include <linux/kernel.h>  // printk()
#include <linux/syscalls.h> // SYSCALL_DEFINE

SYSCALL_DEFINE0(hello)
{
    printk(KERN_INFO "Hello from kernel!\\n");
    return 0;
}

/* 说明：
SYSCALL_DEFINE0 这个宏是定义无参数系统调用。
如果要带参数，比如1个参数，可以用 SYSCALL_DEFINE1(name, type, arg1)，依次类推。
 */

############################ 注册系统调用号 ######################################

在文件arch/x86/entry/syscalls/syscall_64.tbl最后加一行：
	<空格> 系统调用号  common  hello   __x64_sys_hello
	
	解释:
		系统调用号（选择一个空的系统调用号）
		common 是ABI
		hello 是系统调用名（用户态调用名字）
		__x64_sys_hello 是内核里的实际函数名字（SYSCALL_DEFINE0定义的那个）


########################## 声明系统调用原型（可选） ################################

打开头文件include/linux/syscalls.h加一行声明
	asmlinkage long sys_hello(void);

注意： 如果用 SYSCALL_DEFINE 系列宏，并且不想显式声明，也可以跳过。


############################# 重新编译内核 #######################################

make menuconfig
make -j$(nproc)
make modules_install
make install
update-grub  # 如果需要更新引导
reboot       # 重启进入新内核

详情:
	./mytool.py --show ckernel


############################ 用户态调用测试 ######################################

自己写一个小程序来测试刚添加的系统调用！
因为我们新增了新的系统调用号，但标准C库（glibc）里还没提供接口，所以需要用系统调用指令（比如 syscall）自己触发。
比如写个C程序 test_hello.c：
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>

#define __NR_hello 440  // 你定义的系统调用号

int main() {
    long ret = syscall(__NR_hello);
    printf("syscall returned %ld\\n", ret);
    return 0;
}

编译运行：
gcc test_hello.c -o test_hello
./test_hello

然后用 dmesg 查看内核日志：
dmesg | tail

应该能看到内核打印的：
Hello from kernel!

   """
    print(syscall_instance_cmd) 

def print_interrupt_cmd():
    interrupt_cmd = """

中断（Interrupt） 是一种机制，允许硬件或软件打断CPU正在执行的程序流程，转而处理更紧急的任务。

################################ Introduction #############################################

硬中断：通常由外部设备（如键盘、网卡、硬盘）发出，告诉CPU“我有新情况了，需要你马上处理”。
软中断：Linux 内核中一种延迟处理机制，用于在中断上下文之外高效处理高频率、非紧急的任务
	   （如网络收包、定时任务）。
异常：CPU 执行指令时同步触发的事件，通常由程序错误（如除零）或主动请求（如系统调用）引发。

		CPU0				CPU1
	--------------			    --------------
	|	     |	                    |		 |	
	|   ------   |			    |	------	 |			
	|   |本 地|--------   本地IRQs	    |   |本地|--------   本地IRQs			
	|   |APIC |--------（LINT0，LINT1） |	|APIC|--------（LINT0，LINT1）		
	|   ------   |                      |	------	 |
	|	     |                      |		 |
	--------------                      --------------
	      ^				  	  ^
	      |                                   |
	      v                                   v
	中   断   控   制   器   通   信  （ICC）   总   线
  			    ^
                            |
                            v
		 	  ------	
		  	  |I/O |
		  	  |APIC|
		  	  ------	
		   	    ^
		    	    |
		         外部IROs

IRQ (Interrupt Request)	中断请求线
	每个能够发出中断请求的硬件设备控制器都有一条名为IRQ的输出线
I/O APIC: I/O Advanced Programmable Interrupt Controller
	所有现有的IRQ线（IRQ line）都与一个名为可编程中断控制器（PIC）的硬件电路的输入引脚相连

################### Linux中的中断处理流程（概览） #############################

1、中断发生：
	设备向CPU发送中断信号。
2、CPU响应：
	CPU暂停当前正在执行的程序（保存上下文，即当前执行状态）。
3、确定中断源：
	通过中断控制器（如x86的APIC）识别是哪个设备发的中断。
4、执行中断处理程序（Interrupt Handler）：
	Linux调用对应设备注册好的中断处理函数。
5、处理中断：
	设备驱动快速处理紧急工作（称为上半部top half），剩下的可以放到稍后处理（下半部bottom half，如软中断、tasklet、工作队列等）。
6、恢复执行：
	恢复到中断前被打断的程序，继续运行。

########################## 常见的术语 #####################################

术语				含义
IRQ (Interrupt Request)		中断请求信号
ISR (Interrupt Service Routine)	中断服务例程
Top Half			中断上半部，紧急处理中断
Bottom Half			中断下半部，稍后处理，减少中断延迟
Softirq / Tasklet / Workqueue	不同层次的下半部处理机制

########################## src code ######################################

在Linux中，设备驱动注册中断通常用：
	int request_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char *name, void *dev);
		irq：中断号
		handler：你的中断处理函数
		flags：是否共享、是否边缘触发等选项
		name：名字（用于 /proc/interrupts）
		dev：设备ID（用于共享中断时区分）
注销中断：
	void free_irq(unsigned int irq, void *dev);

######################## releated file ###################################

文件/目录		用途
/proc/interrupts	硬件中断统计
/proc/softirqs		软中断统计
/proc/irq/<IRQ>/	单个IRQ的配置（如亲和性）
/proc/stat		系统中断总数
/sys/kernel/irq/	结构化中断属性（较新内核）
内核启动参数(grub)	控制中断的全局行为

源码路径			作用
kernel/irq/			中断子系统核心代码：
  irqdesc.c			IRQ 描述符管理（struct irq_desc）。
  handle.c			中断处理逻辑（如 handle_irq_event_percpu）。
arch/x86/kernel/apic/		x86 平台的中断控制器（APIC、IOAPIC）实现。
drivers/irqchip/		各类中断控制器驱动（如 GIC、MSI）。
include/linux/interrupt.h	中断相关头文件（定义 request_irq()、softirq 等）。

###################### Interrupt Request #################################

类型	   范围		    典型示例
CPU 异常   0-31（x86）	    除零错误（0）、页错误（14）、NMI（2）。
硬件 IRQ   32-255（x86）    键盘（1）、RTC（8）、网卡（动态分配）。
软中断	   Linux 内部编号   网络收包（NET_RX）、定时器（TIMER）。
ARM 中断   GIC 动态分配	    定时器（16）、USB（45）。

########################## instance ######################################

./mytool.py --show interrupt_instance
   """
    print(interrupt_cmd) 

def print_interrupt_instance_cmd():
    interrupt_instance_cmd = """
将以下代码保存为 simple_irq_demo.c
########################## src code ######################################

#include <linux/module.h>
#include <linux/interrupt.h>
#include <linux/kernel.h>

#define DEMO_IRQ    1    // 使用键盘的IRQ 1号（仅演示用，小心别影响系统）

static irqreturn_t demo_irq_handler(int irq, void *dev_id)
{
    printk(KERN_INFO "simple_irq_demo: Interrupt received! irq=%d\\n", irq);
    return IRQ_HANDLED;
}

static int __init demo_irq_init(void)
{
    int ret;

    printk(KERN_INFO "simple_irq_demo: Initializing module...\\n");

    // 注册中断
    ret = request_irq(DEMO_IRQ, demo_irq_handler, IRQF_SHARED, "simple_irq_demo", (void *)(demo_irq_handler));
    if (ret) {
        printk(KERN_ERR "simple_irq_demo: Cannot request IRQ %d\\n", DEMO_IRQ);
        return ret;
    }

    printk(KERN_INFO "simple_irq_demo: Successfully requested IRQ %d\\n", DEMO_IRQ);
    return 0;
}

static void __exit demo_irq_exit(void)
{
    printk(KERN_INFO "simple_irq_demo: Exiting module...\\n");
    free_irq(DEMO_IRQ, (void *)(demo_irq_handler));
    printk(KERN_INFO "simple_irq_demo: Freed IRQ %d\\n", DEMO_IRQ);
}

module_init(demo_irq_init);
module_exit(demo_irq_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("YourName");
MODULE_DESCRIPTION("A simple Linux IRQ demo module");


########################## Makefile ######################################
obj-m += simple_irq_demo.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean


########################## launch ######################################

make
sudo insmod simple_irq_demo.ko
dmesg | tail
sudo rmmod simple_irq_demo


########################## caution ######################################

在这个示例中request_irq函数调用 demo_irq_handler 没有成功，free_irq的时候调用 
demo_irq_handler 却成功了，是因为：
IRQ 1 已被系统键盘驱动占用，然用 IRQF_SHARED 注册了中断，但共享中断的机制决定了系统
的主设备先处理，咱们这个“二级监听器”可能永远收不到中断。
   """
    print(interrupt_instance_cmd) 

def print_kthread_cmd():
    kthread_cmd = """

#################################################### DESCRIPTION ###############################################################

通过ps指令看到的带有括号的内容通常表示的是 内核线程（kernel thread）
这些线程并不对应某个用户空间的可执行程序，而是由内核直接创建并运行的，用于处理内核级别的任务（如 I/O 调度、内存回收等）。
以下是常见内核线程分类及示例


| 分类                       | 线程名称示例                                     | 说明
| -------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------
| **1. 内核线程管理类**      | `kthreadd`                                       | 所有内核线程的“父亲”，系统启动后由 PID 0 创建，负责调度和管理其他内核线程。
| **2. 同步机制（RCU）**     | `rcu_gp`、`rcu_par_gp`、`rcuc/N`、`rcub/N`       | 实现 RCU（Read-Copy-Update）机制的各类线程，主要用于高效并发读写数据结构。
| **3. 内存管理类**          | `kswapd0`、`kcompactd0`、`zswap-shrink`、`vmstat`| - `kswapd0`：负责内存回收（页面换出）<br> - `kcompactd0`：内存碎片整理<br> - `zswap-shrink`：Zswap 压缩缓存回收线程
| **4. 虚拟内存压缩与分页**  | `zswapd`、`zram0`                                | 管理内存压缩与分页交换，提高内存利用率
| **5. 块设备 I/O 管理**     | `kblockd`、`blkcg_punt_bio`、`blk_mq_*`          | 管理硬盘等块设备的异步 I/O 请求
| **6. 写回与缓存处理**      | `flush-N:m`、`writeback`                         | - `flush-*:*`：文件系统数据同步写回磁盘<br> - `writeback`：后台写回 dirty 页面
| **7. 文件系统日志（ext4）**| `jbd2/dm-0-8`、`jbd2/sda1-8`                     | JBD2（ext4 日志机制）相关线程，记录事务日志以保障一致性
| **8. 工作队列线程**        | `kworker/N:M`、`kworker/uX:Y`                    | 延迟任务/内核异步任务执行线程（多数由设备驱动或内核子系统排队）
| **9. I/O 调度与节流**      | `kthrotld`、`bfq_*`                              | 用于控制块设备 I/O 的调度、速率限制等（如 blk-throttle）
| **10. 网络处理相关**       | `ksoftirqd/N`、`netns`                           | - `ksoftirqd/N`：处理软中断（如网络接收）<br> - `netns`：网络命名空间相关线程
| **11. 电源与系统状态监控** | `khungtaskd`、`watchdog/N`、`kdevtmpfs`          | - `khungtaskd`：监测长时间无响应的任务<br> - `watchdog/N`：看门狗线程，用于系统健康检查
| **12. 热插拔与设备管理**   | `khelper`、`kmod`、`udevd`（非内核线程但相关）   | 内核模块自动加载与设备事件处理
| **13. TPM 与安全模块**     | `tpm0`、`ima`                                    | 安全模块相关线程，例如完整性度量（IMA）或 TPM 设备管理
| **14. GPU / 显卡驱动线程** | `amdgpu`、`nouveau`、`i915`                      | 图形驱动中可能创建的内核线程，具体依赖于硬件和驱动类型
   """
    print(kthread_cmd) 

def print_task_struct_cmd():
    task_struct_cmd = """
############################## DESCRIPTION ##################################

task_struct 是 Linux 内核中最核心的数据结构之一，它用来表示一个进程（或线程）的完整信息。
每个进程在内核中都有一个对应的 task_struct 结构体实例，内核通过这个结构体来管理和调度进程。
在 Linux 源码中（通常在 include/linux/sched.h 或 include/linux/sched/task.h 中）。
这个结构体非常庞大，包含了进程执行所需的各种信息。

############################# 主要字段分类与说明 ###############################

1. 进程状态与标识
   pid：进程 ID。
   tgid：线程组 ID（对于主线程等于 pid）。
   state：进程状态（如运行、就绪、睡眠、停止、僵尸等）。
   exit_state：退出时的状态。
   flags：进程的各种标志位。
   comm[16]：进程名。
   
2. 进程调度相关
   prio / static_prio / normal_prio：优先级。
   policy：调度策略（如 SCHED_NORMAL、SCHED_FIFO）。
   se：调度实体（调度器用来管理调度队列的部分）。
   rt：实时调度信息。
   sched_class：调度类（如 CFS、RT 等）。
   
3. 内存管理
   mm：指向进程的内存描述符（内核线程为 NULL）。
   active_mm：当前活跃使用的 mm 结构。
   vma：虚拟内存区域链表。
   
4. 文件系统相关
   fs：文件系统信息（如根目录、当前工作目录）。
   files：打开的文件列表（struct files_struct）。
   
5. 信号处理
   signal：共享的信号处理结构（线程组共享）。
   sighand：具体的信号处理函数。
   blocked：当前阻塞的信号。
   
6. 父子关系与线程关系
   real_parent：真正的父进程。
   parent：用于信号发送和审计的父进程。
   children：子进程链表。
   sibling：兄弟进程链表。
   group_leader：线程组的领头线程。
   thread_group：线程组中的其他线程。
   
7. 时间统计
   utime / stime：用户态 / 内核态运行时间。
   start_time：进程启动时间。
   real_start_time：实际启动时间（包含 sleep 的时间）。
   
8. CPU相关
   cpu：当前运行在哪个 CPU 上。
   cpus_allowed：允许在哪些 CPU 上运行。
   thread：体系结构相关的寄存器上下文（切换上下文时用到）。
   
9. 安全与审计
   cred：进程的凭据（UID、GID、权限等）。
   audit_context：审计日志信息。

############################## 与线程的关系 ###################################

在 Linux 中，线程本质上也是一个 task_struct，只是与其它线程共享某些资源（如 mm、files、
signal 等）。通过 CLONE_xxx 标志决定哪些资源共享。


################################# tips ######################################

在调试内核或分析 crash dump 时，可以通过 ps, /proc/[pid], top 等工具间接查看 task_struct 
的内容，也可以在内核模块或使用 gdb 直接分析。
   """
    print(task_struct_cmd) 

def print_maps_cmd():
    maps_cmd = """
/proc/[pid]/maps 是 Linux 系统中的一个伪文件，用于显示指定进程（通过 pid 指定）当前虚拟
内存地址空间的详细映射情况。它对调试程序、分析内存使用、理解进程地址空间布局等非常有用。

############################### overview ####################################

每一行代表一个虚拟内存区域，格式如下：
address           perms offset  dev   inode       pathname
08048000-08056000 r-xp 00000000 03:01 131073      /usr/bin/cat


下面是字段含义：
| 字段名     | 含义
| ---------- | ------------------------------------------------------------------
| `address`  | 该段虚拟内存的地址范围（起始地址-结束地址）
| `perms`    | 访问权限：`r`=可读，`w`=可写，`x`=可执行，`s/p`=共享/私有（copy-on-write）
| `offset`   | 映射文件中对应的偏移量（以十六进制表示）
| `dev`      | 设备号（主设备号:次设备号）
| `inode`    | 文件的 inode 号，为 0 表示不是来自文件映射
| `pathname` | 文件路径，如果是匿名内存（如 malloc），该字段为空或显示为 `[heap]` 等特殊标识

############################### pathname ####################################

| pathname       | 含义说明
| -------------- | --------------------------------------
| `/usr/lib/...` | 映射的动态链接库
| `[heap]`       | 进程的堆区（由 `malloc`、`brk` 等分配）
| `[stack]`      | 主线程的栈区
| `[stack:tid]`  | 其他线程的栈区
| `[vdso]`       | 虚拟动态共享对象（内核提供的用户态接口）
| `[vsyscall]`   | 旧的系统调用支持区域
| `[anon]` 或 空 | 匿名映射的内存（如 `mmap(MAP_ANONYMOUS)`）
| `[heap]`       | 由程序动态分配（`malloc`）的堆区域


############################### instance ####################################

cat /proc/self/maps
/proc/self/smaps 可查看 maps 区域后附加上详细的统计数据，详情：
aa --show smaps
   """
    print(maps_cmd) 


def print_smaps_cmd():
    smaps_cmd = """

/proc/[pid]/smaps 文件是 Linux 中每个进程的内存映射详细信息文件。它提供了比 /proc/[pid]/maps
更丰富的信息，主要用于分析进程内存使用情况的细节，尤其适用于内存泄露排查和内存占用分析。

############################### overview ####################################

/proc/[pid]/maps 显示每个内存区域的起始地址、权限、偏移量、设备、inode、映射文件路径。
/proc/[pid]/smaps 在每个 maps 区域后附加上详细的统计数据

00400000-004dd000 r-xp 00000000 fd:00 6571        /usr/bin/bash
Size:                884 kB
Rss:                 692 kB
Pss:                 205 kB
Shared_Clean:        684 kB
Shared_Dirty:          0 kB
Private_Clean:         8 kB
Private_Dirty:         0 kB
Referenced:          692 kB
Anonymous:             0 kB
AnonHugePages:         0 kB
Swap:                  0 kB
KernelPageSize:        4 kB
MMUPageSize:           4 kB
Locked:                0 kB
VmFlags: rd ex mr mw me dw sd 

关键字段含义:
| 字段名           | 含义说明
| ---------------- | ------------------------------------------------
| `Size`           | 区域的总虚拟内存大小
| `Rss`            | 实际占用物理内存的大小（常驻集）
| `Pss`            | 共享内存按比例分摊到各个进程的大小（更公平的内存占用指标）
| `Shared_Clean`   | 可共享的且干净的内存页（未被修改）
| `Shared_Dirty`   | 可共享的但被修改过的页
| `Private_Clean`  | 进程私有但未修改的页
| `Private_Dirty`  | 进程私有且被修改的页
| `Referenced`     | 最近被访问过的页
| `Anonymous`      | 匿名映射内存（不映射文件）
| `Swap`           | 被换出到 swap 分区的内存大小
| `KernelPageSize` | 页大小，通常为 4 KB 或大页
| `VmFlags`        | 映射区域的标志位（如是否可读、可写、是否匿名、是否私有等）


############################### VmFlags #####################################

| 标志   | 含义说明
| ------ | ----------------------------------------------------
| **rd** | 区域可读（Read）
| **wr** | 区域可写（Write）
| **ex** | 区域可执行（eXecute）
| **sh** | 区域是共享的（Shared）
| **dd** | 区域是私有复制的（Copy-on-write，即 demand-loaded）
| **mr** | 可以被 mmap 读映射
| **mw** | 可以被 mmap 写映射
| **me** | 可以被 mmap 执行映射
| **ms** | 可以被 mmap 共享映射
| **gd** | 区域触发了 grow-down（栈扩展）
| **pf** | 区域已预取（prefaulted）页
| **ac** | 匿名映射（Anonymous mapping）
| **hg** | 使用 hugepage（HugeTLB）
| **nh** | 禁用 transparent hugepages（no hugepages）
| **ar** | Arch-specific read access（架构特定读权限）
| **aw** | Arch-specific write access
| **ae** | Arch-specific execute access
| **lo** | Lockable（可以被 mlock 锁定）
| **io** | 可能是设备 I/O 映射
| **sr** | Soft-dirty 标志（用于用户态增量检查）
| **rr** | 不可回收页（Unreclaimable）
| **dc** | 不缓存的设备内存（uncached device memory）
| **de** | 延迟释放（Delayed free）
| **sd** | Soft-dirty 页面（已被修改）
| **mm** | 使用 memory migration 标志
| **hg** | 使用 HugeTLB huge pages
| **cf** | 匿名共享映射被强制写回（Crazy Force？少见）


############################### instance ####################################

cat /proc/self/smaps
aa --show maps
   """
    print(smaps_cmd) 

def print_proc_cmd():
    proc_cmd = """
Linux 中的 /proc 目录是一个伪文件系统（procfs），它并不对应磁盘上的实际文件，而是内核在运
行时生成的，主要用于向用户空间暴露内核信息和进程状态。你可以把 /proc 理解为 Linux 的“内核控制台”

######################### 与系统整体信息相关的文件 ##############################

| 文件名          | 功能简述
| --------------- | -----------------------------------------------
| `asound`        | ALSA（高级Linux声音架构）的接口信息（实际是符号链接或接口文件）。
| `buddyinfo`     | 展示内存分配器（Buddy System）中各个内存区域的空闲页块分布。
| `cgroups`       | 显示当前启用了哪些 cgroup 子系统。
| `cmdline`       | 显示当前内核启动时使用的启动参数（命令行）。
| `consoles`      | 显示当前已注册的控制台设备及其状态。
| `cpuinfo`       | 每个 CPU 核心的详细信息，如型号、主频、缓存等。
| `crypto`        | 显示内核当前支持的加密算法及其实现方式。
| `devices`       | 显示已注册的字符设备和块设备的主次设备号。
| `diskstats`     | 各磁盘设备的 I/O 操作统计信息。
| `dma`           | 显示当前分配的 DMA 通道。
| `execdomains`   | 显示支持的执行域（用于二进制兼容，比如 iBCS）。
| `fb`            | 显示已注册的帧缓冲设备（framebuffer），用于图形输出。
| `filesystems`   | 显示内核支持的文件系统类型及其挂载方式（nodev 代表伪设备）。
| `interrupts`    | 显示系统中所有中断的使用情况（每个 CPU 的中断次数和源设备）。
| `iomem`         | 显示系统的物理内存地址映射，包括内核和驱动的使用情况。
| `ioports`       | 显示已分配的 I/O 端口地址区间（用于设备通信）。
| `kallsyms`      | 显示内核导出的所有符号（函数名、变量名等，需 root）。
| `kcore`         | 内核虚拟内存的 ELF core dump 接口，可用 GDB 调试分析（伪设备）。
| `keys`          | 当前内核中的密钥信息（密钥管理子系统）。
| `key-users`     | 显示每个 UID 拥有的密钥数量和使用资源限制。
| `kmsg`          | 内核日志缓冲区内容（类似 `dmesg` 输出，可写入触发日志）。
| `kpagecount`    | 显示每个物理页的使用引用计数（与 `pfn` 相关，需 root）。
| `kpageflags`    | 显示每页的页标志，如是否是脏页、活动页等。
| `loadavg`       | 系统负载（1/5/15分钟平均值）、运行队列/总进程数、最后活跃进程PID。
| `locks`         | 显示当前系统上存在的文件锁。
| `mdstat`        | 显示软件 RAID（md设备）的状态（如是否正在重建）。
| `meminfo`       | 内存使用详情，包括空闲、缓存、swap等，最常用的监控信息。
| `misc`          | 显示 misc 类型设备的主设备号和名称（比如 /dev/rtc）。
| `modules`       | 当前已加载的内核模块列表及其使用计数。
| `mounts`        | 显示所有挂载的文件系统（类似 `mount` 命令），格式标准。
| `mtrr`          | MTRR（内存类型范围寄存器）设置情况，常用于优化图形性能。
| `net`           | 伪文件，实际上是一个包含网络状态的子目录（如 `/proc/net/dev` 等）。
| `pagetypeinfo`  | 物理页按照类型（如可回收页、活动页）分类的统计信息。
| `partitions`    | 显示系统识别到的磁盘分区（设备号、名称、大小）。
| `sched_debug`   | 显示内核调度器的调试信息和调度策略状态。
| `schedstat`     | 显示调度器统计信息，如上下文切换次数、运行时间等。
| `self`          | 指向当前访问 `/proc` 目录的进程的 PID 目录（符号链接）。
| `slabinfo`      | 显示内核 slab 分配器的缓存状态，用于调试内存分配器。
| `softirqs`      | 显示软中断的执行统计信息（按 CPU 核心划分）。
| `stat`          | 各类系统运行状态信息：CPU 时间、进程数、上下文切换数等。
| `swaps`         | 显示系统当前启用的 swap 区及其使用情况。
| `sysrq-trigger` | 向此文件写入字符可触发 Magic SysRq 操作（如 `b` 重启，`o` 关机）。
| `timer_list`    | 所有内核定时器的详细信息（调试用），包括到期时间、函数指针等。
| `timer_stats`   | （部分内核版本有）统计哪些进程设置了定时器。需启用定时器统计功能。
| `uptime`        | 系统运行时长和空闲时间（单位秒）。
| `version`       | 内核版本、编译器、构建时间等信息。
| `vmallocinfo`   | 显示内核通过 vmalloc 分配的内存区域（主要用于模块、驱动）。
| `vmstat`        | 虚拟内存子系统的运行统计，如页面换入/出、缺页异常等。
| `zoneinfo`      | 每个内存 zone 的状态信息（如 DMA、Normal、HighMem），细粒度的内存布局。

系统资源类：cpuinfo meminfo stat uptime loadavg vmstat zoneinfo
设备与中断类：interrupts ioports iomem dma fb devices
文件系统类：filesystems mounts partitions
调度与锁类：schedstat sched_debug locks slabinfo
内核调试类：kmsg kallsyms kcore execdomains timer_list
内存调试类：buddyinfo pagetypeinfo kpagecount kpageflags vmallocinfo
模块与驱动类：modules mdstat misc asound
特殊控制类：sysrq-trigger cmdline consoles version swaps


############################# /proc/[pid]/ ##################################

| 文件      | 说明
| --------- | --------------------------------------------------------------
| `cmdline` | 启动该进程时的完整命令行。
| `cwd`     | 当前工作目录（符号链接）。
| `exe`     | 可执行文件路径（符号链接）。
| `fd/`     | 打开的文件描述符目录（0、1、2 分别是 stdin、stdout、stderr）。
| `environ` | 环境变量（用 null 分隔，不能直接用 cat 查看）。
| `status`  | 人类可读格式的进程状态、UID/GID、内存等信息。
| `stat`    | 进程的详细状态（适合程序解析）。
| `maps`    | 显示该进程的内存映射信息（内存布局）。
| `smaps`   | 类似 `maps`，但每段内存区域有更多详细信息（如 RSS、PSS、权限等）。
| `stack`   | 当前线程的调用栈。
| `task/`   | 包含所有线程（TID）子目录，每个线程都有类似上述文件结构。
| `mounts`  | 该进程看到的挂载点信息。


########################### 与内核配置和调试有关的目录 ###########################

| 路径                  | 说明
| --------------------- | --------------------------------------------------------------------------------------
| `/proc/sys/`          | 用于**内核参数配置**（如网络、虚拟内存、文件句柄限制等），支持通过 `sysctl` 动态修改。
			| 如 `/proc/sys/net/ipv4/ip_forward` 控制是否启用 IP 转发。
| `/proc/irq/`          | 显示和设置中断请求线（IRQ）的分配和绑定信息。
| `/proc/iomem`         | 显示物理内存地址映射。
| `/proc/ioports`       | 显示 I/O 端口使用情况。
| `/proc/interrupts`    | 显示各中断号的使用统计和对应的设备。
| `/proc/kcore`         | 把内核内存导出为 ELF 样式的 core 文件（调试用）。
| `/proc/sysrq-trigger` | 允许用户通过写入触发 SysRq 功能（如强制重启）。
| `/proc/buddyinfo`     | 显示内核中伙伴系统（buddy system）的内存分配状态。
| `/proc/vmstat`        | 内存子系统的详细运行时统计信息。


############################# 与硬件和设备相关 #################################

| 文件            | 说明
| --------------- | -----------------------------------------------------------
| `/proc/driver/` | 驱动相关信息（如 `/proc/driver/nvidia/` 用于 NVIDIA 驱动）。
| `/proc/scsi/`   | SCSI 子系统的信息。
| `/proc/acpi/`   | ACPI（电源管理）相关信息。
| `/proc/tty/`    | TTY 设备信息。
| `/proc/net/`    | 网络子系统状态，例如 `/proc/net/dev` 显示网络接口信息。
| `/proc/mounts`  | 当前系统挂载的所有文件系统（包含自动挂载的 pseudo fs）。


############################# 伪设备状态信息 ##################################

| 文件                 | 说明
| -------------------- | -----------------------------------------------------
| `/proc/self/`        | 当前访问 `/proc` 的进程的 PID 目录的快捷方式。
| `/proc/thread-self/` | 当前线程的快捷目录。
| `/proc/mountinfo`    | 比 `/proc/mounts` 更详细的挂载信息（供内核和工具使用）。
| `/proc/stat`         | 系统级统计信息（如 CPU 使用率、上下文切换、进程数量等）。
| `/proc/devices`      | 已注册的字符设备和块设备列表。

   """
    print(proc_cmd) 

def print_kpath_cmd():
    kpath_cmd = """
Linux各发行版OS 内核相关的代码一般会放在 /usr/src/kernels/ 或者 /usr/src/debug/ 下
/usr/src/kernels/ 目录的默认用途是存放「与当前运行内核匹配的内核头文件（kernel headers）」和「编译后的内核模块目录」，而非完整源码。
完整内核源码通常需要用户通过包管理器手动安装，或从发行版官网下载。

include/linux/sched.h
    struct task_struct：进程结构体

include/linux/mm_types.h
    struct vm_area_struct：表示进程地址空间中的一个虚拟内存区域（VMA），描述了一块连续的虚拟地址范围及其属性（如读写权限、映射类型等）。
    struct mm_struct：代表一个进程的整个内存管理上下文，包含了进程所有的虚拟内存区域、页表指针、内存使用统计等信息。

include/linux/mm.h
    struct page：描述物理内存页框的元数据（如页状态、引用计数、映射关系等），是物理内存管理的基础。
    与内存分配、页表操作相关的结构体和宏定义。

arch/<架构>/include/asm/pgtable.h
    struct page_table_entry 或类似命名的结构体，描述页表项的具体格式（因架构而异）。
   """
    print(kpath_cmd) 

