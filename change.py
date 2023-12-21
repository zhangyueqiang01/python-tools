#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import argparse
import sys
import os

def cntoeng(file_path):
    if not os.path.isfile(file_path):
        print("Error: File '{}' not found.".format(file_path))
        sys.exit(1)

    sed_command = "sed -i 's/（/(/g; s/）/)/g; s/：/:/g; s/，/,/g; s/。/./g; s/？/?/g' %s" % file_path

    try:
        subprocess.Popen(sed_command, shell=True).wait()
        print("Sed command executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error executing sed command:", e)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="designed by Michael")
    parser.add_argument("--cntoeng", nargs=1, help="Modify all Chinese punctuation marks into English punctuation marks, like sed -i s/：/:/g test.py")

    args = parser.parse_args()

    if args.cntoeng:
        file_path = args.cntoeng[0]
        cntoeng(file_path)
    else:
        print("Please specify the file path with --cntoeng")

if __name__ == "__main__":
    main()


