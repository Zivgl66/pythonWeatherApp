#!/bin/sh
if [ $# -ne 0 ]
then
for var in $@
do
find . -name $var -exec cp "{}" /tmp \;
done
else 
echo "no arguments"
fi

