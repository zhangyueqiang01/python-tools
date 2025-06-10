#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_h3c_cmd():
    print("h3c usage command:")
    h3c_cmd = """
screen-length disable
display alarm
display logbuffer
display current-configuration
display cpu-usage
display memory
display environment
display device verbose
display fan
display power
display clock
display interface brief


# 显示该接口的当前配置
display current-configuration interface Bridge-Aggregation 145

# 显示该接口的实时状态和统计信息。
display interface Bridge-Aggregation 145

# 查看聚合口下有哪些接口
display link-aggregation verbose Bridge-Aggregation 145
   """
    print(h3c_cmd)   

def print_dp_cmd():
    print("dp usage command:")
    dp_cmd = """
terminal line 0
show running-config
show logging syslog recent 100
show cpu-usage
show cf-card usage
show harddisk usage
show memory all
show device
show interface status
show ip interface brief
show ntp status
show board-power
show environment

#查看接口详情
show interface gigabitEthernet 1/0/23

# 看当前时间
show clock

# 看日志闪断频率 
show logging | include 1/0/23
   """
    print(dp_cmd)   

def print_zte_cmd():
    print("zte usage command:")
    zte_cmd = """
terminal length 0
show interface brief
show alarm current
show running-config
show processor
show temperature
show version
show fan
show power

#查看接口详情
show interface gigabitEthernet 1/0/23

# 看当前时间
show clock

# 看日志闪断频率 
show logging | include 1/0/23
   """
    print(zte_cmd)   

def print_huawei1_cmd():
    print("HUAWEI1 usage command:")
    huawei1_cmd = """
【HUAWEI CE5855/CE6851/CE12808S】
    
screen-l 0 temp
display current-configuration
display logbuffer
display alarm active 
display health
display cpu
display memory
display device
display ntp status
display ip fib slot 2 statistics
display ipv6 fib slot 2 statistics
display device power
display history-command 

通过本地的172.18.122.5 ping远端vpc内的地址10.1.92.248
ping -a 172.18.122.5 -vpn-instance DLine24 10.1.92.248

system-view
security-policy
rule name kaifang80
dis this
destination-address  mask 255.255.255.255
undo destination-address  mask 255.255.255.255

# 查看聚合口2下有哪些接口
display interface Eth-Trunk 2

# 显示聚合接3口的当前配置
display current-configuration interface Eth-Trunk 3

# 查看聚合3口下有哪些接口和实时信息
display interface Eth-Trunk 3
   """
    print(huawei1_cmd)   

def print_huawei2_cmd():
    print("HUAWEI2 usage command:")
    huawei2_cmd = """
【HUAWEI NE40/Eudemon1000E/Eudemon8000E】

screen-l 0 temp
display logbuffer
display alarm active 
display health
display cpu-usage
display device
display device ofc-status
display device pic-status
display voltage
display power 
display fan 
display temperature
display memory-usage
display ntp-service status
display users
display fabric fiber status error
display fabric fiber connection error
display interface brief 
display alarm active
display alarm hardware
display bgp peer
display bgp vpnv4 all peer
display bgp vpnv6 all peer
display mpls ldp
display license state
display info-center
display fib slot clc1/1 statistics all
display ipv6 fib slot clc1/1 statistics all
display mpls ldp lsp statistics
   """
    print(huawei2_cmd)   


def print_pnet_cmd():
    print("合营物理网络设备相关命令:")
    pnet_cmd = """
		#####
		#IPS#
		#####

##################流统##################
写规则----->应用规则------>查看规则

实例：
acl number 3000
  description "test"
  rule 5 permit icmp source 192.168.1.1 0 destination 192.168.2.1 0
interface GigabitEthernet 0/0/0
traffic-filter inbound acl 3000
display acl 3000

[Huawei-GigabitEthernet0/0/0]display acl 3000
Advanced ACL 3000, 1 rule
Acl's step is 5
 rule 5 permit icmp source 192.168.1.1 0 destination 192.168.2.1 0 (5 matches)


##################查看会话##################
display firewall session table source global 1.203.115.195



		######
		#NE40#
		######

   """
    print(pnet_cmd) 


