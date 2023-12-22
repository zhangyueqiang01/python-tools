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
