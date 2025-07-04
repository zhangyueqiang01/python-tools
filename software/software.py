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

# 用 dd 命令备份 MBR
dd if=/dev/sda of=/root/sda_mbr.img count=1 bs=512

bs=N：设置单次读入或单次输出的数据块（block）的大小为 N 个字节。当然也可以使用 ibs 和 obs 选项来分别设置。
ibs=N：单次读入的数据块（block）的大小为 N 个字节，默认为 512 字节。
obs=N：单次输出的数据块（block）的大小为 N 个字节，默认为 512 字节。
count=N：表示总共要复制 N 个数据块（block）

# 使用dd命令直接修改MBR最后两个字节(备份MBR后操作)
dd if=/dev/zero of=/dev/vda bs=1 seek=510 count=2 conv=notrunc
	seek=510：从输出文件的第510字节开始，即写入MBR的倒数两个字节。
	  seek=510K,如果这么写代表从文件的第510K字节开始
	count=2：指定写入两个字节。
	conv=notrunc：表示不截断输出文件，这样 dd 命令在写入两个字节时不会影响文件的其他部分。

#替换MBR中的分区表
dd if=/dev/zero of=/dev/vda bs=1 seek=446 count=64 conv=notrunc

# 将grub中的core.img替换为全0
dd if=/dev/zero of=/dev/vda bs=512 seek=1 count=2023

# 复制grub中的core.img文件
dd if=/dev/vda of=/core.img bs=512 skip=1 count=2023

# 向磁盘上写一个大文件, 来看写性能
dd if=/dev/zero of=testfile bs=1G count=2 oflag=direct 
  oflag=direct：绕过文件系统缓存，直接写入磁盘。
 
# 从磁盘上读取一个大文件, 来看读性能
dd if=testfile of=/dev/null bs=1G count=2 iflag=direct 
  iflag=direct：绕过缓存，直接从磁盘读取。

# 利用 /dev/urandom 进行格式化
dd if=/dev/urandom of=/dev/sda

# 制作启动盘
dd if=mycentos.iso of=/dev/sdb

# 备份 /dev/sda 盘
dd if=/dev/sda of=./sda.img
dd if=/root/sda.img of=/dev/sdb

# 使用 gzip 压缩算法配合 dd 命令来备份 /dev/sda 盘
dd if=/dev/sda | gzip > of=./sda.img.gz

# 更换 bzip2 压缩算法配合 dd 命令再来实现一遍上面示例的效果
dd if=/dev/sda | bzip2 > disk.img.bz2
bzip2 -dc /root/sda.img.gz | dd of=/dev/sdb

# 向磁盘指定的位置写入指定的数据
echo -n  "66666" | dd if=/dev/stdin of=/root/disk.img bs=1024 count=1 seek=513 conv=notrunc
	# 如果是向文件系统的data block中写入数据，需要重新挂载文件系统，或者执行以下命令查看效果
	sync
	  # 将修改同步到磁盘上
	echo 3 > /proc/sys/vm/drop_caches
	    # 本指令为清除内存中的缓存，包括页缓存（实际文件内容）、inode 缓存和目录项缓存,重新从磁盘读取数据
		1：清除页缓存（Page Cache），即文件的实际内容缓存。
		2：清除目录项和 inode 缓存（dentry 和 inode cache），即文件系统的元数据缓存。
		3：同时清除页缓存和目录项、inode 缓存。
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

# Win文本文件转换成Linux文本文件
sed -i 's/\\r$//' windowsfile.txt

# 将文件中的 "\\" 替换为 "\\\\"
sed 's/\\\\/\\\\\\\\/g' filename
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

