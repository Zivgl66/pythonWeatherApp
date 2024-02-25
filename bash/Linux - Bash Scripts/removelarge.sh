#!/bin/bash

# get as argument the dir path and number of bytes and remove dirs larger than the bytes

find $1 -type -name -size $2k -delete
