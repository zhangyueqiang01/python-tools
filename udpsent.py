#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import threading
import logging
import argparse

logging.basicConfig(filename='udp_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_large_message(host, port, size, num_packets):
    message = b'a' * size
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        for _ in range(num_packets):
            s.sendto(message, (host, port))
            logging.info("Sent UDP packet to %s:%s with size %s bytes", host, port, size)
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(description='UDP Message Sender')
    parser.add_argument('--host', default='192.168.2.254', help='Host name or IP address, default is 192.168.2.254')
    parser.add_argument('--port', type=int, default=12345, help='Port number, default is 12345')
    parser.add_argument('--size', type=int, default=1024, help='Message size in bytes, default is 1024 Kb')
    parser.add_argument('--packets-per-thread', type=int, default=3, help='Number of packets per thread, default is 3')
    parser.add_argument('--total-threads', type=int, default=10, help='Total number of threads, default is 10')

    args = parser.parse_args()

    host = args.host
    port = args.port
    message_size = args.size
    packets_per_thread = args.packets_per_thread
    total_threads = args.total_threads

    threads = []
    for _ in range(total_threads):
        thread = threading.Thread(target=send_large_message, args=(host, port, message_size, packets_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

#确保其中的代码只在脚本直接运行时执行，而不会在脚本被导入为模块到其他脚本中时执行
#这个设计很有用，因为它允许你在脚本中包含可重用的代码（如函数定义），这些代码可以在被导入时使用，但只有在直接执行脚本时才执行特定的操作
if __name__ == "__main__":
    main()



