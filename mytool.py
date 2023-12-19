#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from socket import *
import os
import subprocess
import time
import sys
from random import choice
import string
import socket
import threading
import logging


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

def print_xxx_header():
    print("rfc url")
    print("xxx Header Format:")
    xxx_header_format = """
    xxx
   """
    print(xxx_header_format)

def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )
    if rc:
        print('%s: down' % host)
    else:
        print('%s: up' % host)

def gen_pass(n=16):
    all_chs = string.ascii_letters + string.digits  
    result = ''
    for i in range(n):
        ch = choice(all_chs)
        result += ch
    return result

def http(port):
    # 定义命令
    command = "python -m SimpleHTTPServer %s" % port

    # 使用subprocess执行命令
    try:
        # shell=True参数允许您在命令中使用管道和其他Shell功能
        process = subprocess.Popen(command, shell=True)
        process.wait()  # 等待子进程完成
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))


def tcpdump(port):
    # 定义命令
    command = "tcpdump -i any tcp port %s -ennl" % port

    # 使用subprocess执行命令
    try:
        # shell=True参数允许您在命令中使用管道和其他Shell功能
        process = subprocess.Popen(command, shell=True)
        process.wait()  # 等待子进程完成
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))

def udpdump(port):
    command = "tcpdump -i any udp port %s -ennl -vv" % port

    try:
        process = subprocess.Popen(command, shell=True)
        process.wait()  
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))

def arpdump():
    command = "tcpdump -i any arp -ennl -vv"

    try:
        process = subprocess.Popen(command, shell=True)
        process.wait()  
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))
 

def send_large_message(host, port, size, num_packets):
    logging.basicConfig(filename='udp_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
    message = b'a' * size
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        for _ in range(num_packets):
            s.sendto(message, (host, port))
            logging.info("Sent UDP packet to %s:%s with size %s bytes", host, port, size)
    finally:
        s.close()

def run_threads(args):
    threads = []
    for _ in range(args.total_threads):
        thread = threading.Thread(target=send_large_message, args=(args.host, args.port, args.size, args.packets_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def main():
    parser = argparse.ArgumentParser(description="designed by Michael")
    parser.add_argument("--udp", action="store_true", help="Print UDP header format")
    parser.add_argument("--tcp", action="store_true", help="Print TCP header format")
    parser.add_argument("--ipv4", action="store_true", help="Print IPV4 header format")
    parser.add_argument("--icmp", action="store_true", help="Print ICMP header format")
    parser.add_argument("--ethernet2", action="store_true", help="Print Ethernet II header format")
    parser.add_argument("--vlan", action="store_true", help="Print vlan header format")
    parser.add_argument("--vxlan", action="store_true", help="Print vxlan header format")
    parser.add_argument("--http", action="store_true", help="Print http header format")
    parser.add_argument("--ftp", action="store_true", help="Print ftp header format")
    parser.add_argument("--ssh", action="store_true", help="Print ssh header format")
    parser.add_argument("--dhcp", action="store_true", help="Print dhcp header format")
    parser.add_argument("--ipv6", action="store_true", help="Print ipv6 header format")

    parser.add_argument("-i", "--install", action='store', dest="pkg",help="install packages on remote host")
    parser.add_argument("-p", "--ping", action="store", dest='ping', help="ping a net such as ping 8.8.8")
    parser.add_argument('-d','--ihost',action='store',dest='host',help='combine with -i')
    parser.add_argument('-z','--zombie',action='store',dest='zombie',help='create a zombie process on loalhost machine')
    parser.add_argument('-P','--passwd',action='store',dest='passwd',help='input a number and create a random passwd')
    parser.add_argument('-w','--web',action='store',dest='hport',help='such as python -m SimpleHTTPServer 8080')
    parser.add_argument('-t','--tcpdump',action='store',dest='tport',help='such as tcpdump -i any tcp port 80 and host 8.8.8.8')
    parser.add_argument('-u','--udpdump',action='store',dest='uport',help='such as tcpdump -i any udp port 80 and host 8.8.8.8 -vv')
    parser.add_argument("--arpdump", action="store_true", help="such as tcpdump -i any arp -ennl -vv")
    parser.add_argument('--host', default=' ', help='send UDP packages to Host name or IP address, default is NUll')
    parser.add_argument('--port', type=int, default=12345, help='send UDP packages to Port number, default is 12345')
    parser.add_argument('--size', type=int, default=1024, help='send UDP packages Message size in bytes, default is 1024 Kb')
    parser.add_argument('--packets-per-thread', type=int, default=3, help='Number of UDP packets per thread, default is 3')
    parser.add_argument('--total-threads', type=int, default=10, help='Total number of threads, default is 10')

    args = parser.parse_args()

    if args.udp:
        print_udp_header()
    elif args.tcp:
        print_tcp_header()
    elif args.icmp:
        print_icmp_header()
    elif args.ipv4:
        print_ipv4_header()
    elif args.ethernet2:
        print_ethernet2_header()
    elif args.vlan:
        print_vlan_header()
    elif args.vxlan:
        print_vxlan_header()
    elif args.http:
        print_http_header()
    elif args.pkg:
        HOST=args.ihost
        PORT=2222
        BUFSIZ=1024
        ADDR=(HOST,PORT)
        tcpCliSock=socket(AF_INET,SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        tcpCliSock.send(args.pkg)
        result=tcpCliSock.recv(BUFSIZ)
        print(result)
        tcpCliSock.close()
    
    elif args.ping:
        ips = (args.ping+'.'+'%s' % i for i in range(1, 255))
        for ip in ips:
            pid = os.fork()
            if not pid:
                ping(ip)
                exit()
        time.sleep(20)
    
    elif args.zombie:
        print('zombie process has been created')
        pid = os.fork()
        if pid:
            while True:
                time.sleep(10)
        else:
            time.sleep(3)
    
    elif args.passwd:
       passwd=int(args.passwd)
       print(gen_pass(passwd))
    
    elif args.hport:
        http(args.hport)
    
    elif args.tport:
        tcpdump(args.tport)
    
    elif args.uport:
        udpdump(args.uport)

    elif args.arpdump:
        arpdump()

    elif args.host:
        run_threads(args)

    else:
        print("Please specify args")

if __name__ == "__main__":
    main()


