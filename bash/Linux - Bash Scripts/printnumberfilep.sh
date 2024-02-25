#!/bin/bash

# get a directory path as argument and return the number of files in it

ls -1 $1 | wc -l
