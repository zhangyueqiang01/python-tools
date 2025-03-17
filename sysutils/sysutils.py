#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_ip_cmd():
    print("ip usage command:")
    ip_cmd = """

[root@huawei ~]# rpm -qf /usr/sbin/ip
iproute-4.11.0-30.el7.x86_64


#给网卡临时配置ip
sudo ip addr add 192.168.1.100/24 dev eth0
#也可以简写为sudo ip a a 192.168.1.1 dev eth0

sudo ip link set eth0 up
#ifup eth0 是通过配置文件启动网卡，通过ip命令启动不依赖配置文件

ip a
ip l
#查看网卡配置


#没有route命令时添加路由的方法
sudo ip route add 目标网络/子网掩码 dev bond0.3021
sudo ip route del 目标网络/子网掩码

[root@node9 ~]# ip neigh
192.168.122.254 dev eth1 lladdr 52:54:00:dc:37:d8 DELAY
192.168.4.254 dev eth2 lladdr 52:54:00:a6:5a:f8 STALE
192.168.2.254 dev eth0 lladdr 52:54:00:71:71:68 DELAY
#查看对端网卡MAC地址

[root@node9 ~]# ifconfig eth3 2.2.2.2
[root@node9 ~]# which ifconfig 
/usr/sbin/ifconfig
[root@node9 ~]# rpm -qf /usr/sbin/ifconfig
net-tools-2.0-0.25.20131004git.el7.x86_64
[root@node9 ~]# 
#ifconfig也可以临时配置网卡，但是需要单独安装软件包


# 创建 tap 
ip tuntap add dev tap0 mode tap 
# 创建 tun
ip tuntap add dev tun0 mode tun 
 
# 删除 tap
ip tuntap del dev tap0 mode tap
# 删除 tun
ip tuntap del dev tun0 mode tun 

# 例如使用ip link命令也可以删除tun/tap设备
ip link del tap0
ip link del tun0


# 添加并启动虚拟网卡tap设备
ip tuntap add dev tap0 mode tap 
ip tuntap add dev tap1 mode tap 
ip link set tap0 up
ip link set tap1 up
# 配置IP
ip addr add 10.0.0.1/24 dev tap0
ip addr add 10.0.0.2/24 dev tap1
# 添加netns
ip netns add ns0
ip netns add ns1
# 将虚拟网卡tap0，tap1分别移动到ns0和ns1中
ip link set tap0 netns ns0
ip link set tap1 netns ns1

[root@node01 ~]# ip netns exec ns0 ip a
[root@node01 ~]# ip netns exec ns0 ping 10.0.0.1
#这里代表进入ns0后执行命令，可以查看ip a，route -n等效果

# 创建一对veth
ip link add veth0 type veth peer name veth1
# 将veth移动到netns中
ip link set veth0 netns ns0
ip link set veth1 netns ns1
# 启动
ip netns exec ns0 ip link set veth0 up
ip netns exec ns1 ip link set veth1 up


[root@node9 ~]# ip help
Usage: ip [ OPTIONS ] OBJECT { COMMAND | help }
       ip [ -force ] -batch filename
where  OBJECT := { link | address | addrlabel | route | rule | neigh | ntable |
                   tunnel | tuntap | maddress | mroute | mrule | monitor | xfrm |
                   netns | l2tp | macsec | tcp_metrics | token }
       OPTIONS := { -V[ersion] | -s[tatistics] | -d[etails] | -r[esolve] |
                    -h[uman-readable] | -iec |
                    -f[amily] { inet | inet6 | ipx | dnet | bridge | link } |
                    -4 | -6 | -I | -D | -B | -0 |
                    -l[oops] { maximum-addr-flush-attempts } |
                    -o[neline] | -t[imestamp] | -ts[hort] | -b[atch] [filename] |
                    -rc[vbuf] [size] | -n[etns] name | -a[ll] }
   
[root@node9 ~]# ip link help
Usage: ip link add [link DEV] [ name ] NAME
                   [ txqueuelen PACKETS ]
                   [ address LLADDR ]
                   [ broadcast LLADDR ]
                   [ mtu MTU ]
                   [ numtxqueues QUEUE_COUNT ]
                   [ numrxqueues QUEUE_COUNT ]
                   type TYPE [ ARGS ]
       ip link delete { DEVICE | dev DEVICE | group DEVGROUP } type TYPE [ ARGS ]

       ip link set { DEVICE | dev DEVICE | group DEVGROUP }
	                  [ { up | down } ]
	                  [ type TYPE ARGS ]
	                  [ arp { on | off } ]
...

[root@node9 ~]# ip route help
Usage: ip route { list | flush } SELECTOR
       ip route save SELECTOR
       ip route restore
       ip route showdump
       ip route get ADDRESS [ from ADDRESS iif STRING ]
                            [ oif STRING ]  [ tos TOS ]
                            [ mark NUMBER ]
       ip route { add | del | change | append | replace } ROUTE


#简短的方式显示网卡配置信息
[root@huawei ~]# ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128 
eth0             UP             192.168.6.165/20 fe80::f816:3eff:fe0c:6a09/64 
# 此选项在iproute-4.11.0-30.el7.x86_64以上才支持
   """
    print(ip_cmd)   

