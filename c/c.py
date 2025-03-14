#!/usr/bin/python
# -*- coding: utf-8 -*-


def print_cprintf_cmd():
    print("printf usage:")
    printf_cmd = """

# 函数原型
int printf(const char *format, ...);


# instance
#include <stdio.h>

int main() {
	int i = 42;
        printf("Hello, World!\\n");
	printf("int i = %d\\n", i);
        return 0;
}


# 常见变量类型：
	整型 (int, short, long, long long)
	浮点型 (float, double)
	字符型 (char)
	无符号整型 (unsigned int, unsigned short, unsigned long, unsigned long long)
	长整型 (long)
	布尔型（bool，需要包含<stdbool.h>）

	
# 格式控制字符串
	整数类型
		%d 或 %i：输出带符号的十进制整数。
		%u：输出无符号十进制整数。
		%o：输出无符号八进制整数。
		%x：输出无符号十六进制整数（小写字母）。
		%X：输出无符号十六进制整数（大写字母）。
	浮点数类型
		%f：输出浮点数（默认格式）。
		%e：以科学记数法格式输出浮点数（小写字母）。
		%E：以科学记数法格式输出浮点数（大写字母）。
		%g：根据实际情况自动选择 %f 或 %e。
		%G：根据实际情况自动选择 %f 或 %E。
	字符和字符串类型
		%c：输出一个字符。
		%s：输出一个字符串。
	其他格式控制符
		%p：输出指针的值（内存地址）。
		%%：输出一个百分号字符 %，不需要对应的参数。
	对齐		
		printf("%5d\\n", num);  // 输出宽度为5，默认右对齐
		printf("%-5d\\n", num);  // 输出宽度为5，左对齐
		printf("%10.2f\\n", pi);  // 宽度10，保留2位小数
		printf("%-10.2f\\n", pi); // 宽度10，保留2位小数，左对齐
   """
    print(printf_cmd)  


def print_cmacron_cmd():
    print("macron usage")
    macron_cmd = """
1. 常量定义
#define PI 3.14159
#define MAX_BUFFER_SIZE 1024


2. 宏函数
#define SQUARE(x) ((x) * (x))
SQUARE(3 + 2)  // 这个宏会被替换成 ((3 + 2) * (3 + 2))，所以得到正确的结果 25


3. 条件编译
#define DEBUG 1

#ifdef DEBUG
    printf("Debugging mode enabled\n");
#endif


4. 取消宏定义
#define MAX 100
#undef MAX

   """
    print(macron_cmd)  


def print_git_cmd():
    print("git usage command:")
    git_cmd = """

   """
    print(git_cmd)  

