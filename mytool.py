#!/usr/bin/python3
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
from troubleshooting.troubleshooting import *
from git.git import *
from cmd.cmd import *
from c.c import *
from assembly.assembly import *
from gnu.gnu import *
from hardware.hardware import *
from memory.memory import *
from other.other import *


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
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    all_chs = string.ascii_letters + string.digits + special_chars
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
 
#def healthchk():


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
                                            'ip','nmcli','bond','kvm','kcompose','git','vim','bash','find','linuxbasic','dd','awk',\
					   'sed','ubuntu','echo','grub','initramfs','zip','pam','nova','cinder','neutron','glance',\
					   'diskio','netio','cputop10','memtop10','login','gpt','iostat','vmstat','iotop','sar','parted','systemd','mod','dracut','mount','pnet','iperf','ascii','hexdump','lamp','objdump','dline','ckernel','mysql','nginx','virsh','chntpw','time','yum','nic','newline','regularExp','nfs','kdump','losetup','xxd','dline2','ethtool','grep','dmesg','gcc','trace','c','lvm','kerneldir','wget','process','strace','chage','reboot','gnu','cpu_register','assembly','boot_fail','cpu_cache','src2bin','core_dump','gdb','top','htop','syscall','syscall_instance','launch_ipv6','shell','scp','interrupt','interrupt_instance','kthread','ps','dmidecode','lspci','sysctl','mm','poetry','keepalived','keepalived_nginx','mlag','ruijie','stp','ftp','english','elf','readelf','task_struct','elf_header','elf_program_header','elf_section_header','lsof','ltrace','smartctl','lsscsi','sub_net','arp','selinux','cpu','cpu_mode','cpu_privilege','cpu_component','mem_wr','maps','smaps','proc','iperf3','storage_unit','eg','fio','uname','crun','shadow','port','ipv6','lan','kpath','chpath','psstat','asm_cmd','cpu_flags','date','s2e','docker_image','docker_file','ansible','docker_docker0','ping','net','rootdir','xxxx'], help="Display usage instance")


    parser.add_argument('--item', choices=['main','var', 'printf','macron','struct','vas','mem_consume','cpu_consume','fork','current'], help="Usage: ./mytool.py --show c --item printf")
    parser.add_argument('--option', choices=['basic','cmd','instance_helloworld','instance_add' ], help="Usage: ./mytool.py --show assembly --option basic")
    parser.add_argument('--choice', choices=['concept'], help="Usage: ./mytool.py --show mm --choice concept")

    parser.add_argument("-i", "--install", action='store', dest="pkg",help="install packages on remote host")
    parser.add_argument("-p", "--ping", action="store", dest='ping', help="ping a net such as ping 8.8.8")
    parser.add_argument('-d','--ihost',action='store',dest='host',help='combine with -i')
    parser.add_argument('-z','--zombie',action='store',dest='zombie',help='create a zombie process on loalhost machine')
    parser.add_argument('-P','--passwd',action='store',dest='passwd',help='input a number and create a random passwd')
    parser.add_argument('-w','--web',action='store',dest='hport',help='such as python -m SimpleHTTPServer 8080 or python3 -m http.server 80')
    parser.add_argument('-t','--mytcpdump',action='store',dest='tport',help='such as tcpdump -i any tcp port 80 and host 8.8.8.8')
    parser.add_argument('-u','--udpdump',action='store',dest='uport',help='such as tcpdump -i any udp port 80 and host 8.8.8.8 -vv')
    parser.add_argument('-H', '--healthchk', action='store_true', help='Run Linux health check')
    parser.add_argument('-e', '--SecureEn', action='store_true', help='protect your Linux')
    parser.add_argument("--arpdump", action="store_true", help="such as tcpdump -i any arp -ennl -vv")
    parser.add_argument("--top10", action="store_true", help="{ ps aux | head -1 ; ps aux | sort -k3rn | head ; }")
    parser.add_argument('--host', default=' ', help='send UDP packages to Host name or IP address, default is NUll')
    parser.add_argument('--port', type=int, default=12345, help='send UDP packages to Port number, default is 12345')
    parser.add_argument('--size', type=int, default=1024, help='send UDP packages Message size in bytes, default is 1024 Kb')
    parser.add_argument('--packets-per-thread', type=int, default=3, help='Number of UDP packets per thread, default is 3')
    parser.add_argument('--total-threads', type=int, default=10, help='Total number of threads, default is 10')
    parser.add_argument('--shost', default=' ', help='Scan a special host tcp port, default host is NUll')
    parser.add_argument('--sport', default='', help='Scan a host  speial tcp port like "nc -zv 8.8.8.8 80" or "nmap -sV -p 22 8.8.8.8", default port is NUll')
    parser.add_argument("--cntoeng", nargs=1,help="Modify all Chinese punctuation marks into English punctuation marks, like sed -i 's/：/:/g' test.py")

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
    elif args.show == 'dd':
       print_dd_cmd()
    elif args.show == 'awk':
       print_awk_cmd()
    elif args.show == 'sed':
       print_sed_cmd()
    elif args.show == 'ubuntu':
       print_ubuntu_cmd()
    elif args.show == 'echo':
       print_echo_cmd()
    elif args.show == 'grub':
       print_grub_cmd()
    elif args.show == 'initramfs':
       print_initramfs_cmd()
    elif args.show == 'zip':
       print_zip_cmd()
    elif args.show == 'pam':
       print_pam_cmd()
    elif args.show == 'nova':
       print_nova_cmd()
    elif args.show == 'cinder':
       print_cinder_cmd()
    elif args.show == 'neutron':
       print_neutron_cmd()
    elif args.show == 'glance':
       print_glance_cmd()
    elif args.show == 'diskio':
       print_diskio_cmd()
    elif args.show == 'netio':
       print_netio_cmd()
    elif args.show == 'cputop10':
       print_cputop10_cmd()
    elif args.show == 'memtop10':
       print_memtop10_cmd()
    elif args.show == 'login':
       print_login_cmd()
    elif args.show == 'gpt':
       print_gpt_cmd()
    elif args.show == 'iostat':
       print_iostat_cmd()
    elif args.show == 'vmstat':
       print_vmstat_cmd()
    elif args.show == 'iotop':
       print_iotop_cmd()
    elif args.show == 'sar':
       print_sar_cmd()
    elif args.show == 'parted':
       print_gpt_cmd()
    elif args.show == 'systemd':
       print_systemd_cmd()
    elif args.show == 'mod':
       print_mod_cmd()
    elif args.show == 'dracut':
       print_dracut_cmd()
    elif args.show == 'mount':
       print_mount_cmd()
    elif args.show == 'pnet':
       print_pnet_cmd()
    elif args.show == 'iperf':
       print_iperf_cmd()
    elif args.show == 'ascii':
       print_ascii_cmd()
    elif args.show == 'hexdump':
       print_hexdump_cmd()
    elif args.show == 'lamp':
       print_lamp_cmd()
    elif args.show == 'objdump':
       print_objdump_cmd()
    elif args.show == 'dline':
       print_dline_cmd()
    elif args.show == 'ckernel':
       print_ckernel_cmd()
    elif args.show == 'mysql':
       print_mysql_cmd()
    elif args.show == 'nginx':
       print_nginx_cmd()
    elif args.show == 'virsh':
       print_virsh_cmd()
    elif args.show == 'chntpw':
       print_chntpw_cmd()
    elif args.show == 'time':
       print_time_cmd()
    elif args.show == 'yum':
       print_yum_cmd()
    elif args.show == 'nic':
       print_nic_cmd()
    elif args.show == 'newline':
       print_newline_cmd()
    elif args.show == 'regularExp':
       print_regularExp_cmd()
    elif args.show == 'nfs':
       print_nfs_cmd()
    elif args.show == 'kdump':
       print_kdump_cmd()
    elif args.show == 'losetup':
       print_losetup_cmd()
    elif args.show == 'xxd':
       print_xxd_cmd()
    elif args.show == 'dline2':
       print_dline2_cmd()
    elif args.show == 'ethtool':
       print_ethtool_cmd()
    elif args.show == 'grep':
       print_grep_cmd()
    elif args.show == 'dmesg':
       print_dmesg_cmd()
    elif args.show == 'gcc':
       print_gcc_cmd()
    elif args.show == 'trace':
       print_trace_cmd()
    elif args.show == 'c' and args.item == 'main':
       print_cmain_cmd()
    elif args.show == 'c' and args.item == 'printf':
       print_cprintf_cmd()
    elif args.show == 'c' and args.item == 'macron':
       print_cmacron_cmd()
    elif args.show == 'c' and args.item == 'struct':
       print_struct_cmd()
    elif args.show == 'c' and args.item == 'var':
       print_cvar_cmd()
    elif args.show == 'c' and args.item == 'vas':
       print_cvas_cmd()
    elif args.show == 'c' and args.item == 'mem_consume':
       print_cmem_consume_cmd()
    elif args.show == 'c' and args.item == 'cpu_consume':
       print_ccpu_consume_cmd()
    elif args.show == 'c' and args.item == 'fork':
       print_cfork_cmd()
    elif args.show == 'c' and args.item == 'current':
       print_ccurrent_cmd()
    elif args.show == 'assembly' and args.option == 'basic':
       print_abasic_cmd()
    elif args.show == 'assembly' and args.option == 'cmd':
       print_assembly_cmd()
    elif args.show == 'assembly' and args.option == 'instance_add':
       print_instance_add_cmd()
    elif args.show == 'assembly' and args.option == 'instance_helloworld':
       print_instance_helloworld_cmd()
    elif args.show == 'mm' and args.choice == 'concept':
       print_concept_cmd()
    elif args.show == 'lvm':
       print_lvm_cmd()
    elif args.show == 'kerneldir':
       print_kerneldir_cmd()
    elif args.show == 'wget':
       print_wget_cmd()
    elif args.show == 'process':
       print_process_cmd()
    elif args.show == 'strace':
       print_strace_cmd()
    elif args.show == 'chage':
       print_chage_cmd()
    elif args.show == 'reboot':
       print_reboot_cmd()
    elif args.show == 'gnu':
       print_gnu_cmd()
    elif args.show == 'cpu_register':
       print_cpu_register_cmd()
    elif args.show == 'boot_fail':
       print_boot_fail_cmd()
    elif args.show == 'cpu_cache':
       print_cpu_cache_cmd()
    elif args.show == 'src2bin':
       print_src2bin_cmd()
    elif args.show == 'core_dump':
       print_core_dump_cmd()
    elif args.show == 'gdb':
       print_gdb_cmd()
    elif args.show == 'top':
       print_top_cmd()
    elif args.show == 'htop':
       print_htop_cmd()
    elif args.show == 'syscall':
       print_syscall_cmd()
    elif args.show == 'syscall_instance':
       print_syscall_instance_cmd()
    elif args.show == 'launch_ipv6':
       print_launch_ipv6_cmd()
    elif args.show == 'shell':
       print_shell_cmd()
    elif args.show == 'scp':
       print_scp_cmd()
    elif args.show == 'interrupt':
       print_interrupt_cmd()
    elif args.show == 'interrupt_instance':
       print_interrupt_instance_cmd()
    elif args.show == 'kthread':
       print_kthread_cmd()
    elif args.show == 'ps':
       print_ps_cmd()
    elif args.show == 'dmidecode':
       print_dmidecode_cmd()
    elif args.show == 'lspci':
       print_lspci_cmd()
    elif args.show == 'sysctl':
       print_sysctl_cmd()
    elif args.show == 'poetry':
       print_poetry_cmd()
    elif args.show == 'keepalived':
       print_keepalived_cmd()
    elif args.show == 'keepalived_nginx':
       print_keepalived_nginx_cmd()
    elif args.show == 'mlag':
       print_mlag_cmd()
    elif args.show == 'ruijie':
       print_ruijie_cmd()
    elif args.show == 'stp':
       print_stp_cmd()
    elif args.show == 'ftp':
       print_ftp_cmd()
    elif args.show == 'english':
       print_english_cmd()
    elif args.show == 'elf':
       print_elf_cmd()
    elif args.show == 'readelf':
       print_readelf_cmd()
    elif args.show == 'task_struct':
       print_task_struct_cmd()
    elif args.show == 'elf_header':
       print_elf_header_cmd()
    elif args.show == 'elf_program_header':
       print_elf_program_header_cmd()
    elif args.show == 'elf_section_header':
       print_elf_section_header_cmd()
    elif args.show == 'lsof':
       print_lsof_cmd()
    elif args.show == 'ltrace':
       print_ltrace_cmd()
    elif args.show == 'smartctl':
       print_smartctl_cmd()
    elif args.show == 'lsscsi':
       print_lsscsi_cmd()
    elif args.show == 'sub_net':
       print_sub_net_cmd()
    elif args.show == 'arp':
       print_arp_cmd()
    elif args.show == 'selinux':
       print_selinux_cmd()
    elif args.show == 'cpu':
       print_cpu_cmd()
    elif args.show == 'cpu_mode':
       print_cpu_mode_cmd()
    elif args.show == 'cpu_privilege':
       print_cpu_privilege_cmd()
    elif args.show == 'cpu_component':
       print_cpu_component_cmd()
    elif args.show == 'mem_wr':
       print_mem_wr_cmd()
    elif args.show == 'maps':
       print_maps_cmd()
    elif args.show == 'smaps':
       print_smaps_cmd()
    elif args.show == 'proc':
       print_proc_cmd()
    elif args.show == 'iperf3':
       print_iperf3_cmd()
    elif args.show == 'storage_unit':
       print_storage_unit_cmd()
    elif args.show == 'eg':
       print_eg_cmd()
    elif args.show == 'fio':
       print_fio_cmd()
    elif args.show == 'uname':
       print_uname_cmd()
    elif args.show == 'crun':
       print_crun_cmd()
    elif args.show == 'shadow':
       print_shadow_cmd()
    elif args.show == 'port':
       print_port_cmd()
    elif args.show == 'ipv6':
       print_ipv6_cmd()
    elif args.show == 'lan':
       print_lan_cmd()
    elif args.show == 'kpath':
       print_kpath_cmd()
    elif args.show == 'chpath':
       print_chpath_cmd()
    elif args.show == 'psstat':
       print_psstat_cmd()
    elif args.show == 'asm_cmd':
       print_asm_cmd_cmd()
    elif args.show == 'cpu_flags':
       print_cpu_flags_cmd()
    elif args.show == 'date':
       print_date_cmd()
    elif args.show == 's2e':
       print_s2e_cmd()
    elif args.show == 'docker_image':
       print_docker_image_cmd()
    elif args.show == 'docker_file':
       print_docker_file_cmd()
    elif args.show == 'ansible':
       print_ansible_cmd()
    elif args.show == 'docker_docker0':
       print_docker_docker0_cmd()
    elif args.show == 'ping':
       print_ping_cmd()
    elif args.show == 'net':
       print_net_cmd()
    elif args.show == 'rootdir':
       print_rootdir_cmd()
    elif args.show == 'xxxx':
       print_xxxx_cmd()


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

    elif args.healthchk:
        try:
            # 运行位于当前目录下的 bash 脚本
            subprocess.call(['bash', './bash/CentOS_Check_Script.sh'])
        except subprocess.CalledProcessError as e:
            print("Error running health check script: {}".format(e))
        except OSError:
            print("The script 'bash/CentOS_Check_Script.sh' was not found or cannot be executed.")

    elif args.SecureEn:
        try:
            # 运行位于当前目录下的 bash 脚本
            subprocess.call(['bash', './bash/CentOS_Protective_Script.sh'])
        except subprocess.CalledProcessError as e:
            print("Error running secure Enhance script: {}".format(e))
        except OSError:
            print("The script 'bash/CentOS_Protective_Script.sh' was not found or cannot be executed.")

    elif args.top10:
        try:
            # 运行位于当前目录下的 bash 脚本
            subprocess.call(['bash', './bash/top10.sh'])
        except subprocess.CalledProcessError as e:
            print("Error running top10 script: {}".format(e))
        except OSError:
            print("The script 'bash/top10' was not found or cannot be executed.")

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


