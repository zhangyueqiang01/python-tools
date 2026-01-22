#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_udp_header():
    print("https://www.ietf.org/rfc/rfc768.txt")
    print("UDP Header Format:")
    udp_header_format = """
                  0      7 8     15 16    23 24    31 
                 +--------+--------+--------+--------+
                 |          source address           |
                 +--------+--------+--------+--------+
                 |        destination address        |
                 +--------+--------+--------+--------+
                 |  zero  |protocol|   UDP length    |
                 +--------+--------+--------+--------+

常用端口
+-------+---------------+-------------------+--------+----------+----------------+-------+
|  DNS  |     DHCP      |        SNMP       |  NTP   |  Syslog  |     Radius     |  RIP  |
+-------+---------------+-------------------+--------+----------+----------------+-------+
|  53   | 67（服务器端）|  161（代理端口）  |  123   |   514    |  1812 （认证） |  520  |
+-------+---------------+-------------------+--------+----------+----------------+-------+
|       | 68 （客户端） |  162（Trap端口）  |        |          |  1813 （计费） |       |
+-------+---------------+-------------------+--------+----------+----------------+-------+
"""
    print(udp_header_format)

def print_ethernet2_header():
    print("Ethernet II Header Format:")
    ethernet2_header_format = """
+-------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+
| Preamble          | Start Frame Delimiter| Destination Address  | Source Address       | Type/Length Field    | Data                 | Frame Check Sequence |
| (7 bytes)         | (1 byte)             | (6 bytes)            | (6 bytes)            | (2 bytes)            | (46-1500 bytes)      | (4 bytes)            |
+-------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+
IPv4帧:  值为0x0800,表示数据部分是IPv4协议的数据。
ARP帧: 值为0x0806,表示数据部分是地址解析协议(ARP)的数据。
IPv6帧: 值为0x86DD,表示数据部分是IPv6协议的数据。
VLAN帧: 值为0x8100,表示数据部分包含802.1Q虚拟局域网(VLAN)标签。
IPv4 over IPv6帧: 值为0x0800,表示IPv4数据被封装在IPv6帧中。
PPPoE帧: 值为0x8864,表示数据部分是点对点协议(PPP)的封装。
"""
    print(ethernet2_header_format)

def print_vlan_header():
    print("https://support.huawei.com/enterprise/zh/doc/EDOC1100088136")
    print("IEEE 802.1Q VLAN Header Format:")
    vlan_header_format = """
+-------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+
| Preamble          | Start Frame Delimiter| Destination Address  | Source Address       | Type/Length Field    | VLAN Tag             | Type/Length Field    | Data                 | Frame Check Sequence |
| (7 bytes)         | (1 byte)             | (6 bytes)            | (6 bytes)            | (2 bytes)            | (4 bytes)            | (2 bytes)            | (46-1500 bytes)      | (4 bytes)            |
+-------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+


  0                   1                   2                   3   
  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 | TPI (0x81)    | PRI (PCP+CFI)   |            VLAN ID          |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |            EtherType or Length (for Ethernet II)              |
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


第一个类型/长度字段(2字节): 如果帧的长度小于或等于1500字节,这个字段表示帧中的数据长度;如果长度超过1500字节,这个字段表示帧的类型。在IEEE 802.1Q中,这个字段的值是0x8100,表示后面是802.1Q标签。
标签协议标识(TPID)(2字节): 固定为0x8100,表示这是一个IEEE 802.1Q标签。
优先级(3位)和CFI(Canonical Format Identifier,1位)(1字节): 这4个比特位组成了一个单独的字节。其中,3位的优先级字段用于指定VLAN的优先级,而CFI位通常被设置为0。
VLAN标识(12位): VLAN标识字段用于标识具体的VLAN。这个字段可以包含0到4095之间的值,其中0和4095有特殊用途,0表示不使用VLAN,而4095用于保留所有VLAN标识。
第二个类型/长度字段(2字节): 指示帧中数据的类型或长度,通常是IPv4(0x0800)或IPv6(0x86DD)。

"""
    print(vlan_header_format)

