#!/usr/bin/python
# -*- coding: utf-8 -*-

def print_storage_unit_cmd():
    storage_unit_cmd = """

计算机的存储单位分为基本单位和扩展单位，它们有两个体系：二进制（计算机内部实际使用）和十进
制（硬盘厂商/传输速率常用）

################################ 基本单位 #####################################

| 单位     | 缩写| 含义
| -------- | --- | -------------------
| **bit**  |  b  | 比特，最小的存储单位，存储 0 或 1
| **Byte** |  B  | 字节，1 B = 8 b

############################# 二进制存储单位 ###################################

常用于内存、操作系统显示,以 2 为底，每一级相差 2¹⁰（1024）倍
国际标准用 KiB, MiB, GiB, TiB 来区分二进制单位

| 单位                | 缩写| 关系（字节）     | 常见应用
| ------------------- | --- | ---------------- | -----------
| **KiB**（Kibibyte） | KiB | 1 KiB = 1024 B   | 缓存文件、配置文件大小
| **MiB**（Mebibyte） | MiB | 1 MiB = 1024 KiB | 早期内存容量
| **GiB**（Gibibyte） | GiB | 1 GiB = 1024 MiB | 现代内存、硬盘分区显示
| **TiB**（Tebibyte） | TiB | 1 TiB = 1024 GiB | 大容量硬盘
| **PiB**（Pebibyte） | PiB | 1 PiB = 1024 TiB | 数据中心存储
| **EiB**（Exbibyte） | EiB | 1 EiB = 1024 PiB | 超大规模云存储

############################# 十进制存储单位 ###################################

常见于硬盘广告、网速单位,以 10 为底，每一级相差 10³（1000）倍

| 单位               |缩写| 关系（字节）   | 常见应用
| ------------------ | -- | -------------- | ---------
| **KB**（Kilobyte） | KB | 1 KB = 1000 B  | 早期文档大小
| **MB**（Megabyte） | MB | 1 MB = 1000 KB | 厂商标注的硬盘容量
| **GB**（Gigabyte） | GB | 1 GB = 1000 MB | 硬盘、U盘容量
| **TB**（Terabyte） | TB | 1 TB = 1000 GB | 商用大硬盘
| **PB**（Petabyte） | PB | 1 PB = 1000 TB | 数据中心级别
| **EB**（Exabyte）  | EB | 1 EB = 1000 PB | 全球数据存储统计

################################ caution ####################################

操作系统 vs 厂商容量
厂商硬盘：500 GB = 500 × 1000³ 字节
Windows显示：按 1024 进制计算 → 500 GB ≈ 465 GiB

网速单位
网络带宽常用 bit（b），比如 100 Mbps = 100 兆比特/秒 ≈ 12.5 MB/s（字节每秒）。
   """
    print(storage_unit_cmd) 


def print_mysql_cmd():
    print("mysql usage command:")
    mysql_cmd = """
mysql -s
   """
    print(mysql_cmd)  

def print_etcd_cmd():
    print("etcd usage command:")
    etcd_cmd = """
etcd -s
   """
    print(etcd_cmd)  

def print_postgresql_cmd():
    print("postgresql usage command:")
    postgresql_cmd = """
postgresql -s
   """
    print(postgresql_cmd)  

def print_xml_cmd():
    print("xml usage command:")
    xml_cmd = """
xml -s
   """
    print(xml_cmd)  