def print_iperf_cmd():
    print("iperf usage command:")
    iperf_cmd = """
					########
					#iperf3#
					########

###########################################iper3 VS iperf################################
iPerf: 最初由National Laboratory for Applied Network Research (NLANR)开发，后来不再维护
iPerf3: 由ESnet (Energy Sciences Network)接管并重新开发和维护，增加了许多新功能和改进。
iPerf3在功能、性能、稳定性和可维护性方面都比iPerf有显著的改进和提升。如果你需要进行网络性能测试，建议使用iPerf3。

###########################################启动服务器端##################################
iperf3 -s


###########################################启动客户端#####################################
iperf3 -c <server_ip>

	客户端选项
		-c, --client <host>: 指定服务器IP地址。
		-p, --port <port>: 指定服务器端口（默认5201）。
		-u, --udp: 使用UDP而不是默认的TCP。
		-b, --bandwidth <n>[KMG]: 设置带宽，仅用于UDP模式（例如：-b 10M）。
		-t, --time <n>: 测试时长，单位为秒（默认10秒）。
		-P, --parallel <n>: 使用并行流的数量（例如：-P 4）。
		-R, --reverse: 反向测试模式（服务器向客户端发送数据）。
		-i, --interval <n>: 报告间隔时间，单位为秒（默认1秒）。
		--json: 以JSON格式输出结果。

	服务器端选项
		-s, --server: 启动服务器模式。
		-p, --port <port>: 指定监听端口（默认5201）。
		-1, --one-off: 在一个客户端测试后退出。
	通用选项
		-V, --version: 显示版本信息并退出。
		-h, --help: 显示帮助信息并退出。
		
###########################################示例###########################################

##################基本TCP测试:##############
服务器端：
iperf3 -s
客户端：
[root@docker1 ~]# iperf3 -c 192.168.2.254
Connecting to host 192.168.2.254, port 5201
[  4] local 192.168.2.1 port 48338 connected to 192.168.2.254 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec  5.30 GBytes  45.5 Gbits/sec    0   3.01 MBytes       
[  4]   1.00-2.00   sec  5.84 GBytes  50.1 Gbits/sec    0   3.01 MBytes       
[  4]   2.00-3.00   sec  5.54 GBytes  47.6 Gbits/sec    0   3.01 MBytes       
[  4]   3.00-4.00   sec  5.42 GBytes  46.5 Gbits/sec    0   3.01 MBytes       
[  4]   4.00-5.00   sec  5.52 GBytes  47.4 Gbits/sec    0   3.01 MBytes       
[  4]   5.00-6.00   sec  5.58 GBytes  48.0 Gbits/sec    0   3.01 MBytes       
[  4]   6.00-7.00   sec  5.54 GBytes  47.6 Gbits/sec    0   3.01 MBytes       
[  4]   7.00-8.00   sec  5.65 GBytes  48.5 Gbits/sec    0   3.01 MBytes       
[  4]   8.00-9.00   sec  5.64 GBytes  48.5 Gbits/sec    0   3.01 MBytes       
[  4]   9.00-10.00  sec  5.41 GBytes  46.5 Gbits/sec    0   3.01 MBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  55.4 GBytes  47.6 Gbits/sec    0             sender
[  4]   0.00-10.00  sec  55.4 GBytes  47.6 Gbits/sec                  receiver

每秒传输统计
	[ ID]: 流ID，标识此次测试的会话。
	Interval: 时间间隔（秒）。
	Transfer: 在该时间间隔内传输的数据量。
	Bandwidth: 在该时间间隔内的平均带宽。
	Retr: TCP重传次数（UDP不适用）。
	Cwnd: 拥塞窗口大小（单位为字节），是TCP协议中控制流量的一个参数。
总结统计
	最后三行是统计值，显示的是发送端和接收端的最终的统计平均值



##################UDP测试:##################
服务器端：
iperf3 -s
客户端：
[root@docker1 ~]# iperf3 -c 192.168.2.254 -u -b 10M
Connecting to host 192.168.2.254, port 5201
[  4] local 192.168.2.1 port 53458 connected to 192.168.2.254 port 5201
[ ID] Interval           Transfer     Bandwidth       Total Datagrams
[  4]   0.00-1.00   sec  1.07 MBytes  9.01 Mbits/sec  778  
[  4]   1.00-2.00   sec  1.19 MBytes  10.0 Mbits/sec  863  
[  4]   2.00-3.00   sec  1.19 MBytes  10.0 Mbits/sec  864  
[  4]   3.00-4.00   sec  1.19 MBytes  10.0 Mbits/sec  863  
[  4]   4.00-5.00   sec  1.19 MBytes  10.0 Mbits/sec  863  
[  4]   5.00-6.00   sec  1.19 MBytes  10.0 Mbits/sec  863  
[  4]   6.00-7.00   sec  1.19 MBytes  10.0 Mbits/sec  864  
[  4]   7.00-8.00   sec  1.19 MBytes  9.99 Mbits/sec  863  
[  4]   8.00-9.00   sec  1.19 MBytes  10.0 Mbits/sec  863  
[  4]   9.00-10.00  sec  1.19 MBytes  9.99 Mbits/sec  863  
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Jitter    Lost/Total Datagrams
[  4]   0.00-10.00  sec  11.8 MBytes  9.90 Mbits/sec  0.001 ms  0/8547 (0%)  
[  4] Sent 8547 datagrams

每秒传输统计
	Interval: 时间间隔
	Transfer: 传输的数据量
	Bandwidth: 实际带宽
	Total Datagrams: 传输的数据报数量
总结统计
	Interval: 总时间
	Transfer: 总传输数据量
	Bandwidth: 平均带宽
	Jitter: 抖动，指的是延迟变化，值越小越好
	Lost/Total Datagrams: 丢失的数据报数量和总数据报数量，以及丢包率

	##########################################################
	# 测试带宽用tcp测试即可，用udp进行测试需要指定带宽的大小 #
	# 如果指定的带宽是实际带宽的2倍，那么会造成50%的丢包     #
	##########################################################
   """
    print(iperf_cmd) 