def print_pam_cmd():
    print("pam usage :")
    pam_cmd = """
#########################
#模块类型（module-type）#
#########################
auth： 主要负责用户身份验证，包括检查用户名和密码是否匹配等。但是，并非仅限于用户名和密码，它还可以执行其他验证方式，如基于证书、指纹等。
account： 这一部分主要处理用户账号的状态，例如检查账号是否被禁用、过期等。
password： 负责用户密码的管理，包括密码的修改、过期策略等。
session： 这部分控制用户登录会话的行为，包括在用户登录时设置环境变量、挂载文件系统等。
-type： 表示因为缺失而不能加载的模块将不记录到系统日志,对于那些不总是安装在系统上的模块有用

#############
#control字段#
#############
required：如果模块返回失败，整个身份验证链将立即失败。这是最常见的控制字段，表示该模块的成功是必要的，如果失败则认证失败。
requisite：与required类似，但如果此模块失败，PAM会立即终止身份验证链，而不会执行后续的模块。如果模块成功，则身份验证链继续。
sufficient：
如果模块返回成功，PAM将立即返回成功，不会再执行后续的模块。
如果sufficient模块失败，就继续。
optional：此模块的成功或失败不会影响最终的身份验证结果。通常用于附加功能或日志记录。
include：允许在当前配置中包含其他PAM配置文件。这允许模块的重用和模块的共享。（auth对auth；account对account）
substack ：用于包含其他PAM配置文件中的规则。（auth对auth；account对account）

#######################
#required  VS  request#
#######################
required：
如果模块返回失败，整个身份验证链将立即失败，但是会继续执行后续的模块。
如果 required 模块成功，则身份验证链继续。

requisite：与 required 类似，
如果此模块失败，PAM 会立即终止身份验证链，而不会执行后续的模块。
如果模块成功，则身份验证链继续。

######################
#include VS  substack#
######################
处理方式：
substack：它将其他配置文件的规则插入到当前位置，并继续处理当前文件中的规则。
include：它将其他配置文件的规则完全替换当前位置的规则，并且不会再处理当前文件中的规则。
适用场景：
substack：适用于需要在当前位置插入其他规则，并且仍然需要继续处理当前文件中的规则的情况。常用于将常用的认证规则或会话规则模块化，并在多个 PAM 配置文件中共享和重用。
include：适用于完全替换当前位置的规则，通常用于将整个模块的规则替换为另一个文件中的规则，或者在不同的环境中切换不同的规则集。

##############
#密码安全策略#
##############
password   required      pam_cracklib.so try_first_pass retry=6 minlen=8 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1 enforce_for_root
   """
    print(pam_cmd)  

