#!/bin/bash

if [ -a $1 ]; then
if [ -w $1 ]; then
	echo "file exists with write permission"
else	
	echo "file exists but no write permissions"
fi
else	
	echo "file doesnt exist"
fi
