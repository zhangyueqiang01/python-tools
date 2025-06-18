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

############################## syscall #########################################

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


########################## int 0x80、syscall ####################################

int 是 interrupt（中断） 的缩写。
int 0x80 是在早期32位x86架构Linux系统中，用来触发系统调用的一个指令。
int 0x80 会产生一次软中断，让CPU跳到内核的中断向量表中的第 0x80（也就是128号）条目，去执行与之对应的系统调用处理逻辑。


syscall 是在x86_64（64位）架构引入的新的、更高效的系统调用指令。
相比 int 0x80，syscall 切换内核态的过程更快、开销更小，因为它是专门为系统调用优化设计的，减少了不必要的中断处理步骤。


###################### 常见的系统调用和与之对应的系统调用号 ##########################

在操作系统中查看：
	cat /usr/include/asm/unistd_64.h
	
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

###################### 添加一个新的系统调用到Linux内核 #############################

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


############################## caution #########################################

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

