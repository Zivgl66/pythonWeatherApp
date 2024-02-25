#!/bin/bash

# get a directory and return number of files in it

echo 'enter directory path'
read path
ls -1 $path | wc -l
