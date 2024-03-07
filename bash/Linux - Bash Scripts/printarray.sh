#!/bin/bash

array=("Docker" "Jenkins" "Ansible" "K8s" "Artifactory" "Terraform")
for str in ${array[@]}; do
	echo $str
done

echo ${array[@]} | tr ' ' '\n'
