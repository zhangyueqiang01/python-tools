
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    pid_t pid;

    // 创建子进程
    pid = fork();

    if (pid < 0) {
        // fork失败
        fprintf(stderr, "Fork failed\n");
        return 1;
    } else if (pid == 0) {
        // 子进程
        printf("子进程 (PID: %d) 正在运行\n", getpid());
        printf("子进程 (PID: %d) 即将退出\n", getpid());
        // 子进程立即退出
        exit(0);
    } else {
        // 父进程
        printf("父进程 (PID: %d) 正在运行\n", getpid());
        printf("父进程不会调用wait()，子进程将成为僵尸进程\n");
        printf("请在另一个终端中使用 'ps aux | grep Z' 查看僵尸进程\n");
        printf("按Ctrl+C退出程序\n");
        
        // 父进程休眠30秒，期间不调用wait()，让子进程成为僵尸
        sleep(30);
        
        printf("父进程即将退出\n");
    }

    return 0;
}