def print_bond_cmd():
    print("bond usage command:")
    ip_bond = """

#加载内核模块bonding
[root@node_04 network-scripts]# modprobe --first-time bonding

# 配置系统启动时加载bonding模块
[root@node_04 network-scripts]# vi /etc/sysconfig/modules/bonding.modules
#!/bin/sh
/sbin/modinfo -F /lib/modules/3.10.0-514.el7.x86_64/kernel/drivers/net/bonding/bonding.ko bonding > /dev/null 2>&1
if [ $? -eq 0 ];then
    /sbin/modprobe bonding
fi
 
 
# 设置执行权限
[root@node_04 network-scripts]# chmod 755 /etc/sysconfig/modules/bonding.modules


***管理网网卡1***
[root@cc-hnhyxzspj-x86-controller-1 network-scripts]# cat ifcfg-enp51s0f0
SLAVE=yes
USERCTL=no
BOOTPROTO=none
MASTER=bond0
DEVICE=enp51s0f0
TYPE=Ethernet
ONBOOT=yes
 
***管理网网卡2***
[root@cc-hnhyxzspj-x86-controller-1 network-scripts]# cat ifcfg-enp51s0f1
SLAVE=yes
USERCTL=no
BOOTPROTO=none
MASTER=bond0
DEVICE=enp51s0f1
TYPE=Ethernet
ONBOOT=yes
 
***管理网网卡bond***
[root@cc-hnhyxzspj-x86-controller-1 network-scripts]# cat ifcfg-bond0   
DEVICE=bond0
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO=static
IPV6INIT=no
BONDING_MASTER=yes
BONDING_OPTS="miimon=100 mode=1"
 
***管理网网卡bond.3021子接口***
[root@cc-hnhyxzspj-x86-controller-1 network-scripts]# cat ifcfg-bond0.3021 #管理网网卡
DEVICE=bond0.3021
TYPE=Vlan
PHYSDEV=bond0
ONBOOT=yes
BOOTPROTO=static
REORDER_HDR=yes
IPADDR=10.180.16.52         #管理网ip
PREFIX=22
GATEWAY=10.180.16.254
IPV6INIT=no
BONDING_MASTER=yes
BONDING_OPTS="miimon=100 mode=1"
VLAN=yes	
VLANID=3021
 
 
# 停掉NetworkManager服务
systemctl stop NetworkManager.service 
systemctl disable NetworkManager.service
 
#查看network服务
systemctl restart network.service
 
#没有route命令时查看路由的方法
ip route
 
#没有route命令时添加路由的方法
sudo ip route add 目标网络/子网掩码 dev bond0.3021
 
#没有route命令时临时删除路由的方法
sudo ip route del 目标网络/子网掩码

#查看bond0是否生效
cat /proc/net/bonding/bond0
   """
    print(ip_bond)  


def print_iptables_cmd():
    print("iptables usage command:")
    iptables_cmd = """

#查看所有 iptables 策略
iptables -L

#拒绝所有 ICMP 协议数据包
iptables -I INPUT -p icmp -j REJECT

#只允许管理员从 202.13.0.0/16 网段使用 SSH 远程登录
iptables -A INPUT -p tcp --dport 22 -s 202.13.0.0/16 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP

#删除 INPUT 中的第二条策略
iptables -D INPUT 2           

#删除所有策略，慎用
iptables -F                 

#备份iptabes rules
iptables-save > ./iptables.bak  

#恢复iptables rules
iptables-restore < ./iptables.bak 

#保存iptables
yum install iptables-services
service  iptables save
systemctl enable iptables.service
#其实是将策略写入到了/etc/sysconfig/iptables文件中
   """
    print(iptables_cmd)

def print_tcpdump_cmd():
    print("tcpdump usage command:")
    tcpdump_cmd = """
tcpdump -i any
   """
    print(tcpdump_cmd)  

def print_route_cmd():
    print("route usage command:")
    route_cmd = """
ip route list
route -n
ip route add 10.0.12.0/24 via 10.0.41.1 dev bond0
ip route del 192.168.4.0/24
route add -net 192.56.76.0 netmask 255.255.255.0 dev eth0
route del -net 192.56.76.0 netmask 255.255.255.0 dev eth0

sudo vi /etc/rc.d/rc.local
sudo chmod +x /etc/rc.d/rc.local
sudo systemctl enable rc-local
sudo nmcli connection modify eth0 +ipv4.routes "192.168.3.0/24 192.168.2.12"
sudo nmcli connection modify eth0 -ipv4.routes "192.168.3.0/24 192.168.2.12"
sudo nmcli connection show eth0
   """
    print(route_cmd)  

def print_nmcli_cmd():
    print("nmcli usage command:")
    nmcli_cmd = """
nmcli -n
   """
    print(nmcli_cmd) 

def print_vim_cmd():
    print("vim usage command:")
    vim_cmd = """
命令模式：
        yy  复制当前行正行 	
        nyy 复制从光标所在行开始的n行
        dd  剪切当前光标所在行   	
        ndd 剪切从光标所在行开始的n行
        p   粘贴光标位置之后   
        G   跳转至尾行
        g   跳转至首行    
        dw  删至词尾
        ndw 删除后n个词
        d$  删至行尾
        nd$ 删除后n行（从光标当前处开始算起）        
        u   撤销上一次修改
        U   撤销一行内的所有修改

末行模式
        :r /etc/passwd  读文件内容进vim
        :r! ls -l / 读命令结果保存到文件中
        :set number 行号
        :set nonumber   去除行号
        :s/old/new/g    在当前行中查找到的所有字符串old替换为new
        :2,6s/old/new/g 2-6行替换
        :%s/old/new/g   在整个文件范围内替换
        :X  加入密码
        :q  不保存退出
        :q! 强制退出不保存
        :wq 保存退出，同x
        :wq!    强制保存退出

进入编辑模式
        a   光标后插入
        i   当前光标前插入
        o   在当前光标下插入空行
        A   在光标所在行尾插入 
        I   在光标行首插入内容
        O   在当前光标上插入空行

设置行号
    echo ":set number" >> /etc/vimrc

   """
    print(vim_cmd)   

def print_bash_cmd():
    print("bash usage command:")
    bash_cmd = """
控制台的快捷键
	Tab健补全
	Ctrl + Insert 组合键或用鼠标选中 复制
	Shift + Insert 组合键或单击鼠标滚轮  粘贴
	Ctrl+l 清空屏幕或者clear
	Ctrl+c 退出某个正在执行中的操作
	Ctrl+d退出shell或者exit退出
	Ctrl+a 将光标移到行首
	Ctrl+e 将光标移到行尾
	Ctrl+u 删除光标前的字符
	Ctrl+k 删除光标后的字符
	Ctrl+w 删除光标前空格为界线的单词
	Ctrl+左右箭头 以单词为单位移动光标
	Ctrl+r 搜索历史命令
	^tmp^mnt 替换上一个命令中的tmp为mnt

查看系统默认的shell
	 echo    $SHELL

查看是内部命令还是外部命令
	type  cd
	type  yum
   """
    print(bash_cmd)

