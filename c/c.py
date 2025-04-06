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


def print_struct_cmd():
    struct_cmd= """

##############################定义一个结构体类型##################################
struct Student {
    char name[50];  // 学生姓名
    int age;        // 学生年龄
    float score;    // 学生成绩
};

int main() {
    struct Student stu1 = {"张三", 20, 88.5};	// 定义结构体变量
    printf("姓名: %s\\n", stu1.name);		// 访问结构体成员
    return 0;
}

##############################结构体的别名（typedef）##################################
typedef struct {
    char name[50];
    int age;
    float score;
} Student;  // 结构体别名

int main() {
    Student stu1 = {"李四", 22, 90.0};  // 直接使用别名
    printf("姓名: %s, 年龄: %d, 成绩: %.2f\\n", stu1.name, stu1.age, stu1.score);
    return 0;
}

##############################结构体指针##################################
typedef struct {
    char name[50];
    int age;
} Person;

void printPerson(const Person *p) {  // 使用指针避免拷贝，提高效率
    printf("姓名: %s, 年龄: %d\\n", p->name, p->age);
}

int main() {
    Person p1 = {"王五", 25};
    printPerson(&p1);  // 传递结构体地址
    return 0;
}


##############################结构体嵌套##################################
typedef struct {
    int year, month, day;
} Date;

typedef struct {
    char name[50];
    Date birthDate;  // 结构体嵌套
} Student;

int main() {
    Student stu = {"赵六", {2000, 5, 20}};
    printf("姓名: %s, 生日: %d-%d-%d\\n", stu.name, stu.birthDate.year, stu.birthDate.month, stu.birthDate.day);
    return 0;
}


##############################结构体数组##################################
typedef struct {
    char name[50];
    int age;
} Student;

int main() {
    Student students[3] = {
        {"张三", 20},
        {"李四", 21},
        {"王五", 22}
    };

    for (int i = 0; i < 3; i++) {
        printf("姓名: %s, 年龄: %d\\n", students[i].name, students[i].age);
    }

    return 0;
}

##############################结构体在函数中的应用##################################
typedef struct {
    char brand[50];
    float price;
} Car;

void printCar(Car c) {  // 结构体传参（按值传递）
    printf("品牌: %s, 价格: %.2f\\n", c.brand, c.price);
}

int main() {
    Car car1 = {"Tesla", 350000.0};
    printCar(car1);
    return 0;
}

   """
    print(struct_cmd) 

def print_cvar_cmd():
    var_cmd = """
#####################################基本数据类型（Primitive Data Types）################################
C 语言的基本数据类型可以分为以下几类：

整型（Integer Types）：
	int：	用于表示整数，通常为 4 字节，具体大小取决于平台。
	short：	表示较小的整数，通常为 2 字节。
	long：	表示较大的整数，通常为 4 字节，但在 64 位系统上可能为 8 字节。
	long long：用于表示更大的整数，通常为 8 字节。
	无符号整型（Unsigned Integer Types）：
		unsigned int：		无符号整数，通常为 4 字节，取值范围从 0 到 4,294,967,295。
		unsigned short：	无符号短整数，通常为 2 字节，取值范围从 0 到 65,535。
		unsigned long：		无符号长整数，通常为 4 字节。
		unsigned long long：无符号长长整数，通常为 8 字节。

字符型（Character Types）：
	char：		表示一个字符，通常为 1 字节，取值范围从 -128 到 127（如果是有符号的）。
	unsigned char：	无符号字符，通常为 1 字节，取值范围从 0 到 255。
	signed char：	有符号字符，通常为 1 字节，取值范围从 -128 到 127。

浮点型（Floating-point Types）：
	float：		表示单精度浮点数，通常为 4 字节。
	double：	表示双精度浮点数，通常为 8 字节。
	long double：表示扩展精度浮点数，通常为 12 字节或 16 字节，具体取决于平台。

派生数据类型（Derived Data Types）
	数组（Array）：	由相同类型元素组成的集合。
	结构体（Struct）：由多个不同类型的数据组成的集合。
	联合体（Union）	与结构体类似，但所有成员共用同一内存空间。
	枚举（Enum）：	用于定义一组命名的整型常量。

指针类型（Pointer Types）
	指针：用于存储变量地址的类型。例如，int* 表示指向 int 类型的指针。

空类型（Void Type）
	void：表示没有类型，用于函数没有返回值的情况，或者作为指针类型（如 void*）表示指向未知类型的数据。

类型限定符（Type Qualifiers）
	const：常量类型，表示变量的值不能被修改。
	volatile：表示变量的值可能会随时发生变化，通常用于硬件寄存器或多线程环境。
   """
    print(var_cmd)

