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
    print("iptables command usage:")
    iptables_cmd = """
############################## basic command ######################################

# 查看所有 iptables 策略
iptables -L

# 显示详细信息（如命中次数、字节数等）。
Iptables -L -v

# 拒绝所有 ICMP 协议数据包
iptables -I INPUT -p icmp -j REJECT

# 拒绝所有 ICMP 协议数据包等同与,但是上一条指令不是直接修改的以下这个文件
echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all

# 只允许管理员从 202.13.0.0/16 网段使用 SSH 远程登录
iptables -A INPUT -p tcp --dport 22 -s 202.13.0.0/16 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP

# 删除 INPUT 中的第二条策略
iptables -D INPUT 2           

# 删除所有策略，慎用
iptables -F                 

# 备份iptabes rules（一次性备份所有表（filter、nat、mangle、raw、security））
iptables-save > /root/iptables_backup_$(date +%F).rules

# 恢复iptables rules
iptables-restore < ./iptables.bak 

# 保存iptables
yum install iptables-services
service  iptables save
systemctl enable iptables.service
# 其实是将策略写入到了/etc/sysconfig/iptables文件中

 
############################## NAT表相关指令 ######################################

# 配置所有发往 192.168.2.4 的icmp流量，都转发给 192.168.2.5。
iptables -t nat -A PREROUTING -d 192.168.2.4 -p icmp -j DNAT --to-destination 192.168.2.5

# 配置让192.168.2.5收到icmp发给原始的192.168.2.4，然后192.168.2.4再回给客户端
iptables -t nat -A POSTROUTING -d 192.168.2.5 -p icmp -j SNAT --to-source 192.168.2.4

# 内核必须开启 IP 转发
echo 1 > /proc/sys/net/ipv4/ip_forward
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sysctl -p

# 查看NAT 表中的所有规则
iptables -t nat -L -n -v
	-t nat：指定查看 NAT 表（默认是 filter 表）。
	-L：列出规则。
	-n：不解析域名和端口，加快显示速度。
	-v：显示详细信息（如命中次数、字节数等）。

# 清空 NAT 表中的所有规则
iptables -t nat -F

# nat 表的规则保存与恢复依旧通过iptables-save iptables-restore即可，无单独指令


############################## cuation ######################################

# 在一些现代的Linux发行版中，可能使用了firewalld、ufw（Uncomplicated Firewall）等防火墙管理工具。但是在这些
# 系统中底层使用的依旧是iptables，熟悉iptables命令就可以避免学习重复性的知识
   """
    print(iptables_cmd)

def print_tcpdump_cmd():
    print("tcpdump usage command:")
    tcpdump_cmd = """
############################## 常见选项 ######################################

-i 指定从哪个接口抓包
-w 将抓包信息保存到文件中
-r 从抓取的包中读取抓包内容
-n 不转换主机名，看到的是 IP ，而不是主机名 
-nn 不转换主机名和协议名
-c 指定抓包的数量
-e 打印二层信息，查看vlan，vxlan等常用
-p 忽略端口的混杂模式，如果端口是混杂模式，只抓取端口ip的报文，别的报文不抓取
-vv 展示抓包详情
-vvv 展示更详细的抓包内容

############################## instance ######################################

# 只抓取 eth1 接口上的 icmp 报文
tcpdump -i eth1 icmp 

# 抓取 virbr1 接口上所有 udp 80 的报文直接打印到屏幕
tcpdump -i virbr1 udp port 80 

# 抓取所有接口
tcpdump -i any

# 抓取指定接口
tcpdump -i virbr1

# tcp 和 udp 80端口
tcpdump -i virbr1 port 80 

tcpdump -i virbr1 tcp port 80 
tcpdump -i virbr1 udp port 80 

# 抓取 virbr1 接口上所有 tcp 80 的报文并另存到 /tmp/ 目录下
tcpdump -i virbr1 tcp port 80 -w /tmp/http.cap

# 抓取主机上所有与 8.8.8.8 通信的报文
tcpdump -i any host 8.8.8.8 

# 不进行ip地址到主机名的转换
tcpdump  -i any host 8.8.8.8  -n

############################## caution ######################################

# 如果抓包发现没有ping的应答报文，可检查此文件，“1”代表忽略所有 ICMP 回显请求，“0代表”不忽略
cat /proc/sys/net/ipv4/icmp_echo_ignore_all

# 如果云主机网络异常的话的话，还可以查看控制台网卡的原目的功能是否开启，可以关闭进行测试

# VXLAN 流量是封装过的，tcpdump 只会看到 外层的 UDP 包，如果你想分析 内部的以太网
帧、IP、ARP 等，建议用 Wireshark 打开 .pcap 文件，它能解析 VXLAN 封装。

tcpdump -i <interface> udp port 4789 -vv -n -s 0 -w vxlan.pcap
	-s 0：抓取完整报文（否则默认只抓一部分）
	udp port 4789：VXLAN 使用的 UDP 端口，抓的就是它
	
部分 Linux 系统上的 tcpdump（可能支持 VXLAN 协议解码
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
        G   跳转至文件尾
        g   跳转至文件首
	$   跳转至行尾
	^   跳转至行首
        dw  删至词尾
        ndw 删除后n个词
        d$  删至行尾
        nd$ 删除后n行（从光标当前处开始算起）        
        u   撤销上一次修改
        U   撤销一行内的所有修改
	多行同时添加空格的方法    Ctrl + v ---> 上下箭头选中 ---> Shift + i ---> 空格 ---> Esc

末行模式
        :r /etc/passwd  读文件内容进vim
        :r! ls -l / 读命令结果保存到文件中
        :set number 显示行号
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
    bash_cmd = """
############################## 控制台的快捷键 ######################################
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

############################## 内部命令 VS 外部命令 ######################################

查看是内部命令还是外部命令
	type  cd
	type  yum