def print_find_cmd():
    print("find usage command:")
    find_cmd = """
find [路径]  [参数] [表达式]  -exec  指令 {}  \；
常用选项：
    -name	根据文件名寻找文件
    -user	根据文件拥有者寻找文件
    -group	根据文件所属组寻找文件
    -perm	根据文件权限寻找文件
    -size	根据文件大小寻找文件[±Sizek]
    -type      根据文件类型寻找文件，常见类型有： f(普通文件) 、c(字符设备文件)、b(块设备文件)、l(连接文件)、d（目录）、s(套接字文件)、p(命名管道FIFO)
    -o 	         表达式或
    -a	         表达式与
	
    find ./ *.py
    find / -name passwd
    find /tmp/ -user zyq
    find /tmp/ -group zyq
    find /tmp/ -perm 644
    find /tmp/ -size +10k
    find /etc/ -size -10k
    find /etc/ -type f/c/b/l/d/s/p
    find /tmp/ -type f -exec rm -rf {} \;
	{}代表find找到的文件
	；命令结束标志，由于各个系统中的;会有不同的意义，所以前面加 \ 转义
    以上命令更简便的操作方式：
	rm -rf `find /tmp/ -type f`
   """
    print(find_cmd)   

def print_linuxbasic_cmd():
    print("linux basic knowledges:")
    linuxbasic_cmd = """
重定向
+----------+--------------+--------------+-------------+
|  设  备  |  设备名称    | 文件描述符   |   类型      |
+----------+--------------+--------------+-------------+
|  键  盘  | /dev/stdin   |	0        |  标准输入   |
+----------+--------------+--------------+-------------+
|  显示器  | /dev/stdout  |	1        |  标准输出   |
+----------+--------------+--------------+-------------+
|  显示器  | /dev/stderr  |	2        | 标准错误输  |
+----------+--------------+--------------+-------------+
错误重定向：2>错误重定向
    wadwadwad 2> test
双重输出重定向
    # 将正确的输出结果与错误输出结果一次性单独地送到不同的地方
    find /etc/ -name passwd >file 2> test
    # 不管是正确输出还是错误输结果都送到同一个指定的地方则可使用“&> 或 &>>”
    find /etc/ -name passwd &> test

输入重定向
    cat > ok << EOF
    123
    456
    EOF

文件操作命令	
	more    文件分页查看，空格向下一屏，Ctrl+B 返回上一屏
	less    文件分页查看， 使用[pageup] [pagedown]来往前往后翻看文件，回车一行，空格翻页，q退出
	head /etc/passwd    默认前10行		
	head -5 /etc/passwd
	tail /etc/passwd    默认后10行
	tail -n 5 /etc/passwd
	tail -f /var/log/message    实时监测文件
	wc -l /etc/passwd   显示行数
	paste file1 file2 file3	    把每个文件以列对列的方式，一列列地加以合并

sort
    -r 以相反的顺序来排序
    -n 依照数值的大小排序
    -k 是指按照那一列进行排序
    -t <分隔字符>指定排序时所用的栏位分隔字符。
    -c 在每行旁边显示该行重复出现的次数

打印cpu使用率top10的进程，倒序排列
ps aux | sort -k4rn | head
添加标题再进行打印
{ ps aux | head -1 ; ps aux | sort -k4rn | head ; }
   """
    print(linuxbasic_cmd)   

def print_gpt_cmd():
    print("gpt usage command:")
    gpt_cmd = """
# 在执行这些操作时，请确保您已经备份了重要数据

parted /dev/vdb
(parted) mklabel gpt  
# mkpart后跟分区名称、文件系统类型、起始位置和结束位置
(parted) mkpart primary ext4 1MB 100%  
(parted) print
(parted) quit
sudo mkfs.ext4 /dev/vdb1


# 创建多个分区的方法
mkpart primary ext4 1MB 10GB
mkpart primary ext4 10GB 20GB
mkpart primary ext4 20GB 100%
   """
    print(gpt_cmd) 

