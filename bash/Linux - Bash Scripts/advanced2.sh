#!/bin/bash

string=$(xsel -ob)
echo "Word to trnaslate: $string \n"
        if [[ $string =~ ^[ת-א]+$ ]];
	then
                trans he:en $string
        else
                trans en:he $string
        fi




