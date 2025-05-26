#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_concept_cmd():
    mm_concept = """
CPU实模式（Real Mode）：实模式是 Intel 8086 引入的最初工作模式，是 CPU 上电后默认的模式，它提供了一种简单直接的方式访问内存，内存地址=段寄存器*16+偏移量（BIOS 初始化，bootloader）。
CPU保护模式（Protected Mode）：保护模式由 Intel 80286 引入，80386 起正式流行，支持内存保护、多任务、分页机制等现代操作系统特性，内核启动后会立即从实模式切换到保护模式。
虚拟地址（Virtual Address）：又称线性地址（Linear Address），是分页机制下，经过段机制转换后的地址，在开启分页时，线性地址会被转换为物理地址。
逻辑地址：逻辑地址是程序在运行时看到和使用的地址，在x86保护模式中，逻辑地址 = 段寄存器（CS、DS、SS 等） + 偏移地址，在分页机制下，逻辑地址通常就是虚拟地址。
物理地址（Physical Address）：实际访问内存芯片时使用的地址，通过内存管理单元（MMU）将虚拟地址映射到物理地址。
内存管理单元（Memory Management Unit）：管理内存并把虚拟地址转换为物理地址的硬件。
程序中的段机制：./mytool.py --show c --item vas
用户空间地址（User Space）：用户程序可访问的内存区域，保护机制防止用户程序访问内核空间。
内核空间地址（Kernel Space）：操作系统核心代码使用的内存区域，受保护，用户态无法直接访问。

地址总线（Address Bus）：CPU通过地址总线发送内存地址。
数据总线（Data Bus）：CPU与内存之间传输数据。
控制总线（Control Bus）：用于发送读写等控制信号。
内存芯片：

内存存储单元：一个存储单元通常是8bit（1Byte）。
页（page）：
分页单元（paging unit）：把所有的 RAM 分成固定长度的页框（page frame）（有时叫做物理页）
页表（page table）：把虚拟地址映射到物理地址的数据结构，存放在主存中，并在启用分页单元之前必须由内核对页表进行适当的初始化。
   """
    print(mm_concept) 


def print_mm_cmd():
    print("mm usage command:")
    mm_cmd = """
mm -n
   """
    print(mm_cmd) 

