通过运行./mytool.py 添加以下选项可以实现不同的功能

optional arguments:
  -h, --help            show this help message and exit
                        Display usage instance
  --item {main,var,printf,macron,struct,vas,mem_consume,cpu_consume,fork,current}
                        Usage: ./mytool.py --show c --item printf
  --option {basic,cmd,instance_helloworld,instance_add}
                        Usage: ./mytool.py --show assembly --option basic
  --choice {concept}    Usage: ./mytool.py --show mm --choice concept
  -i PKG, --install PKG
                        install packages on remote host
  -p PING, --ping PING  ping a net such as ping 8.8.8
  -d HOST, --ihost HOST
                        combine with -i
  -z ZOMBIE, --zombie ZOMBIE
                        create a zombie process on loalhost machine
  -P PASSWD, --passwd PASSWD
                        input a number and create a random passwd
  -w HPORT, --web HPORT
                        such as python -m SimpleHTTPServer 8080 or python3 -m
                        http.server 80
  -t TPORT, --mytcpdump TPORT
                        such as tcpdump -i any tcp port 80 and host 8.8.8.8
  -u UPORT, --udpdump UPORT
                        such as tcpdump -i any udp port 80 and host 8.8.8.8
                        -vv
  -H, --healthchk       Run Linux health check
  -e, --SecureEn        protect your Linux
  --arpdump             such as tcpdump -i any arp -ennl -vv
  --top10               { ps aux | head -1 ; ps aux | sort -k3rn | head ; }
  --host HOST           send UDP packages to Host name or IP address, default
                        is NUll
  --port PORT           send UDP packages to Port number, default is 12345
  --size SIZE           send UDP packages Message size in bytes, default is
                        1024 Kb
  --packets-per-thread PACKETS_PER_THREAD
                        Number of UDP packets per thread, default is 3
  --total-threads TOTAL_THREADS
                        Total number of threads, default is 10
  --shost SHOST         Scan a special host tcp port, default host is NUll
  --sport SPORT         Scan a host speial tcp port like "nc -zv 8.8.8.8 80"
                        or "nmap -sV -p 22 8.8.8.8", default port is NUll
  --cntoeng CNTOENG     Modify all Chinese punctuation marks into English
                        punctuation marks, like sed -i s/：/:/g test.py


通过运行./mytool.py —show [arg] 可以进行信息展示，以下是对各种不常用的参数的备注

reboot: 系统重启原因定位
shell: shell 概念讲解
launch_ipv6: Linux 上开启ipv6的方法
src2bin: Linux上源代码变成二进制文件的详细过程
syscall_instance: 创建系统调用instance
syscall: 系统调用概念
login: bj2 pool快速登录方法
ubuntu: ubuntu 系统上相关指令的使用
ckernel: 内核编译
nginx: nginx 配置实例
chntpw:  linux上重置windows密码的方法
kdump: kdump相关知识和配置方法
core_dump:  程序崩溃自动产生core文件的方法
cpu_cache: cpu 缓存讲解
boot_fail: 启动失败troubleshooting
cpu_register: cpu寄存器讲解
kerneldir: 内核目录讲解
nic: 网卡配置实例
time: 时钟相关的知识
mod: 查看内核模块依赖关系的方法
newline: 换行符相关的知识
nfs: 配置网络文件系统的方法
regularExp: 常用的正则表达式
xxd: 修改磁盘上特定存储空间的数据，例如破坏mbr，文件系统
losetup: 创建环回设备，例如在本地虚拟一个磁盘文件
process: 进程相关的知识
Hexdump: 调试和分析二进制文件
kthread: 常见内核线程功能概述
lspci/dmidecode: 硬件信息查看
sysctl: 系统级行为调优
keepalived: 实现 VIP 在两台主机上漂移
keepalived_nginx：实现 nginx 的高可用
stp: 生成树基本概念介绍
mlag: 多机箱链路聚合基本概念介绍
ftp: ftp交互模式下常用的指令
mysql: mysql 基础指令
