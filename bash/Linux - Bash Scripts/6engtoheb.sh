<<Psuedo
A script that accepts a string as a parameter, 
string can be in hebrew or english
I will use a assoc array with  each key having the value of the other lang respective letter
a condition will check wether the string is in hebrew or english and run a set of commands depending on the language
Will need to create two arrays, one for hebrew to english and one for english to hebrew
if string = hebrew 
for letter in string 
letter = letter_eng using assoc_array key-value and vise versa.
 ^ Approach ^
Psuedo

#!/bin/bash

string=$1

declare -A engtoheb=(
["q"]="/" ["w"]="'" ["e"]="ק" ["r"]="ר" ["t"]="א" ["y"]="ט" ["u"]="ו" ["i"]="ן" ["o"]="ם" ["p"]="פ" 
["a"]="ש" ["s"]="ד" ["d"]="ג" ["f"]="כ" ["g"]="ע" ["h"]="י" ["j"]="ח" ["k"]="ל" ["l"]="ך" [";"]="ף" ["'"]=","
["z"]="ז" ["x"]="ס" ["c"]="ב" ["v"]="ה" ["b"]="נ" ["n"]="מ" ["m"]="צ" [","]="ת" ["."]="ץ" ["/"]="."
)

declare -A hebtoeng=(
["/"]="q" ["'"]="w" ["ק"]="e" ["ר"]="r" ["א"]="t" ["ט"]="y" ["ו"]="u" ["ן"]="i" ["ם"]="o" ["פ"]="p"
["ש"]="a" ["ד"]="s" ["ג"]="d" ["כ"]="f" ["ע"]="g" ["י"]="h" ["ח"]="j" ["ל"]="k" ["ך"]="l" ["ף"]=";" [","]="'"
["ז"]="z" ["ס"]="x" ["ב"]="c" ["ה"]="v" ["נ"]="b" ["מ"]="n" ["צ"]="m" ["ת"]="/" ["ץ"]="."
    )


for (( i=0; i<${#string}; i++ )); do
	letter="${string:$i:1}"
	if [[ -v "hebtoeng[$letter]" ]]; then
		newstring+=${hebtoeng[$letter]}
		#echo "eng"
	else
		newstring+=${engtoheb[$letter]}
		#echo "heb"
	fi
done
echo $newstring
