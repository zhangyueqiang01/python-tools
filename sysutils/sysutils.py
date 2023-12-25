#!/usr/bin/python
# -*- coding: utf-8 -*-

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

def print_ip_cmd():
    print("ip usage command:")
    ip_cmd = """
ip -n
   """
    print(ip_cmd)   

