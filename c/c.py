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

############################## 指令实现方法 #################################

# 如果你只是想测试 CPU 负载，可以直接用 stress 命令：

sudo yum install -y epel-release && sudo yum install -y stress  # 安装 stress
stress --cpu 2 --timeout 60  # 运行 2 个 CPU 负载线程，持续 60 秒

# 这条指令创建的是两个进程，如果想实现一个进程下多个线程分别打满各个cpu核心，可编译以下代码

############################## source code #################################

下面是一个用 C 编写的示例程序，创建两个线程，并将它们分别绑定到两个不同的 CPU 核心上（假设
系统至少有两个核心）。这两个线程会执行一个“打满 CPU”的计算密集型任务（如死循环计算），将使用
	pthread 创建线程
	sched_setaffinity 绑定 CPU
	一个死循环任务打满 CPU
	
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sched.h>
#include <unistd.h>

// 线程运行函数：死循环计算以打满CPU
void *burn_cpu(void *arg) {
    int cpu_id = *(int *)arg;
    cpu_set_t cpuset;

    CPU_ZERO(&cpuset);
    CPU_SET(cpu_id, &cpuset);

    pthread_t thread = pthread_self();

    // 设置线程CPU亲和性
    if (pthread_setaffinity_np(thread, sizeof(cpu_set_t), &cpuset) != 0) {
        perror("pthread_setaffinity_np");
        pthread_exit(NULL);
    }

    printf("Thread running on CPU %d\\n", cpu_id);

    volatile unsigned long long i = 0;
    while (1) {
        i++;  // 死循环计算
    }

    return NULL;
}

int main() {
    pthread_t threads[2];
    int cpu_ids[2] = {0, 1};  // 分别指定第0核和第1核

    for (int i = 0; i < 2; ++i) {
        if (pthread_create(&threads[i], NULL, burn_cpu, &cpu_ids[i]) != 0) {
            perror("pthread_create");
            exit(1);
        }
        sleep(1); // 确保线程创建时传参不会冲突
    }

    // 主线程等待子线程（实际上不会返回）
    for (int i = 0; i < 2; ++i) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}



############################## caution #################################

编译方式
	gcc -pthread -o burn burn.c
	如果是较旧版本的 GCC
		gcc -std=gnu99 -pthread -o burn burn.c

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
#include <unistd.h>	//为了使用fork

int main() {
    pid_t pid = fork(); // 创建子进程

    if (pid > 0) {
        printf("父进程: PID = %d, 子进程 PID = %d\\n", getpid(), pid);
    } else if (pid == 0) {
        printf("子进程: PID = %d, 父进程 PID = %d\\n", getpid(), getppid());
    } else {
        perror("fork failed");
    }

    return 0;
}

##################################### 头文件和库文件 ################################

unistd.h	是一个 头文件，提供了 Unix 系统 API 的 声明（如 fork()、read()、write()等），主要用于编译阶段(一般位于/usr/include/unistd.h)。
libc.so.6	是一个 共享库文件（动态链接库），也就是 GNU C Library (glibc) 的主要部分，里面包含了这些 API 的 具体实现，主要用于程序运行时（链接和执行阶段）。
			一般位于/lib64/libc.so.6

编译阶段：
	编译器看到 #include <unistd.h>，找到对应头文件，知道 fork() 是一个合法的函数，返回 pid_t，不报错。
	此时只是用到了函数的“声明”。
链接阶段：
	编译器生成的目标文件会标记 fork() 是一个外部符号。
	链接器（ld）会从 libc.so.6 或 libc.a 中找到 fork 的实现，链接进你的可执行文件中。
运行阶段：
	你的程序真正执行 fork() 函数的机器码，是从 libc.so.6 中加载进内存的。
	
一句话总结：	
	unistd.h 负责 告诉编译器 fork() 的“长相”；libc.so.6 负责 提供运行时 fork() 的“真身”。


##################################### fork() 详细过程 ################################