def print_grub_cmd():
    grub_cmd = """

######################################## gurb映像的构成 ###############################################

grub1
+-----------------------------------------------------------------------+
| boot.img   |   core.img   |  |   |  modules   |   |  modules  |       |
| (stage1)   |  (stage1.5)  |  |   | (stage2)   |   |  (stage2) |       |
+-----------------------------------------------------------------------+
| 1 sector   | 2043 sectors    |           Partion 1            | 
|            |                 |                                |

core.img
+---------------------------------------------------------------------------------------------------------------------------+
| bootloader |  decompression  | compressed kernel image |   disk    |     mbr     |   filesystem  |  secondary bootloader  |
| stage1.5   |    code         |                         | drivers   |   partition |     module    |                        |
|            |                 |                         |  module   |    module   |               |                        |
+---------------------------------------------------------------------------------------------------------------------------+
|1 sector    |   uncompressed  |                         |      compressed                         |    bootloader stage2   |
|            |                 |                         |                                         |                        |


######################################## troubleshooting ###############################################

# 在MBR与MBR后面的空闲空间中安装grub，安装grub1与grub1.5 stage
grub2-install --boot-directory=/disk/boot /dev/vdb 
--boot-directory 一般不用手动指定，使用默认即可

# 创建grub.cfg文件
grub2-mkconfig -o /boot/grub2/grub.cfg

# grub.cfg文件丢失后进行修复，相关文件可以自动补全
grub > ls
grub > set root='hd0,msdos1'
grub > linux16 /vmlinuz-3.10.0-514.el7.x86_64 root=/dev/mapper/cl-root
grub > initrd16 /initramfs-3.10.0-514.el7.x86_64.img

# 手动进入救援模（将故障系统盘作为数据盘挂载到正常的Linux上，然后再将根切换到故障盘，前提是故障盘中的分区和根文件系统必须是正常的）
    mount /dev/vdb /mnt
    mount --bind /proc /mnt/proc
    mount --bind /dev /mnt/dev
    mount --bind /sys /mnt/sys
    chroot /mnt

# 大面积systemd服务启动报错
    1）在grub界面按e选择进入指定内核的编辑模式
    2）在linux16行末尾添加systemd.debug-shell=1，CRTL+x系统启动
    启用该参数后，在系统启动时，systemd 会在 tty9（即第 9 个终端）上启动一个 root 权限的 shell，不需要密码即可访问(Ctrl+Alt+F9)。
    通过 systemctl list-jobs 去分析什么服务导致getty@tty1.service没有启动
	getty@tty1.service 启动 tty1 进一步启动 login 程序

		
######################################## others ###############################################

# 查看mbr
dd if=/dev/sda of=/tmp/sda_mbr.img count=1 bs=512
hexdump -C /tmp/sda_mbr.img

# 设置50秒的倒计时
set timeout=50

# 默认按照menuentry的顺序启动对应的内核

# 设置默认启动条目
sudo grub2-set-default 'Linux Kernel 4.19.0'
# 对应grub.cfg中menuentry后面的引号中的内容
# 不能在menuentry中直接使用default来设置默认启动项

# efi模式下(GPT分区)grub.cfg文件存放路径
/boot/efi/EFI/redhat/grub.cfg

# grub设置密码
[root@node09 ~]# grub2-setpassword 
Enter password: 
Confirm password: 
[root@node09 ~]# 

# grub cmdline 向内核传递的常见相关参数解读
root=：指定根文件系统的位置。
ro：以只读方式挂载根文件系统。
quiet：禁用大部分启动信息输出。
splash：启用启动屏幕。
nomodeset：禁用内核模式设置（KMS）。
acpi=off：禁用ACPI（高级配置和电源接口）。
net.ifnames=0：禁用基于设备路径的网络接口命名规则，使网络接口使用传统的命名方式（例如 eth0、eth1），而不是基于硬件位置的名称（例如 enp0s3）。
consoleblank=600：设置控制台空闲600秒（10分钟）后屏幕变黑。
console=tty0：将内核消息输出到第一个虚拟控制台（通常是显示器上的文本控制台）。
console=ttyS0,115200n8：将内核消息输出到串行端口 ttyS0，波特率为115200，8个数据位，无校验位，1个停止位（115200n8）。
spectre_v2=off：禁用对Spectre v2漏洞的缓解措施。这些缓解措施通常用于防止通过分支预测漏洞进行的攻击。
nopti：禁用页表隔离（Page Table Isolation，PTI）功能，用于缓解Meltdown漏洞。这可能会提高性能，但会增加系统的安全风险。
crashkernel=auto：为崩溃转储保留内存。通常在发生系统崩溃时，用于转储内存内容以便于分析崩溃原因。
spectre_v2=retpoline：启用Retpoline（“Return Trampoline”）缓解措施来防止Spectre v2漏洞攻击。
init：参数指定内核启动后要运行的初始化程序（init process）。这个程序负责启动和管理系统的各个服务和进程。通常情况下，这个初始化程序是 init 或 systemd。
rd.break: 此参数回在启动过程中，中断chroot到真正的根文件系统，停留在初始的initramfs文件系统中，对于修复系统非常有用，如下所示，就可以进行系统修复操作了。
    mount -o remount,rw /sysroot
    mount --bind /dev /sysroot/dev (sys、proc等目录)
    chroot /sysroot
net.ifnames=0:这是用来禁用一致性网络设备命名法（predictable network interface names）,设置 net.ifnames=0 会禁用这种新命名方式，使系统恢复使用传统的 ethX 命名规则。
biosdevname=0:这是用来禁用 biosdevname 工具对网络接口名称的影响。biosdevname 是一个工具，它根据设备的 BIOS 或固件中的信息来命名网络接口，通常会生成类似 em1、p2p1 的接口名称。
设置 biosdevname=0 会禁用这种命名方式，避免 BIOS 层面的网络接口命名干扰,通常会结合 net.ifnames=0 一起使用。
   """
    print(grub_cmd)  