def print_iostat_cmd():
    print("iostat usage command:")
    iostat_cmd = """
[root@node07 ~]# iostat -x vda -d 1
#######
每隔一秒查看一下vda的IO详情

[root@node07 ~]# iostat -x
Linux 3.10.0-514.el7.x86_64 (node07) 	06/27/2024 	_x86_64_	(1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.56    0.00    0.19    0.21    0.00   99.04

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
vda               0.01     0.23    4.53    2.48   160.90    76.94    67.90     0.04    5.33    0.76   13.71   0.69   0.48
vdb               0.00     0.00    0.21    0.00     1.60     0.00    15.10     0.00    0.09    0.09    0.00   0.07   0.00
dm-0              0.00     0.00    0.11    0.00     0.90     0.00    16.69     0.00    0.05    0.05    0.00   0.05   0.00
dm-1              0.00     0.00    3.17    2.06   139.18    75.19    81.97     0.04    8.18    1.04   19.18   0.91   0.47

#########
以下字段可以通过man进行查看
Device：磁盘设备的名称。dm-0，dm-1对应的逻辑卷，可以通过ls -l /dev/mapper进行查看
rrqm/s：全称是 “The number of read requests merged per second”，即每秒合并的读请求数。
wrqm/s：每秒合并的写请求次数。
r/s：每秒完成的读请求次数。
w/s：每秒完成的写请求次数。
rkB/s：每秒读取的数据量（千字节）。
wkB/s：每秒写入的数据量（千字节）。
avgrq-sz：全称是 “Average Request Size”，即平均每次请求的数据量（扇区）。
avgqu-sz：全称是 “Average Queue Length”，即平均请求队列长度。
await：平均每次请求的等待时间（毫秒）。
r_await：平均每次读请求的等待时间（毫秒）。
w_await：平均每次写请求的等待时间（毫秒）。
svctm：全称是 “The average service time”，即服务时间。这个指标表示磁盘平均每次请求的服务时间（毫秒）。服务时间是指从磁盘接收到一个 I/O 请求到请求被完全服务的时间，包括寻道时间、旋转延迟和数据传输时间。
%util：磁盘 I/O 使用率。


`avg-cpu` 部分展示了 CPU 使用情况的平均值，这些值是基于 `iostat` 命令指定的时间间隔内所有 CPU 的总体表现。下面是每个参数的说明：
- `%user`：显示在用户空间（应用程序）运行的进程所占用的 CPU 百分比时间。这包括常规用户进程和应用程序的执行时间。如果这个值很高，说明系统正在积极地处理应用程序的任务。
- `%nice`：显示运行在较低优先级（通过 `nice` 值调整）的进程所占用的 CPU 百分比时间。如果这个值很高，说明系统正在执行很多被调整为较低优先级的任务。
- `%system`：显示在内核空间运行的进程所占用的 CPU 百分比时间。这包括系统调用和内核进程的执行时间。如果这个值很高，说明系统可能在处理大量的系统调用或内核级别的任务。
- `%iowait`：显示 CPU 等待 I/O 完成的百分比时间。这个值高表示 CPU 经常在等待磁盘 I/O 操作完成，可能是 I/O 子系统成为性能瓶颈的迹象。
- `%steal`：在虚拟化环境中，这个值显示被虚拟机管理器（如 hypervisor）偷走的 CPU 时间百分比。当物理 CPU 被其他虚拟机使用时，这个值会升高。
- `%idle`：显示 CPU 空闲时间的百分比。如果这个值很高，说明 CPU 很少被使用，系统可能比较空闲或者 CPU 资源充足。如果这个值很低，说明 CPU 非常繁忙，系统可能需要更多的 CPU 资源来处理负载。
   """
    print(iostat_cmd) 

def print_vmstat_cmd():
    print("vmstat usage command:")
    vmstat_cmd = """
vmstat 是一个在类Unix系统中使用的监控工具，用于报告虚拟内存统计信息。
vmstat 命令可以提供关于进程、内存、分页、块IO、中断和CPU活动的信息。

vmstat 2 3
每2秒更新一次，更新3次

vmstat -s
查看包括内存单元大小的详细内存统计：


[root@node07 ~]# vmstat 
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 2  0      0 607744   1012 290104    0    0    59    29   21   48  0  0 100  0  0

### 参数解释

`vmstat` 的输出分为几个部分，每部分代表系统不同方面的性能指标：

#### procs（进程）
- `r`：等待运行的进程数。
- `b`：在不可中断睡眠状态的进程数。

#### memory（内存）
- `swpd`：使用的虚拟内存（swap）大小。
- `free`：空闲的内存大小。
- `buff`：用于缓冲的内存大小。
- `cache`：用于缓存的内存大小。

#### swap（交换）
- `si`：从交换区到主存的交换页数量（每秒）。
- `so`：从主存到交换区的交换页数量（每秒）。

#### io（块设备IO）
- `bi`：从块设备接收的块数（每秒）。
- `bo`：发送到块设备的块数（每秒）。

#### system（系统）
- `in`：每秒中断数，包括时钟中断。
- `cs`：每秒上下文切换数。

#### cpu（CPU）
- `us`：用户态时间（百分比）。
- `sy`：系统态时间（百分比）。
- `id`：空闲时间（百分比）。
- `wa`：等待IO时间（百分比）。
- `st`：从虚拟机偷取的时间（百分比）（仅当系统是虚拟机时适用）。
   """
    print(vmstat_cmd) 

def print_iotop_cmd():
    print("iotop usage command:")
    iotop_cmd = """
iotop 是Linux系统上一个用来监视磁盘I/O使用状况的命令行工具，它以类似 top 命令的界面显示进程的磁盘读写情况。
iotop 需要管理员权限才能运行，因为它需要访问到 /proc 文件系统中的敏感信息。

[root@node07 ~]# sudo iotop -b 
Total DISK READ :       0.00 B/s | Total DISK WRITE :       0.00 B/s
Actual DISK READ:       0.00 B/s | Actual DISK WRITE:       0.00 B/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN      IO    COMMAND
    1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd --switched-root --system --deserialize 21
    2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
    3 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/0]


iotop 以非交互方式每2秒刷新一次，总共刷新5次
sudo iotop -b -d 2 -n 5

iotop 以非交互方式每2秒刷新一次，总共刷新5次，查看进程的IO使用情况，默认是线程。
sudo iotop -b -d 2 -n 5 -P


1. **输出内容解读**：
Total DISK READ/WRITE: 显示总的磁盘读/写速度，单位是字节每秒（B/s）。
Actual DISK READ/WRITE: 显示实际的磁盘读/写速度，这也是字节每秒（B/s）。这个值表示实际发生的数据传输速率，可能因为缓存或其他因素而与Total DISK READ/WRITE不同。
TID: 线程ID，这是Linux内核中的一个概念，用于标识线程。
PID: 进程ID。
PRIO: 进程的优先级。
USER: 运行进程的用户。
DISK READ/WRITE: 分别显示每个进程或线程的磁盘读/写速度，单位是字节每秒（B/s）。
SWAPIN: 表示进程在交换区（swap）中的时间百分比。
IO: 表示进程的I/O等待时间百分比。
COMMAND: 进程的命令名称或命令行。


2. **使用 `iotop` 的交互命令**：
   - 在 `iotop` 运行时，你可以使用以下按键进行交互：
     - `q`：退出 `iotop`。
     - `o`：改变排序方式，在进程和总I/O之间切换。
     - `a`：使用所有进程，而不是仅限于当前线程。
     - `r`：反向排序，默认情况下，iotop 是根据进程的磁盘写速度进行排序的。
     - `P`：只显示进程，不显示线程。
     - `1`：在进程和线程之间切换。
	 
3. **使用参数运行 `iotop`**：
   - `-o`：只显示有实际I/O操作的进程或线程。
   - `-b`：批量模式输出，不进行交互式显示。
   - `-n`：指定 `iotop` 的刷新次数。
   - `-d`：指定 `iotop` 的刷新间隔，单位是秒。
   - `-P`：查看进程的IO使用情况，默认是线程。


找到磁盘读取速度最高的进程
sudo iotop -b -n 1 | grep -v 'Total' | grep -v 'Actual' | awk '{print $12 " "$4}' | sort -nr | head -1

找到磁盘写入速度最高的进程
sudo iotop -b -n 1 | grep -v 'Total' | grep -v 'Actual' | awk '{print $12 " "$6}' | sort -nr | head -1


####命令解读###
sudo iotop -b -n 1：以批处理模式运行 iotop，并且只输出最新的1次数据。
grep -v 'Total'：使用 grep 过滤掉包含 “Total” 的行。
grep -v 'Actual'：使用 grep 过滤掉包含 “Actual” 的行。
awk '{print $12 " "$3}'：使用 awk 打印出进程名称（COMMAND）和磁盘读速度（DISK READ）。
sort -nr：对读速度进行数值排序，-n 表示按数值排序，-r 表示逆序排序。
head -1：只输出排序后的第一行，即读速度最高的进程。
   """
    print(iotop_cmd) 

