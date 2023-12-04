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
    command = "tcpdump -i any tcp port %s -en" % port

    # 使用subprocess执行命令
    try:
        # shell=True参数允许您在命令中使用管道和其他Shell功能
        process = subprocess.Popen(command, shell=True)
        process.wait()  # 等待子进程完成
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))

def udpdump(port):
    # 定义命令
    command = "tcpdump -i any udp port %s -en" % port

    # 使用subprocess执行命令
    try:
        # shell=True参数允许您在命令中使用管道和其他Shell功能
        process = subprocess.Popen(command, shell=True)
        process.wait()  # 等待子进程完成
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
    parser = argparse.ArgumentParser(description="design by Michael")
    parser.add_argument("--udp", action="store_true", help="Print UDP header format")
    parser.add_argument("--tcp", action="store_true", help="Print TCP header format")
    parser.add_argument("--ipv4", action="store_true", help="Print IPV4 header format")
    parser.add_argument("--icmp", action="store_true", help="Print ICMP header format")
    parser.add_argument("-i", "--install", action='store', dest="pkg",help="install packages on remote host")
    parser.add_argument("-p", "--ping", action="store", dest='ping', help="ping a net such as ping 8.8.8")
    parser.add_argument('-d','--ihost',action='store',dest='host',help='combine with -i')
    parser.add_argument('-z','--zombie',action='store',dest='zombie',help='create a zombie process on loalhost machine')
    parser.add_argument('-P','--passwd',action='store',dest='passwd',help='input a number and create a random passwd')
    parser.add_argument('-w','--http',action='store',dest='hport',help='such as python -m SimpleHTTPServer 8080')
    parser.add_argument('-t','--tcpdump',action='store',dest='tport',help='such as tcpdump -i any tcp port 80 and host 8.8.8.8')
    parser.add_argument('-u','--udpdump',action='store',dest='uport',help='such as tcpdump -i any udp port 80 and host 8.8.8.8')
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
    elif args.host:
        run_threads(args)

    else:
        print("Please specify args")

if __name__ == "__main__":
    main()


