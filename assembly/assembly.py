#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_abasic_cmd():
    basic_cmd = """
########################################### 基础知识 ################################

机器指令： 机器指令（Machine Instruction），也叫机器码指令、机器语言，计算机CPU能够直接识别和执行的最基本
指令，由一串二进制代码组成。每条机器指令都对应CPU要执行的一种基本操作，比如：
	数据的传输（如从内存读数据到寄存器）
	算术运算（如加减乘除）
	逻辑运算（如与、或、非）
	控制跳转（如条件跳转、函数调用）

汇编语言的产生： 写程序不方便
汇编语言的组成：
	汇编指令：机器码的助记符，有对应的机器码。
	伪指令：没有对应的机器码，由编译器执行，计算机并不执行。
	其他符号：如+、-、*、/等，由编译器识别，没有对应的机器码。
指令&数据： 指令和数据是应用上的概念。在内存或磁盘上，指令和数据没有任何区别，都是二进制信息。

cpu对存储器的读写： 通过操作存储芯片
	存储单元的地址（地址信息）
	器件的选择，读或写的命令（控制信息）
	读或写的数据（数据信息）

地址总线： 64位CPU上通常40~52条
数据总线： 64位CPU一般意味着数据总线为64位，即一次可以并行传输64位（8字节）数据
控制总线： 64位CPU控制总线的数量不固定，取决于CPU设计，一般20~40条左右
	读/写（RD/WR）
	中断请求（IRQ）
	内存请求（MEMREQ）
	I/O请求
	时钟
	复位
	
各类存储器芯片：
		|||	RAM（内存）
                |||	  |||
                |||=======================
		|||
		|||
		|||	ROM（bios）
		|||	  |||
		|||=======================
		|||
|-----|		|||			      |------|
| cpu |=========|||	RAM（显存）-----------|显示器|
|-----|    总线 |||	  |||		      |------|		
                |||=======================
                |||
		|||	RAM（内存扩展）
		|||	  |||
		|||=======================
		|||
		|||
		|||	RAM（网卡）
		|||	  |||
		|||=======================
		|||
		|||
		|||其他器件
    """
    print(basic_cmd)

def print_assembly_cmd():
    assembly_cmd = """

########################################### 简介 ################################
汇编语言是一种底层编程语言，直接操作计算机硬件。以下是一些常用的汇编指令，主要基于x86架构：


########################################### 常用指令 ##################################

数据传输指令
	MOV - 将数据从一个位置传送到另一个位置。例如：MOV AX, BX将BX寄存器中的值复制到AX寄存器。
	PUSH - 将数据压入堆栈。例如：PUSH AX将AX寄存器中的值压入堆栈。
	POP - 从堆栈中弹出数据。例如：POP AX从堆栈中弹出一个值并存储在AX寄存器中。
	LEA - 获取有效地址。例如：LEA AX, [BX+SI]将BX+SI的内存地址加载到AX中。
	
算术运算指令
	ADD - 加法运算。例如：ADD AX, BX将AX和BX中的值相加，结果存储在AX中。
	SUB - 减法运算。例如：SUB AX, BX将BX从AX中减去，结果存储在AX中。
	MUL - 无符号乘法。例如：MUL BX用AX中的值乘以BX中的值，结果存储在AX和DX中。
	DIV - 无符号除法。例如：DIV BX用AX中的值除以BX，商存储在AX中，余数存储在DX中。
	INC - 自增运算。例如：INC AX将AX中的值加1。
	DEC - 自减运算。例如：DEC AX将AX中的值减1。
	
逻辑运算指令
	AND - 位与操作。例如：AND AX, BX对AX和BX中的值进行位与操作，结果存储在AX中。
	OR - 位或操作。例如：OR AX, BX对AX和BX中的值进行位或操作，结果存储在AX中。
	XOR - 位异或操作。例如：XOR AX, BX对AX和BX中的值进行位异或操作，结果存储在AX中。
	NOT - 位非操作。例如：NOT AX对AX中的值进行位取反。
	
控制转移指令
	JMP - 无条件跳转。例如：JMP LABEL跳转到LABEL处执行代码。
	JE/JZ - 如果相等或零，则跳转。例如：JE LABEL当上一次计算结果为零时跳转到LABEL。
	JNE/JNZ - 如果不相等或不为零，则跳转。例如：JNE LABEL当上一次计算结果不为零时跳转到LABEL。
	CALL - 调用子程序。例如：CALL SUBROUTINE跳转到子程序SUBROUTINE执行，并在完成后返回调用点。
	RET - 从子程序返回。例如：RET从子程序返回到调用点。
	
数据比较指令
	CMP - 比较两个操作数。例如：CMP AX, BX比较AX和BX的值，并设置标志寄存器。
	TEST - 测试操作数。例如：TEST AX, BX对AX和BX进行位与操作，但不存储结果，仅设置标志寄存器。


########################################### 备注 ##################################

这些指令是x86汇编语言中的基础，掌握它们有助于理解底层计算机操作和编写高效的低级代码。
   """
    print(assembly_cmd) 


