#!/usr/bin/python
# -*- coding: utf-8 -*-


import socket
import sys

def scan_ports(host, start_port, end_port):
    try:
        # 获取远程主机的IP地址
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("无法解析主机名，请检查并重试")
        sys.exit()

    print("开始扫描主机: {}".format(remote_ip))
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # 设置超时
        result = sock.connect_ex((remote_ip, port))  # 尝试连接
        if result == 0:
            print("port {}: up".format(port))
        else:
            print("port {}: down".format(port))
        sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("用法: python port_scanner.py <主机> <起始端口> <结束端口>")
        sys.exit()

    host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    scan_ports(host, start_port, end_port)


