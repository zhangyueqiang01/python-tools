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
+---------------------+
|Outer Ethernet Header|
+---------------------+
| IP Header (UDP)     |
+---------------------+
| UDP Header          |
+---------------------+
| VXLAN Header        |
+---------------------+
| Original Ethernet   |
| Frame (Payload)     |
+---------------------+


0                   1                   2                   3   
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|R|R|R|R|I|R|R|R|            Reserved                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                VXLAN Network Identifier (VNI)                 |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                UDP Source Port (Default: 4789)                |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                UDP Destination Port (Default: 4789)           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
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
   """
    print(tcp_header_format)

def print_ipv4_header():
    print("https://datatracker.ietf.org/doc/html/rfc791")
    print("ipv4 Header Format:")
    ipv4_header_format = """
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
   """
    print(ipv4_header_format)

def print_icmp_header():
    print("https://datatracker.ietf.org/doc/html/rfc792")
    print("ICMP Header Format:")
    ipv4_header_format = """
	0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |     Type      |     Code      |          Checksum             |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                             unused                            |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |      Internet Header + 64 bits of Original Data Datagram      |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   """
    print(ipv4_header_format)

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

