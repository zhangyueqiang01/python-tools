#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import absolute_import

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

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

from sysutils.sysutils import *
from software.software import *
from network.devices import *
from network.header import *
from databases.databases import *
from program.program import *
from kernel.kernel import *
from git.git import *



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


def cntoeng(file_path):
    if not os.path.isfile(file_path):
        print("Error: File '{}' not found.".format(file_path))
        sys.exit(1)

    sed_command = "sed -i 's/（/(/g; s/）/)/g; s/：/:/g; s/，/,/g; s/。/./g; s/？/?/g' %s" % file_path

    try:
        subprocess.Popen(sed_command, shell=True).wait()
        print("Sed command executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error executing sed command:", e)
        sys.exit(1)

def ncscanport(host, port):
    command = "nc -zv {} {}".format(host, port)
    try:
        process = subprocess.Popen(command, shell=True)
        process.wait()
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))

def nmapscanport(host, port):
    command = "nmap -sV -p {} {}".format(port,host)
    try:
        process = subprocess.Popen(command, shell=True)
        process.wait()
    except subprocess.CalledProcessError as e:
        print("Error executing command: {}".format(e))

def main():
    parser = argparse.ArgumentParser(description="designed by Michael")
    parser.add_argument("--show", choices=['ceph', 'docker','udp','tcp','icmp','ipv4','ipv6','ethernet2','vlan','vxlan','http',\
                                           'h3c','dp','huawei1','huawei2','zte','osp','ceph','docker','iptables','tcpdump','route',\
                                            'ip','nmcli','bond','kvm','kcompose','git','vim','bash','find','linuxbasic'], help="Display usage instance")


    parser.add_argument("-i", "--install", action='store', dest="pkg",help="install packages on remote host")
    parser.add_argument("-p", "--ping", action="store", dest='ping', help="ping a net such as ping 8.8.8")
    parser.add_argument('-d','--ihost',action='store',dest='host',help='combine with -i')
    parser.add_argument('-z','--zombie',action='store',dest='zombie',help='create a zombie process on loalhost machine')
    parser.add_argument('-P','--passwd',action='store',dest='passwd',help='input a number and create a random passwd')
    parser.add_argument('-w','--web',action='store',dest='hport',help='such as python -m SimpleHTTPServer 8080 or python3 -m http.server 80')
    parser.add_argument('-t','--mytcpdump',action='store',dest='tport',help='such as tcpdump -i any tcp port 80 and host 8.8.8.8')
    parser.add_argument('-u','--udpdump',action='store',dest='uport',help='such as tcpdump -i any udp port 80 and host 8.8.8.8 -vv')
    parser.add_argument("--arpdump", action="store_true", help="such as tcpdump -i any arp -ennl -vv")
    parser.add_argument('--host', default=' ', help='send UDP packages to Host name or IP address, default is NUll')
    parser.add_argument('--port', type=int, default=12345, help='send UDP packages to Port number, default is 12345')
    parser.add_argument('--size', type=int, default=1024, help='send UDP packages Message size in bytes, default is 1024 Kb')
    parser.add_argument('--packets-per-thread', type=int, default=3, help='Number of UDP packets per thread, default is 3')
    parser.add_argument('--total-threads', type=int, default=10, help='Total number of threads, default is 10')
    parser.add_argument('--shost', default=' ', help='Scan a special host tcp port, default host is NUll')
    parser.add_argument('--sport', default='', help='Scan a host  speial tcp port like "nc -zv 8.8.8.8 80" or "nmap -sV -p 22 8.8.8.8", default port is NUll')
    parser.add_argument("--cntoeng", nargs=1,help="Modify all Chinese punctuation marks into English punctuation marks, like sed -i s/：/:/g test.py")

    args = parser.parse_args()

    if args.show == 'udp':
        print_udp_header()
    elif args.show == 'tcp':
        print_tcp_header()
    elif args.show == 'icmp':
        print_icmp_header()
    elif args.show == 'ipv4':
        print_ipv4_header()
    elif args.show == 'ethernet2':
        print_ethernet2_header()
    elif args.show == 'vlan':
        print_vlan_header()
    elif args.show == 'vxlan':
        print_vxlan_header()
    elif args.show == 'http':
        print_http_header()
    elif args.show == 'h3c':
        print_h3c_cmd()
    elif args.show == 'dp':
        print_dp_cmd()
    elif args.show == 'huawei1':
        print_huawei1_cmd()
    elif args.show == 'huawei2':
        print_huawei2_cmd()
    elif args.show == 'zte':
        print_zte_cmd()
    elif args.show == 'osp':
        print_osp_cmd()
    elif args.show == 'ceph':
        print_ceph_cmd()
    elif args.show == 'docker':
        print_docker_cmd()
    elif args.show == 'iptables':
        print_iptables_cmd()
    elif args.show == 'tcpdump':
        print_tcpdump_cmd()
    elif args.show == 'route':
        print_route_cmd()
    elif args.show == 'ip':
        print_ip_cmd()
    elif args.show == 'nmcli':
        print_nmcli_cmd()
    elif args.show == 'bond':
        print_bond_cmd()
    elif args.show == 'kvm':
        print_kvm_cmd()
    elif args.show == 'kcompose':
       print_kernel_compose()
    elif args.show == 'git':
       print_git_cmd()
    elif args.show == 'vim':
       print_vim_cmd()
    elif args.show == 'bash':
       print_bash_cmd()
    elif args.show == 'find':
       print_find_cmd()
    elif args.show == 'linuxbasic':
       print_linuxbasic_cmd()


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

    elif args.cntoeng:
        cntoeng(args.cntoeng[0])

    elif args.shost is not None and args.sport is not None:
        print('nc -zv {} {}'.format(args.shost, args.sport))
        ncscanport(args.shost,args.sport)
        print('nmap -sV -p {} {}'.format(args.sport, args.shost))
        nmapscanport(args.shost,args.sport)

    else:
        print("Please specify args")

if __name__ == "__main__":
    main()


