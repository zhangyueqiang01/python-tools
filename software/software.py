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

def print_awk_cmd():
    print("awk usage command:")
    awk_cmd = """
#例子
awk '{print $0}' file    #打印所有列
awk '{print $1}' file  #打印第一列
awk '{print $1, $3}' file   #打印第一和第三列
cat file | awk '{print $3, $1}'   #打印第三列和第一列，注意先后顺序。
cat file | awk '{print $3, $NF}' #打印第三列和最后一列
awk -F ":" '{print $1, $3}' /etc/passwd  #以“:”为分隔符分割列，然后打印第一列和第三列awk -F ":" '/root/ {print $0}' /etc/passwd #匹配有root的行 


#打印某列：
awk '{print $1}' filename

#使用分隔符打印某列：
awk -F',' '{print $2}' filename

#打印特定行：
awk 'NR==5' filename
#这将打印filename文件的第5行。

#打印特定行范围：
awk 'NR>=3 && NR<=5' filename
#这将打印filename文件的第3行到第5行。

#根据条件过滤行：
awk '$3 > 50 {print}' filename
#这将打印filename文件中第三列大于50的行。

#自定义输出格式：
awk '{printf "%-10s %-10s\n", $1, $2}' filename
#这将以指定的格式打印filename文件的第一列和第二列。

#去掉第一行
ps aux | awk 'NR >1 {print $0}'

#执行脚本文件：
awk -f script.awk filename
#这将执行名为script.awk的脚本文件对filename进行处理。


#awk语法格式
‘BEGIN { cmd; ... cmd; }   #读取文件之前的操作
            { cmd; ... cmd; }    #每一行都进行的操作
            { cmd; ... cmd; }    #每一行执行的第二个操作，会换一行输出
...                                      #以此类推
条件判断 || /regex/ { cmd; ... cmd; }    #匹配到的行进行的操作
...                                      #以此类推
END { cmd; ... cmd; }’      #读取文件之后进行的操作
   """
    print(awk_cmd)  

def print_sed_cmd():
    print("sed usage command:")
    sed_cmd = """
#替换文本：
sed 's/old_text/new_text/' filename

#全局替换：
sed 's/old_text/new_text/g' filename

#从指定行开始替换：
sed '3s/old_text/new_text/' filename

#从指定行范围替换：
sed '3,5s/old_text/new_text/' filename

#保存修改到原文件：
sed -i 's/old_text/new_text/' filename

#仅打印替换后的文本：
sed -n 's/old_text/new_text/p' filename

#使用正则表达式进行替换：
sed 's/regex_pattern/new_text/' filename

#删除行：
sed '/pattern_to_match/d' filename

#插入行：
sed '3i\New_line_text' filename

#追加行：
sed '3a\New_line_text' filename
   """
    print(sed_cmd)  

def print_ubuntu_cmd():
    print("ubuntu dpkg command usage:")
    ubuntu_cmd = """
#更新软件包列表：
sudo apt update
这会更新本地软件包索引，使系统能够获取到最新的软件包信息。

#升级已安装的软件包：
sudo apt upgrade
这会升级系统中已安装的所有软件包到最新版本。

#安装软件包：
sudo apt install package_name
用具体的软件包名称替换 package_name，可以安装指定的软件包。

#删除软件包：
sudo apt remove package_name
这会从系统中删除指定的软件包，但保留其配置文件。

#完全删除软件包：
sudo apt purge package_name
这会从系统中删除指定软件包及其相关的配置文件。

#搜索软件包：
apt search search_term
用具体的搜索词替换 search_term，可以搜索软件包。

#显示软件包信息：
apt show package_name
这会显示有关特定软件包的详细信息。

#列出已安装的软件包：
apt list --installed
这会列出系统中已安装的所有软件包。

#查看软件包中有哪些文件
dpkg -L package_name

#查看某个文件属于哪个软件包
dpkg -S file_name
   """
    print(ubuntu_cmd)  

def print_echo_cmd():
    print("echo usage command:")
    echo_cmd = """
# 输出红色文本
echo -e "\e[31mThis is red text\e[0m"

# 输出绿色文本
echo -e "\e[32mThis is green text\e[0m"

# 输出黄色文本
echo -e "\e[33mThis is yellow text\e[0m"

# 输出蓝色文本
echo -e "\e[34mThis is blue text\e[0m"

# 输出洋红色文本
echo -e "\e[35mThis is magenta text\e[0m"

# 输出青色文本
echo -e "\e[36mThis is cyan text\e[0m"

# 输出白色文本
echo -e "\e[37mThis is white text\e[0m"

# 输出彩色文本
echo -e "\e[91mThis is bright red text\e[0m"
echo -e "\e[92mThis is bright green text\e[0m"
echo -e "\e[93mThis is bright yellow text\e[0m"
echo -e "\e[94mThis is bright blue text\e[0m"
echo -e "\e[95mThis is bright magenta text\e[0m"
echo -e "\e[96mThis is bright cyan text\e[0m"
echo -e "\e[97mThis is bright white text\e[0m"

# 输出背景色
echo -e "\e[41mThis has red background\e[0m"
echo -e "\e[42mThis has green background\e[0m"
echo -e "\e[43mThis has yellow background\e[0m"
echo -e "\e[44mThis has blue background\e[0m"
echo -e "\e[45mThis has magenta background\e[0m"
echo -e "\e[46mThis has cyan background\e[0m"
echo -e "\e[47mThis has white background\e[0m"

#在这些示例中，\e[xm 是ANSI转义码，其中x是数字，代表不同的颜色和样式。例如，31表示红色，32表示绿色，33表示黄色，依此类推。\e[0m 用于重置颜色设置，以确保后续输出不受影响。
   """
    print(echo_cmd)  

def print_grub_cmd():
    print("grub usage command:")
    grub_cmd = """
ovs -s
   """
    print(grub_cmd)  

def print_initramfs_cmd():
    print("initramfs usage command:")
    initramfs_cmd = """
ovs -s
   """
    print(initramfs_cmd)  

def print_zip_cmd():
    print("zip usage command:")
    zip_cmd = """
ovs -s
   """
    print(zip_cmd)  

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
