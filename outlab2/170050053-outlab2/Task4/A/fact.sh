#! /bin/bash

let v1=$1%1

factorial()
{
    if [[ $1 -le 0 ]] || [[ $v1 != 0 ]];
    then
        echo 1
    else
        var=$(factorial $[$1-1])
        echo $(($1 * var))
    fi
}
factorial $1

