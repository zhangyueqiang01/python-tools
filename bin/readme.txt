
1. burn 是一个用 C 编写的程序，创建两个线程，并将它们分别绑定到两个不同的 CPU 核心上（假设系统至少有两个核心）。这两个线程会执行一个“打满 CPU”的计算密集型任务
   通过top指令可以看到，burn进程cpu使用率为200%，交互模式下按1键可以看到cpu0、和cpu1被burn进程下的两个线程打满，对应的源码为./mytool.py --show c --item cpu_consume