def print_instance_add_cmd():
    add_cmd = """
下面是一个用 x86 汇编语言（64位，适用于如 nasm 汇编器 + Linux 系统环境）编写的简单程序
它计算 1 + 2 并将结果以 字符 形式打印到屏幕上。
########################################### instance ################################

section .data
    msg     db  "Result: ", 0          ; 输出前缀字符串
    len     equ $ - msg
    newline db 10                      ; 换行符 \n

section .bss
    result  resb 3                     ; 至少 2 字节用于两位数 + 1字节终止符

section .text
    global _start

_start:
    ; --------------------------------
    ; 计算 1 + 2 -> rax = 3
    ; --------------------------------
    mov     rax, 1
    add     rax, 2                     ; rax = 3

    ; --------------------------------
    ; 转换为 ASCII 字符（只支持个位数）
    ; --------------------------------
    add     al, '0'                    ; AL + '0' => ASCII 字符
    mov     [result], al              ; 存入 result[0]
    
    ; --------------------------------
    ; 打印前缀 "Result: "
    ; --------------------------------
    mov     rax, 1                     ; syscall number for write
    mov     rdi, 1                     ; stdout (fd = 1)
    mov     rsi, msg                   ; message address
    mov     rdx, len                   ; length of message
    syscall

    ; --------------------------------
    ; 打印结果字符
    ; --------------------------------
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, result
    mov     rdx, 1                     ; 只打印一个字符
    syscall

    ; --------------------------------
    ; 打印换行符
    ; --------------------------------
    mov     rax, 1
    mov     rdi, 1
    mov     rsi, newline
    mov     rdx, 1
    syscall

    ; --------------------------------
    ; 正常退出
    ; --------------------------------
    mov     rax, 60                    ; syscall number for exit
    xor     rdi, rdi                   ; return 0
    syscall

########################################### 编译与运行 ################################
nasm -f elf64 add64.asm -o add64.o
ld -o add64 add64.o
./add64


########################################### 代码解读 ################################
    """
    print(add_cmd)


def print_instance_helloworld_cmd():
    helloworld_cmd = """
以下是适用于 Linux x86-64 架构 的 64 位汇编语言版本的 Hello, world! 程
序，使用 NASM 语法，并使用 syscall 指令调用内核服务

################################### 源码 ################################

# 将以下内容保存为hello64.asm

section .data
    hello_msg db "Hello, world!", 0xA    ; 字符串 + 换行符
    hello_len equ $ - hello_msg          ; 字符串长度

section .text
    global _start

_start:
    ; write(int fd, const void *buf, size_t count)
    ; 调用 write 系统调用：向标准输出（屏幕）输出字符串
    ; 告诉cpu请把我内存里这个字符串（通过1号系统调用，地址在 rsi，长度在 rdx）打印到标准输出（fd = 1）上去。
    mov rax, 1              ; syscall number for write (1)
    mov rdi, 1              ; file descriptor: stdout
    mov rsi, hello_msg      ; 将字符串的地址写入rsi寄存器
    mov rdx, hello_len      ; 将字符串的长度写入rdx寄存器
    syscall                 ; 调用内核服务

    ; exit(int status)
    ; 调用 exit 系统调用：程序退出
    ; 告诉cpu通过60系统调用，退出码在rdi结束程序的运行
    mov rax, 60             ; syscall number for exit (60)
    xor rdi, rdi            ; status = 0，把 rdi 设为 0，表示退出码为 0（正常退出）
    syscall                 ; 调用内核服务


############################## 编译与运行命令 ################################

nasm -f elf64 hello64.asm         # 编译成 ELF64 对象文件（汇编器：.asm -> .o）
ld -o hello64 hello64.o           # 链接成可执行文件（链接器：.o -> 可执行程序）
./hello64                         # 运行程序


############################## 代码解读 ################################

section .data
	这是数据段
hello_msg db "Hello, world!", 0xA
	db 表示定义一个字节序列。
	"Hello, world!" 是我们要打印的字符串。
	0xA 是 ASCII 的换行符（即 \\n），打印完后换行更美观。
hello_len equ $ - hello_msg
	equ 是“等于”的意思，用来定义一个常量。
	$ 表示当前位置的地址，减去 hello_msg 就得到了字符串的字节长度。
	相当于 strlen("Hello, world!\\n")

section .text
	这是 代码段，也就是程序的主逻辑。
global _start
	声明 _start 是全局符号，链接器会从这里开始执行程序。
	注意：这是 Linux 系统程序的默认入口（不像 C 程序从 main 开始）。

syscall：
	告诉CPU我要从用户态切入到内核态，请帮我执行编号为 rax 的系统调用！
        (在 64位CPU（x86_64架构） 上运行的 Linux系统中，系统调用号是存放在 RAX 寄存器 中的)

############################## 命令解读 ################################

nasm： 
	表示调用 NASM（Netwide Assembler），这是一个流行的汇编语言编译器
-f elf64：
	-f 是 format（格式） 的缩写，告诉 NASM 你要生成哪种格式的目标文件（object file）。
	elf64 表示生成 ELF 64-bit 格式的目标文件。
hello64.o：
	生成的目标文件名称
.o 是目标文件（Object File）
	它是编译后的中间产物，里面包含了机器码，但还不是完整程序。
	它还没把“程序入口地址”确定好，也可能引用了外部符号（比如库函数），需要链接器解决。
	格式仍然是 ELF（Executable and Linkable Format），但状态是“未链接”。
链接器 ld 把 .o 文件转成最终可以执行的程序
	链接器的主要工作：
		把所有代码段、数据段、符号地址“拼”成一个整体。
		设置程序入口点（比如 _start）。
		添加 ELF 头、程序头（program headers）等，告诉操作系统怎么加载它。

		
nasm -f elf64 hello64.asm
hexdump -C hello64.o          # 看原始字节
objdump -d hello64.o          # 反汇编，看程序长啥样
readelf -S hello64.o          # 查看 ELF 文件的段信息
readelf -h hello64.o	      # 查看 ELF 文件的header	
    """
    print(helloworld_cmd)


def print_axxx_cmd():
    xxx_cmd = """
    """
    print(xxx_cmd)

def print_axxx_cmd():
    xxx_cmd = """
    """
    print(xxx_cmd)