def print_systemd_cmd():
    print("systemd usage command:")
    systemd_cmd = """
基本语法
Unit 文件由多个部分组成，每部分以一个方括号包围的段名开始。
每个部分包含一系列 Key=Value 形式的配置选项。
注释以 # 或 ; 开头。


常见的部分
[Unit]：描述 unit 本身的元数据和依赖关系。
[Service]：定义服务的行为（仅用于 service 类型的 unit）。
[Install]：定义如何安装该 unit，例如是否在系统启动时启用。


[Unit] 部分
Description=：对 unit 的简短描述。
Documentation=：指向有关该 unit 的文档的 URL。
After=：定义该 unit 应该在另一个 unit 之后启动。
Requires=：定义该 unit 运行所需的其他 unit。如果所需的 unit 没有启动，该 unit 也不会启动。
Wants=：定义该 unit 运行时希望启动的其他 unit，但不强制要求。

[Service] 部分
Type=：定义服务的启动类型，常见值有：
simple：默认类型，ExecStart 启动的进程为主进程。
forking：ExecStart 启动的进程会派生一个子进程，并且子进程成为主进程。
oneshot：用于短暂运行的进程。
notify：服务在启动过程中会向 systemd 发送通知。
idle：服务会在其他任务完成后再启动。
ExecStart=：定义启动服务的命令。
ExecStop=：定义停止服务的命令。
ExecReload=：定义重新加载服务的命令。
Restart=：定义服务在失败时的重启策略，例如 on-failure。
User=：以哪个用户身份运行服务。
Group=：以哪个用户组身份运行服务。

[Install] 部分
WantedBy=：定义该 unit 所依赖的 target（目标），通常用于 enable/disable。
RequiredBy=：类似于 WantedBy，但更严格，表示必须有。

unit文件路径
/lib/systemd/system/：这是主要的系统级 unit 文件存放目录。
/etc/systemd/system/：这个目录用于存放管理员自定义的 unit 文件和配置覆盖文件。
/run/systemd/system/：这个目录用于存放运行时生成的 unit 文件，优先级高于以上两个
/usr/lib/systemd/user/：系统级用户服务的默认目录。
/etc/systemd/user/：管理员自定义的用户服务目录。
/run/systemd/user/：运行时用户服务目录。
~/.config/systemd/user/：每个用户的自定义 unit 文件目录。
   """
    print(systemd_cmd) 

def print_mod_cmd():
    print("mod usage command:")
    mod_cmd = """
# 内核模块可以依赖于其他内核模块，但通常不直接依赖于用户空间中的库文件


# 查看模块的依赖关系
[root@node07 ~]# modinfo -F depends xfs
libcrc32c

[root@node07 ~]# modinfo -F depends virtio_pci
virtio_ring,virtio

   """
    print(mod_cmd) 

def print_dracut_cmd():
    print("dracut usage command:")
    dracut_cmd = """
# 生成默认 initramfs 文件：
dracut
# 这将在 /boot 目录下生成一个新的 initramfs 文件，通常命名为 initramfs-<kernel_version>.img。

# 指定生成的 initramfs 文件名：
dracut /path/to/initramfs.img

# 指定内核版本：
dracut --kver <kernel_version>
# 生成特定内核版本的 initramfs 文件。

# 显示帮助信息：
dracut --help

# 生成特定内核模块的 initramfs 文件：
dracut --add <module_name> /path/to/initramfs.img

# 列出所有可能的模块：
dracut --list-modules

# 假设你需要为一个特定的内核版本生成 initramfs 文件，可以使用以下命令：
dracut --kver 5.4.0-74-generic /boot/initramfs-5.4.0-74-generic.img

# 通过配置修改文件生成initramfs文件
vi /etc/dracut.conf  
# additional kernel modules to the default  
add_drivers+="xen-blkfront xen-netfront virtio_blk virtio_scsi virtio_net virtio_pci virtio_ring virtio"
dracut -f /boot/initramfs-2.6.32-573.8.1.el6.x86_64.img
   """
    print(dracut_cmd) 

