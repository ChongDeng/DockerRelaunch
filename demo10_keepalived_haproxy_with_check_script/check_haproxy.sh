#!/bin/bash

haproxy_docker_id="86cd04b0d1d7"

cmd=`docker container ls | grep $haproxy_docker_id`

if test -z "$cmd"; then
  echo "container $haproxy_docker_id is not running"
  
  docker container start $haproxy_docker_id
  if [ $? -ne 0 ]; then
	echo "can't start docker now! `date`"
	service keepalived stop
  else
	echo "restart docker successfully now! `date`"
  fi
  

else
  echo "container $haproxy_docker_id is running"    	
fi