def print_vxlan_header():
    print("https://support.huawei.com/enterprise/zh/doc/EDOC1100065793/2845c625")
    print("vxlan Header Format:")
    vxlan_header_format = """
############################## VXLAN Position ######################################

                       20 Bytes
                          ^                      8 Bytes
                          |                         ^    
                        72|IP Header                |   
                         8|Protocol                8|VXLAN Flags
                        16|Header Checksum        24|Reserved
                        32|Outer Src IP           24|VNI
                        32|Outer Dst IP            8|Reserved
                          |                         |   
 +-+-+-+-+-+-+-+-+|+-+-+-+|+-+-+-+-+-+-+-+-+-+-+-+-+|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |      Outer     |-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|          |   
 |                |     Outer   |-+-+-+-+-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+|    F     |   
 |                |             |   UDP    |-+-+-+-+|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+|          |   
 |       MAC      |      IP     |          | VXLAN header | Original Ethernet Freame  |    C     |   
 |                |             |  Header  |-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+|          |   
 |                |     Header  |-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|    S     |   
 |      Header    |-+-+-+-+-+-+-+-+-+-|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|          |   
 +-+-+-+-+|+-+-+-+-+-+-+-+-+-+|+-+-+-+|+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          |                           |   
        48|Dst MAC Addr             16|UDP Src Port
        48|Src MAC Addr             16|UDP Dst port(VXLAN Port)
        16|VLAN Type                16|UDP Length
        16|VLAN ID Tag              16|Checksum
        16|Ethernet Type              |   
          |                           v    
          v                        8 Bytes
      14 Bytes
   4 Bytes Optional

############################## VXLAN Header ######################################

字节偏移        字段                            长度            描述
 0~1            Flags                           2 字节          最重要的是第0位（即 bit 8），必须为1，表示 VXLAN 有效，其余为保留位（设为0） 
 2~3            Reserved                        2 字节          保留位，设为0 
 4~6            VXLAN Network Identifier (VNI)  3 字节（24位）  VXLAN的网络标识符，用于区分不同的逻辑二层网络
 7              Reserved                        1 字节          保留位，设为0 
    

############################## VXLAN 封装过程 ######################################
    
                                原始以太帧
                                     ↓   
                                VXLAN Header（8字节）
                                     ↓   
                                UDP Header（目的端口是 4789）
                                     ↓   
                                外层 IP Header（一般是 IPv4 或 IPv6）
                                     ↓   
                                外层 MAC Header


############################## caution ######################################

# vxlan报文使用的udp端口号：
        源端口（Source Port）：一般由操作系统动态分配（可以用作负载均衡的哈希输入）。
        目的端口（Destination Port）：4789，这是 IANA 正式分配给 VXLAN 的端口号。

# VXLAN 流量是封装过的，tcpdump 只会看到 外层的 UDP 包，如果你想分析 内部的以太网
帧、IP、ARP 等，建议用 Wireshark 打开 .pcap 文件，它能解析 VXLAN 封装。

tcpdump -i <interface> udp port 4789 -vv -n -s 0 -w vxlan.pcap
	-s 0：抓取完整报文（否则默认只抓一部分）
	udp port 4789：VXLAN 使用的 UDP 端口，抓的就是它
	
部分 Linux 系统上的 tcpdump（可能支持 VXLAN 协议解码
"""
    print(vxlan_header_format)
    
def print_tcp_header():
    print("https://www.ietf.org/rfc/rfc793.txt")
    print("TCP Header Format:")
    tcp_header_format = """
    0                   1                   2                   3   
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |          Source Port          |       Destination Port        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                        Sequence Number                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Acknowledgment Number                      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Data |           |U|A|P|R|S|F|                               |
   | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
   |       |           |G|K|H|T|N|N|                               |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           Checksum            |         Urgent Pointer        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             data                              |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

常用端口
+--------+---------+-----------------+-------+------+------+------+------+-------+----------------------------+-----------+--------+
|  HTTP  |  HTTPS  |      FTP        |  SSH  | SMTP | POP3 | IMAP | LDAP | MySQL | SMB (Server Message Block) |  NetBIOS  |  NFS   |
+--------+---------+-----------------+-------+------+------+------+------+-------+----------------------------+-----------+--------+
|   80   |   443   |  21（控制连接） |  22   |  23  |  25  | 110  | 389  | 3389  |             445            |   139     |  2049  |
+--------+---------+-----------------+-------+------+------+------+------+-------+----------------------------+-----------+--------+
|        |         |  20（数据连接） |       |      |      |      |      |       |                            |           |        |
+--------+---------+-----------------+-------+------+------+------+------+-------+----------------------------+-----------+--------+
   """
    print(tcp_header_format)

