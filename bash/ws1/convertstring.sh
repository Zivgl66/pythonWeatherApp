#!/bin/bash

# get string input from user
# convert it to an array of chars
# convert each char to hebrew
# return the chars as string

check_heb_or_eng(){
abc="abcdefghijklmnopqrstuvxyz"
char=$(echo $1 | cut -c1-1)
[[ $abc == *$char*  ]] && echo 0 || echo 1
}

engtoheb=(["q"]="/" ["w"]="'" ["e"]="ק" ["r"]="ר" ["t"]="א" ["y"]="ט" ["u"]="ו" ["i"]="ן" ["o"]="ם" ["p"]="פ" ["a"]="ש" ["s"]="ד" ["d"]="ג" ["f"]="כ" ["g"]="ע" ["h"]="י" ["j"]="ח" ["k"]="ל"  ["l"]="ך" [";"]="ף" ["'"]="," ["z"]="ז" ["x"]="ס" ["c"]="ב" ["v"]="ה" ["b"]="נ" ["n"]="מ" ["m"]="צ" [","]="ת" ["."]="ץ" ["/"]=".")

hebtoeng=(["/"]="q" ["'"]="w" ["ק"]="e" ["ר"]="r" ["א"]="t" ["ט"]="y" ["ו"]="u" ["ן"]="i" ["ם"]="o" ["פ"]="p" ["ש"]="a" ["ד"]="s" ["ג"]="d" ["כ"]="f" ["ע"]="g" ["י"]="h" ["ח"]="j" ["ל"]="k" ["ך"]="l" ["ף"]=";" [","]="'" ["ז"]="z" ["ס"]="x" ["ב"]="c" ["ה"]="v" ["נ"]="b" ["מ"]="n" ["צ"]="m" ["ת"]="/" ["ץ"]=".")

echo 'give me a string:'
read str
check=$(check_heb_or_eng $str)
echo $check
length=${#str}
newstring=''
for ((i = 0; i < length; i++)); do
	letter="${str:$i:1}"
	if [ $check == 0 ]; then
		if [ -v "${engtoheb[$letter]}" ]; then
			echo ${engtoheb[$letter]}
#		newstring+=${engtoheb[$letter]}
	fi
	else
		newstring+=${hebtoeng[$letter]}
	fi
done	
echo $newstring

