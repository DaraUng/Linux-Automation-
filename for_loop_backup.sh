#!/bin/bash
for file in $(ls -p /etc/httpd/conf.d | grep -v / ); do
        echo :backing up $file: cp $file $file.orig
done
