#!/bin/bash
if [ $# -ne 1 ];then
    echo "用法: $0 进程PID"
    exit 1
fi
PID=$1

echo "==================== 进程基础信息 ===================="
ps -p $PID -o pid,ppid,nlwp,pcpu,state,cmd

echo -e "\n==================== 所有子进程(树形) ===================="
pstree -ap $PID

echo -e "\n==================== 直接子进程列表 ===================="
ps -ef | awk -v ppid=$PID '$3==ppid {print $2,$3,$8}'

echo -e "\n==================== 所有线程列表(TID) ===================="
ps -T -p $PID -o pid,tid,state,pcpu,cmd

echo -e "\n==================== 线程总数 ===================="
echo "总线程数: $(ps -mp $PID -o nlwp | grep -v NLWP)"

echo -e "\n==================== /proc 线程目录 ===================="
ls /proc/$PID/task 2>/dev/null
