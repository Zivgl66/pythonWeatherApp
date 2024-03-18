#!/bin/bash

vm_list=('19' '20')
i=0
sshpass -p "Student2021!" ssh devops@10.1.3.12 << EOF

while sleep 5; 
	do
		for i in {0..1}; do
				echo "${vm_list[$i]}"
				if vim-cmd vmsvc/power.getstate "${vm_list[$i]}" | grep "Powered off";
				then
				vim-cmd vmsvc/power.on ${vm_list[$i]}
				echo "Turned on machine with id: ${vm_list[$i]}"
				fi
				done
	done
EOF





