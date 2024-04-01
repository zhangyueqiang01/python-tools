#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_osp_cmd():
    print("OpenStack usage command:")
    osp_cmd = """
[openstack]
openstack catalog list
openstack endpoint list
openstack compute service list
openstack server show 6e18eca1-497b-4071-ab93-0fd905aba22d


[nova]
nova show 6e18eca1-497b-4071-ab93-0fd905aba22d
nova instance-action-list 6e18eca1-497b-4071-ab93-0fd905aba22d
nova get-vnc-console 6e18eca1-497b-4071-ab93-0fd905aba22d novnc
nova volume-attach <instance_id> <volume_id> 
nova volume-detach <instance_id> <volume_id>
nova flavor-show c6.large.2
nova flavor-key c6.large.2 set hw:numa_nodes=2
openstack --os-compute-api-version 2.11 compute service set --disable --disable-reason "Manually disabled" --down compute2 nova-compute


[glance]
qemu-img convert -f qcow2 -O raw CentOS7-40G.qcow2 CentOS7-40G.raw

glance --debug image-create --name "Michael_test" 
--container-format bare 
--disk-format raw 
--visibility private 
--protected False 
--property hw_qemu_guest_agent=yes 
--property os_type="linux" 
--property os_distro="Redhat" 
--property os_version="7.4" 
--property hw_vif_multiqueue_enabled=true 
--property ctcm_enabled=true 
--architecture x86_64 
--property image_version="R1" 
--owner ddcf403cc70a40f2831ec29c06bec3c3 
--progress

glance image-update --owner ownerid imageid
glance image-show imageid
glance image-update --property __support_kvm=true imageid
glance image-upload --file CentOS7-40G.raw --progress --backend ceph_ssd imageid


[neutron]
neutron  quota-update  --loadbalancer  --tenant_id  tenantID
neutron  quota-update  --loadbalancer=10  --tenant_id  tenantID


[cinder]

[Authentication]
source set_env < <(echo  ;echo 1; echo FusionSphere123);TMOUT=0

[CTCloud]
1、kvm架构
Internet——ECS_UI——APICom——级联层cascading——nova proxy——被级联层openstack（POD）——nova-compute——VM

nova instance-action-list uuid
根据req_id查看操作详情
nova --service-type compute-ext instance-action uuid req_id
nova-sheduler日志
/var/log/fusionsphere/component/nova-scheduler/*
如果调度到pod信息，但在被级联层未查到虚拟机创建信息，查看nova-proxy日志
查询nova-proxy主节点：
cps template-instance-list --service nova nova-proxy00H
登录nova-proxy主节点，,查看nova-proxy日志nova-proxy日志
/var/log/fusionsphere/component/nova proxy00H/*

获取被级联层虚拟机uuid
nova list --all-t [--deleted] --name uuid (级联层)
//[--deleted]查询环境中已经删除的虚机
获取操作的req_id
nova instance-action-list uuid (被级联层)
根据req_id获取操作详情
nova --service-type compute-ext instance-action uuid (被级联层)  req_id

日志
/var/log/fusionsphere/component/nova-scheduler/*
/var/log/fusionsphere/component/nova-conductor/*
/var/log/fusionsphere/component/nova-compute/*

过滤
zgrep req-b2dc3cca-2177-4a4c-825d-144d4be17fba /var/log/fusionsphere/component/nova-*/*
zgrep：专门用于搜索压缩的文件，通常是gzip压缩的文件（.gz 后缀），zgrep 也可以在未压缩的文件中过滤，并且语法与标准的 grep 命令非常相似
   """
    print(osp_cmd)  

def print_ceph_cmd():
    print("ceph usage command:")
    ceph_cmd = """
ceph -s
   """
    print(ceph_cmd)  

def print_docker_cmd():
    print("docker usage command:")
    docker_cmd = """
docker image ls
docker pull wcjiang/linux-command
docker ps
docker run --name linux-command -itd -p 9665:3000 wcjiang/linux-command:latest
docker exec -it myweb /bin/bash
docker ps -a
docker rm d45
docker stop d45
docker update --restart=always 容器ID(或者容器名)
docker run -d  -e MYSQL_ROOT_PASSWORD=redhat -p 3306:3306 docker.io/mysql:5.7
docker inspect docker.io/michaelzhangyq/loganalyzer
docker network create db
docker network  ls
docker network  ls --help
docker network inspect db
   """
    print(docker_cmd)  

def print_dd_cmd():
    print("dd usage command:")
    dd_cmd = """

#用 dd 命令备份 MBR
dd if=/dev/sda of=/root/sda_mbr.img count=1 bs=512

bs=N：设置单次读入或单次输出的数据块（block）的大小为 N 个字节。当然也可以使用 ibs 和 obs 选项来分别设置。
ibs=N：单次读入的数据块（block）的大小为 N 个字节，默认为 512 字节。
obs=N：单次输出的数据块（block）的大小为 N 个字节，默认为 512 字节。
count=N：表示总共要复制 N 个数据块（block）


#向磁盘上写一个大文件, 来看写性能
dd if=/dev/zero bs=1024 count=1000000 of=/root/1Gb.file
 
#从磁盘上读取一个大文件, 来看读性能
dd if=/root/1Gb.file bs=64k | dd of=/dev/null
time dd if=/dev/zero bs=1024 count=1000000 of=/root/1Gb.file

#利用 /dev/urandom 进行格式化
dd if=/dev/urandom of=/dev/sda

#制作启动盘
dd if=mycentos.iso of=/dev/sdb

#备份 /dev/sda 盘
dd if=/dev/sda of=./sda.img
dd if=/root/sda.img of=/dev/sdb

#使用 gzip 压缩算法配合 dd 命令来备份 /dev/sda 盘
dd if=/dev/sda | gzip > of=./sda.img.gz

#更换 bzip2 压缩算法配合 dd 命令再来实现一遍上面示例的效果
dd if=/dev/sda | bzip2 > disk.img.bz2
bzip2 -dc /root/sda.img.gz | dd of=/dev/sdb
   """
    print(dd_cmd)  

def print_ovs_cmd():
    print("ovs usage command:")
    ovs_cmd = """
ovs -s
   """
    print(ovs_cmd)  

def print_php_cmd():
    print("php usage command:")
    php_cmd = """
php -s
   """
    print(php_cmd)  

def print_git_cmd():
    print("git usage command:")
    git_cmd = """
git -s
   """
    print(git_cmd)  
