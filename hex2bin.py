#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys

def hex_to_bin(hex_string):
    # 将16进制字符串转换为整数
    decimal = int(hex_string, 16)
    # 将整数转换为二进制字符串，并去掉前缀 '0b'
    binary_string = bin(decimal)[2:]
    return binary_string

def print_help():
    help_message = """
Usage: python script.py --hex2bin <hexadecimal>

Options:
  --hex2bin  Specify the hexadecimal string to convert to binary.
  -h         Show this help message and exit.
"""
    print(help_message)

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_help()
        sys.exit(0)
    
    if len(sys.argv) != 3 or sys.argv[1] != '--hex2bin':
        print("Invalid arguments.\n")
        print_help()
        sys.exit(1)
    
    hex_string = sys.argv[2]
    binary_string = hex_to_bin(hex_string)
    print('Hexadecimal: {}'.format(hex_string))
    print('Binary: {}'.format(binary_string))


