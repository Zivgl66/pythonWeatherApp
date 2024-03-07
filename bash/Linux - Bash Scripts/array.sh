#!/bin/bash

my_array=(3 4 5 6) 
my_array2=(3,4,5,6)
my_array3=(123, 1234)
array4=(12345 12343)
declare -a arr=("this is" "a test" "of bash")

echo ${#my_array[@]}
echo ${#my_array[*]}
echo ${#my_array2[@]}
echo ${#my_array2[*]}
echo ${#my_array3[@]}
echo ${#my_array3[*]}
echo ${#array4[@]}
echo ${my_array[-1]}
echo ${my_array2[-1]}
echo ${my_array[*]}
echo ${my_array[@]}
echo ${!arr[@]}
echo "LOOP 3"
for x in ${arr[@]}; do
  echo "item: $x"
done
