#!/bin/bash
COUNT=`systemctl status crond | grep 'active (running)' | grep -v grep | wc -l`
if [ $COUNT = 1 ] ;  then
echo "service is running" >> service.log
else
echo "service is not running" >> service.log
fi