fork（）—> glibc（libc.so.6）—>syscall(SYS_fork)—>_do_fork(）—>copy_process()—>wake_up_new_task() 


在用户态，fork() 是由 GNU C Library（glibc） 提供的封装，它最终调用 syscall(SYS_fork) 进入内核。
1. fork() 由 sys_fork() 触发，最终调用 _do_fork()。
2. _do_fork() 调用 copy_process() 复制父进程。
3. copy_process() 复制 PCB、文件描述符、内存空间（COW）。
4. wake_up_new_task() 将新进程加入调度器，等待调度执行。

层级		代码文件				作用
glibc		glibc/sysdeps/unix/sysv/linux/fork.c	用户态 fork() 调用 syscall(SYS_fork)
Linux 内核	kernel/fork.c				SYSCALL_DEFINE0(fork) 进入 _do_fork() 处理进程复制
Linux 内核	kernel/fork.c				copy_process() 复制进程结构
Linux 内核	kernel/sched/core.c			wake_up_new_task() 让新进程加入调度
    """
    print(fork_cmd)

def print_ccurrent_cmd():
    current_cmd = """
/*
 * save this code as current.c in work directory
 ***************************************************************
 */
#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>	/* current() */
#include <linux/cred.h>		/* current_{e}{u,g}id() */


MODULE_AUTHOR("Michael");
MODULE_DESCRIPTION("macron current usage");
MODULE_LICENSE("Dual MIT/GPL");
MODULE_VERSION("0.1");

static int __init current_usage(void)
{
	struct task_struct *current_task = current;
	printk(KERN_INFO "Current process: %s (pid: %d)\\n", current_task->comm, current_task->pid);
	printk(KERN_INFO "Current process prio: %d\\n", current_task->prio);
	printk(KERN_INFO "Current process on_cpu: %d\\n", current_task->on_cpu);
	return 0;		/* success */
}

static void __exit current_usage_exit(void)
{
	printk(KERN_INFO "Goodbye, macron current \\n");
}

module_init(current_usage);
module_exit(current_usage_exit);




/*
 * save this code as Makefile in work directory
 * run make && insmod currunt.ko && dmesg
 ***************************************************************
 */

# Simplest kernel module Makefile

PWD   := $(shell pwd)
obj-m += current.o

all:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) modules
install:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) modules_install
clean:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) clean


/*
 * if you want to print all process info , update this code to the current.c
 ****************************************************************************
 */
 
#include <linux/sched/signal.h>  // 提供 for_each_process 和相关进程遍历宏
 
static int __init current_usage(void)

{
	struct task_struct *task;
	for_each_process(task) {
		printk(KERN_INFO "Process: %s (PID: %d)\\n", task->comm, task->pid);
	}
	return 0;		/* success */
}
    """
    print(current_cmd)


def print_cmain_cmd():
    main_cmd = """
######################## Introduction ###################################

标准规定：
C语言的标准（如 C89、C99、C11）规定了 main() 函数的存在和它的格式，比如以下都是合法的：
	int main()
	int main(void)
	int main(int argc, char *argv[])

在 C 程序里，main() 函数是程序的入口点。无论你的程序里有多少其他函数，最终程序启动时，操作系统总是从 main() 函数开始执行。

main() 函数返回的整数值会传递给操作系统（或者父进程），告诉它程序是正常结束还是异常退出。

C语言要求一个程序必须有一个入口，而 main() 就是这个入口。写代码时必须写出这个函数，告诉编译器和操作系统从哪里开始执行你的程序。


########################## Advanced #####################################

通常来说， 在普通的 C 程序里，main() 是必须要写的，否则程序没有明确的入口点，编译器或者链接器会报错，比如 "undefined reference to main"。
但确实存在一些例外情况，比如：
    1. 写库（Library）而不是程序
    2. 嵌入式系统
    3. 操作系统内核、引导程序（入口是汇编程序，然后调用c程序）
    4. 自己开发的特殊编译器
    """
    print(main_cmd)

def print_chpath_cmd():
    chpath_cmd = """

############################################################## 头文件路径 ########################################################################

#include <文件名>：优先搜索编译器内置的「系统头文件路径」（如 /usr/include、/usr/local/include）
    查看 C 编译器（gcc）的头文件路径： gcc -v -E -x c /dev/null
    查看 C++ 编译器（g++）的头文件路径：g++ -v -E -x c++ /dev/null
	-v：启用详细输出模式，会打印编译器的配置信息和头文件搜索路径；
	-E：仅执行预处理步骤（不进行编译、汇编和链接）；
	-x c / -x c++：指定输入文件的语言（即使输入为空也能正确识别）；
	/dev/null：空输入文件（仅用于触发预处理流程）。

#include "文件名"：优先搜索 当前源代码所在的目录，若找不到再搜索系统头文件路径


############################################################## 常见头文件 ########################################################################