def print_ipv4_header():
    print("https://datatracker.ietf.org/doc/html/rfc791")
    print("ipv4 Header Format:")
    ipv4_header_format = """

############################## header ######################################

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


########################### 常见 Protocol 字段的值及含义 ##################################

位置：IPv4 报头的第 9 个字节（第 9 个字段）
长度：8 位（即 1 字节）
作用：指明该 IP 包载荷部分使用的是哪种传输层或网络层协议

协议名称    Protocol值	 描述
ICMP	 	1	 Internet Control Message Protocol（控制信息）
TCP	 	6	 Transmission Control Protocol（面向连接）
UDP	 	17	 User Datagram Protocol（无连接）
GRE	 	47	 通用路由封装（用于VPN等）
ESP	 	50	 Encapsulating Security Payload（IPSec）
AH	 	51	 Authentication Header（IPSec）
OSPF	 	89	 Open Shortest Path First（动态路由协议）


############################## IPv4 报头字段详解 ######################################

字段名					长度		含义
1. Version（版本）			4位		指定 IP 协议的版本，IPv4 的值为 4
2. IHL（Internet Header Length）	4位		报头长度，单位为 4 字节（最小值 5，即 20 字节）
3. Type of Service（服务类型）		8位		指定服务质量要求，现代中一般为 DSCP + ECN
4. Total Length（总长度）		16位		整个 IP 包的总长度（包括报头 + 数据），单位字节
5. Identification（标识）		16位		标识数据包，用于数据包分片与重组
6. Flags（标志）			3位		控制分片行为：如是否允许分片（DF）、是否是最后一片（MF）
7. Fragment Offset（片偏移）		13位		指明该分片在原始数据包中的偏移位置，单位为 8 字节
8. Time to Live（生存时间，TTL）	8位		限制数据包在网络中能经过的最大路由跳数，防止死循环
9. Protocol（协议）			8位		指明上层协议，如 TCP（6）、UDP（17）、ICMP（1）
10. Header Checksum（头部校验和）	16位		用于校验 IP 头部是否有错误
11. Source IP Address（源 IP）		32位		发送端的 IPv4 地址
12. Destination IP Address（目的 IP）	32位		接收端的 IPv4 地址
13. Options（可选字段）			可变		可选控制信息，不常用，如时间戳、路由记录等
14. Padding（填充）			可变		为保证报头是 4 字节对齐的，进行填充（通常为 0）   
   """
    print(ipv4_header_format)

def print_icmp_header():
    print("https://datatracker.ietf.org/doc/html/rfc792")
    print("ICMP Header Format:")
    icmp_header_format = """

ICMP（Internet Control Message Protocol，互联网控制消息协议）是TCP/IP协议
族中用于传递控制消息的协议，常用于诊断网络连接、报告错误等。

############################## header ######################################

0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     Type      |     Code      |          Checksum             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|           Identifier          |        Sequence Number        | （仅部分类型有）
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

############################## Type（类型） — 8位 ######################################

类型值  | 含义
0 	| 回显应答（Echo Reply）
3 	| 目标不可达（Destination Unreachable）
8 	| 回显请求（Echo Request）
11 	| 超时（Time Exceeded）

############################## Code（代码） — 8位 ######################################
Code    | 意义
0 	| 网络不可达
1 	| 主机不可达
3 	| 端口不可达

############################## Identifier ######################################

Identifier（标识符） 是 ICMP 报头中的一个 16 位字段，主要出现在 ICMP Echo Request（回显请求）
和 Echo Reply（回显应答）类型的消息中，也就是我们用 ping 命令时常见的那类。

它的作用是：
	用来唯一标识一组 ICMP 请求-应答配对，帮助发送端将收到的应答与对应的请求一一对应起来。

Identifier 的应用场景（以 ping 为例）
比如你用 ping www.example.com，其实系统会这样处理：
	生成一个 Identifier（例如 PID：进程号）
	发送多个 ICMP Echo Request 报文，每个报文用相同的 Identifier，不同的 Sequence Number（序列号）
	当目标主机响应 ICMP Echo Reply 报文时，也会带着相同的 Identifier
	接收端用 Identifier 和 Sequence Number 匹配出哪个请求被应答了
	
在很多系统里，ping 命令会将当前进程的 PID（Process ID）作为 Identifier
这样即使多个用户在同时 ping，不同进程的 Identifier 也不一样，不会混淆

配合 Sequence Number 使用
	字段		作用
	Identifier	区分不同的 ping 实例
	Sequence Num	区分同一 ping 实例中第几次请求

############################## other ######################################

Checksum（校验和） — 16位
对整个ICMP报文（包括数据部分）做校验，用于保证数据完整性。如果计算结果不一致，说明数据在传输中被破坏。

Sequence Number（序列号） — 16位（可选，Echo类型使用）
同样用于匹配请求和应答，也能用于统计丢包率和延迟。

Data（数据部分） — 可变长度
可以携带任意数据，ping命令中通常包含一些填充数据，发送端发送什么内容，接收端原样返回。
   """
    print(icmp_header_format)