def print_mount_cmd():
    print("mount usage command:")
    mount_cmd = """
# 基本语法：
mount [-t 文件系统类型] [-o 选项] 设备文件名 挂载点

# -t 文件系统类型：指定要挂载的文件系统类型，如ext4、ntfs等。如果不指定，默认根据设备文件自动识别。
# -o 选项：指定挂载时的选项，比如读写权限、挂载类型等。常见选项包括rw（读写权限，默认）、ro（只读权限）、remount（重新挂载已经挂载的文件系统）等。

# 重新已读写的方式进行挂载
mount -o remount,rw /sysroot


# 绑定挂载一个目录到另一个目录，即两个目录将共享相同的内容
mount --bind /dev /sysroot/dev


# 挂载NFS服务器192.168.1.100上的/exported/share目录到本地的/mnt/nfs_share目录：
sudo mount -t nfs <服务器IP或主机名>:<远程目录> <本地挂载点>
sudo mount -t nfs 192.168.1.100:/exported/share /mnt/nfs_share

# 添加到/etc/fstab文件中自动挂载
192.168.1.100:/exported/share /mnt/nfs_share nfs defaults 0 0

# 使用mount命令将镜像文件挂载为loop设备：
sudo mount -o loop /path/to/imagefile.iso /mnt


# /etc/fstab 文件格式
<file system> <mount point> <type> <options> <dump> <pass>

<file system>：设备名称或UUID，通常是磁盘分区、LVM逻辑卷、网络文件系统路径、或者swap文件。
<mount point>：挂载点，表示设备将被挂载到的目录。如果是swap分区或文件，这个字段应为 none。
<type>：文件系统类型。常见类型包括 ext4、xfs、vfat、ntfs、swap、nfs 等
<options>：挂载选项，逗号分隔。常见选项包括 defaults、ro（只读）、rw（读写）、noexec（不允许执行）、nosuid（不允许set-user-ID或set-group-ID）、nodev（不解译字符或块设备）、noatime（不更新访问时间）等。
<dump>：dump字段用于指定是否使用dump程序对文件系统进行备份。dump是一个传统的UNIX备份工具，它可以创建文件系统的备份。虽然在现代Linux系统中使用dump进行备份的情况较少，但该字段仍然存在于/etc/fstab文件中。0：不需要备份。1：需要备份。
<pass>：指定文件系统在系统启动时是否需要进行一致性检查以及检查的顺序。
	0：不检查。表示该文件系统在启动时不需要进行一致性检查。通常用于虚拟文件系统（如proc、sysfs）或不需要检查的挂载点（如网络文件系统）。
	1：首先检查。通常只为根文件系统（/）指定这个值，以确保根文件系统在其他文件系统之前被检查和修复。
	2：检查顺序在根文件系统之后。对其他非根文件系统进行检查。可以为多个文件系统指定这个值，检查顺序按照它们在/etc/fstab文件中的出现顺序进行。

instance:
UUID=323e4567-e89b-12d3-a456-426614174002 /var            xfs     defaults          1       2
/dev/mapper/rhel-swap   swap                    swap    defaults        0 0
   """
    print(mount_cmd) 


def print_ascii_cmd():
    print("ASCII  Overview:")
    ascii_cmd = """
  ##########################################################################
  #American Standard Code for Information Interchange，美国信息交换标准代码#
  ##########################################################################

			ASCII控制字符（共33个）
 Binary		Dec	Hex	缩写	表示法   名称／意义
0000 0000	0	00	NUL	^@	空字符（Null）
0000 0001	1	01	SOH	^A	标题开始
0000 0010	2	02	STX	^B	本文开始
0000 0011	3	03	ETX	^C	本文结束
0000 0100	4	04	EOT	^D	传输结束
0000 0101	5	05	ENQ	^E	请求
0000 0110	6	06	ACK	^F	确认回应
0000 0111	7	07	BEL	^G	响铃
0000 1000	8	08	BS 	^H	退格
0000 1001	9	09	HT 	^I	水平定位符号
0000 1010	10	0A	LF 	^J	换行键
0000 1011	11	0B	VT 	^K	垂直定位符号
0000 1100	12	0C	FF 	^L	换页键
0000 1101	13	0D	CR 	^M	CR (字符)
0000 1110	14	0E	SO 	^N	取消变换（Shift out）
0000 1111	15	0F	SI 	^O	启用变换（Shift in）
0001 0000	16	10	DLE	^P	跳出数据通讯
0001 0001	17	11	DC1	^Q	设备控制一（XON 激活软件速度控制）
0001 0010	18	12	DC2	^R	设备控制二
0001 0011	19	13	DC3	^S	设备控制三（XOFF 停用软件速度控制）
0001 0100	20	14	DC4	^T	设备控制四
0001 0101	21	15	NAK	^U	确认失败回应
0001 0110	22	16	SYN	^V	同步用暂停
0001 0111	23	17	ETB	^W	区块传输结束
0001 1000	24	18	CAN	^X	取消
0001 1001	25	19	EM 	^Y	连线介质中断
0001 1010	26	1A	SUB	^Z	替换
0001 1011	27	1B	ESC	^[	退出键
0001 1100	28	1C	FS 	^\	文件分割符
0001 1101	29	1D	GS 	^]	组群分隔符
0001 1110	30	1E	RS 	^^	记录分隔符
0001 1111	31	1F	US 	^_	单元分隔符
0111 1111	127	7F	DEL	^?	Delete字符

					ASCII可显示字符（共95个）
  Binary	Dec	Hex	Glyph	  Binary	Dec	Hex	Glyph    Binary		Dec	Hex	Glyph
0010 0000	32	20	(space)	0100 0000	64	40	@	0110 0000	96	60	`
0010 0001	33	21	!	0100 0001	65	41	A	0110 0001	97	61	a
0010 0010	34	22	"	0100 0010	66	42	B	0110 0010	98	62	b
0010 0011	35	23	#	0100 0011	67	43	C	0110 0011	99	63	c
0010 0100	36	24	$	0100 0100	68	44	D	0110 0100	100	64	d
0010 0101	37	25	%	0100 0101	69	45	E	0110 0101	101	65	e
0010 0110	38	26	&	0100 0110	70	46	F	0110 0110	102	66	f
0010 0111	39	27	'	0100 0111	71	47	G	0110 0111	103	67	g
0010 1000	40	28	(	0100 1000	72	48	H	0110 1000	104	68	h
0010 1001	41	29	)	0100 1001	73	49	I	0110 1001	105	69	i
0010 1010	42	2A	*	0100 1010	74	4A	J	0110 1010	106	6A	j
0010 1011	43	2B	+	0100 1011	75	4B	K	0110 1011	107	6B	k
0010 1100	44	2C	,	0100 1100	76	4C	L	0110 1100	108	6C	l
0010 1101	45	2D	-	0100 1101	77	4D	M	0110 1101	109	6D	m
0010 1110	46	2E	.	0100 1110	78	4E	N	0110 1110	110	6E	n
0010 1111	47	2F	/	0100 1111	79	4F	O	0110 1111	111	6F	o
0011 0000	48	30	0	0101 0000	80	50	P	0111 0000	112	70	p
0011 0001	49	31	1	0101 0001	81	51	Q	0111 0001	113	71	q
0011 0010	50	32	2	0101 0010	82	52	R	0111 0010	114	72	r
0011 0011	51	33	3	0101 0011	83	53	S	0111 0011	115	73	s
0011 0100	52	34	4	0101 0100	84	54	T	0111 0100	116	74	t
0011 0101	53	35	5	0101 0101	85	55	U	0111 0101	117	75	u
0011 0110	54	36	6	0101 0110	86	56	V	0111 0110	118	76	v
0011 0111	55	37	7	0101 0111	87	57	W	0111 0111	119	77	w
0011 1000	56	38	8	0101 1000	88	58	X	0111 1000	120	78	x
0011 1001	57	39	9	0101 1001	89	59	Y	0111 1001	121	79	y
0011 1010	58	3A	:	0101 1010	90	5A	Z	0111 1010	122	7A	z
0011 1011	59	3B	;	0101 1011	91	5B	[	0111 1011	123	7B	{
0011 1100	60	3C	<	0101 1100	92	5C	\	0111 1100	124	7C	|
0011 1101	61	3D	=	0101 1101	93	5D	]	0111 1101	125	7D	}
0011 1110	62	3E	>	0101 1110	94	5E	^	0111 1110	126	7E	~
0011 1111	63	3F	?	0101 1111	95	5F	_	
   """
    print(ascii_cmd) 