def print_ethtool_cmd():
    print("ethtool usage command:")
    ethtool_cmd = """
#############################查询类操作################################

# 查看ethtool指令的版本
ethtool --version

# 展示网卡设备的标准信息	
ethtool DEVNAME	

# 查询RX/TX ring parameters
ethtool -g|--show-ring DEVNAME

# Show driver information
ethtool -i|--driver DEVNAME	
# 显示设备的诊断信息
ethtool -d|--register-dump DEVNAME	

# dump 寄存器信息
ethtool -d|--register-dump DEVNAME

# dump (Electrically Erasable Programmable Read-Only Memory)网卡电可擦编程只读存储器中的信息
ethtool -e|--eeprom-dump DEVNAME

# 重启网卡的自协商功能
ethtool -r|--negotiate DEVNAME
		
# 让网卡的端口灯进行闪烁
ethtool -p|--identify DEVNAME

# 显示适配器统计信息
ethtool -S|--statistics DEVNAME

# 查看网卡MAC地址
ethtool -P|--show-permaddr DEVNAME


##############################修改类操作##################################

# 设置网卡的速率为 1000 Mbps，并启用自动协商
ethtool -s eth0 speed 1000 duplex full autoneg on

# 禁用网卡的 GSO（Generic Segmentation Offload）
ethtool -K eth0 gso off

# 设置 RX/TX ring parameters 
ethtool -G <interface> rx <RX_size> tx <TX_size> [other options]
	rx：设置接收缓冲区的大小。
	tx：设置发送缓冲区的大小。
	rx-mini：设置迷你帧接收缓冲区的大小（如果支持的话）。
	rx-jumbo：设置巨帧接收缓冲区的大小（如果支持的话）。

# 修改网卡存储器中的信息
ethtool -E|--change-eeprom DEVNAME	
   """
    print(ethtool_cmd) 

