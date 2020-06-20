#!/bin/bash

OUTPUTNGINX=`cat /usr/local/nginx/logs/nginx.pid | grep -o '[0-9]*' | wc -l`
OUTPUTSTUNNEL=`/etc/init.d/stunnel4 status | grep 'Active: active (running)' | wc -l`
echo "$OUTPUTNGINX"
echo "$OUTPUTSTUNNEL"
if [ $OUTPUTNGINX = 1 ] && [ $OUTPUTSTUNNEL = 1 ]; then
	echo "success"
fi