def print_chntpw_cmd():
    chntpw_cmd = """
yum install ntfe-3g -y
	wget https://tuxera.com/opensource/ntfs-3g_ntfsprogs-2017.3.23.tgz
	tar -zxf ntfs-3g_ntfsprogs-2017.3.23.tgz
	cd ntfs-3g_ntfsprogs-2017.3.23
	./configure make&&make install 

wget http://li.nux.ro/download/nux/dextop/el7/x86_64//chntpw-0.99.6-22.110511.el7.nux.x86_64.rpm
rpm -ivh chntpw-0.99.6-22.110511.el7.nux.x86_64.rpm
mkdir /win
mount -t ntfs-3g /dev/vdb2 /win
cd /win/Windows/System32/config/
cp SAM{,.bak}
chntpw SAM 
	Select: [q] > 1
	Write hive files? (y/n) [n] : y

nova volume-attach centos系统的id win系统盘ID
nova volume-detach centos系统的id win系统盘id
   """
    print(chntpw_cmd) 

def print_time_cmd():
    print("time usage command:")
    time_cmd = """
timedatectl set-timezone Asia/Shanghai
   """
    print(time_cmd) 

def print_newline_cmd():
    print("换行符简介:")
    newline_cmd = """
Linux的换行符是 \\n ，它的ASCII码值是10
Windows系统的换行符 \\r\\n ，Windows使用回车符（\\r，ASCII值13）和换行符（\\n）的组合来表示行结束

例子：
\\n：表示换行符。
\\t：表示制表符（tab）。
\\\：表示实际的反斜杠字符 \。

# Windows文本文件转换成Linux文本文件
sed -i 's/\\r$//' windowsfile.txt
   """
    print(newline_cmd) 

def print_regularExp_cmd():
    print("正则表达式示例:")
    regularExp_cmd = """
		  	    ######################
			    # Regular Expression #
			    ######################


以下是一些常用的正则表达式模式，它们可以用于各种常见的字符串匹配和操作：

#####################################基本匹配################################
^[a-zA-Z0-9_]+$：匹配由字母、数字或下划线组成的字符串。
^\d+$：匹配由数字组成的字符串。

#####################################邮箱地址################################
\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b：匹配大多数电子邮件地址。

#####################################电话号码################################
^\+?\d{10,13}$：匹配国际电话号码，包括国家代码。
(?:\d{3}-)?\d{3}-\d{4}：匹配美国电话号码格式（123-456-7890）。

#####################################日期和时间################################
\d{4}-\d{2}-\d{2}：匹配 YYYY-MM-DD 格式的日期。
\d{2}:\d{2}:\d{2}：匹配 HH:MM:SS 格式的时间。

#####################################IPv4地址################################
^(?:\d{1,3}\.){3}\d{1,3}$

#####################################匹配 HTTP 或 HTTPS URL################################
https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)

#####################################HTML标签################################
<[^>]+>：匹配 HTML 标签。

#####################################特殊字符################################
[^\w\s]：匹配任何非字母数字字符或空白字符。

#####################################字符串开头和结尾################################
^\w+：匹配字符串开头的一个或多个单词字符。
\w+$：匹配字符串结尾的一个或多个单词字符。

#####################################空白字符################################
\s+：匹配一个或多个空白字符（包括空格、制表符、换行符等）。


   """
    print(regularExp_cmd) 

