#!/bin/bash
<<comment
the script will run a select menu from the mentors array.
when user selects an option, we check in a case statement if it
exists in the array, if so we return a mentor email based on the index,
if not we will return an invalid option
comment

declare -A mentors=(["Naftali"]='0' ["Tal"]='1' ["Ilya"]='2' ["Exit"]=exit )

mentors_emails=("naftali@infinitylabs.co.il" "tal@infinitylabs.co.il" "ilya@infinitylabs.co.il")

PS3="please enter your choice: "

select name in ${!mentors[@]} ; 
do
case $name in
	"Exit")
	break ;;
	"Naftali" | "Tal" | "Ilya" )
	echo ${mentors_emails[${mentors[$name]}]} ;;
*)
	echo 'invalid option' ;;
esac
done
