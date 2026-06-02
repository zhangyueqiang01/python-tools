#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_docker_img_create_cmd():
    docker_img_create_cmd = """
############################################################## overview ########################################################################
制作docker镜像的思路：
1、创建程序运行所需的除kernel以外的的完整环境
2、通过docker自带的docker file 功能进行镜像制作

####################################################### 构建只有bash的docker镜像 ##################################################################

1、查看bash指令依赖的动态库文件
ldd /usr/bin/bash

2、 拷贝bash主程序，拷贝所有依赖库
mkdir -p rootfs/{bin,lib64}
cp /usr/bin/bash rootfs/bin/
cp /lib64/libtinfo.so.5 rootfs/lib64/
...

3、编辑Dockerfile文件
[root@ct7_node04 ~]# cat Dockerfile
# 从0开始制作
FROM scratch
# 拷贝提取好的系统文件
COPY rootfs/ /
# 指定默认命令为bash
CMD ["/bin/bash"]

4、 构建与测试
docker build -t centos7-mini-bash:v1 .
docker run -it --rm centos7-mini-bash:v1

##################################################### 构建bash+ls命令的docker镜像 #################################################################
方法同上，把想要添加的程序和库文件添加到rootfs中即可

####################################################### 构建mini os docker镜像 ###################################################################
一个一个复制很麻烦，以下方式快速构建mini os img

1、 创建空根目录
mkdir -p ./fullrootfs

2、 yum初始化安装最小系统到fullrootf
yum install -y --installroot=$(pwd)/fullrootfs centos-release bash coreutils iproute iputils --nogpgcheck
    --installroot=xxx：把软件全部安装到自定义目录，不污染宿主机
    centos-release：系统发行版配置
    coreutils：自带 ls/cat/pwd 等基础命令
    iproute：ip 命令
    iputils：ping 命令

3、编辑Dockerfile文件
[root@ct7_node04 ~]# cat Dockerfile
FROM scratch
COPY fullrootfs/ /
CMD ["/bin/bash"]

4、 构建与测试
docker build -t full-centos7:mini .
docker run -it --rm full-centos7:mini

######################################################### 构建httpd docker镜像 ###################################################################
方法同上：将httpd软件包添加到文件中即可

rm -rf fullrootfs
mkdir fullrootfs
# 把httpd装到自定义根目录
yum --installroot=$(pwd)/fullrootfs install -y httpd bash coreutils iputils iproute --nogpgcheck

[root@ct7_node04 ~]# cat Dockerfile
FROM scratch
COPY fullrootfs/ /
EXPOSE 80
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]

############################################################## others #########################################################################@
# 镜像保存到本地
docker save -o ./httpd-image.tar httpd:latest

# 本地镜像导入到docker
docker load -i ./httpd-image.tar
   """
    print(docker_img_create_cmd) 