def print_initramfs_cmd():
    print("initramfs usage command:")
    initramfs_cmd = """
#查看initramfs
lsinitrd initramfs

#解压initramfs
/usr/lib/dracut/skipcpio initramfs-3.10.0-229.el7.x86_64.img | zcat | cpio -ivd

#手动创建initramfs
find . | cpio -o -H newc | gzip -9 > /tmp/test.img


#向initram中添加驱动
vi /etc/dracut.conf
# additional kernel modules to the default  
add_drivers+="xen-blkfront xen-netfront virtio_blk virtio_scsi virtio_net virtio_pci virtio_ring virtio"  
……     

dracut -f /boot/initramfs-2.6.32-573.8.1.el6.x86_64.img

# initramfs 中的init是载入initramfs文件并解压后自动执行的程序

# initramfs文件中的init实例:
[root@novlm mnt]# cat init 
#!/bin/bash
 
/bin/echo 'Welcome to self defined initramfs (Initramfs)!'

export PATH=/bin:/usr/bin:/usr/sbin
mount -n -t devtmpfs udev /dev
mount -t proc none /proc
mount -t sysfs none /sys
/bin/insmod /lib/virtio.ko
/bin/insmod /lib/virtio_ring.ko
/bin/insmod /lib/virtio_pci.ko
/bin/insmod /lib/virtio_blk.ko
/bin/insmod /lib/libcrc32c.ko
/bin/insmod /lib/xfs.ko

echo 'Starting Switch Root...'

/bin/mount /dev/vda3 /sysroot/
/bin/mount --bind /proc /sysroot/proc
/bin/mount --bind /dev /sysroot/dev
/bin/mount --bind /sys /sysroot/sys
exec chroot /sysroot/ /usr/lib/systemd/systemd
# 只需要补充完相关的驱动命令以及库文件，即可通过这段脚本启动我们真正的根文件系统

# 真实环境真正的根文件系统从grub cmdline中的root变量中读取

# mount 选项解读：
mount: 挂载一个文件系统。
-t sysfs: 指定要挂载的文件系统类型为 sysfs。
none: 表示没有特定的设备需要挂载，因为 sysfs 是一个虚拟文件系统，不依赖于物理设备。
/sys: 挂载点，表示将 sysfs 文件系统挂载到 /sys 目录。
真正的根挂载dev proc sys等内存文件系统之前需要先进行这些文件系统的挂载
init中的二进制文件建议写绝对路径（虽然导入PATH环境变量后也可以直接总变量中搜索二进制程序）
   """
    print(initramfs_cmd)  

def print_nova_cmd():
    print("nova usage command:")
    nova_cmd = """
			####################
			# nova相关组件简介 #
			####################
			
nova-api：用户通过 API 请求创建云主机。nova-api 接收请求并进行初步处理。
nova-scheduler：nova-api 将请求传递给 nova-scheduler。nova-scheduler 根据可用资源和调度策略选择一个合适的计算节点（compute node）来运行云主机。
nova-conductor：nova-scheduler 选择计算节点后，将任务信息传递给 nova-conductor。nova-conductor 负责与数据库交互，记录云主机的状态和其他相关信息，并将操作请求传递给相应的计算节点。
nova-compute：被选中的计算节点上的 nova-compute 组件接收到 nova-conductor 的请求，负责管理虚拟机的生命周期，如创建、删除、停止、启动等。它直接与虚拟化技术（如KVM、Xen等）进行交互，执行实际的虚拟机操作。
nova-network（已被Neutron取代）：负责管理网络资源，如分配IP地址、创建虚拟网络等。目前，大多数网络管理功能已经被更先进和灵活的Neutron组件所取代。
nova-novncproxy 和 nova-spicehtml5proxy：分别提供基于VNC和SPICE协议的远程控制台访问，允许用户通过浏览器远程管理虚拟机。
nova-consoleauth：负责验证和管理远程控制台访问的身份验证令牌。
nova-cert：处理与X.509证书相关的操作（例如EC2接口中的签名），目前已逐步被弃用。
nova-placement：跟踪和管理计算资源的分配和使用情况，为调度器提供资源信息和决策支持。

			################
			# nova常用指令 #
			################
# 磁盘挂载卸载
nova volume-detach ECS_ID DISK_ID
nova volume-attach NEW_ECS_ID DISK_ID

# 冷迁移虚拟机
nova migrate VM_ID

# 手动选择一台主机
nova migrate VM_ID --host dsthost

# 热迁移虚拟机
nova live-migration VM_ID

# 查看虚拟机信息
nova show VM_ID
openstack server show VM_ID

# 查看主机操作记录
nova instance-action-list VM_ID

# 为虚拟机分配vnc连接
nova get-vnc-console VM_ID novnc

# 关闭虚拟机
nova stop VM_ID

# 调整虚拟机规格
nova resize-confirm VM_ID

			##################################
			# 合营资源池主机创建失败排障方法 #
			##################################

# 查看虚拟机 action 对应的 req_id
nova instance-action-list uuid 

# 根据 req_id 查看操作详情
nova –service-type compute-ext instance-action uuid req_id 

# nova-sheduler日志路径：
/var/log/fusionsphere/component/nova-scheduler/*

# 如果调度到pod信息，但在被级联层未查到虚拟机创建信息，查看nova-proxy日志：

#查询nova-proxy主节点：
cps template-instance-list --service nova nova-proxy00H

# nova-proxy日志路径:
/var/log/fusionsphere/component/nova proxy00H/*

#获取被级联层虚拟机uuid：
nova list --all-t [--deleted] --name uuid (级联层)
//[--deleted]查询环境中已经删除的虚机

#获取操作的req_id：
nova instance-action-list uuid (被级联层)

# 根据req_id获取操作详情：
nova --service-type compute-ext instance-action uuid (被级联层)  req_id

# 如果未调度到CNA节点，需要查看nova-scheduler或nova-conductor日志：
/var/log/fusionsphere/component/nova-scheduler/*
/var/log/fusionsphere/component/nova-conductor/*

# 如果调度到CAN节点，查看nova-compute日志：
/var/log/fusionsphere/component/nova-compute/*

# 查看专属云主机id对应的物理服务器主机名称
nova dec-host-list | grep 3fb888b6-7907-483e-bff9-79e94e7773e7（专属云主机ID）
   """
    print(nova_cmd)  