def print_mlag_cmd():
    mlag_cmd = """

############################## DESCRIPTION ##################################

MLAG（Multi-Chassis Link Aggregation Group，多机箱链路聚合组）是网络中一种将多个物理
交换机虚拟成一个逻辑设备来进行链路聚合的技术。它的主要作用是提高链路带宽和可靠性，避免单点故
障，同时又能让终端设备认为它连接的是一个“交换机”。


############################# MLAG的核心功能 ##################################

1、链路聚合但跨设备：传统LACP链路聚合要求所有端口在同一个设备上，而MLAG可以跨两个（或多个）设备聚合链路。
2、增强可靠性：即使其中一台交换机故障，另一个还在，服务不中断。
3、避免STP阻塞：通过打破传统二层网络中生成树协议（STP）的限制，实现双活连接，提升网络收敛速度。

	
############################ MLAG的典型应用场景 #################################

1、服务器双网卡连接两个交换机（双上联）
2、服务器的两个网卡分别接到两台交换机上，形成MLAG，这样实现冗余和负载均衡。
3、汇聚层交换机连接接入层交换机
4、接入层交换机也可以使用MLAG连接到两台汇聚层设备。


############################ 架构示意图（逻辑上） #############################

          +-------------+        +-------------+
          | Switch A    |========| Switch B    |
          +-------------+        +-------------+
                ||                   ||
                ||    MLAG Peer Link ||
                ||                   ||
          +------------------------------------+
          |        End Device (如服务器)       |
          +------------------------------------+

############################### 常见术语解释 #################################

| 术语                              | 含义
| --------------------------------  | ------------------------------
| Peer Link                         | 用于交换MLAG控制信息的链路，通常是两台设备之间的直连链路
| Keepalive Link                    | 心跳检测链路，用于检测MLAG对端是否在线，防止双主
| Dual-active                       | 双主冲突状态，通常需要检测和避免
| ICC（Inter-Chassis Communication）| 某些厂商对Peer Link的专有叫法


############################## 各厂商的叫法 ##################################

| 厂商    | MLAG技术名称
| ------- | ------------------------------------
| Cisco   | vPC（Virtual Port Channel）
| H3C     | IRF（Intelligent Resilient Framework）
| Huawei  | CSS（Cluster Switch System）或M-LAG
| Arista  | MLAG（就叫MLAG）
| Juniper | Virtual Chassis 或 EVPN-MLAG
   """
    print(mlag_cmd) 

