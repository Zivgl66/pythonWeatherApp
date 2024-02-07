#!/bin/bash -i

# bind last script to f10 key
#bind '"\e[22-":"pwd/myscript.sh"'


if [ -t 1 ]
then
    # standard output is a TTY
    bind -x '"^[[21;5~":"/home/ziv/git/bash/ws1/8changeklayout.sh"'
fi