def print_cvas_cmd():
    vas_cmd = """
#####################################virtual address space (VAS)################################

+---------------------------+ 高地址
| 环境变量和命令行参数      |
+---------------------------+
| 栈（Stack）               | <--- 向低地址增长
|	|	 	    |
|	|		    |
|	v		    |
+---------------------------+
| 内存映射区                |
+---------------------------+
| 共享库                    |
+---------------------------+
|	^		    |
|	|		    |
|	|		    |
| 堆（Heap）                | <--- 向高地址增长
+---------------------------+
| 未初始化数据段（BSS）     |
+---------------------------+
| 已初始化数据段（Data）    |
+---------------------------+
| 代码段（Text）            |
+---------------------------+ 低地址

环境变量和命令行参数：存储环境变量和命令行参数。
栈（Stack）：用于存储局部变量、函数调用信息等，增长方向通常向下（地址减少）。
内存映射区（Memory Mapped Region）：文件直接映射到内存，便于高效访问。
共享库（Library mapping）：存储动态链接库的代码和数据。
堆（Heap）：用于动态内存分配，由 malloc、new 等分配，增长方向通常向上（地址增加）。
BSS 段（BSS Segment）：存放未初始化的全局变量和静态变量，在运行时被初始化为零。
数据段（Data Segment）：包括已初始化的全局变量和静态变量。
代码段（Text Segment）：存放可执行程序的代码，通常是只读的。  



# 用户空间stack的查看方法
cat /proc/<pid>/stack

# 内核空间stack的查看方法
bpftrace 是一个高级 eBPF 工具，可以通过此工具捕获内核栈

    """
    print(vas_cmd)

def print_cmem_consume_cmd():
    mem_cmd = """
/*
*以下代码实现可以消耗6GB的内存占用，如果想
*调整内存的消耗情况调整size_t size的大小即可
*使用方法：gcc mem.c && ./a.out
*/


#include <stdlib.h>  // 添加必要的头文件
#include <stdio.h>   // 为了使用printf
#include <string.h>  // 为了使用memset
#include <unistd.h>  // 为了使用pause

int main() {
    size_t size = 6UL * 1024 * 1024 * 1024; // 6GB
    char *mem = malloc(size);
    if(mem) {
        memset(mem, 0, size); // 强制分配物理内存
        printf("Allocated and touched 6GB memory\n");
        pause(); // 保持内存占用
        free(mem); // 释放内存(虽然这里不会执行到)
    }
    return 0;
}


/*
*size_t:
*	这是C语言中专门用于表示内存大小的无符号整数类型
*	在64位系统上通常是unsigned long
*	保证足够大以表示任何对象的大小
*6UL:
*	6 是数字6
*	UL 后缀表示这是一个unsigned long类型的常量
*	6默认是int类型，使用UL确保计算在足够大的类型中进行，避免溢出
*1024 * 1024 * 1024:
*	这是计算GB到字节的转换
*	1024 字节 = 1 KB
*	1024 * 1024 = 1 MB (1,048,576 字节)
*	1024 * 1024 * 1024 = 1 GB (1,073,741,824 字节)
 */

    """
    print(mem_cmd)

def print_ccpu_consume_cmd():
    cpu_cmd = """

# 如果你只是想测试 CPU 负载，可以直接用 stress 命令：
sudo yum install -y epel-release && sudo yum install -y stress  # 安装 stress
stress --cpu 2 --timeout 60  # 运行 2 个 CPU 负载线程，持续 60 秒
    """
    print(cpu_cmd)

def print_cfork_cmd():
    fork_cmd = """
/*
*fork() 是 Linux 进程创建的核心机制，它的作用是创建一个新的子进程，该子进程是父进程的副本。
*fork() 的执行过程
*	fork() 由 调用进程（父进程） 执行。
*	内核为新进程分配 唯一的进程 ID（PID）。
*	子进程继承父进程的用户态数据（变量、堆、栈等），但两者是 独立的地址空间。
*	父进程与子进程继续执行，相同的代码逻辑，但 fork() 返回值不同：
*		父进程：fork() 返回子进程的 PID。
*		子进程：fork() 返回 0。
*/


##################################### fork() instance ################################


#include <stdio.h>
#include <unistd.h>

int main() {
    pid_t pid = fork(); // 创建子进程

    if (pid > 0) {
        printf("父进程: PID = %d, 子进程 PID = %d\n", getpid(), pid);
    } else if (pid == 0) {
        printf("子进程: PID = %d, 父进程 PID = %d\n", getpid(), getppid());
    } else {
        perror("fork failed");
    }

    return 0;
}
    """
    print(fork_cmd)

def print_cxxx_cmd():
    xxx_cmd = """
    """
    print(xxx_cmd)


