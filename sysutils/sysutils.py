#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_ip_cmd():
    print("ip usage command:")
    ip_cmd = """
ip -n
   """
    print(ip_cmd)   

def print_bond_cmd():
    print("bond usage command:")
    ip_bond = """
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
iptables -L
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
   """
    print(find_cmd)   

