#!/bin/bash

#bash script that on every successful run logs to /var/log/syslog

#if [[ $? -eq 0 ]]; then
#	logger "successful run"
#else 
#	echo "failed!"
#fi


# ex 5- bd syntax:
if [[ $? -eq 0 ]]; than
        logger "successful run"
else
        echo "failed!"
fi
~  
