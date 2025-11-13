
1. sleep.c：是一个用 C 编写的程序，通过调用 sleep() 函数实现睡眠功能
2. printf.c：经典hello world程序
3. hello.asm: 是用汇编语言编写的经典hello world程序
     编译和运行方法：
        汇编：nasm -f elf64 hello.asm -o hello.o
        链接：ld hello.o -o hello
        执行：./hello
4. zombie.c: 产生一个僵尸进程，编译gcc zombie.c -o zombie;打开另一个终端，使用ps aux | grep Z或ps -ef | grep defunct查看僵尸进程
5. orphan.c: 产生一个孤儿进程，父进程退出，子进程被1号进程收养;可以用ps -ef | grep 子进程PID命令查看;会发现子进程的 PPID（父进程 ID）已经变为 1（init 进程）
6. my_random.py: python中random函数使用示例，Python 标准库中的random模块在random.py中，所以这里命名进行了区分
7. random.c: c语言中random()函数的使用示例
8. random.sh: bash中实现random函数的示例
9. exit.asm: 最简单的汇编代码演示，只调用了sys_exit系统调用，其中包含了32和64位cpu两个版本的代码
