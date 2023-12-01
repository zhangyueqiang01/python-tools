#!/usr/bin/python
# -*- coding: utf-8 -*-


from optparse import OptionParser
from socket import *
import os
import subprocess
import time
import sys
from random import choice
import string

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

parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")
parser.set_usage(sys.argv[0]+' [option]')
parser.add_option("-i", "--install", action='store', dest="pkg",help="install packages on remote host")
parser.add_option("-p", "--ping", action="store", dest='ping', help="ping a net such as ping 8.8.8")
parser.add_option('-d','--host',action='store',dest='host',help='combine with -i')
parser.add_option('-z','--zombie',action='store',dest='zombie',help='create a zombie process on loalhost machine')
parser.add_option('-P','--passwd',action='store',dest='passwd',help='input a number and create a random passwd')
parser.add_option('-w','--http',action='store',dest='hport',help='such as python -m SimpleHTTPServer 8080')
parser.add_option('-t','--tcpdump',action='store',dest='tport',help='such as tcpdump -i any tcp port 80 and host 8.8.8.8')
parser.add_option('-u','--udpdump',action='store',dest='uport',help='such as tcpdump -i any udp port 80 and host 8.8.8.8')
(options, args) = parser.parse_args()

if options.pkg:
    HOST=options.host
    PORT=2222
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    tcpCliSock=socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.send(options.pkg)
    result=tcpCliSock.recv(BUFSIZ)
    print(result)
    tcpCliSock.close()

if options.ping:
    ips = (options.ping+'.'+'%s' % i for i in range(1, 255))
    for ip in ips:
        pid = os.fork()
        if not pid:
            ping(ip)
            exit()
    time.sleep(20)

if options.zombie:
    print('zombie process has been created')
    pid = os.fork()
    if pid:
        while True:
            time.sleep(10)
    else:
        time.sleep(3)

if options.passwd:
   passwd=int(options.passwd)
   print(gen_pass(passwd))

if options.hport:
    http(options.hport)

if options.tport:
    tcpdump(options.port)

if options.uport:
    udpdump(options.port)

