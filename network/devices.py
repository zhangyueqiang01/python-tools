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
   """
    print(zte_cmd)   

def print_huawei1_cmd():
    print("HUAWEI1 usage command:")
    huawei1_cmd = """
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

system-view
security-policy
rule name kaifang80
dis this
destination-address  mask 255.255.255.255
undo destination-address  mask 255.255.255.255

   """
    print(huawei1_cmd)   

def print_huawei2_cmd():
    print("HUAWEI2 usage command:")
    huawei2_cmd = """
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

