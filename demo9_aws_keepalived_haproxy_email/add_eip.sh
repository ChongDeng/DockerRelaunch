#!/bin/bash

/usr/bin/python3 /root/keepalived_haproxy/email/send_email_master.py

#弹性ip地址（公网ip）
EIP=34.233.236.106
#此服务器（EC2）的实例的id
INSTANCE_ID=i-0cb4ddff3450826b1

aws ec2 disassociate-address --public-ip ${EIP}
aws ec2 associate-address --public-ip ${EIP} --instance-id ${INSTANCE_ID}
