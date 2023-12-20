#!/usr/bin/python
# -*- coding: utf-8 -*-

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
route -n
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