如果 pwd 是 Bash 内建命令：
	直接在 Shell 进程中调用 getcwd() 系统调用获取当前目录路径，并打印结果，不创建新进程。

如果 pwd 是外部命令，Shell 需要创建一个新进程来执行：	
	调用 fork()：	
		Bash 使用 fork() 系统调用创建一个子进程，这个子进程是 Shell 的副本。	
	调用 execve()：	
		在子进程中，Bash 使用 execve() 执行 /bin/pwd 可执行文件，替换子进程的内容为 pwd 的程序代码。	
	进程调度：	
		Linux 内核调度 pwd 进程运行，打印当前工作目录。	
	进程结束：	
		pwd 运行完毕后，调用 exit() 退出，Shell 通过 wait() 回收子进程。

bash -c 'pwd'  		# 使用 Shell 内建命令，不会创建子进程
bash -c '/bin/pwd'  # 创建子进程执行 /bin/pwd

strace -e execve bash -c 'pwd'
# 只会看到 execve("/usr/bin/bash", ["bash", "-c", "pwd"], ...)

strace -e execve bash -c '/bin/pwd' 
# 会看到额外的 execve("/bin/pwd", ...)


# 总结
Bash 内建 pwd：	直接在 Shell 进程中执行，不创建子进程。
外部 pwd（如 /bin/pwd）：	Shell 先 fork() 生成子进程，再 execve() 执行 /bin/pwd，最终 exit() 退出。


############################## tips ######################################

# bash 下进程是如何运行的：
mytool.py --show shell

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
    gpt_cmd = """
############################## DESCRIPTION ##################################

parted 是 Linux 下用于磁盘分区管理的命令行工具，支持 GPT 和 MBR 分区表格式。相比传统的 
fdisk，parted 支持更大的磁盘并具有图形界面（gparted 是其 GUI 版）。

############################### option ####################################

基本语法：
parted [设备路径] [命令] [参数]

| 命令         | 作用                        
| ------------ | -------------------------
| `print`      | 显示当前磁盘的分区表
| `mklabel`    | 创建新的分区表（如 `gpt`, `msdos`） 
| `mkpart`     | 创建新分区
| `rm`         | 删除一个分区
| `resizepart` | 调整某个分区的大小
| `help`       | 查看所有指令的帮助信息
| `quit`       | 退出 parted 工具

############################### instance ####################################
使用 parted 创建两个分区（10G + 剩余空间）

sudo parted /dev/sdX
(parted) print
(parted) mklabel gpt           # 如果是新磁盘或需要 GPT
(parted) mkpart primary 1MiB 10GiB
(parted) mkpart primary xfs 1MB 10G		# 可以指定文件系统，也可以不指定，只是起标记的作用；单位可以是GB也可以是GiB（MB同理）
	1MiB 是起始位置（从 1MB 开始，避免对齐问题）。
	10GiB 是结束位置（100GB）。
(parted) mkpart primary 10GiB 100%		# 100% 代表从10GB开始使用剩下的所有空间
(parted) print
Number  Start   End     Size    File system  Name     Flags
 1      1049kB  10.0GB  9999MB               primary
 2      10.7GB  21.5GB  10.7GB               primary
(parted) quit

sudo mkfs.ext4 /dev/sdX1
sudo mkfs.xfs /dev/sdX2

sudo mkdir /mnt/part1 /mnt/part2
sudo mount /dev/sdX1 /mnt/part1
sudo mount /dev/sdX2 /mnt/part2

############################### caution ####################################
1、确保选择正确的磁盘（/dev/sdX），否则可能导致数据丢失！
2、如果磁盘已有数据，建议先备份。
3、对齐问题：1MiB 起始位置确保 4K 对齐，适合 SSD 和现代硬盘。
4、GPT vs MBR：
  如果磁盘 >2TB，必须使用 GPT（parted 默认使用 GPT）。
  如果磁盘 ≤2TB 且需要 MBR，可以在 parted 中运行 mklabel msdos（但会清除所有分区！）。
   """
    print(gpt_cmd) 

def print_iostat_cmd():
    iostat_cmd = """
########################## DESCRIPTION ####################################

iostat [options] [interval [count]]
    interval：每隔多少秒输出一次。
    count：输出几次。

| 选项          | 含义说明                           
| ------------- | ------------------------------
| `-c`          | 仅显示 CPU 利用率信息
| `-d`          | 仅显示设备（磁盘）I/O 信息
| `-x`          | 显示扩展的设备统计信息（详细）
| `-k`          | 以 KB 为单位显示（默认是 KB）
| `-m`          | 以 MB 为单位显示
| `-t`          | 显示时间戳
| `-p [device]` | 显示指定设备的统计信息及其所有分区信息，如：`-p sda`
| `-N`          | 显示设备名称（如有别名，会显示真实名称）
| `-h`          | 以更人性化方式显示单位（KB、MB、GB 等）


########################## instance ######################################

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

########################## REPORTS ######################################

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
%util：磁盘 I/O 使用率，即”磁盘忙碌时间 / 时间间隔长度 × 100%“
dm-0： 表示 Device Mapper 设备 0，它并不是一个真实的硬件设备，而是 Linux 中通过内核的 Device Mapper 机制抽象出来的逻辑设备
	通过 ll /dev/mapper/ 可进行查看
	通过 -N 选项可以将 dm-0 转换成设备真实的名称


`avg-cpu` 部分展示了 CPU 使用情况的平均值，这些值是基于 `iostat` 命令指定的时间间隔内所有 CPU 的总体表现。下面是每个参数的说明：
- `%user`：显示在用户空间（应用程序）运行的进程所占用的 CPU 百分比时间。这包括常规用户进程和应用程序的执行时间。如果这个值很高，说明系统正在积极地处理应用程序的任务。
- `%nice`：显示运行在较低优先级（通过 `nice` 值调整）的进程所占用的 CPU 百分比时间。如果这个值很高，说明系统正在执行很多被调整为较低优先级的任务。
- `%system`：显示在内核空间运行的进程所占用的 CPU 百分比时间。这包括系统调用和内核进程的执行时间。如果这个值很高，说明系统可能在处理大量的系统调用或内核级别的任务。
- `%iowait`：显示 CPU 等待 I/O 完成的百分比时间。这个值高表示 CPU 经常在等待磁盘 I/O 操作完成，可能是 I/O 子系统成为性能瓶颈的迹象。
- `%steal`：在虚拟化环境中，这个值显示被虚拟机管理器（如 hypervisor）偷走的 CPU 时间百分比。当物理 CPU 被其他虚拟机使用时，这个值会升高。
- `%idle`：显示 CPU 空闲时间的百分比。如果这个值很高，说明 CPU 很少被使用，系统可能比较空闲或者 CPU 资源充足。如果这个值很低，说明 CPU 非常繁忙，系统可能需要更多的 CPU 资源来处理负载。

########################## caution ######################################

本指令的数据采集来源是 /proc/diskstats 文件

在 iostat 中，默认不会显示每个磁盘分区（如 /dev/sda1, /dev/sda2）的 I/O 情况,若查看具体的分区io情况，可用如下方法：
	iostat -x -p sda

磁盘io相关troubleshooting:
     ./mytool.py --show diskio
     ./mytool.py --show iotop
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
    iotop_cmd = """
