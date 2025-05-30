#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_concept_cmd():
    mm_concept = """
CPU实模式（Real Mode）：实模式是 Intel 8086 引入的最初工作模式，是 CPU 上电后默认的模式，它提供了一种简单直接的方式访问内存，内存地址=段寄存器*16+偏移量（BIOS 初始化，bootloader）。
CPU保护模式（Protected Mode）：保护模式由 Intel 80286 引入，80386 起正式流行，支持内存保护、多任务、分页机制等现代操作系统特性，内核启动后会立即从实模式切换到保护模式。
虚拟地址（Virtual Address）：又称线性地址（Linear Address），是分页机制下，经过段机制转换后的地址，在开启分页时，线性地址会被转换为物理地址（用户程序看到的地址）。
逻辑地址：逻辑地址是程序在运行时看到和使用的地址，在x86保护模式中，逻辑地址 = 段寄存器（CS、DS、SS 等） + 偏移地址，在分页机制下，逻辑地址通常就是虚拟地址。
物理地址（Physical Address）：实际访问内存芯片时使用的地址，通过内存管理单元（MMU）将虚拟地址映射到物理地址。
内存管理单元（Memory Management Unit）：是集成在 CPU 中的一个硬件模块，专门负责虚拟地址到物理地址的转换和内存访问控制，包含TLB、页表解析逻辑、访问权限控制单元、异常处理逻辑（访问非法或缺页时触发中断）。

程序中的段机制：./mytool.py --show c --item vas
用户空间地址（User Space）：用户程序可访问的内存区域，保护机制防止用户程序访问内核空间。
内核空间地址（Kernel Space）：操作系统核心代码使用的内存区域，受保护，用户态无法直接访问。
动态内存（dynamic memory）：


地址总线（Address Bus）：CPU通过地址总线发送内存地址。
数据总线（Data Bus）：CPU与内存之间传输数据。
控制总线（Control Bus）：用于发送读写等控制信号。
内存芯片：内存芯片只负责提供物理地址空间，并通过地址总线、控制总线读取或写入数据，芯片本身不会对存储单元进行分页，分页是操作系统和 MMU 层面实现的逻辑概念。


内存存储单元：一个存储单元通常是8bit（1Byte）。
页（Page）：虚拟内存被划分的小块，大小固定（常见4KB），结构体在 /linux-6.11.6/include/linux/mm_types.h 中被定义。
页框（Page Frame）：物理内存被划分的小块，大小和页相同（有时叫做物理页）。
分页单元（Paging Unit）：把所有的 RAM 分成固定长度的页框（page frame）。
页表（Page Table）：存储页与页框之间映射关系的数据结构，用于地址转换，结构体在 /linux-6.11.6/include/linux/XXXXXXXXXXX.h 中被定义。
页表项（PTE: Page Table Entry）：包含映射关系和访问权限等信息。 
page fault
minor page fault
major page fault
多级页表（Multi-level Page Table）：为了节省页表空间，将页表也分页，形成多级结构（如二级页表、三级页表），结构体在 /linux-6.11.6/include/linux/XXXXXXXXXXX.h 中被定义。
TLB（Translation Lookaside Buffer）：为了加速页表查询，引入一个硬件缓存叫做TLB，用于缓存最近访问的页表项。
换页（Page Swapping）：当物理内存不足时，操作系统可以将某些页暂时换出到磁盘（swap分区），提高内存利用率。

区（Zone）：
   """
    print(mm_concept) 


def print_mm_cmd():
    print("mm usage command:")
    mm_cmd = """
mm -n
   """
    print(mm_cmd) 