def print_cinder_cmd():
    print("cinder usage command:")
    cinder_cmd = """
# 查看卷详情
openstack volume show <volume-id>
cinder show <volume-id>

# 查询该卷的操作历史
grep <volume-id> /var/log/cinder/cinder-volume.log
zgrep <volume-id> /var/log/cinder/*.gz

-- 查看卷挂载过的服务器
SELECT * FROM volume_attachment WHERE volume_id = '<volume-id>';

-- 在 nova 数据库中查卷关联
SELECT * FROM block_device_mapping WHERE volume_id = '<volume-id>';

# 创建一个卷 
cinder create --display-name myvolume --size 10

# 删除一个卷
cinder delete <volume-id>

# 创建卷快照
cinder snapshot-create --display-name mysnap <volume-id>

# 查看快照列表
cinder snapshot-list

# 从快照创建卷
cinder create --snapshot-id <snapshot-id> --size 10

# 附加卷到实例
cinder attach <volume-id> <instance-id> <mountpoint>

# 卸载卷
cinder detach <volume-id>

# 修改卷名称或描述
cinder update --display-name newname --display-description "new description" <volume-id>

################################### tips #############################################

建议：使用 openstack 替代 cinder,现代 OpenStack 更推荐使用统一接口：
openstack volume list
openstack volume create
openstack volume delete
openstack snapshot create
   """
    print(cinder_cmd)  

