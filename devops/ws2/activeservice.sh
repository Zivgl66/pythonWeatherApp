#!/bin/bash

options=('Start' 'Stop' 'Check' 'Leave' 'Exit')
running=systemctl is-active --quiet $service_name
PS3="Choose an option: "

echo "Enter an existing SERVICE name"
read service_name

if  $running; then
	echo $service_name | systemctl is-active $service_name
	select option in ${options[@]}	
	do
		case $option in
			"Start")
				if [[ $running ]]; then
					sudo systemctl restart $service_name
				else
					sudo systemctl start $service_name
				fi;;
			"Stop")
				sudo systemctl --no-block stop $service_name
				systemctl is-active $service_name;;
			"Check")
				sudo systemctl is-active $service_name;;
			"Leave")
				echo "OK I wont do shit";;
			"Exit")
				break;;
		esac
	done
fi

