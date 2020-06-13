#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
wget https://nginx.org/download/nginx-1.18.0.tar.gz
tar xzf nginx-1.18.0.tar.gz
sudo apt-get install git -y
git clone https://github.com/satya0307-d/nginx-rtmp-module.git
sudo apt-get install libpcre3 libpcre3-dev -y
sudo apt-get install build-essential -y
sudo apt-get install libssl-dev -y
sudo apt-get install zlib1g-dev -y
cd nginx-1.18.0
./configure --add-module=/root/nginx-rtmp-module
make
make install
