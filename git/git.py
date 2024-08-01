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


