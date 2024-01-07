#! /bin/bash 


cat $1 | tee -a $2

md5sum $2