########################## DESCRIPTION ####################################

iotop 是Linux系统上一个用来监视磁盘I/O使用状况的命令行工具，它以类似 top 命令的界面显示进程的磁盘读写情况。
iotop 需要管理员权限才能运行，因为它需要访问到 /proc 文件系统中的敏感信息。

| 选项      | 全写形式      | 说明
| --------- | ------------- | ---------------------------------------------
| `-o`      | `--only`      | **仅显示有 I/O 活动的进程**，更简洁。
| `-b`      | `--batch`     | **非交互模式**，适合重定向输出到文件或脚本中。
| `-n NUM`  | `--iter=NUM`  | **执行 NUM 次后退出**，常与 `-b` 配合使用。
| `-d SEC`  | `--delay=SEC` | 每 SEC 秒刷新一次（默认 1 秒）。
| `-p PID`  | `--pid=PID`   | 只监控特定的进程 ID。
| `-u USER` | `--user=USER` | 只显示指定用户的进程。
| `-k`      | `--kilobytes` | 显示单位改为 KB/s（默认是显示为 KB/s，但某些版本中默认可能为 Bytes/s）。
| `-t`      | `--time`      | 在非交互模式下显示时间戳。

**使用 `iotop` 的交互命令**：
     - `q`：退出 `iotop`。
     - `o`：改变排序方式，在进程和总I/O之间切换。
     - `a`：使用所有进程，而不是仅限于当前线程。
     - `r`：反向排序，默认情况下，iotop 是根据进程的磁盘写速度进行排序的。
     - `P`：只显示进程，不显示线程。
     - `1`：在进程和线程之间切换。

########################## instance ######################################

[root@node07 ~]# sudo iotop -b 
Total DISK READ :       0.00 B/s | Total DISK WRITE :       0.00 B/s
Actual DISK READ:       0.00 B/s | Actual DISK WRITE:       0.00 B/s
  TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN      IO    COMMAND
    1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd --switched-root --system --deserialize 21
    2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
    3 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [ksoftirqd/0]

# iotop 以非交互方式每2秒刷新一次，总共刷新5次
sudo iotop -b -d 2 -n 5

# iotop 以非交互方式每2秒刷新一次，总共刷新5次，查看进程的IO使用情况，默认是线程。
sudo iotop -b -d 2 -n 5 -P

########################## 输出内容解读 ####################################

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
	 
########################## advance ######################################

找到磁盘读取速度最高的进程
sudo iotop -b -n 1 | grep -v 'Total' | grep -v 'Actual' | awk '{print $12 " "$4}' | sort -nr | head -1

找到磁盘写入速度最高的进程
sudo iotop -b -n 1 | grep -v 'Total' | grep -v 'Actual' | awk '{print $12 " "$6}' | sort -nr | head -1

命令解读：
	sudo iotop -b -n 1：以批处理模式运行 iotop，并且只输出最新的1次数据。
	grep -v 'Total'：使用 grep 过滤掉包含 “Total” 的行。
	grep -v 'Actual'：使用 grep 过滤掉包含 “Actual” 的行。
	awk '{print $12 " "$3}'：使用 awk 打印出进程名称（COMMAND）和磁盘读速度（DISK READ）。
	sort -nr：对读速度进行数值排序，-n 表示按数值排序，-r 表示逆序排序。
	head -1：只输出排序后的第一行，即读速度最高的进程。

磁盘io相关troubleshooting:
    ./mytool.py --show diskio
    ./mytool.py --show iostat
   """
    print(iotop_cmd) 

def print_systemd_cmd():
    systemd_cmd = """
################################################ DESCRIPTION ########################################################

每个服务对应一个 unit 文件，存放在 /etc/systemd/system/ 或 /lib/systemd/system/ 等目录中。unit 文件通常以 .service 结尾，内容类似 ini 格式。

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
   
######################################### systemd 支持的主要 Unit 类型及其扩展名 ######################################