def print_glance_cmd():
    print("glance usage command:")
    glance_cmd = """
# 创建私有镜像
glance --debug image-create --name "Michael_test" \
--container-format bare \
--disk-format raw \
--visibility private \
--protected False \
--property hw_qemu_guest_agent=yes \
--property os_type="linux" \
--property os_distro="Redhat" \
--property os_version="7.4" \
--property hw_vif_multiqueue_enabled=true \
--property ctcm_enabled=true \
--architecture x86_64 \
--property image_version="R1" \
--owner TEST_OWNER_ID \
--progress

# 给用户删除镜像的权利
glance image-update --protected False IMAGE_ID

# 上传镜像到后端存储中
glance image-upload --file CentOS7-40G.raw --progress --backend ceph_ssd 0b53da25-8f5a-435e-87a0-5fce0caf0987


# 修改镜像的标签
glance image-update --property __support_xen=true IMAGE_ID
glance image-update --property __support_kvm=true IMAGE_ID
glance image-update --property __support_highperformance=true 4IMAGE_ID

# 修改镜像拥有者
glance image-update --owner USER_ID IMAGE_ID

# 合营修改私有镜像磁盘属性
glance image-update  --min-disk 300 49431953-eabf-4d63-af49-d62e41635c47 

# 合营修改私有镜像写保护
glance image-update --protected=false <IMAGE_ID>


###############
#合营镜像制作示例#
###############
export OS_IMAGE_API_VERSION=1
glance image-create --owner eda9b53213884b49b3b96fc5f6a33730 --name "Anolis" --disk-format zvhd2 --container-format bare --min-disk 100 --min-ram 0 --is-public False --property __image_location=10.203.45.130:443:bj1-uds-public-image-bucket-001:Anolis --property __image_source_type=uds --property __os_type=Anolis --property __os_version="8" --property __lazyloading=true --property virtual_env_type=FusionCompute
glance image-create --owner eda9b53213884b49b3b96fc5f6a33730 --name "GPU Centos7-Gpu20220914 for G5" --disk-format zvhd2 --container-format bare --min-disk 40 --min-ram 0 --property __image_location=10.203.45.130:443:bj1-uds-public-image-bucket-001:Centos-Gpu20220914 --property __image_source_type=uds --property __os_type=Linux --property __platform="Linux" --property __os_version="Centos7" --property virtual_env_type=FusionCompute --property __imagetype=private --property __os_bit=64 --property __isregistered=true --property __os_feature_list='{"onekey_resetpasswd": "true"}' --property __support_kvm_gpu_type=V100_vGPU --property __account_code=Linux --property __lazyloading=true

+--------------------------------+----------------------------------------------------------+
| Property                       | Value                                                    |
+--------------------------------+----------------------------------------------------------+
| Property '__image_location'    | 10.203.45.130:443:bj1-uds-public-image-bucket-001:Anolis |
| Property '__image_source_type' | uds                                                      |
| Property '__isregistered'      | false                                                    |
| Property '__lazyloading'       | true                                                     |
| Property '__os_type'           | Anolis                                                   |
| Property '__os_version'        | 8                                                        |
| Property 'virtual_env_type'    | FusionCompute                                            |
| checksum                       | None                                                     |
| container_format               | bare                                                     |
| created_at                     | 2023-04-15T04:54:07.259802                               |
| deleted                        | False                                                    |
| deleted_at                     | None                                                     |
| disk_format                    | zvhd2                                                    |
| id                             | 417b24ec-6479-49dd-8839-a7620bb19713                     |
| is_public                      | False                                                    |
| min_disk                       | 100                                                      |
| min_ram                        | 0                                                        |
| name                           | Anolis                                                   |
| owner                          | eda9b53213884b49b3b96fc5f6a33730                         |
| protected                      | False                                                    |
| size                           | 0                                                        |
| status                         | queued                                                   |
| updated_at                     | 2023-04-15T04:54:07.259814                               |
| virtual_size                   | None                                                     |
+--------------------------------+----------------------------------------------------------+

export OS_IMAGE_API_VERSION=2
touch 417b24ec-6479-49dd-8839-a7620bb19713.zvhd2
glance image-upload 417b24ec-6479-49dd-8839-a7620bb19713 --file 417b24ec-6479-49dd-8839-a7620bb19713.zvhd2 
glance image-update --protected false --property __platform=linux --property __imagetype=private --property __os_bit=64 --property __isregistered=true 417b24ec-6479-49dd-8839-a7620bb19713
glance image-update --property __support_xen=true 417b24ec-6479-49dd-8839-a7620bb19713
glance image-update --property __support_kvm=true 417b24ec-6479-49dd-8839-a7620bb19713
glance image-update --property __support_highperformance=true 417b24ec-6479-49dd-8839-a7620bb19713

glance image-update --owner 08faa3231302a07f2f76c01101619dd2 417b24ec-6479-49dd-8839-a7620bb19713
glance image-update --owner eda9b53213884b49b3b96fc5f6a33730 417b24ec-6479-49dd-8839-a7620bb19713


BJ-AZ01-SRV-CascadingOpenstack-001:/home/fsp # glance image-show fc86f110-c36a-4c69-aba9-698f7ee30209
BJ-AZ01-SRV-CascadingOpenstack-001:/home/fsp # glance image-show 417b24ec-6479-49dd-8839-a7620bb19713
BJ-AZ01-SRV-CascadingOpenstack-001:~ # glance image-show 417b24ec-6479-49dd-8839-a7620bb19713

# 北京2资源池切换私有镜像无法选中问题，可能是私有镜像中有EFI分区，需要给镜像添加uefi标签
glance image-update --property hw_firmware_type=uefi <image-id>
glance image-update --remove-property  hw_firmware_type <image-id>	//删除标签
   """
    print(glance_cmd)  


