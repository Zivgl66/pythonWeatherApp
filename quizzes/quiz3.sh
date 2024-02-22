#!/bin/bash

student_array=("Ziv" "Tal" "Yossi" "Yochai" "Liav"  "Sagi" "Sergei" "Maxim" "Dennis" "Romi" "Bar" )
student_array=( $(shuf -e "${student_array[@]}") )
arr_size=${#student_array[@]}
for(( i=0; i < $arr_size; i+=2))
do
	if (($arr_size - $i == 3))
	then
		echo "Partners: ${student_array[$i]} - ${student_array[$i + 1]} - ${student_array[$i + 2]}"
		break
	fi
	echo "Partners: ${student_array[$i]} - ${student_array[$i + 1]}"
done

