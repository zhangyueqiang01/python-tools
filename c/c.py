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