def print_keepalived_cmd():
    keepalived_cmd = """
############################## DESCRIPTION ##################################

Keepalived 最初是为 LVS（Linux Virtual Server）设计的，用于实现主备热备（例如主服务器宕机后自动切换到备用服务器）。
它现在也常用于与 Nginx、HAProxy、Redis、MySQL 等服务结合，实现 VIP 的自动漂移和服务不中断。

核心功能组成：
| 模块                                           | 作用说明
| ---------------------------------------------- | -------------------------------------------------
| **VRRP（Virtual Router Redundancy Protocol）** | 实现 IP 浮动（Virtual IP，VIP）和主备切换，是 Keepalived 的核心模块。
| **Health Check（健康检查）**                   | 检测本地服务是否存活，如 Nginx、HAProxy、MySQL 等。可自定义脚本进行检测。
| **LVS管理**（可选）                            | 管理 Linux 内核中的 LVS 虚拟服务器功能（较老的架构中常用）。

############################### instance ####################################

vip 192.168.2.200
node01 eth1 ip 192.168.0.1
node02 eth1 ip 192.168.0.2

[root@ct7_node01 ~]# yum install  keepalived -y
[root@ct7_node02 ~]# yum install  keepalived -y
[root@ct7_node01 keepalived]# cp /etc/keepalived/keepalived.conf /etc/keepalived/keepalived.conf.bak
[root@ct7_node01 keepalived]# echo > /etc/keepalived/keepalived.conf
[root@ct7_node01 keepalived]# vi /etc/keepalived/keepalived.conf

****** node01 config *******
vrrp_instance VI_1 {
    state MASTER  # 备机上写为 BACKUP
    interface eth1
    virtual_router_id 51
    priority 100  # 备机写 90
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1234
    }
    virtual_ipaddress {
        192.168.2.200
    }
}

***** node02 config******

vrrp_instance VI_1 {
    state BACKUP  # 备机上写为 BACKUP
    interface eth1
    virtual_router_id 51
    priority 90  # 备机写 90
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1234
    }
    virtual_ipaddress {
        192.168.2.200
    }
}

[root@ct7_node01 keepalived]# systemctl start keepalived

############################# verification ##################################

ip a 进行查看，vip 地址在两台主机上都会以子接口的方式显示，关闭其中任何一台主机上的 eth1 网口，vip 都可以 ping 通

3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 74:52:01:01:01:02 brd ff:ff:ff:ff:ff:ff
    inet 192.168.2.1/24 brd 192.168.2.255 scope global eth1
       valid_lft forever preferred_lft forever
    inet 192.168.2.200/32 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::7652:1ff:fe01:102/64 scope link 
       valid_lft forever preferred_lft forever
	   	   
arp -n | grep 200
可以看到 192.168.2.200 对应的 HWaddress 会在 node01 和 node02 两台机器上的 eth1 网卡之间来回切换

############################### caution ####################################

1、默认情况下，keepalived 要求绑定的接口（如 eth1）上至少有一个 非VIP 的已有 IP 地址，用于发送 VRRP 包，否则它会直接退出。

2、master 挂掉后 vip 会漂移到 backup 上 ，master 恢复后 vip 会漂回到 master 上


配置文件参数逐项解读：
| 参数                   | 含义
| ---------------------- | -------------------------------------------------------------------
| `vrrp_instance VI_1`   | 定义一个 VRRP 实例，`VI_1` 是实例名称（可自定义）。一个实例表示一组主备切换逻辑。
| `state MASTER`         | 当前节点初始状态。可为 `MASTER`（主）或 `BACKUP`（备）。Keepalived 会根据优先级等实际情况动态决定谁是主。
| `interface eth0`       | 指定用于绑定 VIP 的网卡接口。这里为 `eth0`，也可写为 `ens33`、`enp3s0` 等别的拥有IP地址的网卡名。
| `virtual_router_id 51` | VRRP 组标识符，同一组中的主备必须保持一致。值范围是 `0–255`，多个 VRRP 实例不能冲突。
| `priority 100`         | 优先级（数值越大越优先）。通常主节点设高值如 `100`，备节点设低值如 `90`。
| `advert_int 1`         | VRRP 通告间隔时间，单位为秒。主节点每隔这个时间广播一次“我还活着”。
| `authentication`       | 验证配置，防止不受信节点加入 VRRP 组。可选 `PASS`（密码）或 `AH`（IPSec AH认证）。
|   └── `auth_type PASS` | 使用明文密码认证方式。
|   └── `auth_pass 1234` | 明文密码（主备节点需一致）。
| `virtual_ipaddress`    | 指定要绑定的虚拟 IP 地址。支持多个 VIP（换行写多个 IP）。VIP 会自动添加到指定接口。

高级参数（可选）：
| 参数                | 含义                                             
| ------------------- | ----------------------------------------------
| `track_script`      | 指定自定义脚本用于健康检查，脚本返回非0表示故障，会自动降权。
| `nopreempt`         | 对于 BACKUP 节点，即使检测到 MASTER 掉线也不自动提升为主，适合双主避免抖动。
| `garp_master_delay` | MASTER 在切换为主之后延迟发送 GARP 报文的时间（防止网络不一致）。

############################### advance ####################################

下面是一个完整的示例，展示如何使用 Keepalived + Nginx 实现高可用的 Web 服务（主备模式 + VIP 浮动）。
./mytool.py --show keepalived_nginx
   """
    print(keepalived_cmd) 


