#!/bin/bash

# prompt a dir name from user and return name and type of files inside

echo 'give me a directory name'
read dir
file $dir/*