| 类型          | 扩展名       | 用途说明
| ------------- | ------------ | ----------------------------
| **Service**   | `.service`   | 定义系统服务（守护进程），最常用
| **Socket**    | `.socket`    | 定义套接字激活机制，用于按需启动服务
| **Timer**     | `.timer`     | 定义定时任务，类似 cron
| **Target**    | `.target`    | 类似 SysV 的运行级别，聚合多个 Unit
| **Device**    | `.device`    | 绑定设备节点，例如 `/dev/sda`
| **Mount**     | `.mount`     | 定义挂载点，自动挂载文件系统
| **Automount** | `.automount` | 自动挂载机制，与 `.mount` 搭配使用
| **Path**      | `.path`      | 监控某路径的变化，触发服务
| **Scope**     | `.scope`     | systemd 管理的临时进程组，通常由外部工具创建
| **Slice**     | `.slice`     | 控制组（cgroups）资源划分，用于资源隔离
| **Swap**      | `.swap`      | 管理交换分区或交换文件
| **BusName**   | `.busname`   | D-Bus 名称激活服务
| **Import**    | `.import`    | （较少见）用于 systemd-importd 管理镜像
| **Image**     | `.image`     | 与容器映像相关的管理（systemd v249+）

################################################# advance ##########################################################

在 systemd 中，带有 @ 符号的 unit 文件表示 "模板 Unit"（template unit）。这是 systemd 的一种高级机制，用于创建多个基于相同模板、但
具有不同实例名的服务或资源。模板 Unit 是一种 可复用的 unit 文件，其文件名中使用了 @ 占位符，比如：
getty@.service
它并不是一个直接被启动的服务，而是一个模板——你需要通过实例名来启动它，比如：
systemctl start getty@tty1.service
这将基于 getty@.service 模板，启动名为 tty1 的服务实例。

在模板 Unit 文件中，可以使用特殊变量 %i 来表示实例名，常见变量占位符如下：

|占位符| 含义                            
| ---- | ----------------------------- 
| `%i` | 实例名（不包含 `@`）
| `%I` | 实例名（保持原始大小写）
| `%n` | 完整单元名称（如 `myapp@foo.service`）
| `%N` | 不带类型的单元名称（如 `myapp@foo`）
| `%p` | 单元名称的前缀部分（如 `myapp`）
| `%u` | 当前用户（用于 user 单元）


# 列出所有正在运行的 xxx@实例名.service
systemctl list-units 'xxx@*.service'
例如：
systemctl list-units getty@*.service
systemctl list-units *@*.service
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

fdisk -l /dev/vdb
    Disk label type: gpt	# gpt
    Disk label type: dos	# MBR

# 给新磁盘分区
fdisk /dev/vdb	    # MBR 只能用fdisk指令
parted /dev/vdb	    # parted 是通用指令（MBR/GPT都可以）,详情 mytool.py --show parted

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

################################# tips #########################################

# 如果不是逻辑卷，磁盘扩容的空间和根分区的空间并且是连续可以通过以下命令扩充根分区
growpart /dev/vda 1
# 然后再判断文件系统的类型（blkid）通过 xfs_growfs 或 resize2fs 进行扩容
lsblk
df -Th /dev/vda1

################################ caution ########################################
1、如果Linux内核版本低于3.6.0，做完 growpart /dev/vda 1 操作后需要重启操作系统再调整文件系统的大小（resize2fs、xfs_growfs操作）

2、MBR 格式单个分区最大支持2T 的存储空间
   """
    print(lvm_cmd) 

def print_wget_cmd():
    print("wget usage command:")
    wget_cmd = """
##############################wget指令的使用方法##################################

# 基本用法
wget https://example.com/file.zip

# 将文件保存为 myfile.zip
wget -O myfile.zip https://example.com/file.zip

# 后台下载（断开终端仍继续），日志默认写入 wget-log 文件
wget -b https://example.com/largefile.iso

# 限制下载速度为 500 KB/s
wget --limit-rate=500k https://example.com/video.mp4

# 如果上次下载中断，使用 -c 继续下载
wget -c https://example.com/largefile.iso

# 从 urls.txt 读取 URL 并依次下载。
echo "https://example.com/file1.zip" > urls.txt
echo "https://example.com/file2.zip" >> urls.txt
wget -i urls.txt

# 通过代理 192.168.1.1:8080 下载文件
wget -e use_proxy=yes -e http_proxy=192.168.1.1:8080 https://example.com/file.zip

# 如果需要登录才能下载
wget --user=admin --password=123456 https://example.com/protected-file.zip

# 绕过 HTTPS 证书验证错误
# 绕过 SSL 证书验证会导致潜在的安全风险，因为它可能使你下载到伪造或被篡改的文件
wget --no-check-certificate https://self-signed.example.com/file.zip

# 如果网站使用了有效的 SSL 证书，不需要添加 --no-check-certificate选项
# 更新证书颁发机构列表即可
sudo yum install ca-certificates
sudo dnf install ca-certificates
sudo apt-get install --reinstall ca-certificates

# 下载脚本，并用 bash 立即执行
wget -qO script.sh https://example.com/script.sh && bash script.sh
wget -qO- https://example.com/script.sh | bash		//如果 wget 失败，bash 仍会执行一个空输入，可能导致错误，不推荐管道的方法
# 解释：
	-q：安静模式（不输出下载信息）
	-O-：将文件内容直接输出到标准输出（stdout），而不是保存到磁盘
	| bash：通过管道 | 把 wget 下载的内容传给 bash 解释器执行


##############################下载整个网站（镜像下载）##################################

wget -r -np -N -k -p https://example.com/
# 参数说明：
	-r 递归下载
	-np 不下载上级目录的文件
	-N 仅下载更新的文件
	-k 转换 HTML 中的链接，使本地可用
	-p 下载网页所需的所有资源（图片、CSS 等）
   """
    print(wget_cmd) 

def print_chage_cmd():
    print("chage usage command:")
    chage_cmd = """

Linux系统中的root密码（以及所有用户密码）可以设置过期时间，这是Linux密码策略的一部分

############################## 密码过期相关设置 ######################################

