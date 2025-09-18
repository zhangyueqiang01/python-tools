
1. sleep.c：是一个用 C 编写的程序，通过调用 sleep() 函数实现睡眠功能
2. printf.c：经典hello world程序
3. hello.asm: 是用汇编语言编写的经典hello world程序
     编译和运行方法：
        汇编：nasm -f elf64 hello.asm -o hello.o
        链接：ld hello.o -o hello
        执行：./hello
4. zombie.c: 产生一个僵尸进程，编译gcc zombie.c -o zombie;打开另一个终端，使用ps aux | grep Z或ps -ef | grep defunct查看僵尸进程
