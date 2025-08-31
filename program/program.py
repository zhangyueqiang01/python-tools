#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_kvm_cmd():
    print("kvm usage command:")
    kvm_cmd = """
[磁盘管理]
创建image
qemu-img create -f raw disk.raw 10G
qemu-img create -f qcow2 -b $IMG_DIR/.${BASEVM}.img $IMG_DIR/${NEWVM}.img &> /dev/null

镜像格式转换
qemu-img convert -f qcow2 -O qcow2 src.img dst-convert.img

镜像压缩
qemu-img convert -c -f qcow2 -O qcow2 src.img dst-compress.qcow2

镜像加密
qemu-img convert -o encryption -f qcow2 -O qcow2 src.qcow2 dst-encrypt.qcow2

查看镜像信息
qemu-img info dst-compress.qcow2

镜像扩容
qemu-img resize test.qcow2 +10G
growpart /dev/vda 1
xfs_growfs /dev/vda1；resize2fs /dev/sda1

写入/写出磁盘中的文件
virt-copy-out -d ct7_node06 /root/zyq /tmp/
virt-copy-in -d ct7_node06 /tmp/test.xml /root/

查看镜像里的磁盘分区信息
virt-filesystems -a centos7.qcow2

将磁盘分区挂载到本地
guestmount -d <vm name> -m <镜像内的磁盘分区> <宿主机上的挂载目录>
guestmount -d ct7_node06 -m /dev/sda1 /mnt/test
guestmount -a <qcow2镜像文件> -m <镜像内的磁盘分区> <宿主机上的挂载目录>

将磁盘分区卸载
guestunmount /mnt/ 或者 umount /mnt/

[虚拟机管理]
virsh list 
virsh list --all
virsh console domainID
virsh console vmID
virsh dumpxml vmID
virsh dumpxml domain-name/vm

# 使用 virsh 命令重启虚拟机
virsh reboot ct7_node09

# 使用 virsh 命令强制关闭虚拟机，然后再启动
virsh destroy ct7_node09
virsh start ct7_node09

# 从kvm系统重删除虚拟机，但是虚拟机的磁盘文件不会一并删除
virsh undefine ct7_node09

   """
    print(kvm_cmd)  

def print_src2bin_cmd():
    src2bin_cmd = """
############################## Assembly Language ######################################

源码：
	./mytool.py --show assembly --option instance_helloworld

流程：
	编写汇编代码 → 汇编 → 生成目标文件 → 链接 → 生成可执行文件
	example.asm --(汇编器:nasm/gas)--> example.o --(链接器:ld/gcc)--> example(可执行文件)

汇编（Assembling）：
	汇编器将每条汇编指令翻译成对应的机器指令（二进制格式）
	但还没有把整个程序和所需库链接到一起，因此它不能单独运行
	nasm -f elf64 example.asm -o example.o
	
链接（Linking）：
	使用 链接器（linker） 把目标文件与所需的运行时库、系统调用接口等“拼接”成一个完整的可执行文件。
	ld example.o -o example
		链接器处理符号（如函数、变量名）的地址重定位
		把多个目标文件（如果有）合并
		加入标准库或系统调用接口
		最终生成可执行文件（ELF 格式）

		
############################## C Language ######################################

源码：
	./mytool.py --show c --item printf

流程：
	hello.c
	  │
	  ▼（预处理 gcc -E）
	hello.i
	  │
	  ▼（编译 gcc -S）
	hello.s
	  │
	  ▼（汇编 gcc -c）
	hello.o
	  │
	  ▼（链接 gcc）
	hello（可执行文件）

预处理（Preprocessing）：
	源文件 .c 会被先交给 预处理器（cpp），处理以 # 开头的指令，比如 #include、#define 等。
	gcc -E hello.c -o hello.i

编译（Compiling）：
	把预处理后的 C 代码翻译成 汇编语言代码。
	gcc -S hello.i -o hello.s
	得到的 hello.s 是对应的汇编语言源码文件。你可以用文本编辑器查看它。
	
汇编（Assembling）：
	把汇编代码翻译成 机器码（目标文件），还不能运行。
	gcc -c hello.s -o hello.o
	生成 .o 文件（目标文件），它是二进制格式，包含了函数、变量等符号信息，但还没和库链接。
	
链接（Linking）：
	使用链接器将目标文件与 C 标准库（如 printf 属于 libc）链接，生成可执行文件。
	gcc hello.o -o hello
	或者一步完成前面所有步骤（GCC 会自动处理）：
	gcc hello.c -o hello

supplement:
         阶段 	| 文件后缀 	| 工具 		| 说明
         预处理	| .i 		| cpp / gcc -E 	| 展开宏和头文件
         编译 	| .s 		| gcc -S 	| 转换为汇编代码
         汇编 	| .o 		| as / gcc -c 	| 转换为目标文件（机器码）
         链接 	| 无扩展名 	| ld / gcc 	| 与库链接生成可执行文件

	通常不能直接用 nasm 把 hello.s 转换成 .o 文件
		GCC 默认生成的是 GNU 汇编器 (GAS) 所用的 AT&T 语法，比如操作数顺序是 movl $1, %eax
		而 nasm 使用的是 Intel 汇编语法，比如 mov eax, 1
		所以，GCC 生成的 .s 文件不能直接被 NASM 识别
   """
    print(src2bin_cmd) 


