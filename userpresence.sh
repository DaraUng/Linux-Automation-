#!/bin/bash
userpresence =$( grep -ic "$1" /etc/passwd
if [ $userpresence -gt 0]; then 
        echo "I found $1"
else
        echo "I didn't find $1"
fi:
