#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
wget https://nginx.org/download/nginx-1.18.0.tar.gz
tar xzf nginx-1.18.0.tar.gz
git clone https://github.com/satya0307-d/nginx-rtmp-module.git
apt-get install libpcre3 libpcre3-dev -y
apt-get install build-essential -y
apt-get install libssl-dev -y
apt-get install zlib1g-dev -y
cd nginx-1.18.0
./configure --add-module=/root/nginx-rtmp-module
make
make install
