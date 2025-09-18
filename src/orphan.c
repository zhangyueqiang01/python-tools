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
        printf("子进程 (PID: %d) 启动，父进程PID: %d\n", getpid(), getppid());
        
        // 父进程已经退出，此时子进程成为孤儿进程，会被init进程收养
        printf("子进程 (PID: %d) 现在的父进程PID: %d (应该是1或进程管理器)\n", 
               getpid(), getppid());
        // 子进程休眠60秒，等待父进程先退出
        printf("子进程将在60秒后自动退出\n");

        sleep(60);
        
    } else {
        // 父进程
        printf("父进程 (PID: %d) 启动，子进程PID: %d\n", getpid(), pid);
        printf("请在3秒后在另一个终端用 ps -ef | grep %d  命令查看,此刻子进程的父进程id为1\n", pid);
        // 父进程休眠3秒后退出，此时子进程仍然在运行
        sleep(3);
        printf("父进程退出\n");
    }

    return 0;
}

