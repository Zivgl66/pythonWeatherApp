#!/bin/bash -i

string=$(cat ~/.bash_history | tail -1)
echo $string

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
		setxkbmap -layout il,us -option
        else
                newstring+=${engtoheb[$letter]}	
		setxkbmap -layout us,il -option
        fi
done
echo $newstring

