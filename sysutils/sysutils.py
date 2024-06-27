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

