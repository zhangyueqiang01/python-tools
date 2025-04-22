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
   """
    print(src2bin_cmd) 


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