/etc/login.defs - 包含默认的密码策略设置
/etc/shadow - 存储实际的密码过期信息
chage命令 - 用于查看和修改用户密码过期设置
passwd命令 - 也可以用于设置密码过期


############################# 相关指令 ######################################

sudo chage -l root
# 查看root密码过期状态
# 或者查看/etc/shadow文件中root用户的条目（第七、八、九字段与过期相关）

sudo chage -M 90 root  
# 设置密码90天后过期

sudo chage -W 7 root   
# 密码过期前7天开始警告

sudo passwd -x 90 root  
# 设置密码90天后过期

sudo chage -M -1 root
sudo passwd -x -1 root
# 以上两个命令都可以让root密码永不过期
# 请注意，保持root密码永不过期可能不符合某些安全策略要求。
   """
    print(chage_cmd) 

def print_elf_cmd():
    elf_cmd = """
############################## DESCRIPTION ##################################

在 Linux 中，**ELF 文件（Executable and Linkable Format，可执行与可链接格式）**是一
种广泛使用的二进制文件格式，用于表示可执行文件、目标代码、共享库以及核心转储文件。Linux 上的
大多数程序（如 /bin/ls、/lib/libc.so 等）都是 ELF 格式的文件。

############################ ELF 文件的类型 ###################################

| 文件类型     | 描述
| ------------ | ----------------
| 可执行文件   | 可以直接运行的程序文件
| 可重定位文件 | 编译后尚未链接的 `.o` 文件
| 共享目标文件 | 动态链接库 `.so` 文件
| 核心转储文件 | 程序崩溃时生成的 core 文件

######################### ELF 文件的结构（逻辑视图） ############################

ELF 文件由多个部分组成，主要包括以下三种表结构：

1. ELF Header（ELF头部）
  描述整个文件的基本信息，比如类型、架构、入口地址等。
  文件的开头 16 字节是 "magic number"，用于标识 ELF 文件。
  更多详细信息请执行：./mytool.py --show elf_header

2. Program Header Table（程序头部表）
  告诉系统如何创建进程的内存映像。
  主要用于运行阶段，比如加载动态库、映射段到内存。
  更多详细信息请执行：./mytool.py --show elf_program_header

3. Section Header Table（节区头部表）
  描述文件中各个节（section）的信息，比如 .text, .data, .bss, .symtab 等。
  主要用于链接阶段，不参与程序运行。
  更多详细信息请执行：./mytool.py --show elf_section_header


########################## 常见节区（Section） ################################

| 节区名称    | 说明
| ----------- | ------------------- 
| `.text`     | 存放代码（只读）
| `.data`     | 已初始化的全局变量
| `.bss`      | 未初始化的全局变量（运行时分配）
| `.rodata`   | 只读数据，比如常量字符串
| `.symtab`   | 符号表（调试或链接用）
| `.strtab`   | 字符串表，保存符号名
| `.rel.text` | 与 `.text` 段相关的重定位信息
| `.debug`    | 调试信息

######################### 查看 ELF 文件信息的常用工具 ##########################

| 工具      | 功能
| --------- | ---------------------
| `file`    | 判断是否是 ELF 文件及其类型
| `readelf` | 显示 ELF 文件的各种表结构（官方工具）
| `objdump` | 查看反汇编、节信息等
| `nm`      | 查看符号表
| `ldd`     | 显示 ELF 文件依赖的共享库
| `strace`  | 跟踪 ELF 程序的系统调用

############################### instance ####################################

$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, ...

$ readelf -h /bin/ls
# 显示 ELF 头信息

$ readelf -S /bin/ls
# 显示节区表

$ objdump -d /bin/ls
# 反汇编代码

########################### Windows 可执行文件 ###############################

在 Windows 系统中，主要使用的二进制文件格式是：PE 文件格式（Portable Executable，可移植可执行格式）
它是 Windows 平台下可执行文件（.exe）、动态链接库（.dll）以及驱动程序（.sys）所采用的标准格式。
   """
    print(elf_cmd) 

def print_elf_header_cmd():
    elf_header_cmd = """
############################## DESCRIPTION ##################################

在 ELF（Executable and Linkable Format） 文件中，**ELF Header（ELF 头部）**是文件
的起始部分，占据固定的 64 字节（在 64 位系统中）或 52 字节（在 32 位系统中）。它是整个 ELF
文件的“身份证”，提供了关于该文件类型、架构、入口地址等关键信息。

######################### ELF Header 的位置与结构定义 ##########################

在 Linux 内核源码中，ELF 头部结构体定义在：

// 32位系统
/usr/include/elf.h: typedef struct {
    ...
} Elf32_Ehdr;

// 64位系统
/usr/include/elf.h: typedef struct {
    ...
} Elf64_Ehdr;


#################### ELF Header 字段详细解释（以 64 位为例） ####################

typedef struct {
    unsigned char e_ident[16];   // 魔数和其他标识
    uint16_t      e_type;        // 文件类型
    uint16_t      e_machine;     // 目标机器架构
    uint32_t      e_version;     // ELF 版本
    uint64_t      e_entry;       // 程序入口地址
    uint64_t      e_phoff;       // 程序头表 (Program Header Table) 的偏移
    uint64_t      e_shoff;       // 节区头表 (Section Header Table) 的偏移
    uint32_t      e_flags;       // 与处理器相关的标志
    uint16_t      e_ehsize;      // ELF Header 的大小（单位：字节）
    uint16_t      e_phentsize;   // 程序头表每项大小
    uint16_t      e_phnum;       // 程序头表项数量
    uint16_t      e_shentsize;   // 节区头表每项大小
    uint16_t      e_shnum;       // 节区头表项数量
    uint16_t      e_shstrndx;    // 字符串表在节区表中的索引
} Elf64_Ehdr;

############################### 各字段说明 ###################################

