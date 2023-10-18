# 0x02. Redis basic

## Learning Objectives

- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache

## Install Redis on Ubuntu 18.04

<code>$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .\*/bind 127.0.0.1/g" /etc/redis/redis.conf
</code>

## Use Redis in a container

Redis server is stopped by default - when you are starting a container, you should start it with: <code>service redis-server start</code>
