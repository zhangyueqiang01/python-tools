#include <stdio.h>
#include <unistd.h>   // Linux/Unix系统使用sleep()函数

int main() {
    int sleep_seconds = 600;

    printf("程序将暂停%d秒...\n", sleep_seconds);
    sleep(sleep_seconds);
    printf("%d秒已过去，程序继续执行...\n", sleep_seconds);
    return 0;
}