| 字段          | 含义说明
| ------------- | -------------------------------------------------------------
| `e_ident[16]` | 魔数（0x7F 'E' 'L' 'F'）、位数（32/64）、字节序（小端/大端）等识别信息
| `e_type`      | 文件类型（如可执行文件 `ET_EXEC`，共享库 `ET_DYN`）
| `e_machine`   | 目标架构（如 x86 是 `EM_386`，x86\_64 是 `EM_X86_64`）
| `e_version`   | ELF 版本，通常为 `1`（当前版本）
| `e_entry`     | 程序入口点地址（即运行时从哪开始执行）
| `e_phoff`     | Program Header Table 的偏移位置（从文件头起）
| `e_shoff`     | Section Header Table 的偏移位置
| `e_flags`     | 处理器相关标志，特定架构用
| `e_ehsize`    | ELF Header 的总大小
| `e_phentsize` | 每个程序头表项的大小
| `e_phnum`     | 程序头表中的条目数量
| `e_shentsize` | 每个节区头表项的大小
| `e_shnum`     | 节区头表中的条目数量
| `e_shstrndx`  | 字符串节 `.shstrtab` 在节表中的索引位置

查看 ELF Header 示例:
readelf -h /bin/ls

############################### 作用总结 #####################################

| 功能     | 描述
| -------- | ---------------------------------------------------------------------
| 文件识别 | 通过 `e_ident` 来识别是否是 ELF 格式、是 32 位或 64 位、是否为小端字节序等。
| 程序加载 | 操作系统根据 `e_entry` 找到程序入口地址开始执行；根据 `e_phoff` 找到加载的段。
| 链接处理 | 链接器（如 `ld`）使用节区表（`e_shoff`）进行符号解析、重定位处理等。
   """
    print(elf_header_cmd) 


def print_elf_program_header_cmd():
    elf_program_header_cmd = """
############################## DESCRIPTION ##################################

Program Header Table（PHT） 告诉操作系统或动态链接器如何将 ELF 文件的内容加载到内存中运行。
每一项（叫一个 Program Header）描述了一个段（Segment），而这些段通常是加载到内存中的代码段、数据段、动态链接信息等。
✅ 注意：段（Segment）是运行时概念，而节（Section）是编译和链接时概念。

########################## 结构定义（以 64 位为例） ############################

定义在内核源码 /usr/include/elf.h 中：
typedef struct {
    uint32_t p_type;    // 段类型（决定用途）
    uint32_t p_flags;   // 段权限（rwx）
    uint64_t p_offset;  // 在文件中的偏移
    uint64_t p_vaddr;   // 虚拟地址（内存中）
    uint64_t p_paddr;   // 物理地址（一般忽略）
    uint64_t p_filesz;  // 文件中段的大小
    uint64_t p_memsz;   // 段在内存中的大小
    uint64_t p_align;   // 对齐方式
} Elf64_Phdr;

############################### 字段解释 #####################################

| 字段       | 含义
| ---------- | --------------------------------------
| `p_type`   | 段类型（如 `PT_LOAD` 表示需要加载）
| `p_flags`  | 权限标志，如可读 `R`，可写 `W`，可执行 `X`
| `p_offset` | 文件中偏移位置（从文件头开始）
| `p_vaddr`  | 加载到内存后的虚拟地址
| `p_paddr`  | 物理地址（仅用于嵌入式）
| `p_filesz` | 文件中这段的大小
| `p_memsz`  | 加载后在内存中占用的大小（可包含未初始化部分）
| `p_align`  | 对齐方式（一般为页面大小，0x1000）


常见的 p_type 类型：
| 值           | 含义                               
| ------------ | --------------------------------------- 
| `PT_NULL`    | 忽略条目
| `PT_LOAD`    | 可加载到内存的段（代码/数据段）
| `PT_DYNAMIC` | 动态链接信息
| `PT_INTERP`  | 指向解释器路径（比如 `/lib/ld-linux.so.2`）
| `PT_NOTE`    | 附注信息（core dump）
| `PT_PHDR`    | 包含程序头表的自身信息
| `PT_TLS`     | 线程局部存储段

查看 Program Header 表：
readelf -l /bin/ls
############################### instance ####################################

Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flags  Align
  LOAD           0x000000 0x0000000000400000 0x0000000000400000 0x001000 0x001000 R      0x200000
  LOAD           0x001000 0x0000000000401000 0x0000000000401000 0x002000 0x002000 R E    0x200000
  LOAD           0x003000 0x0000000000403000 0x0000000000403000 0x001000 0x002000 RW     0x200000
解释：
  第一段是只读（R），可能是 ELF 头 + 程序头
  第二段是代码段（R + E）
  第三段是数据段（RW），可能还包括 .bss（未初始化变量）
  
############################### 作用总结 #####################################

| 功能         | 描述
| ------------ | ---------------------------------------------------------------- 
| 加载指导     | 操作系统根据 `PT_LOAD` 项将文件的各段加载进内存
| 动态链接     | 动态链接器根据 `PT_DYNAMIC`, `PT_INTERP` 等执行链接逻辑
| 栈保护等功能 | 有时包含 `GNU_STACK`, `GNU_RELRO` 段做安全加固
| 不依赖节表   | 程序运行时不需要 Section Header Table，只用 Program Header Table 即可运行
   """
    print(elf_program_header_cmd) 

def print_elf_section_header_cmd():
    elf_section_header_cmd = """
############################## DESCRIPTION ##################################

ELF 文件中的 Section Header Table（节区头表），这是 ELF 文件结构中非常重要的一部分，主
要用于链接、重定位、调试等阶段，不直接参与程序运行。

Section VS Segment
Segment（段）：运行时概念，由 Program Header Table 控制，操作系统用它来加载程序。
Section（节）：链接时概念，由 Section Header Table 控制，链接器用它来组织和管理代码、数据、符号等信息。
➤ ELF 文件中常见的 .text, .data, .bss, .symtab, .strtab 都是 section。