1. 输入输出相关
stdio.h（Standard Input/Output）
最基础的 I/O 头文件，提供控制台输入输出、文件操作等函数：
    输入输出：printf()、scanf()、putchar()、getchar()
    文件操作：fopen()、fclose()、fread()、fwrite()、fprintf()、fscanf()
    其他：feof()（判断文件结束）、fflush()（刷新缓冲区）

2. 字符串操作
string.h
提供字符串处理函数（注意：C 语言中没有内置字符串类型，通过字符数组实现）：
    长度计算：strlen()（求字符串长度）
    复制：strcpy()（字符串复制）、strncpy()（指定长度复制）
    拼接：strcat()（字符串拼接）、strncat()（指定长度拼接）
    比较：strcmp()（字符串比较）、strncmp()（指定长度比较）
    查找：strchr()（查找字符位置）、strstr()（查找子串位置）

3. 数学函数
math.h
提供常用数学运算函数（编译时需链接数学库 -lm，如 gcc main.c -lm）：
    基本运算：sqrt()（平方根）、pow()（幂运算，如 pow(2,3)=8）
    三角函数：sin()、cos()、tan()（参数为弧度）
    其他：abs()（整数绝对值）、fabs()（浮点数绝对值）、ceil()（向上取整）、floor()（向下取整）

4. 标准库工具函数
stdlib.h（Standard Library）
功能较杂，包含内存管理、类型转换、随机数等工具函数：
    内存管理：malloc()（动态分配内存）、free()（释放内存）、realloc()（重新分配内存）
    类型转换：atoi()（字符串转整数）、atof()（字符串转浮点数）
    随机数：rand()（生成随机数）、srand()（设置随机数种子）
    程序控制：exit()（终止程序）、system()（调用系统命令，如 system("pause")）

5. 字符处理
ctype.h
提供字符属性判断和转换函数：
    判断：isdigit(c)（是否为数字）、isalpha(c)（是否为字母）、islower(c)（是否为小写字母）
    转换：toupper(c)（转为大写字母）、tolower(c)（转为小写字母）

6. 条件编译与宏
assert.h
提供断言宏 assert(表达式)，用于调试阶段检查条件是否成立：
    若表达式为假，程序会终止并输出错误信息（如文件名、行号）；
    发布版本可通过定义 NDEBUG 禁用断言（如 #define NDEBUG）。

7. 日期与时间
time.h
提供日期和时间相关函数：
    time()：获取当前系统时间（返回秒数时间戳）；
    ctime()：将时间戳转换为人类可读的字符串（如 Wed Sep 16 10:00:00 2025）；
    localtime()：将时间戳转换为本地时间结构体（包含年、月、日、时、分、秒等）。

8. 数组与内存操作
string.h（补充）
除字符串外，还提供内存块操作函数（不依赖字符串结束符 \0）：
    memcpy()：复制指定字节数的内存块；
    memset()：将内存块填充为指定值（如 memset(arr, 0, sizeof(arr)) 清空数组）；
    memcmp()：比较指定字节数的内存块。


############################################################## UNIX 系统标准头文件 ########################################################################

unistd.h 是 UNIX 系统标准头文件（名字来源于 "UNIX Standard"），主要提供与 UNIX/Linux 操作系统交互的函数声明、宏定义和类型，是编写系统级或依赖操作系统功能的 C 程序时常用的头文件。
路径：/usr/include/unistd.h
软件包：rpm -qf /usr/include/unistd.h

unistd.h 中常用的功能和函数

1. 进程控制与程序执行
    fork()：创建新进程（UNIX 中进程创建的核心函数）。
    execve() / execl() 等：在当前进程中执行新程序（替换进程映像）。
    exit()：终止当前进程（与 stdlib.h 中的 exit() 功能类似，此处为 UNIX 标准实现）。
    getpid() / getppid()：获取当前进程 ID 和父进程 ID。
    
2. 文件与 I/O 操作
    read() / write()：底层文件读写函数（比 stdio.h 的 fread() / fwrite() 更接近系统调用）。
    close()：关闭文件描述符（对应 open() 打开的文件，open() 声明在 <fcntl.h> 中）。
    lseek()：移动文件读写指针（用于随机访问文件）。
    access()：检查文件是否存在或是否有读写权限。
    
3. 时间与休眠
    sleep(seconds)：让进程休眠指定秒数（整数秒）。
    usleep(microseconds)：让进程休眠指定微秒数（1 微秒 = 1e-6 秒，已逐渐被 nanosleep() 替代）。
    
