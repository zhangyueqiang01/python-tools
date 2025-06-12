#!/bin/bash

echo -e "\e[31m cpu top10 \e[0m"
{ ps aux | head -1 ; ps aux | sort -k3rn | head ; }
echo ''

echo -e "\e[31m MEM top10\e[0m"
{ ps aux | head -1 ; ps aux | sort -k4rn | head ; }
echo ''

echo -e "\e[31m VSZ top 10\e[0m"
{ ps aux | head -1 ; ps aux | sort -k5rn | head ; }

