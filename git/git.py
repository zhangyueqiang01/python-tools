#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_git_cmd():
    print("git usage command:")
    git_cmd = """
	git add .
	git commit -m "提交信息"
	git push
	git log
	git status
	git pull origin master   #只同步变化的内容
   """
    print(git_cmd)  


