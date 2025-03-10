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


def print_gcc_cmd():
    print("gcc usage command:")
    gcc_cmd = """

##############################gcc基本操作##################################


# Linux 系统中 gcc 源码目录
/usr/lib/gcc/x86_64-redhat-linux/8/include/stddef.h


# 使用 gcc -dumpmachine 查看目标架构
gcc -dumpmachine
   """
    print(gcc_cmd) 