def print_nfs_cmd():
    print("nfs build cookbook")
    nfs_cmd = """

		  	    ##################
			    # NFS 搭建和挂载 #
			    ##################


在CentOS上搭建网络文件系统（NFS），并让客户端进行挂载，具体步骤如下：

#####################################服务器端操作################################


1、安装NFS服务器软件包： 执行以下命令安装NFS服务：
sudo yum install nfs-utils -y


2、启动并启用NFS服务： 运行以下命令来启动NFS服务，并配置为开机自动启动：
sudo systemctl start nfs-server
sudo systemctl enable nfs-server


3、创建NFS共享目录： 假设要共享的目录为/mnt/nfs_share，创建该目录并配置相应的权限：
sudo mkdir -p /mnt/nfs_share
sudo chown -R nfsnobody:nfsnobody /mnt/nfs_share
sudo chmod 755 /mnt/nfs_share


4、编辑NFS配置文件： 编辑/etc/exports文件，添加共享目录的配置。假设允许客户端IP范围192.168.2.0/24进行挂载：
sudo nano /etc/exports
添加如下行：
/mnt/nfs_share 192.168.2.0/24(rw,sync,no_root_squash,no_subtree_check)
	参数说明：
	rw：读写权限。
	sync：同步写入数据。
	no_root_squash：允许客户端的root用户拥有root权限。
	no_subtree_check：不检查子目录。


5、导出共享目录： 保存并关闭文件后，运行以下命令使更改生效：
sudo exportfs -r


6、配置防火墙： 允许NFS服务通过防火墙（如果防火墙处于启用状态）：
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --reload

#####################################客户端操作################################


1、安装NFS客户端软件包： 在客户端安装NFS客户端工具：
sudo yum install nfs-utils -y


2、创建挂载目录： 创建本地用于挂载NFS共享目录的挂载点：
sudo mkdir -p /mnt/nfs_client


3、挂载NFS共享目录： 使用以下命令将NFS服务器上的共享目录挂载到本地挂载点，假设NFS服务器IP为192.168.2.1：
sudo mount 192.168.2.1:/mnt/nfs_share /mnt/nfs_client


4、验证挂载： 使用df -h命令查看是否挂载成功：
df -h

#####################################配置开机自动挂载################################

1、如果需要在客户端机器开机时自动挂载NFS共享目录，可以编辑/etc/fstab文件。

2、编辑/etc/fstab文件：
sudo nano /etc/fstab

3、添加如下行：
192.168.2.1:/mnt/nfs_share /mnt/nfs_client nfs defaults 0 0

4、保存并关闭文件后，运行以下命令来测试挂载：
sudo mount -a

   """
    print(nfs_cmd) 

def print_kdump_cmd():
    print("kdump usage command:")
    kdump_cmd = """
# 测试kdump服务及配置是否真正生效
echo c > /proc/sysrq-trigger
# 如果kdump配置正确/var/crash目录下产生新的文件

wget http://debuginfo.centos.org/7/x86_64/kernel-debuginfo-common-x86_64-`uname -r`.rpm
wget http://debuginfo.centos.org/7/x86_64/kernel-debuginfo-`uname -r`.rpm
rpm -ivh kernel-debuginfo*.rpm
rpm -ql kernel-debuginfo | grep vmlinux
yum install crash
crash /usr/lib/debug/lib/modules/3.10.0-1160.el7.x86_64/vmlinux /var/crash/127.0.0.1-2023-01-09-16\:16\:49/vmcore
   """
    print(kdump_cmd) 

def print_losetup_cmd():
    print("losetup usage command:")
    losetup_cmd = """
# 创建环回设备并将 disk.img 文件关联上去：
losetup -fP disk.img


# 查找设备名称。使用 losetup 确认设备分配情况：
losetup -l | grep disk.img


# 挂载分区：
mkdir /mnt/disk_img1
mount /dev/loop0p1 /mnt/disk_img1
# 按此方法可以依次挂载 /dev/loop0p2 和 /dev/loop0p3：


# 卸载和清理（完成挂载后）：
umount /mnt/disk_img1
umount /mnt/disk_img2
umount /mnt/disk_img3
losetup -d /dev/loop0


# 释放所有环回设备
losetup -D
   """
    print(losetup_cmd) 

def print_trace_cmd():
    print("trace usage command:")
    trace_cmd = """
##############################常用的网络跟踪指令##################################


# tracepath：适合普通用户快速检查路径，能自动探测 MTU，输出简洁。
# traceroute：更适合网络管理员进行详细排查，可选多种协议（如 ICMP、UDP、TCP），输出更丰富。
# mtr（My Traceroute）结合了 ping 和 traceroute 的功能，能动态更新丢包率和 RTT

			  
# The default probes method is udp
traceroute 39.156.66.10

# Use ICMP ECHO for probes
sudo traceroute -I 39.156.66.10

# Use TCP SYN for probes
sudo traceroute -T 39.156.66.10

# Only support UDP probes in Linux
tracepath 39.156.66.10

# 默认情况下，它会持续发送数据包并更新网络路径信息
mtr 39.156.66.10
# 输出字段说明：
	Loss%：该跳的丢包率
	Snt：发送的探测包数量
	Last：最近一次探测的延迟（ms）
	Avg：平均延迟（ms）
	Best：最低延迟（ms）
	Wrst：最高延迟（ms）
	StDev：延迟的标准偏差（抖动）
	
# 只发送 10 组探测包后自动退出（默认是无限运行）
mtr -c 10 example.com

# 以 traceroute 样式一次性输出完整结果，不动态更新
mtr -r example.com

# 以 JSON 方式输出
mtr -j example.com

# 指定协议 icmp(default)、udp、tcp
mtr example.com
mtr -u example.com
mtr -T example.com
   """
    print(trace_cmd) 

def print_lvm_cmd():
    print("lvm usage command:")
    lvm_cmd = """
##############################lvm扩容方法##################################

创建物理卷--->扩容卷组--->扩容逻辑卷--->扩容文件系统


# 给新磁盘分区
fdisk /dev/vdb

# 创建pv物理卷
pvcreate /dev/vdb1

# 查看新创建的物理卷
pvdisplay

# 查看VG
vgdisplay

# 扩展VG
vgextend cl /dev/vdb1

# 查看VG
vgdisplay

# 查看LV
lvs

# 扩展LV
lvextend -L +19G /dev/cl/root

# 扩容逻辑卷的文件系统
xfs_growfs /dev/cl/root
resize2fs /dev/cl/root
   """
    print(lvm_cmd) 

