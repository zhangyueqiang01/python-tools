#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_kvm_cmd():
    print("kvm usage command:")
    kvm_cmd = """
[磁盘管理]
创建image
qemu-img create -f raw disk.raw 10G
qemu-img create -f qcow2 -b $IMG_DIR/.${BASEVM}.img $IMG_DIR/${NEWVM}.img &> /dev/null

镜像格式转换
qemu-img convert -f qcow2 -O qcow2 src.img dst-convert.img

镜像压缩
qemu-img convert -c -f qcow2 -O qcow2 src.img dst-compress.qcow2

镜像加密
qemu-img convert -o encryption -f qcow2 -O qcow2 src.qcow2 dst-encrypt.qcow2

查看镜像信息
qemu-img info dst-compress.qcow2

镜像扩容
qemu-img resize test.qcow2 +10G
growpart /dev/vda 1
xfs_growfs /dev/vda1；resize2fs /dev/sda1

写入/写出磁盘中的文件
virt-copy-out -d ct7_node06 /root/zyq /tmp/
virt-copy-in -d ct7_node06 /tmp/test.xml /root/

查看镜像里的磁盘分区信息
virt-filesystems -a centos7.qcow2

将磁盘分区挂载到本地
guestmount -d <vm name> -m <镜像内的磁盘分区> <宿主机上的挂载目录>
guestmount -d ct7_node06 -m /dev/sda1 /mnt/test
guestmount -a <qcow2镜像文件> -m <镜像内的磁盘分区> <宿主机上的挂载目录>

将磁盘分区卸载
guestunmount /mnt/ 或者 umount /mnt/

[虚拟机管理]
virsh list 
virsh list --all
virsh console domainID
virsh console vmID
virsh dumpxml vmID
virsh dumpxml domain-name/vm

# 使用 virsh 命令重启虚拟机
virsh reboot ct7_node09

# 使用 virsh 命令强制关闭虚拟机，然后再启动
virsh destroy ct7_node09
virsh start ct7_node09

   """
    print(kvm_cmd)  


def print_python27_cmd():
    print("python27 usage command:")
    python27_cmd = """
python27 -s
   """
    print(python27_cmd)  

def print_python3_cmd():
    print("python3 usage command:")
    python3_cmd = """
python3 -s
   """
    print(python3_cmd) 

def print_clan_cmd():
    print("clan usage command:")
    clan_cmd = """
clan -s
   """
    print(clan_cmd)  

def print_html_cmd():
    print("html usage command:")
    html_cmd = """
html -s
   """
    print(html_cmd)  

def print_css_cmd():
    print("css usage command:")
    css_cmd = """
css -s
   """
    print(css_cmd)  
