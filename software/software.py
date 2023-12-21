#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_osp_cmd():
    print("OpenStack usage command:")
    osp_cmd = """
nova show 6e18eca1-497b-4071-ab93-0fd905aba22d
nova instance-action-list 6e18eca1-497b-4071-ab93-0fd905aba22d
nova get-vnc-console 6e18eca1-497b-4071-ab93-0fd905aba22d novnc
openstack catalog list
openstack endpoint list
openstack compute service list
openstack server show 6e18eca1-497b-4071-ab93-0fd905aba22d
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
   """
    print(docker_cmd)  

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