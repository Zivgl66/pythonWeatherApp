#!/bin/bash

for dir in "$@"
do
	touch ./$dir/dummy.md
done