def print_http_header():
    print("rfc url")
    print("http Header Format:")
    http_header_format = """
   +--------------------------------------+
   |           HTTP Request Header        |
   +--------------------------------------+
   | Method: GET                          |
   | Path: /path/resource                 |
   | Protocol: HTTP/1.1                   |
   | Host: www.example.com                |
   | User-Agent: Mozilla/5.0              |
   | Accept: text/html, application/xml   |
   | Connection: keep-alive               |
   +--------------------------------------+

   +--------------------------------------+
   |          HTTP Response Header        |
   +--------------------------------------+
   | Protocol: HTTP/1.1                   |
   | Status Code: 200 OK                  |
   | Status Text: OK                      |
   | Content-Type: text/html              |
   | Content-Length: 12345                |
   | Server: Apache/2.4.38                |
   | Set-Cookie: sessionid=12345;         |
   |    Path=/; Expires=Wed, 18 Dec 2024  |
   +--------------------------------------+

   1xx(信息性状态码): 服务器收到请求，需要请求者继续执行操作。
   100 Continue: 服务器已经收到请求的头部，并且客户端应该继续发送请求的其余部分。

   2xx(成功状态码): 请求被成功接收、理解、并接受。
   200 OK: 请求成功。
   201 Created: 请求已经被实现，而且有一个新的资源已经依据请求的需要而建立。
   204 No Content: 服务器成功处理了请求，但没有返回任何内容。

   3xx(重定向状态码): 需要客户端采取进一步的操作才能完成请求。
   301 Moved Permanently: 请求的资源已被永久移动到新位置。
   302 Found: 请求的资源临时从不同的URI响应请求。
   304 Not Modified: 资源未被修改，可以使用缓存的版本。

   4xx(客户端错误状态码): 客户端似乎有错误，无法完成请求。
   400 Bad Request: 服务器不理解请求的语法。
   401 Unauthorized: 请求要求身份验证。
   403 Forbidden: 服务器理解请求，但拒绝执行。
   404 Not Found:(未找到)

   5xx(服务器错误状态码): 服务器在处理请求的过程中发生错误。
   500 Internal Server Error: 服务器遇到了一个未曾预料的状况。
   502 Bad Gateway: 服务器作为网关或代理，从上游服务器收到无效响应。
   503 Service Unavailable: 服务器暂时不可用。
   """
    print(http_header_format) 


def print_net_cmd():
    net_cmd = """
######################################################## 内核接收网络包（RX）全过程 ################################################################

方向：网卡 → 内核 → Socket → 用户态

1、网卡收到数据（DMA + 中断）
2、NAPI 轮询机制（软中断）
3、协议栈处理流程（L2 → L4）
   Ethernet -> IP层 -> TCP/UDP -> Socket
4、放入 Socket 接收队列
5、用户态读取数据
   内核把 skb 数据 copy 到用户态,skb 被释放

######################################################## 内核发送网络包（TX）全过程 ################################################################

方向：用户态 → 内核 → 网卡

1、用户态系统调用
2、Socket 层
   创建 skb
   拷贝用户数据到 skb
3、传输层（TCP / UDP）
4、IP 层
5、二层 & 邻居子系统
6、Qdisc（流控 / 排队）
7、驱动发送（DMA）


######################################################## TAP 设备收发网络包的过程 #################################################################

TAP = 二层虚拟网卡，内核 ↔ 用户态 之间用 skb 传递以太网帧

一、TAP 接收包流程（外部 → 内核 → 用户态）
方向：物理网卡 → Linux 协议栈 → TAP → 用户态程序


二、TAP 发送包流程（用户态 → 内核 → 外部）
方向：用户态 → TAP → Linux 协议栈 → 物理网卡
   """
    print(net_cmd) 

