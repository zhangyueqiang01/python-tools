#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_git_cmd():
    print("git usage command:")
    git_cmd = """
	#添加一个特定的目录，比如my_folder
	git add my_folder

	#添加当前目录及其所有子目录中的所有文件
	git add .

	git commit -m "提交信息"
	git push
	git log
	git status

	# 暂存本地更改
	git stash
	
	# 拉取远程仓库的更新
	git pull origin master
	
	# 恢复暂存的更改（如果需要）
	git stash pop

   """
    print(git_cmd)  


def print_lamp_cmd():
    print("lamp 快速搭建方法:")
    lamp_cmd = """

[root@node07 html]#yum install httpd mariadb-server

[root@node07 html]# rpm -qa | grep -i php
php-pdo-5.4.16-43.el7_4.x86_64
php-common-5.4.16-43.el7_4.x86_64
php-5.4.16-43.el7_4.x86_64
php-mysql-5.4.16-43.el7_4.x86_64
php-cli-5.4.16-43.el7_4.x86_64


[root@node07 html]# cat /var/www/html/index.php 
<?php
phpinfo();
?>


#设置mqriadb账号密码
mysql_secure_installation


#数据库

   """
    print(lamp_cmd) 