4. 目录与路径操作
    chdir(path)：改变当前进程的工作目录。
    getcwd(buf, size)：获取当前工作目录的路径（写入 buf 缓冲区）。
    
5. 权限与用户信息
    getuid() / geteuid()：获取当前用户的实际 ID 和有效 ID。
    getgid() / getegid()：获取当前用户组的实际 ID 和有效 ID。
    chmod(path, mode)：修改文件权限（如 chmod("file.txt", 0644)）。
    
6. 常用宏定义
    STDIN_FILENO / STDOUT_FILENO / STDERR_FILENO：标准输入、输出、错误的文件描述符（分别为 0、1、2）。
    R_OK / W_OK / X_OK / F_OK：配合 access() 使用的权限检查宏（分别表示读、写、执行权限，以及文件是否存在）。
    NULL：空指针定义（部分系统中也可能在其他头文件中定义）。


使用场景
unistd.h 主要用于编写 依赖 UNIX/Linux 系统特性 的程序，例如：
    系统工具（如命令行程序）、后台服务；
    进程管理、文件系统操作相关的程序；
    需要直接调用系统级接口（而非标准库封装）的场景。


############################################################## stdlib.h ########################################################################

stdlib.h（Standard Library Header）是 C 语言标准库中非常重要的头文件，提供了一系列通用工具函数，涵盖内存管理、类型转换、随机数生成、程序控制等基础功能。它的作用是封装那些不特定于输入输出、字符串操作等专项领域，但又被广泛使用的工具函数。

stdlib.h 中常用的功能分类及函数


1. 内存管理（最核心功能之一）
提供动态内存分配与释放的函数，是 C 语言手动管理内存的基础：

malloc(size_t size)
    从堆区分配一块大小为 size 字节的连续内存，返回指向该内存的指针（未初始化，内容随机）。
    示例：int *arr = (int*)malloc(5 * sizeof(int));（分配能存储 5 个 int 的内存）。
calloc(size_t num, size_t size)
    分配 num 个大小为 size 字节的连续内存（总大小 num*size），并将内存初始化为 0。
    示例：int *arr = (int*)calloc(5, sizeof(int));（5 个 int，初始值全为 0）。
realloc(void *ptr, size_t new_size)
    调整已分配内存的大小（扩大或缩小），返回新内存的指针（可能移动原内存块）。
    示例：arr = (int*)realloc(arr, 10 * sizeof(int));（将原内存扩大到能存 10 个 int）。
free(void *ptr)
    释放由 malloc()/calloc()/realloc() 分配的内存，避免内存泄漏。
    示例：free(arr);（释放后需将指针置空：arr = NULL;）。
	
2. 类型转换函数
用于字符串与基本数据类型的转换：
    atoi(const char *str)：字符串转整数（如 "123" → 123）。
    atol(const char *str)：字符串转长整数（long 类型）。
    atof(const char *str)：字符串转浮点数（double 类型，如 "3.14" → 3.14）。

3. 随机数生成
提供伪随机数相关函数：

rand(void)
    返回一个范围在 0 到 RAND_MAX（通常为 2147483647）之间的伪随机整数。
srand(unsigned int seed)
    设置随机数种子（用于初始化随机数序列）。若种子相同，rand() 会生成相同的序列，因此通常用系统时间作为种子：
	
4. 程序控制函数
用于控制程序的执行流程和终止：

exit(int status)
    立即终止程序，释放所有资源，并将 status 作为退出状态码返回给操作系统（0 表示正常退出，非 0 表示异常）。
    示例：exit(0);（正常终止程序）。
abort(void)
    异常终止程序（类似崩溃），不执行清理操作（如 atexit() 注册的函数），通常用于调试阶段。
system(const char *command)
    调用系统命令（依赖操作系统），返回命令执行结果。
    示例：system("ls");（在 Linux 中列出当前目录文件）、system("pause");（在 Windows 命令行中暂停程序）。
	
5. 其他常用功能
abs(int n)：返回整数 n 的绝对值（如 abs(-5) → 5）。
    （注：浮点数绝对值 fabs() 在 math.h 中）。
qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void*))
    快速排序函数，可对任意类型的数组排序（需自定义比较函数）。
bsearch(const void *key, const void *base, size_t nitems, size_t size, int (*compar)(const void *, const void*))
    二分查找函数（需在已排序的数组中使用）。
   """
    print(chpath_cmd) 

def print_cxxx_cmd():
    xxx_cmd = """
    """
    print(xxx_cmd)

