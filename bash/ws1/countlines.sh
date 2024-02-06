#!/bin/bash
var1=$1

function checklines() {
var2= wc -l $var1
echo $var2
}

result=$(checklines)
echo $result
 
