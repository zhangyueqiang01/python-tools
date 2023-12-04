[root@bj5l2 python-tools]# ./mytool.py -h  
usage: mytool.py [-h] [--udp] [--tcp] [--ipv4] [--icmp] [-i PKG] [-p PING]  
                 [-d HOST] [-z ZOMBIE] [-P PASSWD] [-w HPORT] [-t TPORT]  
                 [-u UPORT] [--host HOST] [--port PORT] [--size SIZE]  
                 [--packets-per-thread PACKETS_PER_THREAD]  
                 [--total-threads TOTAL_THREADS]  

design by Michael  

optional arguments:  
  -h, --help            show this help message and exit  
  --udp                 Print UDP header format  
  --tcp                 Print TCP header format  
  --ipv4                Print IPV4 header format  
  --icmp                Print ICMP header format  
  -i PKG, --install PKG  
                        install packages on remote host  
  -p PING, --ping PING  ping a net such as ping 8.8.8  
  -d HOST, --ihost HOST  
                        combine with -i  