########################## 结构定义（以 64 位为例） ############################

在 Linux 内核源码中的头文件 /usr/include/elf.h ，64 位 ELF 定义如下：
typedef struct {
    uint32_t sh_name;       // 节区名称（在字符串表中的偏移）
    uint32_t sh_type;       // 节区类型
    uint64_t sh_flags;      // 节区标志（可执行/可写等）
    uint64_t sh_addr;       // 节区在内存中的地址（可执行文件中有效）
    uint64_t sh_offset;     // 节区在文件中的偏移
    uint64_t sh_size;       // 节区大小（单位：字节）
    uint32_t sh_link;       // 节区间的链接信息（具体含义依类型而异）
    uint32_t sh_info;       // 附加信息（通常是一个索引或数量）
    uint64_t sh_addralign;  // 对齐要求
    uint64_t sh_entsize;    // 若节中包含表格结构，此为每项大小
} Elf64_Shdr;

############################## 主要字段解释 ####################################
| 字段           | 含义
| -------------- | -----------------------------------------------------
| `sh_name`      | 名称在字符串表 `.shstrtab` 中的偏移
| `sh_type`      | 节区类型（如 `SHT_PROGBITS`, `SHT_SYMTAB` 等）
| `sh_flags`     | 权限标志（如 `SHF_WRITE`, `SHF_ALLOC`, `SHF_EXECINSTR`）
| `sh_addr`      | 节区在内存中的地址（仅用于可执行文件）
| `sh_offset`    | 节区在 ELF 文件中的偏移
| `sh_size`      | 节区大小
| `sh_link`      | 链接信息，依类型不同而异
| `sh_info`      | 附加信息，依类型不同而异
| `sh_addralign` | 对齐边界
| `sh_entsize`   | 如果是表格（如符号表），则是每个条目的大小

########################### 常见节区类型（sh_type） ############################
| 类型常量       | 含义                       
| -------------- | ------------------------ 
| `SHT_NULL`     | 保留，不使用
| `SHT_PROGBITS` | 程序数据（如 `.text`, `.data`）
| `SHT_SYMTAB`   | 符号表（静态）
| `SHT_DYNSYM`   | 动态符号表
| `SHT_STRTAB`   | 字符串表
| `SHT_RELA`     | 重定位表（带附加项）
| `SHT_REL`      | 重定位表（不带附加项）
| `SHT_NOBITS`   | 占用内存但不占文件空间（如 `.bss`）

############################ 常见节区（section） ##############################
| 节区名      | 说明                         
| ----------- | ------------------------------- 
| `.text`     | 程序代码段，`SHT_PROGBITS`，`R-X`
| `.data`     | 初始化数据，`SHT_PROGBITS`，`RW-`
| `.bss`      | 未初始化数据，`SHT_NOBITS`，`RW-`
| `.rodata`   | 只读数据，如字符串常量
| `.symtab`   | 静态符号表
| `.strtab`   | 符号名字符串表
| `.shstrtab` | 节区名称字符串表
| `.rel.text` | 针对 `.text` 的重定位表
| `.debug*`   | 调试信息节（GDB 使用）

############################### instance ####################################
readelf -S /bin/ls
There are 29 section headers, starting at offset 0x25b40:
  [Nr] Name      Type            Address          Offset
  [ 0]           NULL            0000000000000000 00000000
  [ 1] .interp   PROGBITS        0000000000000238 00000238
  [ 2] .note.ABI-tag NOTE        0000000000000254 00000254
  [ 3] .text     PROGBITS        0000000000001000 00001000
  ...
  
########################### Section Header 的用途 ############################
| 用途         | 描述
| ------------ | ------------------------------------------------------------- 
| 链接器使用   | 识别符号表、重定位信息、节名等
| 调试器使用   | `.debug_info`, `.symtab`, `.strtab` 提供调试信息
| 静态分析     | 分析代码段、数据段、符号关系
| 并不用于运行 | 加载运行时主要使用 **Program Header Table**，而非 Section Header Table

################# 关联字段回顾：e_shoff, e_shnum, e_shstrndx ##################
| 字段         | 说明
| ------------ | -------------------------------
| `e_shoff`    | Section Header Table 的文件偏移
| `e_shnum`    | 节区表的条目数量
| `e_shstrndx` | `.shstrtab` 字符串表的节索引（即节名表）

############################### 作用总结 #####################################
Section Header Table 是链接器、调试器等工具的主要依据；
每个 Section 描述 ELF 文件中的一个内容单元，如代码、数据、符号等；
程序运行时几乎不使用 Section Header Table，而是依赖 Program Header Table；
利用 readelf -S 可以快速查看 ELF 文件的结构。
   """
    print(elf_section_header_cmd) 

def print_sub_net_cmd():
    sub_net_cmd = """
############################## DESCRIPTION ##################################

在 Linux 中，网卡次要地址（secondary IP address） 和 子接口（sub-interface） 都可以
用来给一个物理网卡分配多个 IP 地址，但它们在配置方式、使用场景和底层机制上有所不同。

############################### 定义 #########################################

网卡次要地址（Secondary IP Address）
  给同一个物理网卡添加多个 IP 地址，这些 IP 地址都属于同一个接口（如 eth0）。
  不区分 VLAN、物理层，只是逻辑上的额外 IP。

子接口（Sub-interface）
  在一个物理网卡上通过“接口别名”或“VLAN 接口”的方式创建逻辑接口，如 eth0:1 或 eth0.100。
  常用于 VLAN 或需要逻辑隔离的网络配置场景。

################################ 配置方式 ####################################

添加次要 IP
  ip addr add 192.168.1.100/24 dev eth0
  ifconfig eth0:1 192.168.1.100 netmask 255.255.255.0 up
  注意：这种 eth0:1 写法其实并不创建真正的“子接口”，只是为了标识方便。