def print_keepalived_nginx_cmd():
    keepalived_nginx_cmd = """
############################## DESCRIPTION ##################################
主机 A：192.168.1.101，作为 MASTER
备机 B：192.168.1.102，作为 BACKUP
虚拟IP（VIP）：192.168.1.100
使用 eth0 网卡
检查 Nginx 是否正常运行，异常时自动切换

########################### 主节点（MASTER）配置 ###########################

文件路径：/etc/keepalived/keepalived.conf

vrrp_script chk_nginx {
    script "/etc/keepalived/check_nginx.sh"
    interval 2
    weight -10
}

vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1234
    }
    virtual_ipaddress {
        192.168.1.100
    }
    track_script {
        chk_nginx
    }
}

########################### 备节点（MASTER）配置 ############################

唯一不同是 state 和 priority：

vrrp_script chk_nginx {
    script "/etc/keepalived/check_nginx.sh"
    interval 2
    weight -10
}

vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 90
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1234
    }
    virtual_ipaddress {
        192.168.1.100
    }
    track_script {
        chk_nginx
    }
}

########################### nginx 检查脚本 ################################

检查脚本 /etc/keepalived/check_nginx.sh

#!/bin/bash
if ! pidof nginx > /dev/null; then
    exit 1
else
    exit 0
fi
该脚本用于检测 Nginx 是否运行。失败会触发优先级下降。

chmod +x /etc/keepalived/check_nginx.sh

########################### 启动流程 ######################################

确保两台机器都已安装并启动 nginx
两台机器都安装 keepalived
将配置文件放入 /etc/keepalived/keepalived.conf
启动服务：
systemctl enable keepalived
systemctl start keepalived

############################ verification ################################

访问 http://192.168.1.100，确认正常响应；
停止主机 A 上的 nginx：
systemctl stop nginx
继续访问 http://192.168.1.100，确认正常响应；

############################# advance ####################################

如需要 LVS 模式、双主模式或使用双网卡的配置示例。
./mytool.py --show LVS

   """
    print(keepalived_nginx_cmd) 


def print_neutron_cmd():
    print("neutron usage command:")
    neutron_cmd = """
# 查看eip的属性信息
neutron floatingip-show EIP_ID
   """
    print(neutron_cmd)  

def print_login_cmd():
    print("login usage command:")
    login_cmd = """
# 快速进行登录方法
source set_env < <(echo  ;echo 1; echo FusionSphere123);TMOUT=0
   """
    print(login_cmd)  

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
