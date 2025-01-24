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
ethtool -e|--eeprom-dump DEVNAME	Do a EEPROM dump

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