添加子接口（VLAN 子接口）
  ip link add link eth0 name eth0.100 type vlan id 100
  ip addr add 192.168.100.1/24 dev eth0.100
  ip link set eth0.100 up

################################# 路由与隔离 ##################################

次要地址：所有 IP 地址共用一个路由表、MAC 地址。
子接口（如 VLAN 子接口）：虽然共享物理设备，但可有不同 VLAN tag，有独立的逻辑接口名、MAC 地址（可配置）。

######################## 配置文件差异（以 RHEL/CentOS 为例） ####################

主/次地址：
  /etc/sysconfig/network-scripts/ifcfg-eth0
  可用 IPADDR1=... IPADDR2=... 添加多个 IP。

子接口：
  文件名如 ifcfg-eth0.100，内容中指定 VLAN 信息。

################################## 总结 #####################################

| 项目           | 网卡次要地址      | 子接口         
| -------------- | ----------------- | ----------- 
| 本质           | 同一接口多个 IP   | 基于物理接口的逻辑接口 
| 是否 VLAN 支持 | ❌                 | ✅           
| 适用场景       | 多 IP、多网段访问 | VLAN、网络隔离   
| 命令复杂度     | 简单              | 稍复杂         
| 配置文件       | 与主接口共享或独立| 独立文件        


通过 ip a 指令查看：
网卡次要地址
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 74:52:01:01:01:01 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.21/24 brd 192.168.122.255 scope global dynamic eth0
       valid_lft 3582sec preferred_lft 3582sec
    inet 2.2.2.2/8 brd 2.255.255.255 scope global eth0:0
       valid_lft forever preferred_lft forever
    inet6 fe80::7652:1ff:fe01:101/64 scope link 
       valid_lft forever preferred_lft forever

子接口(eth0.10@eth0)
6: eth0.10@eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether 74:52:01:01:01:01 brd ff:ff:ff:ff:ff:ff
    inet 192.168.10.1/24 scope global eth0.10
       valid_lft forever preferred_lft forever
   """
    print(sub_net_cmd) 

def print_selinux_cmd():
    selinux_cmd = """
############################## DESCRIPTION ##################################

SELinux（Security-Enhanced Linux）是由 NSA（美国国家安全局） 开发的一个 Linux 安全子
系统，它提供了强制访问控制（MAC, Mandatory Access Control）机制，用于增强 Linux 系统
的安全性。它最早被集成到 Red Hat Enterprise Linux 和 Fedora 系统中，现在也可用于
 Debian、Ubuntu 等发行版。

########################### SELinux 的基本概念 ################################

1. 访问控制类型比较：
| 类型                                | 说明
| ----------------------------------- | -------------------------------------------------------
| DAC（Discretionary Access Control） | 自主访问控制，Linux 默认使用的访问控制机制，用户可以更改自己拥有文件的权限。
| MAC（Mandatory Access Control）     | 强制访问控制，系统统一策略管理，即使是 root 用户也不能随意访问资源。SELinux 使用的就是 MAC。

2. SELinux 核心思想：
   系统中每个对象（如文件、端口）和主体（如进程）都有一个 安全上下文。
   SELinux 通过策略规则来判断某个进程是否可以访问某个资源。
   安全策略不依赖于传统的 chmod/chown/chgrp。

########################### SELinux 的工作模式 ################################

| 模式           | 描述
| -------------- | -----------------------
| **Enforcing**  | 强制执行 SELinux 策略（默认生产模式）
| **Permissive** | 不拦截违规操作，只记录（用于调试策略）
| **Disabled**   | 禁用 SELinux

查看当前模式：
getenforce

临时切换模式（重启后失效）：
setenforce 0     # 切换为 Permissive
setenforce 1     # 切换为 Enforcing

永久修改（需重启）：
编辑 /etc/selinux/config 文件：
SELINUX=enforcing       # 或者 permissive / disabled

########################### SELinux 安全上下文结构 ############################

一个文件或进程的 SELinux 上下文类似这样：
  -rw-r--r--. root root system_u:object_r:httpd_sys_content_t:s0 index.html
格式：用户:角色:类型:级别
  用户（user）：如 system_u、staff_u、unconfined_u
  角色（role）：如 object_r、system_r
  类型（type）：最重要的一项，如 httpd_t 表示 Apache 进程类型
  级别（level）：一般用于 MLS（多级安全），如 s0，多数情况可忽略

########################### 常用 SELinux 工具命令 #############################

查看文件的 SELinux 上下文
ls -Z filename

修改文件的 SELinux 类型
chcon -t httpd_sys_content_t /var/www/html/index.html

还原默认 SELinux 上下文
restorecon -v /var/www/html/index.html

查看策略允许哪些操作
semanage fcontext -l     # 查看文件路径与类型的匹配关系

查看某个端口是否被允许：
semanage port -l | grep 80

############################ SELinux 日志分析 ################################

SELinux 拒绝操作会记录在 /var/log/audit/audit.log 文件中。
可以使用 ausearch 或 audit2why、audit2allow 工具进行分析和建议：
# 找出最近一次被拒绝的操作
ausearch -m avc -ts recent

# 分析原因
cat /var/log/audit/audit.log | audit2why

# 自动生成允许该操作的 SELinux 策略模块
cat /var/log/audit/audit.log | audit2allow -M mypol
semodule -i mypol.pp

########################### SELinux 常见场景示例 ##############################

1. Apache 无法访问网页目录
可能原因：文件类型不对，应为 httpd_sys_content_t
chcon -t httpd_sys_content_t /var/www/html/index.html

或者设置并持久生效：
semanage fcontext -a -t httpd_sys_content_t "/var/www/html(/.*)?"
restorecon -Rv /var/www/html
   """
    print(selinux_cmd) 