def print_ruijie_cmd():
    ruijie_cmd = """
terminal length 0
show memory
show cpu
show upgrade auto
show cpu-protect m
show ip route count
show route-res usage all 
show ip route
show ip route count
show ip route summary all 
show ipv6 route
show ipv6 route summary 
show ipv6 route summary all 
show ip route vrf NET-manage count
show ip route vrf NET-manage
show ipv6 route vrf NET-manage
show arp detail vrf NET-manage
show arp count
show version detail
show version slot
show tcam-mode status
show switch-mode
show aggregatePort capacity 
show switch-mode status
show interface counters summary up
show interface counters rate up 
show interface counters errors up
show interface usage up 
show interface link-state-change statistics 
show interface counters drops up 
show memory
show cpu
show upgrade auto
show power
show fan
show tem
show alarm
show vap data-sync
show vap keepalive
show vap peer-link
show run | in vap
show interface description
show lldp neighbor
show lacp summary
show interface switchport
show interface trunk
show vlan
show span summary
show vrf
show vrrp brief
show ipv6 vrrp brief
show ip ospf neighbor
show ip bgp neighbor
show bgp al lsummary
show bgp all
show isis neighbor
show mac count
show mac
show vxlan mac
show ipv6 neighbors ve
show ipv6 neighbors statistics 
show acl res 
show acl res detail
show vxlan
show vxlan vtep-nbr
show aggregatePort summary
show lacp summary
show aggregatePort summary 
show run
show clock
show logging reverse
terminal no length

# 通过SSH协议连接到锐捷（Ruijie）网络设备		   
ssh -l COC_operator 30.16.80.33 /vrf CTVPN1107
	ssh：Secure Shell协议，用于加密的远程登录
	-l COC_operator：指定登录用户名为"COC_operator"
	30.16.80.33：目标设备的IP地址
	/vrf CTVPN1107：指定使用名为"CTVPN1107"的VRF(Virtual Routing and Forwarding)实例进行连接
		/vrf 参数 告诉 SSH 客户端，不要使用默认路由表，而是查询 CTVPN1107 的路由表来确定如何连接到 30.16.80.33，确保 SSH 流量走正确的接口或隧道（如 MPLS VPN、专线等）。
		如果 CTVPN1107 不可达，可通过 show ip vrf brief 查看别的vrf
   """
    print(ruijie_cmd) 

def print_stp_cmd():
    stp_cmd = """
############################## DESCRIPTION ##################################

STP（Spanning Tree Protocol，生成树协议）是以太网中防止二层网络环路的一种协议。它可以在网
络中自动选择一棵树形结构的拓扑来屏蔽多余的环路，从而避免广播风暴、MAC地址表震荡、重复帧等问题。


############################# 为什么需要 STP #################################

在以太网中，如果存在物理环路（比如交换机之间互联形成环形结构），广播帧会在网络中不断地循环，导致：
    广播风暴（Broadcast Storm）
    MAC表频繁学习和刷新
    网络拥堵甚至瘫痪
STP 通过“阻塞某些端口”的方式打破环路，使网络成为一个无环的树形拓扑。


############################ STP 的核心工作原理 ###############################

1. 选举根桥（Root Bridge）
	所有交换机会通过**Bridge ID（桥 ID）**参与选举。
	Bridge ID = 优先级（默认32768） + MAC地址。
	数值最小的设备当选为 Root Bridge。
2. 计算到 Root 的最短路径
	所有非 Root 交换机会计算到 Root Bridge 的最小路径开销（Path Cost）。
3. 确定各端口角色
	| 端口角色                  | 功能说明
	| --------------------------| -------------------------------
	| Root Port（RP）           | 通向 Root Bridge 的最佳路径端口（每台交换机一个）
	| Designated Port（DP）     | 某段链路中“负责转发”的端口
	| Blocked Port（备用端口）  | 被 STP 主动阻塞，防止环路
4. 端口状态转换
	Blocking → Listening → Learning → Forwarding
		Blocking：阻塞，不转发数据
		Listening：监听BPDU，准备选举
		Learning：学习MAC，不转发
		Forwarding：正常转发数据


############################ 架构示意图（逻辑上） #############################

           +----------------+
           |   SW1 (Root)   |
           +----------------+
              |          |
              |          |
     +-------------+  +-------------+
     |    SW2      |  |     SW3     |
     +-------------+  +-------------+
              \           /
               \         /
            +-------------+
            |    SW4      |
            +-------------+
在这个结构中，STP 会阻塞其中一条连接（如 SW3 到 SW4），以打破环路。

############################### STP 的优缺点 #################################

| 优点       	     | 缺点
| ------------------ | -----------------
| 防止二层环路       | 收敛慢（传统 STP）
| 自动选路，配置简单 | 部分网络链路资源浪费（被阻塞）
| 高兼容性           | 无法充分利用冗余带宽（非负载均衡）

   """
    print(stp_cmd) 

