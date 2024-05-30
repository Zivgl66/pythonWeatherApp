#!/bin/bash
echo "Enter a valid ip address"
read ip_address
#regex_n='^[0-9]+(\.[0-9]+)*$'

regex_ip='([1-9]?[0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))'


if [[ "${ip_address}" =~ ^(${regex_ip}\.){3}${regex_ip}$ ]]; then
#if [[ $ip_address =~ $regex_n ]];then
ping $ip_address
else
echo "not a valid ip address"
fi