def print_crun_cmd():
    crun_cmd = """

用最经典的 C语言 Hello World 程序 来说明整个 编译和链接 的详细过程

################################ 程序源码 ####################################

假设我们写了一个最简单的程序 hello.c：

#include <stdio.h>

int main(void) {
    printf("Hello, World!\\n");
    return 0;
}

C 语言从源码到可执行文件，通常分为 预处理 → 编译 → 汇编 → 链接。

######################### 预处理 (Preprocessing) #############################

gcc -E hello.c -o hello.i

发生的事情：
  展开头文件 #include <stdio.h>，把标准库头文件中的内容复制进来。
  处理宏定义 #define，替换宏。
  处理条件编译 #ifdef/#endif。
  删除注释。
结果：得到一个 纯净的 C 源码文件（hello.i）。里面的 printf 已经声明好了（通过 stdio.h）。

########################### 编译 (Compilation) ###############################

gcc -S hello.i -o hello.s

发生的事情：
  把预处理后的 C 代码翻译成 汇编代码。
  编译器会进行语法分析、语义分析、优化。
  例如 printf("Hello, World!\\n"); 会变成对外部函数 printf 的调用指令（比如 call printf）。
结果：生成汇编代码文件（hello.s）。

############################ 汇编 (Assembly) #################################

gcc -c hello.s -o hello.o

发生的事情：
  汇编器把汇编代码转为 机器码（目标文件）。
  目标文件 hello.o 里包含：
  .text 段：机器指令（main函数的二进制代码）。
  .data 段：已初始化的全局/静态变量。
  .bss 段：未初始化的全局/静态变量。
  符号表：记录 main、printf 等函数和变量的名字，以及是否已定义/未定义。
  此时 hello.o 里的 main 是定义好的，但 printf 只是一个 未定义符号 (undefined symbol)。

############################# 链接 (Linking) #################################

gcc hello.o -o hello

发生的事情：
  链接器把 hello.o 和 C 标准库 glibc（比如 libc.so 或 libc.a）进行合并。
  在 libc 里找到 printf 的实现地址，把 hello.o 中未定义的 printf 符号解析掉。
  链接器同时处理：
  重定位 (Relocation)：把代码和数据段的地址调整到最终可执行文件里的地址。
  符号解析 (Symbol Resolution)：找到 printf 的真正实现。
结果：生成一个可执行文件 hello。

############################# 运行程序时的过程 #################################

当你运行：
./hello

操作系统（Linux）会把 hello 程序加载进内存。
程序的入口是 _start（不是 main，由 crt1.o 提供）。
_start 会调用运行时库初始化环境（堆栈、全局变量初始化等），然后再调用 main()。
main 里调用 printf，最终通过系统调用 write 把字符串输出到终端。
main 返回后，运行时库调用 exit 系统调用退出进程。

################################ 总结图示 ####################################

源码 (hello.c)
   │
   ▼
[预处理] ──> hello.i
   │
   ▼
[编译] ─────> hello.s
   │
   ▼
[汇编] ─────> hello.o (目标文件，未定义printf)
   │
   ▼
[链接] ─────> hello (可执行文件，printf已解析)
   │
   ▼
[运行] ─────> 输出 Hello, World!


用 objdump 和 readelf 来实际分析一下 hello.o 和 hello 的符号表和段信息，能直观地看到 printf 在编译阶段和链接阶段的不同状态。
   """
    print(crun_cmd) 


def print_python27_cmd():
    print("python27 usage command:")
    python27_cmd = """
python27 -s
   """
    print(python27_cmd)  

def print_python3_cmd():
    print("python3 usage command:")
    python3_cmd = """
python3 -s
   """
    print(python3_cmd) 

def print_clan_cmd():
    print("clan usage command:")
    clan_cmd = """
clan -s
   """
    print(clan_cmd)  

def print_html_cmd():
    print("html usage command:")
    html_cmd = """
html -s
   """
    print(html_cmd)  

def print_css_cmd():
    print("css usage command:")
    css_cmd = """
css -s
   """
    print(css_cmd)  
